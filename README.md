# 📥 YouTube Video Downloader (Python + yt-dlp)

A simple Python tool to download YouTube videos in MP4 format and choose the download location using a folder selection dialog.

This project uses `yt-dlp` for downloading and `tkinter` for GUI folder selection.

---

## 🚀 Features

- ✅ Download videos in best available MP4 quality  
- ✅ Select download folder using GUI dialog  
- ✅ Simple CLI interface  
- ✅ Automatic file naming  
- ✅ Error handling  
- ✅ Cross-platform support  

---

## 🛠️ Tech Stack

- Python 3  
- yt-dlp  
- tkinter  

---

## 📦 Installation (Manual Setup)

Follow the steps below to set up the project.

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/youtube-downloader.git
cd youtube-downloader
2️⃣ Install Required Library
pip install yt-dlp
⚠️ tkinter comes pre-installed with most Python versions.

3️⃣ Run the Program
python downloader.py
▶️ Usage
After running the script, follow these steps:

Enter the YouTube video URL in terminal.

Select a download folder in the popup window.

Download starts automatically.

Video is saved in selected folder.

🧪 Example
Please enter a YouTube url: https://www.youtube.com/watch?v=abc123
Selected folder: /Users/abhiraj/Downloads
Downloading...
Video Downloaded Successfully!
📂 Output Format
Downloaded videos are saved as:

<Video_Title>.mp4
Example:

Learn Python in 1 Hour.mp4
📁 Project Structure
youtube-downloader/
│
├── downloader.py
└── README.md
⚠️ Error Handling
The program handles:

Invalid URLs

Private/unavailable videos

Network issues

Download failures

Example:

Download failed!
Reason: Video unavailable
📜 Legal Disclaimer
This project is for educational and personal use only.

Downloading copyrighted content without permission may violate YouTube’s Terms of Service and local laws.

Use responsibly.