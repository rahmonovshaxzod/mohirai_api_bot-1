# import logging
#
# from aiogram import Bot, Dispatcher, executor, types
# import requests
# from functions import create_json_file, read_json_url
# from ad import download_audio
# import os
#
# def save_file_from_url(url: str, filename: str):
#     response = requests.get(url)
#     with open(filename, 'wb') as f:
#         f.write(response.content)
#
# API_TOKEN = '6556698243:AAELsOPgbSBsSLkjFk6AGa-6zLJKWxKeln0'
#
# # Configure logging
# logging.basicConfig(level=logging.INFO)
#
# # Initialize bot and dispatcher
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
#
#
# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     await message.answer(
#         "Assalomu alaykum qaysi ovoz kerak o'g'il bola (2ni yuboring) qiz bola (1 ni yuboring) va bitta probel tashab textni yuborng")
#
#
# async def send_voice(chat_id,file_name):
#
#     # Voice faylini yuklash
#     with open(f'E:\github\mohirai_api_bot/audios/'+str(file_name[0]), 'rb') as audio_file:
#         await bot.send_voice(chat_id, audio_file)
#
#
# @dp.message_handler()
# async def echo(message: types.Message):
#     t = message.text
#     author = message.text.split(" ")[0]
#     textt = message.text.split(" ")[1:]
#     text = ""
#     for i in textt:
#         text += f"{i} "
#     k = "c28c44e2-4361-4649-bb61-e14f2469ddc1:87b18c62-b24f-4b3e-b3c7-93d5bae88033"
#     if author == "1":
#         author = "dilfuza"
#     if author == "2":
#         author = "davron"
#     print(author)
#     print(text)
#     create_json_file(text,author,k)
#     url = read_json_url()
#     download_audio(url)
#     audio_file = os.listdir('E:/github/mohirai_api_bot/audios')
#     print(audio_file)
#     await send_voice(chat_id=message.from_user.id,file_name=audio_file)
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
#
