import grpc
from . import (
    inference_pb2,
    inference_pb2_grpc
)
from typing import List, Tuple
from logger import logger
from pydub import AudioSegment
import io
import asyncio

import os

INFERENCE_NAME = os.environ.get("INFERENCE_NAME")
INFERENCE_PORT = os.environ.get("INFERENCE_PORT")
INFERENCE_ADDRESS = f"{INFERENCE_NAME}:{INFERENCE_PORT}"

# Audio Format Constants
SAMPLE_RATE = 44100
CHANNELS = 2
SAMPLE_WIDTH = 2

async def classify_audio(audio_data: bytes) -> bool:
    channel = grpc.aio.insecure_channel(INFERENCE_ADDRESS)
    stub = inference_pb2_grpc.InferenceStub(channel)

    # Create a stream of audio data to send to the server
    async def audio_stream():
        audio_segment = AudioSegment(
            audio_data,
            frame_rate=SAMPLE_RATE,
            sample_width=SAMPLE_WIDTH,
            channels=CHANNELS
        )
        
        # Convert the chunk into a valid audio file format (e.g. WAV)
        with io.BytesIO() as audio_file:
            audio_segment.export(audio_file, format="wav")
            yield inference_pb2.AudioRequest(audio_data=audio_file.read())

    try:
        response_iterator = stub.ClassifyStream(audio_stream())

        async for response in response_iterator:
            logger.info(f"Received response: is_deepfake={response.is_deepfake}")
            return response.is_deepfake
    except asyncio.CancelledError:
        logger.error("The request was cancelled, either by timeout or by the server.")
    except grpc.aio.AioRpcError as e:
        logger.error(f"gRPC error: {e.details()} - {e.code()}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
    finally:
        await channel.close()