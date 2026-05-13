import json
import urllib.request

from strands import Agent, tool
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from model.load import load_model

app = BedrockAgentCoreApp()
log = app.logger

SYSTEM_PROMPT = """You are a helpful weather assistant.
Use the get_weather tool to fetch current conditions and forecasts.
When comparing cities, call the tool for each location and summarize the differences clearly."""


@tool
def get_weather(location: str) -> str:
    """Get current weather conditions and 3-day forecast for a location.

    Args:
        location: City name and state (e.g., 'Austin TX', 'Seattle WA')

    Returns:
        Current conditions and 3-day forecast including temperature and precipitation
    """
    url = f"https://wttr.in/{location.replace(' ', '+')}?format=j1"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read())

        current = data['current_condition'][0]
        weather = data['weather']

        result = f"Weather for {location}:\n"
        result += (f"Current: {current['weatherDesc'][0]['value']}, "
                   f"{current['temp_F']}°F, "
                   f"Feels like {current['FeelsLikeF']}°F, "
                   f"Humidity: {current['humidity']}%\n")
        result += "3-Day Forecast:\n"
        for day in weather[:3]:
            result += (f"  {day['date']}: "
                       f"High {day['maxtempF']}°F / Low {day['mintempF']}°F, "
                       f"{day['hourly'][4]['weatherDesc'][0]['value']}\n")
        return result
    except Exception as e:
        return f"Error fetching weather for {location}: {str(e)}"


_agent = None


def get_or_create_agent():
    global _agent
    if _agent is None:
        _agent = Agent(
            model=load_model(),
            system_prompt=SYSTEM_PROMPT,
            tools=[get_weather],
        )
    return _agent


@app.entrypoint
async def invoke(payload, context):
    log.info("Invoking Agent...")
    agent = get_or_create_agent()
    stream = agent.stream_async(payload.get("prompt"))
    async for event in stream:
        if "data" in event and isinstance(event["data"], str):
            yield event["data"]


if __name__ == "__main__":
    app.run()
