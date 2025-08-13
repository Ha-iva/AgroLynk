# apis/agmarknet.py
import requests
from typing import List, Dict, Any
from config import settings

BASE = "https://api.data.gov.in/resource"
RESOURCE_ID = "35985678-0d79-46b4-9ed6-6f13308a1d24"

def get_mandi_prices(
    commodity: str,
    state: str = None,
    district: str = None,
    limit: int = 20,
    api_key: str = settings.DATA_GOV_API_KEY
) -> List[Dict[str, Any]]:
    if not api_key:
        # Mocked data for demo
        return [{
            "Commodity": commodity, "State": state or "Uttar Pradesh", "District": district or "Kanpur",
            "Market": "Kanpur", "Modal_Price": "2400", "Min_Price": "2000", "Max_Price": "2600", "Arrival_Date": "2025-08-12"
        }]
    
    params = {
        "api-key": api_key,
        "format": "json",
        "limit": limit,
        "filters[commodity]": commodity.title()
    }
    if state:
        params["filters[state]"] = state
    if district:
        params["filters[district]"] = district

    try:
        url = f"{BASE}/{RESOURCE_ID}"
        r = requests.get(url, params=params, timeout=20)
        r.raise_for_status()
        data = r.json()
        return data.get("records", [])
    except requests.exceptions.RequestException as e:
        return [{"error": f"Request failed: {str(e)}"}]
    except ValueError:
        return [{"error": "Invalid JSON format returned by API"}]
