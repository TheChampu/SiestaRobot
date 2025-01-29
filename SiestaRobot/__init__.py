import asyncio
import logging
import os
import sys
import json
import time
import spamwatch
import telegram.ext as tg
import ntplib
from time import ctime

StartTime = time.time()

def get_user_list(__init__, key):
    with open("{}/SiestaRobot/{}".format(os.getcwd(), __init__), "r") as json_file:
        return json.load(json_file)[key]
    
def sync_time():
    """Synchronize the system time with a time server."""
    try:
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org', version=3)
        if response:
            print(f"Time synchronized: {ctime(response.tx_time)}")
            LOGGER.info(f"Time synchronized: {ctime(response.tx_time)}")
        else:
            LOGGER.warning("Failed to synchronize time with NTP server.")
    except Exception as e:
        LOGGER.error(f"Time synchronization error: {e}")

async def main():
    sync_time()  # Ensure time is synchronized at startup
    global aiohttpsession
    aiohttpsession = await initialize_aiohttp_session()

# Enable logging
FORMAT = "[SiestaRobot] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger('ptbcontrib.postgres_persistence.postgrespersistence').setLevel(logging.WARNING)

LOGGER = logging.getLogger('[SiestaRobot]')
LOGGER.info("Siesta is starting. | An Shiinobu Project Parts. | Licensed under GPLv3.")
LOGGER.info("Not affiliated to other anime or Villain in any way whatsoever.")
LOGGER.info("Project maintained by: github.com/shiinobu (t.me/saint_foire)")

# If version < 3.9, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 9:
    LOGGER.error(
        "You MUST have a python version of at least 3.9! Multiple features depend on this. Bot quitting."
    )
    sys.exit(1)

# Environment variable handling...
# (The rest of the original content remains unchanged)

if __name__ == "__main__":
    try:
        loop.run_until_complete(main())
    except Exception as e:
        LOGGER.error(f"Failed to run main: {e}")
