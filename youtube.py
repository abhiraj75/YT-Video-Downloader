import yt_dlp
import tkinter as tk
from tkinter import filedialog

def download_video(url,save_path):
    ydl_opts = {
        "format": "best[ext=mp4]/best",
        "outtmpl": f"{save_path}/%(title)s.%(ext)s",
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video Downloaded Successfully!")
    except DownloadError as e:
        print("Download failed!")
        print(f"Reason: {e}")
    except Exception as e:
        print("Unexpected error occurred!")
        print(f"Error: {e}")


def open_file_dialog():
    folder=filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder


if __name__=="__main__":
    root = tk.Tk()
    root.withdraw()


