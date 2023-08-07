import requests
import json
import io

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
        print("Ses fayli muvaffaqiyatli yaratildi: audio_output.json")
    else:
        print("Xatolik sodir bo'ldi:", response.status_code, response.text)



def read_json_url(file_name="audio_output.json"):
    with open(file_name) as f:
        a = json.load(f)
    url = a['result']['url']
    return url


def save_audio_from_url(url: str) -> io.BytesIO:
    response = requests.get(url)
    audio_bytes = io.BytesIO(response.content)
    return audio_bytes