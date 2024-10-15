# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23401377"))
API_HASH = getenv("API_HASH", "a253e1cdcb1bdbad27dc4f1fcefca125")
BOT_TOKEN = getenv("BOT_TOKEN", "7606701563:AAFMSIS1sKFCp4jiDx4NtR3bcnGH1SwUmVs")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7608856647").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://rajeshgiri3824ptc:amangiri1026gms@cluster0.aqxkd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "1002326063269")
CHANNEL_ID = int(getenv("CHANNEL_ID", "amangiribot"))
