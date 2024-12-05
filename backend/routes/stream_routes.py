from fastapi import APIRouter, UploadFile, WebSocket, WebSocketDisconnect
from typing import List
from services.inference import classify_audio
from logger import logger
import random
import json
from services.inference import classify_audio

router = APIRouter(prefix="/inference")

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_bytes()
            # print(f"Received data: {data}")
            logger.debug(f"Received {len(data)} bytes of audio data.")

            payload = {
                "deepfake": await classify_audio(data)
            }
            await websocket.send_text(json.dumps(payload))
    except WebSocketDisconnect:
        print("Client disconnected")

# @router.post("/")
# async def infer_audio():
#     logger.info(
#         f"[POST : /inference"
#     )
#     await classify_audio()