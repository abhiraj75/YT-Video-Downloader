# 📥 YouTube Video Downloader (Python)

A simple Python tool to download YouTube videos in MP4 format using `yt-dlp` and select the download folder using a file dialog.

---

## 🚀 Features

- Download videos in best available quality
- Save videos in MP4 format
- Folder selection using GUI dialog
- Lightweight and easy to use
- Cross-platform (Windows, macOS, Linux)

---

## 📦 Requirements

- Python 3.7 or above
- Internet connection

### Libraries Used

- yt-dlp
- tkinter (pre-installed with Python)

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/youtube-downloader.git
cd youtube-downloader
2. (Optional) Create Virtual Environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
3. Install Dependency
pip install yt-dlp
▶️ Usage
Run the script using:

python downloader.py
Steps
Enter the YouTube video URL.

Select a folder from the dialog.

Download starts automatically.

Video will be saved in selected folder.

📌 Example
Please enter a YouTube url: https://www.youtube.com/watch?v=abc123
Selected folder: /Users/abhiraj/Downloads
Downloading...
Video Downloaded Successfully!
📂 Output
Videos are saved as:

Video_Title.mp4
Example:

My Song.mp4
⚠️ Error Handling
The program handles:

Invalid URLs

Network errors

Download failures

Unexpected crashes

Example:

Download failed!
Reason: Video unavailable
📁 Project Structure
youtube-downloader/
│
├── downloader.py
└── README.md
📜 Disclaimer
This project is for educational and personal use only.

Downloading copyrighted content without permission may violate YouTube’s Terms of Service and local laws.

Use responsibly.