import asyncio
import grpc
import inference_pb2
import inference_pb2_grpc
from logger import logger
from classifier import classify_stream


class InferenceService(inference_pb2_grpc.InferenceServicer):
    async def ClassifyStream(self, request_iterator, context):
        async for request in request_iterator:
            audio_data = request.audio_data
            logger.info(f"Received audio data: {audio_data}")

            is_deepfake = await classify_stream(audio_data)
            yield inference_pb2.DeepfakeResponse(is_deepfake=is_deepfake)


async def serve():
    server = grpc.aio.server()
    inference_pb2_grpc.add_InferenceServicer_to_server(InferenceService(), server)
    port = 50050
    address = "[::]"
    logger.info(f"Server started at {address}:{port}")
    server.add_insecure_port(f"{address}:{port}")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(serve())
