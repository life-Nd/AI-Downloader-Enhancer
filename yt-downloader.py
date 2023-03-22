import os
import urllib.request
from bs4 import BeautifulSoup
from yt_dlp import YoutubeDL

# specify the YouTube playlist URL
# playlist_url = (
# ""
# )

# specify the output folder for the downloaded videos
output_folder = ""

# create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


video_links = [
   
]
# # download each video using youtube-dl
for link in video_links:
    # print(f'{link=}')
    # video_url = 'https://www.youtube.com' + link['href']
    video_url = link
    output_path = os.path.join(output_folder, link + '.mp4')
    ydl_opts = {'outtmpl': output_path}
    with YoutubeDL() as ydl:
        ydl.download([video_url])
