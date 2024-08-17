> [!NOTE]
> this for only education pruposes


#  Requirements!
> [!WARNING]
> This bot uses
> "scdl" for downloading
> "PytelegramBotAPI" for running the bot.

```bash
pip install pyTelegramBotAPI scdl
```

### Explanation

1. **Setup:**
   - The bot needs your Telegram API token (`API_TOKEN`).
   - `scdl` is used to download tracks from SoundCloud.

2. **Download Directory:**
   - The directory `downloaded_tracks` is created if it doesn't exist, where tracks will be saved.

3. **Handlers:**
   - The `/start` command sends a greeting message.
   - All other messages are treated as SoundCloud links for downloading tracks.

4. **Download and Send:**
   - The bot uses `scdl` to download the track to the `downloaded_tracks` directory.
   - Once downloaded, it sends the file to the user and deletes the file to free up space.

### Replace `YOUR_TELEGRAM_BOT_API_TOKEN`
Make sure to replace `YOUR_TELEGRAM_BOT_API_TOKEN` with your actual Telegram bot API token.

Now, run the script and interact with your Telegram bot by sending SoundCloud track links!

