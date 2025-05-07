from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio

server_params = StdioServerParameters(
    command="uv", 
    args=["run", "/Users/kolithawarnakulasooriya/Projects/MCP/zipcode/zip.py"], 
    env=None,
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            
            await session.initialize()
            tools = await session.list_tools()
            print(tools)
            result = await session.call_tool("get_zipcode_tool", arguments={"zipcode": "33162"})
            print(result)

if __name__ == "__main__":
    asyncio.run(run())