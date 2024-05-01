# FBvidDownloader

This is a Python script for downloading videos from Facebook.

## Prerequisites

You need to have Python installed on your computer. You also need the following Python packages:

- selenium
- beautifulsoup4

You can install them with pip:

```bash
pip install selenium beautifulsoup4
```
## Usage
Clone this repository:
Edit the save_location variable in main.py to the path where you want to save the videos.

Run the script:
```bash
python main.py
```


## Known Issues

Currently, there are instances where the downloaded MP4 file contains only audio and no video. This is due to the way the script parses the Facebook webpage to find the video URL.