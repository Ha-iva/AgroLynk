import requests
import json
from config import settings  # Make sure settings.DATA_GOV_API_KEY is set

def test_reservoir_api(resource_id: str):
    url = f"https://api.data.gov.in/resource/{resource_id}"
    params = {
        "api-key": settings.DATA_GOV_API_KEY,
        "format": "json",
        "limit": 5
    }
    resp = requests.get(url, params=params, timeout=20)
    print("URL:", resp.url)
    print("Status:", resp.status_code)
    print("Response:\n", json.dumps(resp.json(), indent=2))
    return resp

# Example usage
if __name__ == "__main__":
    # Paste the correct resource ID below after you've copied it
    resource_id = "1fc2148c-fc41-46f5-a364-bdc03f77053f"
    test_reservoir_api(resource_id)
