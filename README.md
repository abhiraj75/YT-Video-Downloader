# YouTube Video Downloader

A simple Python script to download YouTube videos using a GUI folder selector.

## Features

- Download YouTube videos in the best available MP4 format
- Interactive folder selection using a GUI dialog
- Command-line URL input
- Error handling for failed downloads

## Prerequisites

Before running this script, make sure you have Python installed on your system (Python 3.7 or higher recommended).

## Installation

1. Clone or download this repository

2. Install the required dependencies:

```bash
pip install yt-dlp
```

> **Note:** `tkinter` is included with most Python installations. If you encounter issues, you may need to install it separately depending on your operating system.

## Usage

1. Run the script:

```bash
python video_downloader.py
```

2. Enter the YouTube video URL when prompted

3. Select the destination folder using the file dialog

4. Wait for the download to complete

## Example

```
Please enter a YouTube url: https://www.youtube.com/watch?v=example
Selected folder: /Users/username/Downloads
Downloading...
Video Downloaded Successfully!
```

## Error Handling

The script includes error handling for:
- Download failures
- Unexpected errors during the download process
- Missing folder selection

## Dependencies

- `yt-dlp` - YouTube video downloader library
- `tkinter` - Python's standard GUI library

## Notes

- Videos are saved with their original title as the filename
- The script automatically selects the best available MP4 format
- If MP4 is not available, it falls back to the best available format

## License

This project is open source and available for personal use.

## Troubleshooting

If you encounter issues:
- Ensure `yt-dlp` is up to date: `pip install --upgrade yt-dlp`
- Check that the YouTube URL is valid
- Verify you have write permissions in the selected folder