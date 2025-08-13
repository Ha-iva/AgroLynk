# apis/weather.py
import requests
from typing import Dict, Any, List

def get_forecast_openweather(api_key: str, lat: float, lon: float, lang: str = "en") -> Dict[str, Any]:
    if not api_key:
        # Mock for demo when key missing
        return {"list": [
            {"dt_txt": "2025-08-13 12:00:00", "main": {"temp": 34.5}, "weather":[{"description":"clear sky"}]},
            {"dt_txt": "2025-08-13 15:00:00", "main": {"temp": 36.0}, "weather":[{"description":"few clouds"}]},
        ]}
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {"lat": lat, "lon": lon, "appid": api_key, "units": "metric", "lang": lang}
    r = requests.get(url, params=params, timeout=20)
    r.raise_for_status()
    return r.json()

def next_24h_rain_chance(forecast_json: Dict[str, Any]) -> float:
    # Very simple heuristic: if any weather description mentions rain in next ~8 slots, return 0.7 else 0.1
    slots = forecast_json.get("list", [])[:8]
    descs = " ".join([s["weather"][0]["description"] for s in slots if "weather" in s])
    return 0.7 if "rain" in descs.lower() else 0.1
