import telebot
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")#add your token from BotFather

bot = telebot.TeleBot(TOKEN)