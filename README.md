📥 YouTube Video Downloader (Python + yt-dlp)

A simple Python-based YouTube video downloader that lets users download videos in MP4 format and choose a save location using a folder selection dialog.

This tool uses:

yt-dlp for downloading videos

tkinter for folder selection

Command-line input for URLs

🚀 Features

✅ Download YouTube videos in best available MP4 quality

✅ Select download folder using GUI dialog

✅ Simple and lightweight

✅ Error handling for failed downloads

✅ Works on Windows, macOS, and Linux

📦 Requirements

Make sure you have:

Python 3.7+

Internet connection

Required libraries:

yt-dlp

tkinter (usually pre-installed with Python)

🔧 Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/youtube-downloader.git
cd youtube-downloader

2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install yt-dlp


tkinter is included with most Python installations. If not, install it from your OS package manager.

▶️ Usage
Run the Script
python downloader.py

Steps

Enter the YouTube video URL in the terminal.

A folder selection dialog will open.

Choose the folder where you want to save the video.

The download will start automatically.

Example
Please enter a YouTube url: https://www.youtube.com/watch?v=example123
Selected folder: /Users/abhiraj/Downloads
Downloading...
Video Downloaded Successfully!

📂 Output Format

Downloaded videos are saved as:

Video_Title.mp4


Example:

My Favorite Song.mp4


They will appear inside the selected folder.

⚠️ Error Handling

The script handles:

Invalid URLs

Network issues

Download failures

Unexpected errors

Example error:

Download failed!
Reason: Video unavailable

🛠️ Project Structure
youtube-downloader/
│
├── downloader.py
└── README.md

📜 Legal Disclaimer

This tool is intended for educational and personal use only.

Downloading copyrighted content without permission may violate YouTube’s Terms of Service and local laws. Use responsibly.