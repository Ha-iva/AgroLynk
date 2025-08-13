# main.py
from config import settings
from apis.agmarknet import get_mandi_prices

# Example: Fetch wheat prices in Uttar Pradesh
commodity = "Rice"
state = "Uttar Pradesh"
district = "Ghaziabad"

prices = get_mandi_prices(settings.DATA_GOV_API_KEY, commodity, state, district)

# Print nicely
for p in prices:
    print(f"{p['commodity']} in {p['market']} ({p['district']}): {p['modal_price']} Rs/qtl on {p['arrival_date']}")
