# Scheduled Telegram Group Voice Chat Bot

This repository contains a simple example of a Telegram bot that starts a
group video chat and plays an audio file at a specific time.

## Requirements

- Python 3.8 or newer
- [pyrogram](https://docs.pyrogram.org/)
- [pytgcalls](https://github.com/pytgcalls/pytgcalls)
- [apscheduler](https://apscheduler.readthedocs.io/)

Install the dependencies with:

```bash
pip install pyrogram tgcrypto pytgcalls apscheduler
```

## Configuration

Export these environment variables with your own Telegram API credentials and
bot settings:

```bash
export API_ID=12345
export API_HASH="your_api_hash"
export BOT_TOKEN="123456:token"
export GROUP_ID=-1001234567890  # ID of the group to join
export AUDIO_FILE="path/to/track.mp3"
export SCHEDULE_TIME="2024-01-01 12:00"  # YYYY-MM-DD HH:MM
```

## Usage

Run the bot with:

```bash
python scheduled_player_bot.py
```

When the scheduled time is reached, the bot will start a video chat in the
configured group and stream the specified audio file.
