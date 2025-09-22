# Local MCP Time Server

A lightweight Model Context Protocol (MCP) server that exposes a `current_time` tool for clients such as LM Studio. The tool returns the current time in ISO, locale, or epoch formats and supports optional timezone selection via IANA names—now your local LLM actually knows what time it is.

## Setup

1. Install Python 3.12 (see `.python-version`).
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Start the MCP server over stdio:

```bash
python time_server.py
```

Connect to the server from your MCP-compatible client (e.g., LM Studio) using the stdio transport.

```
{
  "mcpServers": {
    "local-time": {
      "command": "python",
      "args": [
        "/path/to/time_server.py"
      ]
    }
  }
}
```

## Tool Reference

`current_time(timezone_name: str | None = None, format: Literal["iso", "locale", "epoch"] = "iso")`

- `timezone_name` — Optional IANA timezone identifier. Defaults to UTC when omitted.
- `format`
  - `iso` (default): ISO 8601 timestamp including offset.
  - `locale`: Human-readable local format like `2025-09-22 13:45:12 HKT+0800`.
  - `epoch`: Unix timestamp in whole seconds.

Tip: When adding logging, write to stderr rather than stdout so the MCP transport remains valid.
