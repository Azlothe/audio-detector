import pandas as pd
from .models import random_forest_model
from .utils import (
    extract_features,
    audio_bytes_to_numpy
)
from logger import logger
from sklearn.preprocessing import StandardScaler

# scaler = StandardScaler()
# scaler.fit([[0] * 26])

async def classify_stream(audio_data: bytes) -> bool:
    y, sr = audio_bytes_to_numpy(audio_data)
    features = extract_features(y, sr)
    feature_df = pd.DataFrame([features])
    # feature_scaled = scaler.transform(feature_df)
    predictions = random_forest_model.predict(feature_df)
    
    logger.info(f"Prediction: {predictions}")

    return bool(predictions[0])