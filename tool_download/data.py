import os
import json
import eyed3
import uuid
from datetime import date


# Function to extract MP3 file properties
def extract_mp3_properties(mp3_file):
    audiofile = eyed3.load(mp3_file)
    
    
    properties = {
        "file_name": os.path.basename(mp3_file) or "",
        "title": audiofile.tag.title or "",
        "artist_name": (audiofile.tag.artist) or "",
        "artist": [] ,
        "album": audiofile.tag.album or "",
        "genre": [],
        "duration": audiofile.info.time_secs,
        "year": audiofile.tag.recording_date.year or "",
        "coverArt":f"{str(uuid.uuid4())}.jpg",
        # You can add more properties as needed
    }
    
    image = audiofile.tag.images[0]

    # Create the output directory if it doesn't exist
    if not os.path.exists("D:\Automation"):
        os.makedirs("D:\Automation")

    # Construct the output filename
    output_filename = os.path.join("D:/new_images" ,f"{properties["coverArt"]}.jpg")

    # Save the album cover image to the specified output directory
    with open(output_filename, "wb") as f:
        f.write(image.image_data)

    return properties

# Folder containing the MP3 files
folder_path = "D:/music_data_all/audio"

# List to store the properties of all MP3 files
mp3_properties_list = []

# Iterate through the MP3 files in the folder
for filename in os.listdir(folder_path):
   
    if filename.endswith(".mp3"):
        mp3_file = os.path.join(folder_path, filename)
        mp3_properties = extract_mp3_properties(mp3_file)
        mp3_properties_list.append(mp3_properties)

# Save the properties to a JSON file
output_file = f"D:/music_data_all/({date.today()})3.json"
with open(output_file, "w") as json_file:
    json.dump(mp3_properties_list, json_file, indent=4)

print(f"MP3 properties saved to {output_file}")
