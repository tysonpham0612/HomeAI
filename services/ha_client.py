import requests
from configs.config import HA_BASE_URL, HA_TOKEN

def send_ha_command(domain: str, service: str, entity_id: str):
    url = f"{HA_BASE_URL}/api/services/{domain}/{service}"
    headers = {
        "Authorization": f"Bearer {HA_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {"entity_id": entity_id}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()