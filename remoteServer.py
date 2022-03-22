from websockets import serve
import asyncio

async def echo(websocket):
    async for message in websocket:
        await websocket.send(f"Recived data: {message}...")
        print(f"Recived data: {message}...")


async def main():
    async with serve(echo, "localhost", 8000):
        await asyncio.Future()  # run forever

asyncio.run(main())