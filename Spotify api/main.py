from dotenv import load_dotenv
import os
from requests import post,get
import json
import csv
import pandas as pd

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    url ='https://accounts.spotify.com/api/token'
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type":"client_credentials",
            "client_id":"8e51166e34c84304a67e4b54ecf8c2e1",
            "client_secret":"65c7cd7d0f9e4cd4b83e1b21beffcc50"}
    result = post(url,headers=headers,data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization":"Bearer "+token}

def get_track(token,id):
    url = f'https://api.spotify.com/v1/tracks/{id}'
    headers = get_auth_header(token)

    try:
        result = get(url,headers=headers)
        json_result = json.loads(result.content)
    except:
        return None
    return json_result
def get_artists(token,artist_id):
    url = f'https://api.spotify.com/v1/artists/{artist_id}'
    headers = get_auth_header(token)

    try:
        result = get(url, headers=headers)
        json_result = json.loads(result.content)
    except:
        return None
    return json_result
def get_song_by_artist(token,artist_id):
    url = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=VN'
    headers = get_auth_header(token)
    try:
        result = get(url, headers=headers)
        json_result = json.loads(result.content)
    except:
        return None
    return json_result

def get_tracks_analysis(token,track_id):
    url = f'https://api.spotify.com/v1/audio-analysis/{track_id}'
    headers = get_auth_header(token)
    try:
        result = get(url, headers=headers)
        json_result = json.loads(result.content)
    except:
        return None
    return json_result

def get_playlist(token,playlist_id):
    url = f'https://api.spotify.com/v1/playlists/{playlist_id}?fields=tracks%28items.track.id%29'
    headers = get_auth_header(token)
    try:
        result = get(url, headers=headers)
        json_result = json.loads(result.content)
    except:
        return None
    return json_result

def get_tracks_audio_features(token,track_id):
    url = f'https://api.spotify.com/v1/audio-features/{track_id}'
    headers = get_auth_header(token)
    try:
        result = get(url, headers=headers)
        json_result = json.loads(result.content)
    except:
        return None
    return json_result
token = get_token()

csv_file_name = "data.csv"


def to_csv(csv_file_name,data):
    # Mở tệp CSV trong chế độ ghi (append mode)
    with open(csv_file_name, 'a', newline='',encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        # csv_writer.writerow(data.keys())
        csv_writer.writerow(data.values())
    print("done")
#array dictionary to json
def to_json(json_file_name,data):
    with open(json_file_name, "w",newline='') as json_file:
        json.dump(data, json_file)
# #get tracks_id from playlist_id
# csv_file_playlist_id = "id_playlist.csv"
# playlist_id = (get_playlist(token,"37i9dQZF1DXbLMw3ry7d7k")["tracks"])["items"]
#
# for i in range(len(playlist_id)):
#     arr_id = (playlist_id[i]['track'])
#     to_csv(csv_file_playlist_id,arr_id)

## get tracks_audio_features from tracks_id to csv

# df = pd.read_csv('id_playlist.csv')
# value_track_id = df.values[4686:]
# songs = get_tracks_audio_features(token, "6lbme14HiDWYmGiw1I2Dv6")
# print(songs)
# print(songs)
# for i in value_track_id:
#
#         songs = get_tracks_audio_features(token, str(i[0])) or ""
#         to_csv(csv_file_name,songs)


# get artist_id from track_id
# df = pd.read_csv('id_playlist.csv')
# value_track_id = df.values[4000:]
# artist_id_file = "artists_id.csv"
# for i in value_track_id:
#     artists_id = {"id":(get_track(token,str(i[0]))['album']['artists'])[0]['id']}
#     to_csv(artist_id_file,artists_id)

# get genre from artist_id
# genre_file = "genre.csv"
# df = pd.read_csv("artists_id.csv")
# value_artists_id = df.values[5000:]
# for i in value_artists_id:
#     genre = {"id":(get_artists(token,i[0]))["genres"]}
#     to_csv(genre_file,genre)

# properties = {}
# for i in value_track_id:
#     try:
#         properties = {
#         "name":str(get_track(token, i[0])["name"]) or "",
#         "artists":str((get_track(token, i[0])["artists"])[0]['name']) or ""
#         }
#     except:
#         None
#     to_csv("name_song_artist.csv", properties)
# print((get_track(token, "7L7UYxdL9yqBgZWjU1L0tW")["name"]))
# print((get_track(token, "7L7UYxdL9yqBgZWjU1L0tW")["artists"])[0]['name'])
# properties_track = []

# df = pd.read_csv('id_playlist.csv')
# value_track_id = df.values[:200]
# for i in value_track_id:
#     properties ={
#     "file_name":"",
#     "title": (get_track(token, str(i[0]))["name"] or ""),
#     "artist_name": ((get_track(token, str(i[0]))["artists"])[0]['name'] or ""),
#     "artist":[],
#     "album":(get_track(token,str(i[0]))["album"]["name"] or ""),
#     "genre":[],
#     "duration":(get_track(token,str(i[0]))["duration_ms"]/1000 or ""),
#     "year":(get_track(token,str(i[0]))["album"]["release_date"] or ""),
#     "coverArt":(get_track(token,str(i[0]))["album"]["images"][0]["url"] or "")
#     }
#     properties_track.append(properties)
#     print("done")
