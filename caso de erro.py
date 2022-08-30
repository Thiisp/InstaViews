from instabot import Bot
import os
import glob

cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])

