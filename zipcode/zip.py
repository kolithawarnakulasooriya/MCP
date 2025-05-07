from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

ZIP_CODE_URL = "https://api.zippopotam.us/us/"

zipcode_mcp = FastMCP("zipcode")

async def get_zip_code_info_helper(zipcode: str) -> dict[str, Any] | None:
    headers = {
        "Accept": "application/json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{ZIP_CODE_URL}{zipcode}", headers=headers)
            response.raise_for_status()
            response = response.json()
            return response
        except Exception:
            return None
        
@zipcode_mcp.tool()
async def get_zipcode_tool(zipcode: str) -> str:
    
    data = await get_zip_code_info_helper(zipcode)

    if not data:
        return "Unable to find the zip code information for the server"
    places = data.get("places")
    if len(places) > 0 :
        city = places[0].get("name")
        state = places[0].get("state")
        country = data.get("country")
        return f"{city},{state},{country}"
    else:
        return f"No Place Found for Zip Code {zipcode}"

if __name__ == "__main__":
    zipcode_mcp.run(transport='stdio')