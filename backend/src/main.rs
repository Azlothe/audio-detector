pub mod inference {
    tonic::include_proto!("inference");
}
use tonic::Request;
use inference::{inference_client::InferenceClient, AudioRequest, DeepfakeResponse};
use bytes::Bytes;
use futures::stream::{self, StreamExt};


#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Connect to the gRPC server
    let mut client = InferenceClient::connect("http://localhost:50050").await?;

    // Prepare the stream of AudioRequest
    let audio_data1 = Bytes::from_static(b"chunk1");
    let audio_data2 = Bytes::from_static(b"chunk2");

    let request = Request::new(
        stream::iter(vec![
            AudioRequest { audio_data: audio_data1.to_vec() },
            AudioRequest { audio_data: audio_data2.to_vec() },
        ]),
    );

    // Make the stream request
    let mut response = client.classify_stream(request).await?.into_inner();

    // Process the responses from the stream
    while let Some(deepfake_response) = response.next().await {
        match deepfake_response {
            Ok(DeepfakeResponse { is_deepfake }) => {
                println!("Deepfake: {}", is_deepfake);
            }
            Err(e) => {
                eprintln!("Error receiving response: {}", e);
            }
        }
    }

    Ok(())
}
