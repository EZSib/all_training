
import logging
import asyncio
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# задаем уровень логов
logging.basicConfig(level=logging.INFO)
# создаем объекты бота и диспетчера
bot = Bot(token='YOUR_TOKEN_HERE')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
# создаем класс для получения ответа на вопрос
class QnA(StatesGroup):
    question = State()
    answer = State()
# создаем клавиатуру для выбора действий
markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup.add(KeyboardButton('Добавить раздел'))
markup.add(KeyboardButton('Просмотреть разделы'))
# обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_cmd_handler(message: types.Message):
    await message.answer("Привет! Я бот для ответов на вопросы. Выбери действие:", reply_markup=markup)
# обработчик команды /help
@dp.message_handler(commands=['help'])
async def help_cmd_handler(message: types.Message):
    help_text = "Список команд:\n/start - запустить бота\n/help - показать список команд\n"
    await message.answer(help_text)
# обработчик кнопки "Добавить раздел"
@dp.message_handler(Text(equals='Добавить раздел'))
async def add_section_handler(message: types.Message):
    await message.answer("Введите название раздела:")
    await QnA.question.set()
# обработчик ввода названия раздела
@dp.message_handler(state=QnA.question)
async def process_question(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question'] = message.text
    await message.answer("Введите ответ на вопрос:")
    await QnA.answer.set()
# обработчик ввода ответа на вопрос
@dp.message_handler(state=QnA.answer)
async def process_answer(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['answer'] = message.text
        # сохраняем раздел с ответом в базу данных
        # выход из состояния
        await state.finish()
    await message.answer(f"Раздел '{data['question']}' успешно добавлен!")
# обработчик кнопки "Просмотреть разделы"
@dp.message_handler(Text(equals='Просмотреть разделы'))
async def view_sections_handler(message: types.Message):
    # получаем список разделов из базы данных
    # создаем клавиатуру со списком разделов
    sections_markup = InlineKeyboardMarkup()
    for section in sections:
        sections_markup.add(InlineKeyboardButton(section['question'], callback_data=f"view_section_{section['id']}"))
    await message.answer("Выбери раздел:", reply_markup=sections_markup)
# обработчик нажатия кнопки на просмотр раздела
@dp.callback_query_handler(lambda c: c.data.startswith('view_section'))
async def process_callback_view_section(callback_query: types.CallbackQuery):
    section_id = int(callback_query.data.split('_')[2])
    # получаем раздел из базы данных
    # отправляем ответ на выбранный вопрос
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f"{section['answer']}", parse_mode=ParseMode.HTML)
# запускаем бота
async def main():
    # создаем таблицу в базе данных для хранения разделов
    # запускаем сервер для приема входящих сообщений
    await dp.start_polling()
if __name__ == '__main__':
    asyncio.run(main())