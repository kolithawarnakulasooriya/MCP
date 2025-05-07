from zip import get_zip_code_info
import asyncio

async def main():
    print(await get_zip_code_info("33162"))

asyncio.run(main())
