import re
import json
import requests
import secrets
import os
from selenium import webdriver
from bs4 import BeautifulSoup

# Set the save location
save_location = "C:\\your\\chosen\\location\\for\\down"

def get_facebook_url():
    url = input("Please enter the Facebook video URL: ")
    return url

def parse_webpage(url):
    driver = webdriver.Firefox()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    return soup

def find_video_url(soup):
    scripts = soup.find_all('script')
    for script in scripts:
        match = re.search(r'"(https:\\/\\/video\.fyaw1-1\.fna\.fbcdn\.net\\/v.+?)"', script.text)
        if match:
            # Unescape the URL
            video_url = json.loads('"' + match.group(1) + '"')
            return video_url
    return None

facebook_url = get_facebook_url()
print(f"You entered: {facebook_url}")

soup = parse_webpage(facebook_url)

video_url = find_video_url(soup)

if video_url is None:
    print("Video URL not found")
    exit()

print(f"Video URL: {video_url}")

def download_video(url, filename):
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print(f"Video downloaded successfully as {filename}")
    else:
        print("Failed to download video")

# Extract the video ID from the Facebook URL
match = re.search(r'([a-zA-Z0-9]+)/?$', facebook_url)
if match:
    video_id = match.group(1)
else:
    print("Could not extract video ID from URL. Generating a random filename.")
    video_id = "failedextract" + secrets.token_hex(2)  # generates a random string

filename = f"{video_id}.mp4"

# Join the save location and filename to create the full path
full_path = os.path.join(save_location, filename)

download_video(video_url, full_path)