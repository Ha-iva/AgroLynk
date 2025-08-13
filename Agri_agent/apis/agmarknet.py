# apis/agmarknet.py
import requests
from typing import List, Dict, Any

BASE = "https://api.data.gov.in/resource"
# Popular resource ID for daily prices (example; confirm on data.gov.in)
RESOURCE_ID = "9ef84268-d588-465a-a308-a864a43d0070"

def get_mandi_prices(api_key: str, commodity: str, state: str = None, district: str = None, limit: int = 20) -> List[Dict[str, Any]]:
    if not api_key:
        # Return mocked data if no key (for demo)
        return [{
            "commodity": commodity, "state": state or "Uttar Pradesh", "district": district or "Kanpur",
            "market": "Kanpur", "modal_price": "2400", "min_price": "2000", "max_price": "2600", "arrival_date": "2025-08-12"
        }]
    params = {
        "api-key": api_key,
        "format": "json",
        "limit": limit,
        "filters[commodity]": commodity.title()
    }
    if state: params["filters[state]"] = state
    if district: params["filters[district]"] = district

    url = f"{BASE}/{RESOURCE_ID}"
    r = requests.get(url, params=params, timeout=20)
    r.raise_for_status()
    data = r.json()
    return data.get("records", [])
