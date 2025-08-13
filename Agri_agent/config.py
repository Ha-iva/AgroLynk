# config.py
from dataclasses import dataclass
import os

@dataclass
class Settings:
    # Agriculture & Market
    DATA_GOV_API_KEY: str = os.getenv("/resource/35985678-0d79-46b4-9ed6-6f13308a1d24", "579b464db66ec23bdd00000113c18681782c47e1421ddbd587190bd7")        # Agmarknet, mandi prices, crop data
    CROP_CALENDAR_API_KEY: str = os.getenv("CROP_CALENDAR_API_KEY", "")  # Sowing/harvest schedules
    SOIL_HEALTH_API_KEY: str = os.getenv("SOIL_HEALTH_API_KEY", "")  # Soil testing & fertility data
    FERTILIZER_API_KEY: str = os.getenv("FERTILIZER_API_KEY", "")    # Recommended fertilizers
    FPO_API_KEY: str = os.getenv("FPO_API_KEY", "")                  # Farmer Producer Org / FCI data

    # Weather, Water & Environment
    OPENWEATHER_API_KEY: str = os.getenv("OPENWEATHER_API_KEY", "")  # Weather forecasts
    CWC_WATER_API_KEY: str = os.getenv("CWC_WATER_API_KEY", "")      # Reservoir & irrigation data
    IMD_RAINFALL_API_KEY: str = os.getenv("IMD_RAINFALL_API_KEY", "")# Rainfall & climate data
    SATELLITE_API_KEY: str = os.getenv("SATELLITE_API_KEY", "")      # Satellite crop health imagery

    # Finance & Economy
    RBI_API_KEY: str = os.getenv("RBI_API_KEY", "")                  # Interest rates, lending data
    NSE_API_KEY: str = os.getenv("NSE_API_KEY", "")                  # Commodity futures prices

    # Policy & Schemes
    GOVT_POLICY_API_KEY: str = os.getenv("GOVT_POLICY_API_KEY", "")  # Government schemes & subsidies

    # AI / NLP
    HF_TOKEN: str = os.getenv("HF_TOKEN", "")                        # Hugging Face models

    # Default Location (for fallback queries)
    DEFAULT_STATE: str = "Uttar Pradesh"
    DEFAULT_CITY: str = "Kanpur"
    DEFAULT_LAT: float = 26.4499
    DEFAULT_LON: float = 80.3319

settings = Settings()
