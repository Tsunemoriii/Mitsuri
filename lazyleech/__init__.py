import os
import logging
import aiohttp
from io import BytesIO, StringIO
from pyrogram import Client

API_ID = os.environ.get('API_ID', '20628383')
API_HASH = os.environ.get('API_HASH', '65a242463b8af9ba7b3c41d8de9738d1')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '1881338776:AAFeT4_llHPqIEAvK7gZr6Cs-cDqvTLQPo4')
TESTMODE = os.environ.get('TESTMODE')
TESTMODE = TESTMODE and TESTMODE != '0'

EVERYONE_CHATS = os.environ.get('EVERYONE_CHATS')
EVERYONE_CHATS = list(map(int, EVERYONE_CHATS.split(' '))) if EVERYONE_CHATS else [-1001378211961]
ADMIN_CHATS = os.environ.get('ADMIN_CHATS', '-1001252296278')
ADMIN_CHATS = list(map(int, ADMIN_CHATS.split(' '))) if ADMIN_CHATS else [441422215]
ALL_CHATS = EVERYONE_CHATS + ADMIN_CHATS
# LICHER_* variables are for @animebatchstash and similar, not required
LICHER_CHAT = os.environ.get('LICHER_CHAT', '')
try:
    LICHER_CHAT = int(LICHER_CHAT)
except ValueError:
    pass
LICHER_STICKER = os.environ.get('LICHER_STICKER')
LICHER_FOOTER = os.environ.get('LICHER_FOOTER', '').encode().decode('unicode_escape')
LICHER_PARSE_EPISODE = os.environ.get('LICHER_PARSE_EPISODE')
LICHER_PARSE_EPISODE = LICHER_PARSE_EPISODE and LICHER_PARSE_EPISODE != '0'

PROGRESS_UPDATE_DELAY = int(os.environ.get('PROGRESS_UPDATE_DELAY', 5))
MAGNET_TIMEOUT = int(os.environ.get('LEECH_TIMEOUT', 60))
LEECH_TIMEOUT = int(os.environ.get('LEECH_TIMEOUT', 300))
ARIA2_SECRET = os.environ.get('ARIA2_SECRET', '')
IGNORE_PADDING_FILE = os.environ.get('IGNORE_PADDING_FILE', '1')
IGNORE_PADDING_FILE = IGNORE_PADDING_FILE and IGNORE_PADDING_FILE != '0'
DB_URL = os.environ.get('DB_URL', 'mongodb+srv://utahheroku10:utahheroku10@cluster0.lt5bp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
NYAA_RSS_LINKS = os.environ.get('NYAA_RSS_LINKS', 'https://nyaa.si/?page=rss&c=0_0&f=0&u=Ember_Encodes')
RSS_RECHECK_INTERVAL = os.environ.get('RSS_RECHECK_INTERVAL', '5')

logging.basicConfig(level=logging.INFO)
app = Client('lazyleech', API_ID, API_HASH, plugins={'root': os.path.join(__package__, 'plugins')}, bot_token=BOT_TOKEN, test_mode=TESTMODE, parse_mode='html', sleep_threshold=30)
session = aiohttp.ClientSession()
help_dict = dict()
preserved_logs = []

class SendAsZipFlag:
    pass

class ForceDocumentFlag:
    pass

def memory_file(name=None, contents=None, *, bytes=True):
    if isinstance(contents, str) and bytes:
        contents = contents.encode()
    file = BytesIO() if bytes else StringIO()
    if name:
        file.name = name
    if contents:
        file.write(contents)
        file.seek(0)
    return file
