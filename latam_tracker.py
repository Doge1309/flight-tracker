import requests
import json

url = "https://www.latamairlines.com/bff/air-offers/v2/offers/search"

params = {
    "adult": 1,
    "child": 0,
    "infant": 0,
    "locale": "es-co",
    "origin": "SCL",
    "destination": "ZCO",
    "inFrom": "2026-08-15",
    "outFrom": "2026-08-12",
    "cabinType": "Economy",
    "sort": "RECOMMENDED",
    "redemption": "false"
}

headers = {
    "accept": "application/json"
}

r = requests.get(url, params=params, headers=headers, timeout=30)

print("STATUS:", r.status_code)

try:
    data = r.json()
    print(json.dumps(data, indent=2)[:5000])
except Exception:
    print(r.text[:5000])
