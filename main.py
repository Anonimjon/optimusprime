from  aiogram import  Bot,Dispatcher  #Bot va Dispatcher chaqirilgan
from asyncio import  run    #Doimiy ishlab turadigan run metodi
from aiogram.filters import  Command  ,CommandStart #Buyruqlardan biri chaqirildi
from  aiogram.types import  Message #
t="7596232884:AAHKxD1G6sxix5D08kESxFLy-bCKOPOXKek"
dp=Dispatcher()
#Dekorat bilan Dispetchirga vazifalar yaratish
@dp.message(CommandStart)   #Xabar ko'rinishida
# javob beradigan dekorator Command("start") Start buyrug'i berilganda
async  def start_bosilganda(j:Message):
    await j.answer(f"Xush kelibsiz")
    # await  bot.send_message("692239005","Xush kelibsiz  2")
    await  j.delete()

async  def main():
    bot=Bot(token=t)
    # dp.message.register(start_bosilganda,CommandStart)
    await  dp.start_polling(bot)
run(main())
6228290478
7596232884:AAHKxD1G6sxix5D08kESxFLy-bCKOPOXKek