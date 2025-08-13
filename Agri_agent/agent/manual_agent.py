# agent/manual_agent.py
from typing import Dict, Any
from config import settings
from nlp.router import detect_intent, extract_entities
from tools.market_tool import answer_market_price
from tools.weather_tool import answer_weather

def handle_query(text: str) -> Dict[str, Any]:
    intent = detect_intent(text)
    slots = extract_entities(text)

    if intent == "market_price_query":
        if not slots.get("commodity"):
            return {"text": "कौन-सी फसल का भाव चाहिए?", "intent": intent, "need": "commodity"}
        return {
            "intent": intent,
            **answer_market_price(
                settings.DATA_GOV_API_KEY,
                commodity=slots["commodity"],
                state=slots.get("state") or settings.DEFAULT_STATE,
                city_or_district=slots.get("city")
            )
        }

    if intent in ["weather_forecast", "irrigation_advice"]:
        # You can enhance: geocode city->lat/lon
        return {
            "intent": intent,
            **answer_weather(settings.OPENWEATHER_API_KEY, settings.DEFAULT_LAT, settings.DEFAULT_LON, lang="hi")
        }

    # Stubs for other intents
    if intent == "government_scheme":
        return {"intent": intent, "text": "योजना मिलान जल्द जोड़ा जाएगा।", "sources": ["MyGov"], "confidence": "low"}
    if intent == "pest_diagnosis":
        return {"intent": intent, "text": "पत्ते की फोटो अपलोड करें ताकि रोग पहचान हो सके।", "confidence": "low"}

    return {"intent": intent, "text": "माफ़ कीजिए, समझ नहीं पाया। कृपया दोबारा पूछें।", "confidence": "low"}
