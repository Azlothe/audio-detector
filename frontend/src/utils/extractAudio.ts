// Function to extract bytes of the audio from a specific starting time and duration in seconds
export async function extractBytes(audioBuffer: AudioBuffer, startTimeInSeconds: number, durationInSeconds: number): Promise<Uint8Array | null> {
  const sampleRate = audioBuffer.sampleRate;
  const totalDurationInSeconds = audioBuffer.duration;

  const startSampleIndex = Math.max(0, Math.min(startTimeInSeconds, totalDurationInSeconds) * sampleRate);
  const endSampleIndex = Math.min(audioBuffer.length, startSampleIndex + durationInSeconds * sampleRate);

  // Extract the PCM data for the specified time range (from startSampleIndex to endSampleIndex)
  const channelData = Array.from({ length: audioBuffer.numberOfChannels }, (_, channel) => audioBuffer.getChannelData(channel).slice(startSampleIndex, endSampleIndex));

  // Convert the PCM data to bytes (e.g., 16-bit PCM)
  const bytes = convertToBytes(channelData);

  return bytes;
}

function convertToBytes(channelData: Float32Array[]): Uint8Array {
  const bytes: number[] = [];

  channelData.forEach((channelSamples) => {
      channelSamples.forEach((sample) => {
          // Convert float sample to 16-bit PCM range
          const int16Sample = Math.floor(sample * 32767); // Assuming the sample is in the range [-1, 1]
          bytes.push((int16Sample >> 8) & 0xFF); // High byte
          bytes.push(int16Sample & 0xFF);        // Low byte
      });
  });

  return new Uint8Array(bytes);
}
