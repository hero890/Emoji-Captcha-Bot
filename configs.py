# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 22672907))
    API_HASH = os.environ.get("API_HASH", "0ff15ae2153bd8e03b48cb293010bc6a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7087741098:AAFhQ6yKXdScmNcKPlutvHL1sHhUKdb5dws")
    SESSION_NAME = os.environ.get("SESSION_NAME", "URL_TO_Video_File_Bot")
    GROUP_CHAT_ID = int(os.environ.get("GROUP_CHAT_ID", -1002088051309))
