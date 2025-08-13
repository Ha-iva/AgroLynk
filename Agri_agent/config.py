from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    # Agriculture & Market
    DATA_GOV_BASE_URL: str = os.getenv("DATA_GOV_BASE_URL")
    DATA_GOV_API_KEY: str = os.getenv("DATA_GOV_API_KEY")
    
    CROP_CALENDAR_API_KEY: str = os.getenv("CROP_CALENDAR_API_KEY")
    SOIL_HEALTH_API_KEY: str = os.getenv("SOIL_HEALTH_API_KEY")
    FERTILIZER_API_KEY: str = os.getenv("FERTILIZER_API_KEY")
    FPO_API_KEY: str = os.getenv("FPO_API_KEY")

    # Weather, Water & Environment
    OPENWEATHER_BASE_URL: str = os.getenv("OPENWEATHER_BASE_URL")
    OPENWEATHER_API_KEY: str = os.getenv("OPENWEATHER_API_KEY")

    CWC_WATER_BASE_URL: str = os.getenv("CWC_WATER_BASE_URL")
    CWC_WATER_API_KEY: str = os.getenv("CWC_WATER_API_KEY")

    IMD_RAINFALL_BASE_URL: str = os.getenv("IMD_RAINFALL_BASE_URL")
    IMD_RAINFALL_API_KEY: str = os.getenv("IMD_RAINFALL_API_KEY")

    SATELLITE_API_KEY: str = os.getenv("SATELLITE_API_KEY")

    # Finance & Economy
    RBI_API_KEY: str = os.getenv("RBI_API_KEY")
    NSE_API_KEY: str = os.getenv("NSE_API_KEY")

    # Policy & Schemes
    GOVT_POLICY_API_KEY: str = os.getenv("GOVT_POLICY_API_KEY")

    # AI / NLP
    HF_TOKEN: str = os.getenv("HF_TOKEN")

    # Default location
    DEFAULT_STATE: str = "Uttar Pradesh"
    DEFAULT_CITY: str = "Kanpur"
    DEFAULT_LAT: float = 26.4499
    DEFAULT_LON: float = 80.3319

settings = Settings()


'''Find CROP_CALENDAR_API_KEY
SOIL_HEALTH_API_KEY
FERTILIZER_API_KEY
FPO_API_KEY
SATELLITE_API_KEY
RBI_API_KEY
NSE_API_KEY
GOVT_POLICY_API_KEY'''


# # config.py
# from dataclasses import dataclass
# import os

# @dataclass
# class Settings:
#     # Agriculture & Market
#     CROP_CALENDAR_API_KEY: str = os.getenv("CROP_CALENDAR_API_KEY", "")  # Sowing/harvest schedules
#     SOIL_HEALTH_API_KEY: str = os.getenv("SOIL_HEALTH_API_KEY", "")  # Soil testing & fertility data
#     FERTILIZER_API_KEY: str = os.getenv("FERTILIZER_API_KEY", "")    # Recommended fertilizers
#     FPO_API_KEY: str = os.getenv("FPO_API_KEY", "")                  # Farmer Producer Org / FCI data

#     # Weather, Water & Environment
#     SATELLITE_API_KEY: str = os.getenv("SATELLITE_API_KEY", "")      # Satellite crop health imagery

#     # Finance & Economy
#     RBI_API_KEY: str = os.getenv("RBI_API_KEY", "")                  # Interest rates, lending data
#     NSE_API_KEY: str = os.getenv("NSE_API_KEY", "")                  # Commodity futures prices

#     # Policy & Schemes
#     GOVT_POLICY_API_KEY: str = os.getenv("GOVT_POLICY_API_KEY", "")  # Government schemes & subsidies

#     # AI / NLP
#     HF_TOKEN: str = os.getenv("HF_TOKEN", "")  # Hugging Face models


