import logging

from fastapi import FastAPI, WebSocket
from starlette.websockets import WebSocketDisconnect

app = FastAPI()


@app.websocket("/ws")
async def ping_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            if data.lower() == "ping":
                await websocket.send_text("pong")
    except WebSocketDisconnect:
        logging.info("Client disconnected")
