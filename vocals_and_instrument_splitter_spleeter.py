# -*- coding: utf-8 -*-
"""vocals and instrument splitter spleeter.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13eq8eWY_rF91UcHaqIN6bjvHZYRzos1u

Spleeter separates vocals/voice and instruments into different mp3 files.
A useful wiki on github [getting started](https://github.com/deezer/spleeter/wiki/2.-Getting-started#usage)

# Install spleeter
"""

import os
import shutil

!apt install ffmpeg

pip install spleeter

"""# Separate file(s) in content folder from command line

"""

#upload mp3 to content folder
from google.colab import files

# Upload files from your local machine to the Colab environment
uploaded = files.upload()

# The 'uploaded' variable is a dictionary of the uploaded files
for filename in uploaded.keys():
    print(f"Uploaded file '{filename}' with length {len(uploaded[filename])} bytes")

# to view the help page
!spleeter separate --help

# Default audio split in two (vocals and accompaniment)
!spleeter separate -o audio_output "/content/{filename}"

#This time, it will generate four files: vocals.wav, drums.wav, bass.wav and other.wav.
!spleeter separate -o audio_output -p spleeter:4stems "/content/{filename}"

#This time, a pretrained 5 stems (vocals / bass / drums / piano / other)
!spleeter separate -o audio_output -p spleeter:5stems "/content/{filename}"

"""Spleeting multiple files at one time you will need to upload multiple files"""

# If you have multiple audio files that you want to spleet
# Directory containing the music files
directory = '/content/'  # Change this path to your specific directory

# List all music files
music_files = [os.path.join(directory, file) for file in os.listdir(directory)
               if file.endswith(('.mp3', '.wav', '.ogg'))]

# Print out the files to be processed
print("Files to be processed:")
for file in music_files:
    print(file)

# Define the output format for the filenames
output_format = "{foldername}/{filename}_{instrument}.{codec}"

# Construct and run the spleeter command
if music_files:
    files_string = " ".join(f'"{path}"' for path in music_files)
    !spleeter separate -o /content/audio_output -p spleeter:4stems -f {output_format} {files_string}
else:
    print("No music files found to process.")

# for downloading all the spleeted files
from google.colab import files

# Function to collect all files recursively
def list_files(directory):
    paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            paths.append(os.path.join(root, file))
    return paths

# Directory containing the files
directory = '/content/audio_output'

# Compress the entire directory
zip_path = '/content/audio_output.zip'
shutil.make_archive(zip_path.replace('.zip', ''), 'zip', directory)

# Download the ZIP file
files.download(zip_path)