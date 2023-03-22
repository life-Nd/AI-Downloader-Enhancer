import os
import subprocess

# Create output directories if they don't already exist


# path = "../../Data/Gates/Videos"
path = "/Users/lifen/Data/Gates"
path_videos = path + "/Videos"

os.makedirs(path+"/Wav", exist_ok=True)
os.makedirs(path+"/Mp4", exist_ok=True)
# Loop through all files in the Gates directory
for filename in os.listdir(path_videos):
    # Check if the file is an mp4 video
    if filename.endswith(".mp4"):
        # Create output filenames for the audio files
        wav_filename = os.path.join(path+"/Wav", os.path.splitext(filename)[0] + ".wav")
        mp4_filename = os.path.join(path+"/Mp4", os.path.splitext(filename)[0] + ".mp4")

        # Use ffmpeg to convert the mp4 video to wav and mp4 audio
        subprocess.call(["ffmpeg", "-i", os.path.join(path_videos, filename), "-vn", "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "2", wav_filename])
        subprocess.call(["ffmpeg", "-i", os.path.join(path_videos, filename), "-vn", "-acodec", "copy", mp4_filename])

        print(f"{filename} converted to audio")
