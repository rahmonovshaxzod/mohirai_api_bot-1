from aiogram import Bot, types, Dispatcher, executor
import os
import logging
from functions import stt

API_TOKEN = '6556698243:AAELsOPgbSBsSLkjFk6AGa-6zLJKWxKeln0'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def save_voice(message: types.Message):
    # Agar "audios2" papkasi mavjud bo'lmasa, uni yaratish
    if not os.path.exists('audios2'):
        os.makedirs('audios2')

    # Voice faylini yuklab olish
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path

    # Yuklab olingan ma'lumotni faylga yozish
    with open(os.path.join('audios2', 'voice.wav'), 'wb') as audio_file:
        data = await bot.download_file(file_path)
        audio_file.write(data.read())


# Foydalanuvchi xabarini qabul qilish
@dp.message_handler(content_types=types.ContentType.VOICE)
async def handle_docs_photo(message: types.Message):
    await save_voice(message)
    await bot.send_message(message.from_user.id, stt())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
