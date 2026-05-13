# AgentCore + Strands Tutorial Series

Build AI agents with the Strands framework and deploy them to Amazon Bedrock AgentCore Runtime — end to end.

## The Stack

- **[Strands Agents](https://strandsagents.com)** — AWS open-source Python SDK for building agents
- **[Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)** — managed runtime that hosts Strands agents in production
- **AWS AI Dev Server** — EC2 + IAM role, Bedrock access, no API keys in code

## Prerequisites

- AWS account with Bedrock access enabled
- AI Dev Server running ([setup guide](https://medium.com/@jdluther2020))
- Python 3.11+

## Tutorials

| Tutorial | Title | Focus |
|----------|-------|-------|
| [01](./tutorial-01/) | Your First Strands Agent | `http_request`, NWS weather API, two-hop reasoning |
| [02](./tutorial-02/) | Custom Tools | `@tool` decorator, boto3, querying your AWS environment |
| [03](./tutorial-03/) | The Strands Toolbox | Complete directory of `strands-agents-tools` (40 tools) |
| [04](./tutorial-04/) | Natural Language SQL | `strands-sql`, ask your database in plain English |
| 05–11 | AgentCore CLI | Scaffold → Deploy → Observe → Memory → Payments |

## Setup

```bash
pip install strands-agents strands-agents-tools
```

No API keys needed — runs on Bedrock via IAM role.

## Series on Medium

[AI & ML Human Training/Coaching](https://medium.com/@jdluther2020)
