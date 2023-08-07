import logging

from aiogram import Bot, Dispatcher, executor, types
import requests
from main import create_json_file, read_json_url


def save_file_from_url(url: str, filename: str):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

API_TOKEN = '6556698243:AAELsOPgbSBsSLkjFk6AGa-6zLJKWxKeln0'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Assalomu alaykum qaysi ovoz kerak o'g'il bola (2ni yuboring) qiz bola (1 ni yuboring) va bitta probel tashab textni yuborng")



@dp.message_handler()
async def echo(message: types.Message):
    t = message.text
    author = message.text.split(" ")[0]
    textt = message.text.split(" ")[1:]
    text = ""
    for i in textt:
        text += f"{i} "
    k = "ccccfc55-eb2c-4054-ae0d-53800b4dc9f6:3732419b-bce7-472c-bd8c-b639128a28fc"
    if author == "1":
        author = "dilfuza"
    if author == "2":
        author = "davron"
    print(author)
    print(text)
    create_json_file(text,author,k)
    url = read_json_url()
    await message.answer(url)
    # file_au = "aa.mp3"
    # save_file_from_url(url, file_au)
    # await bot.send_audio(message.from_user.id, open("aa.mp3", "r"))
    # await bot.send_audio(chat_id=message.chat.id, audio=url)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

