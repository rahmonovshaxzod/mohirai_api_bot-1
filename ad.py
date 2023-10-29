import requests
import os

def download_audio(url):
    file_name = 'a.wav'
    response = requests.get(url)
    if not os.path.exists('audios'):
        os.makedirs('audios')
    d1 = response.content
    with open(os.path.join('audios', file_name), 'wb') as file:
        file.write(d1)

