import aiogram.types
from aiogram import Bot, Dispatcher,Router,F
from aiogram.filters import Command
from aiogram.types import Message
from asyncio import run
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import CallbackQuery
from os import getenv
from dotenv import load_dotenv
import sys
import logging
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
load_dotenv()
def get_inline()->InlineKeyboardMarkup:
    inline=InlineKeyboardBuilder()
    inline.button(text="Japan",callback_data="Japan")
    inline.button(text="Janubiy karea",callback_data="Janubiy karea")
    inline.button(text="Shvetsariya", callback_data="Shvetsariya")
    inline.button(text="Portugaliya", callback_data="Portugaliya")
    inline.button(text="Saudiya Arabiston", callback_data="Saudiya Arabiston")
    inline.button(text="Morokko", callback_data="Morokko")


    inline.adjust(2)
    return inline.as_markup()


def get_ha_yoq()->ReplyKeyboardMarkup:
    tt=ReplyKeyboardBuilder()
    tt.button(text="Ha")
    tt.button(text="Yoq")
    tt.adjust(2)
    return tt.as_markup(resize_keyboard=True)
def tozalash() -> InlineKeyboardMarkup:
    inline=InlineKeyboardBuilder()
    inline.button(text="Ha",callback_data="Ha")
    inline.button(text="Yo'q",callback_data="Yo'q")
    return inline.as_markup()
jj=Dispatcher()
my_router=Router()
jj.include_router(my_router)

tokenm=getenv("BOT_TOKEN")

global tanlov

@my_router.startup()
async def bot_ishlaganda(bot:Bot):
    await bot.send_message(chat_id=getenv("MY_ID"), text="Bot ishladi✅")

@my_router.shutdown()
async def bot_toxtaganda(bot:Bot):
    await bot.send_message(chat_id=getenv("MY_ID"), text="Bot toxtadi❌")
# @jj.message(Command("start"))
@my_router.message(Command("start"))
async def start_bosilganda(j:Message):
    await j.answer("Xush kelibsiz")
    await j.answer("Davlat tanlang",reply_markup=get_inline())

@my_router.message(F.data==("Ha"))
async def ha_tanlanganda(call:CallbackQuery):
    await call.message.delete_reply_markup()
    await call.message.delete()
    global tanlov
    matn=str(tanlov)
    await call.message.answer(f"{matn}ni tanladingiz")
    r=getenv("ADMINS")
    for i in r:
        await call.bot.send_message(chat_id=i,text=f"{call.from_user.full_name}ni tanladi")

@my_router.callback_query(F.data=="Japan")
async def Japan_bosilganda(call:CallbackQuery):
    await call.message.edit_text("Yaponiyani tanladingiz ")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    await call.message.answer("🇯🇵")

@my_router.callback_query(F.data=="Janubiy karea")
async def Janubiy_karea_bosilganda(call:CallbackQuery):
    await call.message.edit_text("Janubiy kareani tanladingiz ")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    await call.message.answer("🇰🇷")

@my_router.callback_query(F.data=="Shvetsariya")
async def Shvetsariya_bosilganda(call:CallbackQuery):
    await call.message.edit_text("Shvetsariya tanladingiz ")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    await call.message.answer("🇨🇭")

@my_router.callback_query(F.data=="Portugaliya")
async def Portugaliya_bosilganda(call:CallbackQuery):
    await call.message.edit_text("Portugaliya tanladingiz ")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    await call.message.answer("🇵🇹")

@my_router.callback_query(F.data=="Saudiya Arabiston")
async def Saudiya_Arabiston_bosilganda(call:CallbackQuery):
    await call.message.edit_text("Saudiya Arabiston tanladingiz ")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    await call.message.answer("🇸🇦")

@my_router.callback_query(F.data=="Morokko")
async def Morokko_bosilganda(call:CallbackQuery):
    await call.message.edit_text("Morokko tanladingiz ")
    await call.message.edit_reply_markup(reply_markup=tozalash())
    await call.message.answer("🇲🇦")

# @my_router.message(F.text.lower()=="ha")
# async def ha_tanlanganda(j:Message):
#     await j.answer("ooo buyuk vatanparvar",reply_markup=aiogram.types.ReplyKeyboardRemove())
#
# @my_router.message(F.text.lower()=="yoq")
# async def yoq_tanlanganda(g:Message):
#     await g.answer("yaxshi ish",reply_markup=aiogram.types.ReplyKeyboardRemove())


@my_router.message()
async def xabar_kelganda(m:Message,bot:Bot):
    await m.copy_to(chat_id=m.from_user.id)
    await m.copy_to(chat_id="6402500187")
    await m.answer(chat_id="6402500187",text=f"{m.from_user.full_name}sizning botingizga '{m.text}' deb yozdi")


@my_router.message
async def xabar_yuborilganda(j:Message):
    await j.copy_to(chat_id=j.from_user.id)
async def main():
    botim = Bot(token=tokenm,defoult=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await jj.start_polling(botim)
if __name__=="__main__":
    logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",\
handlers=[
    logging.FileHandler("bot.log"),
    logging.StreamHandler(sys.stdout)
    ])
    run(main())