import requests
import os
from configs.config import HA_TOKEN
from configs.config import HA_URL

HEADERS = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "Content-Type": "application/json"
}


