- 👋 Hi, I’m @Shailogix
- 👀 New here
- 🌱 Python MySQL
- 💞️ Building Telegram Bots
- 📫 Reach me on Telegram @shailogix
- 😄 Helping Humanity
- ⚡ Eploring within

## Scheduled Player Bot

This repository includes a basic example of a Telegram bot that can start a
video call in a specific group and play an audio file at a scheduled time.

The `scheduled_player_bot.py` script requires the following Python packages:

- [pyrogram](https://docs.pyrogram.org/)
- [pytgcalls](https://github.com/pytgcalls/pytgcalls)
- [apscheduler](https://apscheduler.readthedocs.io/)

Before running the bot, export these environment variables with your own
Telegram API credentials and configuration:

```bash
export API_ID=12345
export API_HASH="your_api_hash"
export BOT_TOKEN="123456:token"
export GROUP_ID=-1001234567890  # ID of the group to join
export AUDIO_FILE="path/to/track.mp3"
export SCHEDULE_TIME="2024-01-01 12:00"  # YYYY-MM-DD HH:MM
```

Run the bot with `python scheduled_player_bot.py`.
