# tools/market_tool.py
from typing import Dict, Any
from apis.agmarknet import get_mandi_prices

def answer_market_price(api_key: str, commodity: str, state: str = None, city_or_district: str = None) -> Dict[str, Any]:
    records = get_mandi_prices(api_key, commodity, state, city_or_district, limit=5)
    if not records:
        return {"text": "कोई ताज़ा भाव नहीं मिला।", "sources": ["Agmarknet (data.gov.in)"], "confidence": "low"}
    r0 = records[0]
    text = f"आज {r0.get('market', city_or_district or '')} में {commodity.title()} का औसत भाव ₹{r0['modal_price']}/क्विंटल है (तारीख: {r0['arrival_date']})."
    return {"text": text, "raw": records, "sources": ["Agmarknet (data.gov.in)"], "confidence": "medium"}

# tools/weather_tool.py
from typing import Dict, Any
from apis.weather import get_forecast_openweather, next_24h_rain_chance

def answer_weather(api_key: str, lat: float, lon: float, lang: str = "hi") -> Dict[str, Any]:
    fc = get_forecast_openweather(api_key, lat, lon, lang)
    rain_p = next_24h_rain_chance(fc)
    risk = "बारिश की संभावना अधिक" if rain_p > 0.5 else "बारिश की संभावना कम"
    text = f"अगले 24 घंटे: {risk}. (अनुमानित संभावना: {int(rain_p*100)}%)."
    return {"text": text, "raw": fc, "sources": ["OpenWeatherMap"], "confidence": "medium"}
