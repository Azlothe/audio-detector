import librosa
import numpy as np

def extract_features(y, sr):
    features = {}
    features.update({f"mfcc_{i}": val for i, val in enumerate(np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20), axis=1))})
    features["chroma_mean"] = np.mean(librosa.feature.chroma_stft(y=y, sr=sr))  # Single chroma feature (mean of all bins)
    features["spectral_centroid"] = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
    features["spectral_bandwidth"] = np.mean(librosa.feature.spectral_bandwidth(y=y, sr=sr))
    features["spectral_rolloff"] = np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr))
    features["zero_crossing_rate"] = np.mean(librosa.feature.zero_crossing_rate(y=y))
    features["rms_energy"] = np.mean(librosa.feature.rms(y=y))
    return features