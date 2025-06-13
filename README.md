# Scheduled Telegram Group Voice Chat Bot

Easily start a group video chat in Telegram and stream a music track at a time
you choose. Once the bot is configured, it will handle everything on its own —
no manual intervention required.

## Features

- Automatically opens a video chat in the selected group
- Plays an audio file from disk
- Runs at the scheduled time you configure

## Requirements

- Python 3.8 or newer
- [Pyrogram](https://docs.pyrogram.org/)
- [PyTgCalls](https://github.com/pytgcalls/pytgcalls)
- [APScheduler](https://apscheduler.readthedocs.io/)

Install these packages with:

```bash
pip install pyrogram tgcrypto pytgcalls apscheduler
```

## Configuration

Before running the bot export the following environment variables with your
Telegram API credentials and desired schedule:

| Variable | Description |
| --- | --- |
| `API_ID` | Telegram API ID |
| `API_HASH` | Telegram API hash |
| `BOT_TOKEN` | Token from BotFather |
| `GROUP_ID` | ID of the group to start the call in |
| `AUDIO_FILE` | Path to the music file to play |
| `SCHEDULE_TIME` | Time to start the call (YYYY-MM-DD HH:MM) |

Example setup:

```bash
export API_ID=12345
export API_HASH="your_api_hash"
export BOT_TOKEN="123456:token"
export GROUP_ID=-1001234567890
export AUDIO_FILE="./track.mp3"
export SCHEDULE_TIME="2024-01-01 12:00"
```

### Permissions

The bot **must** be an administrator in the group with permission to manage
video chats. Otherwise it cannot start the call on its own.

### Audio file

`AUDIO_FILE` accepts any absolute or relative path. If the file `track.mp3` is
in this directory, use `AUDIO_FILE="./track.mp3"`.

## Usage

Run the bot with:

```bash
python scheduled_player_bot.py
```

At the scheduled time the bot will launch the video chat in the configured
group and begin streaming the specified audio file.
