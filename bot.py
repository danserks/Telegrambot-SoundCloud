import telebot
import subprocess
import os

API_TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

# Directory to save the downloaded soundtracks
DOWNLOAD_DIRECTORY = 'downloaded_tracks'

if not os.path.exists(DOWNLOAD_DIRECTORY):
    os.makedirs(DOWNLOAD_DIRECTORY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Send me a SoundCloud link and I'll download it for you!")

@bot.message_handler(func=lambda message: True)
def download_soundcloud_track(message):
    soundcloud_url = message.text.strip()
    
    bot.reply_to(message, "Downloading your track or playlist... Please wait.")
    
    # Use scdl to download the track or playlist
    download_command = f"scdl -l {soundcloud_url} -o {DOWNLOAD_DIRECTORY}"
    try:
        subprocess.run(download_command, shell=True, check=True)

        # Find the downloaded files
        downloaded_files = [os.path.join(DOWNLOAD_DIRECTORY, f) for f in os.listdir(DOWNLOAD_DIRECTORY) if os.path.isfile(os.path.join(DOWNLOAD_DIRECTORY, f))]
        if downloaded_files:
            for file_path in downloaded_files:
                with open(file_path, 'rb') as track:
                    bot.send_audio(message.chat.id, track)
                # Clean up the downloaded file
                os.remove(file_path)
        else:
            bot.reply_to(message, "Failed to download the track. Please check the URL and try again.")
    except subprocess.CalledProcessError:
        bot.reply_to(message, "Failed to download the track. Please check the URL and try again.")

if __name__ == '__main__':
    bot.polling()
