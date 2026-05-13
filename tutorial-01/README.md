# Tutorial 01 — Your First Strands Agent

Build a weather agent using Strands and a built-in tool. No API keys — runs on Bedrock via IAM role.

## What You'll Learn

- How Strands abstracts the agent loop
- The `http_request` tool — making API calls without writing tool code
- Two-hop reasoning — agent sequences multiple API calls autonomously
- `AgentResult` — built-in metrics for every agent run

## Run It

```bash
python3 weather_agent.py
```

## What's Happening

```python
agent = Agent(tools=[http_request])
agent("What's the weather forecast for Austin, Texas?")
```

Three lines. Strands handles the loop, tool dispatch, and conversation history.
The agent calls the NWS API, parses the response, and answers in plain English — no instructions needed.
