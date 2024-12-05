<script lang="ts">
	import InnerGlowVisualizer from '$lib/visualizations/core/InnerGlowVisualizer.svelte';
	import Glow from '$lib/visualizations/core/Glow.svelte';
	import AudioFrequency from '$lib/visualizations/audio/AudioFrequency.svelte';
	import { WavRecorder, AudioFilePlayer } from '$lib/visualizations/wavtools';
	import CircleBarAudioVisualizer from '$lib/visualizations/audio/CircleBarAudioVisualizer.svelte';
	import BarAudioVisualizer from '$lib/visualizations/audio/BarAudioVisualizer.svelte';
	import { onMount } from 'svelte';
	import { connect, UPDATE_INTERVAL } from '../../../services/AudioStreamer';
	import { extractBytes } from '../../../utils/extractAudio';

	export let file: File;
	export let player = new AudioFilePlayer();
	export let currentlyPlaying: WavRecorder | AudioFilePlayer | null = null;

	let startHue = 0;
	let endHue = 50;

	let paused = false;
	const analysisType: 'music' | 'voice' | 'frequency' = 'voice';

	let socket: WebSocket | null = null;
	let deepfakeStatus: boolean | null = null;

	onMount(async () => {
		await player.loadFile(file);
		startAudio();

		socket = await connect((data) => {
			try {
				const payload = JSON.parse(data);
				deepfakeStatus = payload['deepfake'];
			} catch (error) {
				deepfakeStatus = null;
				console.error(error);
			}
		});

		setTimeout(() => {
			setInterval(() => {
				extractBytes(file, 3)
				.then((bytes) => {
					console.log(bytes);
					if (bytes) socket?.send(bytes);
				})
			}, UPDATE_INTERVAL);
		}, UPDATE_INTERVAL);
	});

	$: switch (deepfakeStatus) {
		case true:
			startHue = 0;
			endHue = 0;
			break;
		case false:
			startHue = 120;
			endHue = 120;
			break;
		case null:
			startHue = 0;
			endHue = 50;
			break;
	}

	async function startAudio() {
		if (!paused) {
			player.pause();
			paused = true;
			return;
		}
		
		console.log(player);

		player.play();
		currentlyPlaying = player;

		paused = false;
	}
</script>

<div class="relative h-full w-full">
	<AudioFrequency audio={currentlyPlaying} let:getValues {analysisType}>
		<div class="h-full w-full overflow-hidden rounded-xl border border-white/15 p-2">
			<Glow glow={10}>
				<InnerGlowVisualizer values={getValues(64)} {startHue} {endHue} />
			</Glow>
		</div>
	</AudioFrequency>

	<div
		class="absolute left-0 top-1/4 flex h-1/2 w-full flex-col items-center justify-center rounded-xl border border-white/15 p-4 px-24 opacity-50 blur-lg"
	>
		<BarAudioVisualizer
			audio={currentlyPlaying}
			barSpacing={16}
			{startHue}
			{endHue}
			center
			{analysisType}
		/>
	</div>

	<div
		class="absolute left-0 top-0 flex h-full w-full flex-col items-center justify-center rounded-xl"
	>
		<CircleBarAudioVisualizer
			audio={currentlyPlaying}
			{startHue}
			{endHue}
			rotate={2}
			{analysisType}
		/>
		{#if paused}
			<button
				class="absolute ml-4 h-32 w-32 rounded-full outline-none"
				on:click={startAudio}
				aria-label="button"
			>
				<svg
					fill="white"
					version="1.1"
					id="Layer_1"
					xmlns="http://www.w3.org/2000/svg"
					xmlns:xlink="http://www.w3.org/1999/xlink"
					viewBox="0 0 330 330"
					xml:space="preserve"
				>
					<path
						id="XMLID_308_"
						d="M37.728,328.12c2.266,1.256,4.77,1.88,7.272,1.88c2.763,0,5.522-0.763,7.95-2.28l240-149.999
c4.386-2.741,7.05-7.548,7.05-12.72c0-5.172-2.664-9.979-7.05-12.72L52.95,2.28c-4.625-2.891-10.453-3.043-15.222-0.4
C32.959,4.524,30,9.547,30,15v300C30,320.453,32.959,325.476,37.728,328.12z"
					/>
				</svg></button
			>
		{/if}
	</div>
</div>
