import json
import  csv
import pandas as pd
csv_songs = 'id_songs.csv'
csv_songs_star = 'id_songs_star.csv'
def to_csv(csv_file_name,data):
    # Mở tệp CSV trong chế độ ghi (append mode)
    with open(csv_file_name, 'a', newline='',encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data.values())
    print("done")
# data1 = set()
#
# with open(csv_songs, 'r',encoding="utf8") as csv_file:
#     data_songs = csv.reader(csv_file)
#     for row in data_songs:
#         data1.add(tuple(row))
#
# data2 = set()
#
# with open(csv_songs_star, 'r',encoding="utf8") as csv_file:
#     data_songs_star = csv.reader(csv_file)
#     for row in data_songs_star:
#         data2.add(tuple(row))
#
# difference = data1.difference(data2)
# print(len(difference))
# csv_difference = 'id_difference.csv'
#
# json_songs = 'D:/Python/audioServerDev.Songs.json'
#
# data = pd.read_csv(csv_difference).values
#
# with open(json_songs,'r',encoding="utf-8") as json_file:
#     data_songs = json.load(json_file)
#
# for i in data:
#     for j in data_songs:
#        if i[0] == j['_id']['$oid']:
#            propertise = {
#                "title": j['title'],
#                "artist":j['artist_name']
#            }
#            to_csv('title_and_artist.csv',propertise)

with open("D:/Python/data.csv",'r',encoding='utf-8') as csv_file:
    data = csv.reader(csv_file)
    for i in data:
        print(i)
