pub mod inference {
    tonic::include_proto!("inference");
}
use tonic::Request;
use inference::{inference_client::InferenceClient, AudioRequest, DeepfakeResponse};
use bytes::Bytes;
use futures::stream::{self, StreamExt};
use std::path::Path;
use tokio::fs::File;
use async_stream::stream;  // Import async_stream crate
use std::time::Duration;
use tokio::io::{AsyncReadExt, AsyncSeekExt};
use tokio::time::sleep;


const AUDIO_FILE_PATH: &str = "sample-0.mp3"; // Adjust to your file's location


#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Connect to the gRPC server
    let mut client = InferenceClient::connect("http://localhost:50050").await?;

    // Prepare the stream of AudioRequest
    // let audio_data1 = Bytes::from_static(b"chunk1");
    // let audio_data2 = Bytes::from_static(b"chunk2");

    // let request = Request::new(
    //     stream::iter(vec![
    //         AudioRequest { audio_data: audio_data1.to_vec() },
    //         AudioRequest { audio_data: audio_data2.to_vec() },
    //     ]),
    // );

    let mut file = File::open(Path::new(AUDIO_FILE_PATH)).await?;

    const CHUNK_SIZE: usize = 1024 * 4;


    let audio_stream = stream! {
        let mut buffer = vec![0; CHUNK_SIZE];
        loop {
            // Read a chunk of the audio file into the buffer
            let bytes_read = match file.read(&mut buffer).await {
                Ok(0) => break, // EOF
                Ok(n) => n,
                Err(_) => break, // Error reading file
            };

            // Send the chunk as an AudioRequest
            yield AudioRequest {
                audio_data: buffer[..bytes_read].to_vec(),
            };

            // Simulate delay between chunks (like in Python)
            sleep(Duration::from_millis(100)).await;
        }
    };

    let request = Request::new(audio_stream);

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
