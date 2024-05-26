import os
import json
import eyed3
from datetime import date
import csv
import shutil
import hashlib
import uuid




error_files = []

# Function to extract MP3 file properties
def extract_mp3_properties(mp3_file):
    try:
        audio_file = eyed3.load(mp3_file)
        
        image = audio_file.tag.images[0]
        str = audio_file.tag.album
        hash_str = hashlib.md5(str.encode())
        cover_art = hash_str.hexdigest()
        output_filename = os.path.join("D:/new_images" ,f"{cover_art}.jpg")

        with open(output_filename, "wb") as f:
            f.write(image.image_data)
            
            
        
        properties = {
            "file_name": os.path.basename(mp3_file) or "",
            "title": audio_file.tag.title or "",
            "artist_name": audio_file.tag.artist or "",
            "artist": [] ,
            "album": audio_file.tag.album or "",
            "genre": [] or [],
            "duration": audio_file.info.time_secs,
            "year": audio_file.tag.recording_date.year or "",
            "coverArt":f"{str(uuid.uuid4())}.jpg",
        }
    except:
        print('failed to extract : ',os.path.basename(mp3_file))
        error_files.append(os.path.basename(mp3_file))
        return None
        
    return properties
    




folder_path = "D:/music_data_all/Newfolder"


mp3_properties_list = []


for filename in os.listdir(folder_path):
    if filename.endswith(".mp3"):
        mp3_file = os.path.join(folder_path, filename)
        mp3_properties = extract_mp3_properties(mp3_file)
        if(not mp3_properties) : continue
        mp3_properties_list.append(mp3_properties)


output_file = f"D:/music_data_all/({date.today()})11.json"

with open(output_file, "w", encoding='utf-8') as json_file:
    json.dump(mp3_properties_list, json_file, indent=4,ensure_ascii=False)

print(f"MP3 properties saved to {output_file}")






# for file_name in error_files:
#     print(file_name)
#     shutil.move(f'D:/music_data_all/{file_name[0]}',f'D:/music_data_all/fail_audio/')

