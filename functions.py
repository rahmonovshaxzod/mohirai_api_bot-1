import requests
import json
import io
from ad import download_audio

def create_json_file(text,author,api_key):
    url = "https://studio.mohir.ai/api/v1/tts"

    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "model": author
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        # Matn-to-ses natijasini faylga yozish
        with open("audio_output.json", "wb") as f:
            f.write(response.content)
        print("json fayli muvaffaqiyatli yaratildi: audio_output.json")
    else:
        print("Xatolik sodir bo'ldi:", response.status_code, response.text)



def read_json_url(file_name="audio_output.json"):
    with open(file_name) as f:
        a = json.load(f)
    url = a['result']['url']
    return url
def stt():
    api_key = "c28c44e2-4361-4649-bb61-e14f2469ddc1:87b18c62-b24f-4b3e-b3c7-93d5bae88033"
    audio_file_path = 'E:/github/mohirai_api_bot/audios2/voice.wav'

    url = "https://studio.mohir.ai/api/v1/stt"

    headers = {
        "Authorization": api_key
    }

    files = {
        "file": (audio_file_path, open(audio_file_path, "rb"))
    }

    # POST so'rovini yuborish
    response = requests.post(url, headers=headers, files=files)

    # Javobni qaytarish
    return response.json()['result']['text']
