import asyncio
import logging
import time

import websockets

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


async def ping_server():
    while True:
        try:
            async with websockets.connect("ws://server:8000/ws") as websocket:
                logger.info("Connected to server")
                while True:
                    message = "ping"
                    await websocket.send(message)
                    logger.info(f"> {message}")
                    greeting = await websocket.recv()
                    logger.info(f"< {greeting}")
                    logger.info("Sleeping for 3 seconds...")
                    time.sleep(3)
        except OSError as exc:
            logger.error(str(exc))
            logger.error("Server is not running")
            await asyncio.sleep(5)
            continue
        except KeyboardInterrupt:
            await websocket.close()
            logger.info("Disconnected from server")
        except websockets.exceptions.ConnectionClosedError:
            logger.error("Server closed connection")
            await asyncio.sleep(5)
            continue


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(ping_server())
