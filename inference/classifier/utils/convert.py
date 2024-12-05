from pydub import AudioSegment
import numpy as np
import io


def audio_bytes_to_numpy(audio_data: bytes):
    audio = AudioSegment.from_file(io.BytesIO(audio_data))

    samples = np.array(audio.get_array_of_samples())
    samples = samples.astype(np.float32)
    samples /= 2**15

    return samples, audio.frame_rate
