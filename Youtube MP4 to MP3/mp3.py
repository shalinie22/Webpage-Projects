import yt_dlp
import moviepy.editor as mp
import os

def video_to_mp3(youtube_url, output_path):
    try:
        # Download audio using yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'temp_audio.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])

        print(f"Conversion successful! MP3 saved at {output_path}")
        return output_path

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

video_to_mp3("https://www.youtube.com/watch?v=SbAKYgfYET8","\\")
