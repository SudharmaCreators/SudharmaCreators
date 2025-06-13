
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

 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/README.md b/README.md
index 8e016ceb3e9639e88366b3d151e2c147e206958f..2672b1dbe9208239bfaf0dd8caadb1167bca76fc 100644
--- a/README.md
+++ b/README.md
@@ -1,12 +1,57 @@
-- 👋 Hi, I’m @Shailogix
-- 👀 New here
-- 🌱 Python MySQL
-- 💞️ Building Telegram Bots
-- 📫 Reach me on Telegram @shailogix
-- 😄 Helping Humanity
-- ⚡ Eploring within
-
-<!---
-SudharmaCreators/SudharmaCreators is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
-You can click the Preview link to take a look at your changes.
---->
+# Scheduled Telegram Group Voice Chat Bot
+
+This repository contains a simple example of a Telegram bot that starts a
+group video chat and plays an audio file at a specific time.
+
+The bot will automatically create the group call when the scheduled time is
+reached. No human action is required once it is configured and running.
+
+## Requirements
+
+- Python 3.8 or newer
+- [pyrogram](https://docs.pyrogram.org/)
+- [pytgcalls](https://github.com/pytgcalls/pytgcalls)
+- [apscheduler](https://apscheduler.readthedocs.io/)
+
+Install the dependencies with:
+
+```bash
+pip install pyrogram tgcrypto pytgcalls apscheduler
+```
+
+## Configuration
+
+Export these environment variables with your own Telegram API credentials and
+bot settings:
+
+```bash
+export API_ID=12345
+export API_HASH="your_api_hash"
+export BOT_TOKEN="123456:token"
+export GROUP_ID=-1001234567890  # ID of the group to join
+export AUDIO_FILE="path/to/track.mp3"
+export SCHEDULE_TIME="2024-01-01 12:00"  # YYYY-MM-DD HH:MM
+```
+
+### Permissions
+
+The bot account **must** be an administrator in the target group with the
+permission to manage video chats. Without these rights it cannot start the
+group call on its own.
+
+### Audio file location
+
+Set `AUDIO_FILE` to the path of the music file you want to play. The path can be
+absolute or relative. For example, if you place `track.mp3` in this repository
+folder you would export `AUDIO_FILE="./track.mp3"`.
+
+## Usage
+
+Run the bot with:
+
+```bash
+python scheduled_player_bot.py
+```
+
+When the scheduled time is reached, the bot will start a video chat in the
+configured group and stream the specified audio file.
 
EOF
)

