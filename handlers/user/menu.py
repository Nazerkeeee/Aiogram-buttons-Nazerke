from aiogram.dispatcher.filters import Command,Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from keyboards.default import menu


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("She ... to school everyday", reply_markup=menu)


@dp.message_handler(Text(equals=["goes", "go", "went","gone"]))
async def get_food(message: Message):
    await message.answer(f"Choosen {message.text}. Thanks", reply_markup=ReplyKeyboardRemove())
    if "goes" == message.text :
        await message.answer( "true")
    elif "go" == message.text :
        await message.answer( "false")
    elif "went" == message.text :
        await message.answer( "false")
    elif "gone" == message.text :
        await message.answer( "false")

    dp.send_message(message.chat.id, "true")

# @dp.message_handler(Command("question_2"))
# async def show_menu(message: Message):
#     await message.answer("She .... her homework yesterday", reply_markup=menu)



