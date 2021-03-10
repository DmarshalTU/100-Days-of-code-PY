import requests
from bs4 import BeautifulSoup
from youtubesearchpython import VideosSearch

URL = f'https://www.billboard.com/charts/hot-100/{input("Enter the date YYYY-MM-DD: ")}'

response = requests.get(url=URL)
data = response.text

soup = BeautifulSoup(data, "html.parser")

songs = soup.find_all(class_="chart-element__information__song text--truncate color--primary")

song_names = []

for song in songs:
    name = song.getText()
    videosSearch = VideosSearch(name, limit=2)
    song_names.append({name, videosSearch.result()['result'][0]['link']})

print(song_names)

with open('songs.txt', 'w') as file:
    file.writelines("%s\n" % item for item in song_names)
