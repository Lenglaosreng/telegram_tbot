import asyncio
import logging
from server import start_webserver
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    asyncio.run(start_webserver())