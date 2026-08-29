# gemini-rag-demo
# BigQuery Data Agent using Gemini & ADK

This repository showcases an AI Data Agent built with Google Agent Development Kit (ADK) and Gemini, integrated with Model Context Protocol (MCP) to query BigQuery datasets using natural language.

## Architecture
- **Agent Framework:** Google ADK (`LlmAgent`)
- **Model:** `gemini-3.6-flash`
- **Tooling:** BigQuery MCP Server (`McpToolset`)
- **Dataset:** NYC CitiBike Public Dataset (`bigquery-public-data.new_york_citibike`)

## Project Structure
```text
.
├── data_agent/
│   ├── __init__.py
│   └── agent.py
└── requirements.txt

Local Setup & Run
Clone the repository:
git clone [https://github.com/zahrakhorram2314-del/gemini-rag-demo.git](https://github.com/zahrakhorram2314-del/gemini-rag-demo.git)
cd gemini-rag-demo
Run local web UI using uv:
uv tool run --with "mcp==1.29.*" --from "google-adk[mcp]==2.4.*" adk web --agent data_agent
