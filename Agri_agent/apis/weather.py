# apis/weather.py
import requests
from typing import Dict, Any

# Try to import settings from config.py (project mode)
try:
    from config import settings
    DEFAULT_API_KEY = getattr(settings, "OPENWEATHER_API_KEY", "")
except ImportError:
    # Fallback for standalone run
    DEFAULT_API_KEY = "cebfe2bfcbc0e2500038f2bf9ba7cf2f"  # Your API key here


def get_forecast_openweather(
    lat: float,
    lon: float,
    api_key: str = DEFAULT_API_KEY,
    lang: str = "en"
) -> Dict[str, Any]:
    """
    Get 5-day / 3-hour weather forecast from OpenWeatherMap.
    If API key is missing, returns mock data.
    """
    if not api_key:
        # Mock for demo when key missing
        return {
            "list": [
                {"dt_txt": "2025-08-13 12:00:00", "main": {"temp": 34.5}, "weather": [{"description": "clear sky"}]},
                {"dt_txt": "2025-08-13 15:00:00", "main": {"temp": 36.0}, "weather": [{"description": "few clouds"}]},
            ]
        }

    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric",
        "lang": lang
    }

    try:
        r = requests.get(url, params=params, timeout=20)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except ValueError:
        return {"error": "Invalid JSON format from API"}


def next_24h_rain_chance(forecast_json: Dict[str, Any]) -> float:
    """
    Very simple heuristic:
    - Checks first ~24h (8 slots of 3 hours) for 'rain' in description.
    - Returns 0.7 if rain detected, else 0.1.
    """
    slots = forecast_json.get("list", [])[:8]
    descs = " ".join(
        [s.get("weather", [{}])[0].get("description", "") for s in slots]
    )
    return 0.7 if "rain" in descs.lower() else 0.1


# Standalone test
# if __name__ == "__main__":
#     data = get_forecast_openweather(lat=28.6139, lon=77.2090)  # Delhi
#     print("Rain chance (next 24h):", next_24h_rain_chance(data))
