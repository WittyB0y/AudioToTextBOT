from audioToText import audio_to_text
from aiogram import Bot, Dispatcher, executor, types
from key import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(msg: types.Message):
    name = msg.from_user.first_name.capitalize()
    await msg.reply(f"Привет, {name}!\nЯ -- Аудиобот. Согласись, это бесит, когда ты на парах, а друг скидыват "
                    f"голосовуху на 5 минут?!))\nЯ помогу тебе избежать ненужного стресса. Просто перешли мне "
                    f"сообщение, а я отправлю тебе текст сообщения.")


@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def audio_message_handler(msg: types.Message):
    num_of_msg = msg.message_id
    id_user = msg.from_user.id
    res = await msg.voice.download(make_dirs=f'voice\\{id_user}',
                                   destination_file=f'voice\\{id_user}\\{num_of_msg}.oga')
    text = audio_to_text(res.name)
    await bot.send_message(chat_id=msg.chat.id, text=f'{text}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
