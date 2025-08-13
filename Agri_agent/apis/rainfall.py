# apis/rainfall.py
import requests
import json
from config import settings

# TODO: Replace with actual rainfall resource ID from data.gov.in
RESOURCE_ID = "6c05cd1b-ed59-40c2-bc31-e314f39c6971"
BASE_URL = "https://api.data.gov.in/resource"

def get_rainfall_data(
    state: str = None,
    district: str = None,
    station: str = None,
    limit: int = 10,
    debug: bool = True
):
    params = {
        "api-key": settings.DATA_GOV_API_KEY,
        "format": "json",
        "limit": limit
    }
    if state:
        params["filters[State]"] = state
    if district:
        params["filters[District]"] = district
    if station:
        params["filters[Station]"] = station

    url = f"{BASE_URL}/{RESOURCE_ID}"
    resp = requests.get(url, params=params, timeout=20)

    if debug:
        print(f"[DEBUG] Request URL: {resp.url}")
        print(f"[DEBUG] Status Code: {resp.status_code}")

    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"[ERROR] HTTP Error: {e}")
        return []

    data = resp.json()

    if debug:
        print("[DEBUG] API Response:")
        print(json.dumps(data, indent=2))

    records = data.get("records", [])
    if not records:
        print("[WARNING] No records returned — check RESOURCE_ID or filters.")
    return records


# Example usage
if __name__ == "__main__":
    result = get_rainfall_data(state="Uttar Pradesh", limit=5)
    print("\nRainfall Data:")
    print(json.dumps(result, indent=2))
