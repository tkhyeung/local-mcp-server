from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Local Time Server")

@mcp.tool()
def current_time(
    timezone_name: str | None = None,
    format: str = "iso",
) -> str:
    """
    Return the current time.
    - timezone_name: IANA timezone defaults to UTC if not provided
    - format: 
        "iso"    -> ISO 8601 / RFC3339 format
        "locale" -> Human-readable local format
        "epoch"  -> Unix timestamp (seconds)
    """
    tz = ZoneInfo(timezone_name) if timezone_name else timezone.utc
    now = datetime.now(tz)

    if format == "epoch":
        return str(int(now.timestamp()))
    if format == "locale":
        # Example: 2025-09-22 13:45:12 HKT+0800
        return now.strftime("%Y-%m-%d %H:%M:%S %Z%z")
    # Default: ISO 8601 (with offset), e.g. 2025-09-22T13:45:12+08:00
    return now.isoformat(timespec="seconds")

if __name__ == "__main__":
    # Run as a stdio server (for LM Studio to connect)
    # IMPORTANT: Do not use print() to stdout in an MCP server
    # If you need logging, write to stderr using `logging`
    mcp.run()
