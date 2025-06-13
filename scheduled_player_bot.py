# Scheduled Telegram Voice Chat Bot
# This script starts a group video chat in a configured group and plays an
# audio file when the scheduled time is reached. The bot account must be an
# administrator in that group with permission to manage video chats.
#
# Requirements:
#   - pyrogram
#   - pytgcalls
#   - apscheduler
# These packages must be installed in your environment. See the README for
# setup instructions.

import os
import asyncio
from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram import Client
from pyrogram.raw.functions.phone import CreateGroupCall
from pytgcalls import PyTgCalls, idle
from pytgcalls.types.input_stream import AudioPiped

API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
GROUP_ID = int(os.environ.get("GROUP_ID", 0))  # e.g. -1001234567890
AUDIO_FILE = os.environ.get("AUDIO_FILE", "track.mp3")
SCHEDULE_TIME = os.environ.get("SCHEDULE_TIME", "2099-01-01 00:00")

app = Client("scheduled_player", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
voice = PyTgCalls(app)

async def start_video_chat():
    """Start group video chat and stream audio."""
    # Attempt to create the group call if not already present
    try:
        await app.invoke(CreateGroupCall(peer=await app.resolve_peer(GROUP_ID), random_id=app.rnd_id()))
    except Exception:
        # A call might already exist
        pass

    # Start streaming the audio file
    await voice.join_group_call(GROUP_ID, AudioPiped(AUDIO_FILE))

async def main() -> None:
    scheduler = AsyncIOScheduler()
    run_time = datetime.strptime(SCHEDULE_TIME, "%Y-%m-%d %H:%M")
    scheduler.add_job(start_video_chat, "date", run_date=run_time)
    scheduler.start()

    await app.start()
    await voice.start()
    await idle()
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
