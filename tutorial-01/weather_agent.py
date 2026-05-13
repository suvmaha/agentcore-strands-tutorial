"""
Tutorial 01 — Your First Strands Agent
Demonstrates: http_request tool, two-hop reasoning, AgentResult metrics

Run on AI Dev Server (Bedrock via IAM role — no API keys needed):
    python3 weather_agent.py
"""

from strands import Agent
from strands_tools import http_request

agent = Agent(
    model="us.anthropic.claude-sonnet-4-5-20251001",
    tools=[http_request],
)

# Single-hop: one API call
print("=" * 60)
print("Query 1 — Single location")
print("=" * 60)
result = agent("What's the weather forecast for Austin, Texas?")

# Two-hop: agent sequences two API calls without being told how
print("\n" + "=" * 60)
print("Query 2 — Two-hop reasoning")
print("=" * 60)
result = agent(
    "Compare the weather forecast for Austin TX and Seattle WA. "
    "Which city has better weather this week?"
)

print("\n" + "=" * 60)
print("Agent Metrics")
print("=" * 60)
print(f"Stop reason:   {result.stop_reason}")
print(f"Input tokens:  {result.metrics.accumulated_usage['inputTokens']}")
print(f"Output tokens: {result.metrics.accumulated_usage['outputTokens']}")
