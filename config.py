# +++ Modified By Yato [telegram username: @i_killed_my_clan & @ProYato] +++ # aNDI BANDI SANDI JISNE BHI CREDIT HATAYA USKI BANDI RAndi 
import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

# Recommended
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "29245477"))
API_HASH = os.environ.get("API_HASH", "0abc83883262245c90ca337b7a0375c4")

# Main
OWNER_ID = int(os.environ.get("OWNER_ID", "7654385403"))
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "cluster0")

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()] # dont change anything 
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @AnimeNexusNetwork</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "40"))
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

# Start pic
START_PIC_FILE_ID = "https://files.catbox.moe/jxbdb3.jpg"
START_IMG = "https://files.catbox.moe/jxbdb3.jpg"
# Messages
START_MSG = os.environ.get("START_MESSAGE", "<b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʟɪɴᴋs sʜᴀʀɪɴɢ ʙᴏᴛ. ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ʟɪɴᴋs ᴀɴᴅ ᴋᴇᴇᴘ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟs sᴀғᴇ ғʀᴏᴍ ɪssᴜᴇs.\n\n<blockquote>‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/EternalsHelplineBot'>ᴏᴡɴᴇʀ</a></blockquote></b>")
HELP = os.environ.get("HELP_MESSAGE", "<b><blockquote><a>Hᴇʟʟᴏ!! Wᴇʟᴄᴏᴍᴇ ᴛᴏ <a href=https://t.me/Anime_Eternals>Aɴɪᴍᴇ Eᴛᴇʀɴᴀʟs</a>\nYᴏᴜ ɴᴇᴇᴅ ᴛᴏ Jᴏɪɴ ɪɴ ᴍʏ Cʜᴀɴɴᴇʟ/Gʀᴏᴜᴘ ғɪʀsᴛ, Pʟᴇᴀsᴇ sᴜʙsᴄʀɪʙᴇ</a>\n\nHᴇʟᴘʟɪɴᴇ @EternalsHelplineBot</a>\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n\nsɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.!</a></blockquote></b>")
ABOUT = os.environ.get("ABOUT_MESSAGE", "<b><blockquote>◈sᴜᴘʀᴇᴀᴍ : <a href='https://t.me/AnimeNexusNetwork'>ɴᴇᴛᴡᴏʀᴋ</a>\n◈ᴀɴɪᴍᴇ : <a href='https://t.me/Anime_Eternals'>ᴀɴɪᴍᴇ ᴇᴛᴇʀɴᴀʟꜱ</a>\n◈ᴏɴɢᴏɪɴɢ ᴀɴɪᴍᴇ: <a href='https://t.me/Anime_Ongoing_Airing'>ᴏɴɢᴏɪɴɢ ᴀɪʀɪɴɢꜱ</a>\n◈ᴇᴄᴄʜɪ : <a href='https://t.me/Ecchi_Dex'>ᴇᴄᴄʜɪ ᴅᴇx</a>\n◈ʜᴇʟᴘʟɪɴᴇ : <a href='https://t.me/EternalsHelplineBot'>ʜᴇʟᴘʟɪɴᴇ</a></b></blockquote>")

ABOUT_TXT = """<b><blockquote>◈sᴜᴘʀᴇᴀᴍ : <a href='https://t.me/AnimeNexusNetwork'>ɴᴇᴛᴡᴏʀᴋ</a>\n◈ᴀɴɪᴍᴇ : <a href=https://t.me/Anime_Eternals''>ᴀɴɪᴍᴇ ᴇᴛᴇʀɴᴀʟꜱ</a>\n◈ᴏɴɢᴏɪɴɢ ᴀɴɪᴍᴇ: <a href='https://t.me/Anime_Ongoing_Airing'>ᴏɴɢᴏɪɴɢ ᴀɪʀɪɴɢꜱ</a>\n◈ʜᴇʟᴘʟɪɴᴇ : <a href='https://t.me/EternalsHelplineBot'>ʜᴇʟᴘʟɪɴᴇ</a></b></blockquote>""" # Bhosdiwalo agar developer me Yato ka username hataya to agli baar se koi repo public nhi krunga!!

CHANNELS_TXT = """<b><blockquote>◈sᴜᴘʀᴇᴀᴍ : <a href='https://t.me/AnimeNexusNetwork'>ɴᴇᴛᴡᴏʀᴋ</a>\n◈ᴀɴɪᴍᴇ : <a href=https://t.me/Anime_Eternals''>ᴀɴɪᴍᴇ ᴇᴛᴇʀɴᴀʟꜱ</a>\n◈ᴏɴɢᴏɪɴɢ ᴀɴɪᴍᴇ: <a href='https://t.me/Anime_Ongoing_Airing'>ᴏɴɢᴏɪɴɢ ᴀɪʀɪɴɢꜱ</a>\n◈ʜᴇʟᴘʟɪɴᴇ : <a href='https://t.me/EternalsHelplineBot'>ʜᴇʟᴘʟɪɴᴇ</a></b></blockquote>""" # Bhosdiwalo agar developer me Yato ka username hataya to agli baar se koi repo public nhi krunga!!

#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -
# Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "⚠️ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ᴍʏ ᴍᴀsᴛᴇʀ @EternalsHelplineBot🙃!"

# Logging
LOG_FILE_NAME = "links-sharingbot.txt"
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-1002880639258")) # Channel where user links are stored
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "7654385403").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Admin == OWNER_ID
ADMINS.append(OWNER_ID)
ADMINS.append(7654385403)


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
