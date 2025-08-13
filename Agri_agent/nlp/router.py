# nlp/router.py
from transformers import pipeline
import re

# Multilingual zero-shot classifier
zc = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")

INTENT_LABELS = [
    "market_price_query",
    "weather_forecast",
    "irrigation_advice",
    "government_scheme",
    "pest_diagnosis"
]

# Very small gazetteers for demo; extend with CSVs later
COMMODITIES = ["wheat", "rice", "paddy", "tomato", "onion", "cotton", "soybean", "maize", "chana", "tur"]
CITIES = ["kanpur", "lucknow", "pune", "delhi", "patna", "bengaluru", "mumbai", "hyderabad", "chennai", "jaipur"]
STATES = ["uttar pradesh", "maharashtra", "karnataka", "bihar", "tamil nadu", "telangana", "gujarat", "rajasthan", "madhya pradesh", "delhi"]

def detect_intent(text: str) -> str:
    result = zc(text, INTENT_LABELS, multi_label=False)
    return result["labels"][0]

def extract_entities(text: str) -> dict:
    t = text.lower()
    # Commodity
    commodity = None
    for c in COMMODITIES:
        if re.search(rf"\b{re.escape(c)}\b", t):
            commodity = c
            break
    # City/State
    city = None
    for c in CITIES:
        if re.search(rf"\b{re.escape(c)}\b", t):
            city = c.title()
            break
    state = None
    for s in STATES:
        if re.search(rf"\b{re.escape(s)}\b", t):
            state = s.title()
            break
    return {"commodity": commodity, "city": city, "state": state}
