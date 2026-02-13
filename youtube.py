import yt_dlp
import tkinter as tk
from tkinter import filedialog

def download_video(url,save_path):
    ydl_opts = {
        "format": "best[ext=mp4]/best",
        "outtmpl": f"{save_path}/%(title)s.%(ext)s",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Video Downloaded Successfully!")

    


url="https://www.youtube.com/watch?v=jtXSW5dGtr0&list=RDjtXSW5dGtr0&start_radio=1"
save_path="/Users/abhiraj/Downloads"

download_video(url,save_path)