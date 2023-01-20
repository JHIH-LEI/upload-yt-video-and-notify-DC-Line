from linebot import LineBotApi
from linebot.models import TextSendMessage

from dotenv import load_dotenv
from os import getenv

load_dotenv()


def notify_to_line(message):
    line_bot_api = LineBotApi(getenv('LINE_CHANNEL_ACCESS_TOKEN'))
    line_bot_api.broadcast(TextSendMessage(text=message))