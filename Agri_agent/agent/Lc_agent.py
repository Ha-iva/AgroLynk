# agent/lc_agent.py
from typing import Dict, Any
from langchain.tools import tool
from langchain.agents import initialize_agent, AgentType
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
from config import settings
from apis.agmarknet import get_mandi_prices
from apis.weather import get_forecast_openweather

# 1) Define tools
@tool("get_market_price", return_direct=False)
def get_market_price_tool(commodity: str, state: str = "Uttar Pradesh", district: str = None) -> str:
    """Return recent mandi prices for a commodity in a given state/district (Agmarknet)."""
    recs = get_mandi_prices(settings.DATA_GOV_API_KEY, commodity, state, district, limit=3)
    if not recs:
        return "No recent records."
    lines = [f"{r['arrival_date']} | {r['market']} | ₹{r['modal_price']}/q" for r in recs]
    return "\n".join(lines)

@tool("get_weather_brief", return_direct=False)
def get_weather_brief_tool(lat: float, lon: float, lang: str = "en") -> str:
    """Return a brief next-24h forecast heuristic from OpenWeatherMap."""
    fc = get_forecast_openweather(settings.OPENWEATHER_API_KEY, lat, lon, lang)
    desc = fc["list"][0]["weather"][0]["description"] if fc.get("list") else "N/A"
    temp = fc["list"][0]["main"]["temp"] if fc.get("list") else "N/A"
    return f"Next slot: {desc}, temp {temp}°C."

# 2) LLM (local HF pipeline)
def build_llm():
    tok = AutoTokenizer.from_pretrained("google/flan-t5-base")
    mdl = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
    pipe = pipeline("text2text-generation", model=mdl, tokenizer=tok, max_new_tokens=256)
    return HuggingFacePipeline(pipeline=pipe)

def build_agent():
    llm = build_llm()
    tools = [get_market_price_tool, get_weather_brief_tool]
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )
    return agent

# 3) Usage
# agent = build_agent()
# resp = agent.run("आज कानपुर में टमाटर का भाव बताओ।")
# print(resp)
