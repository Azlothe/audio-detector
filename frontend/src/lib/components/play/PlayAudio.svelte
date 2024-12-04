<script lang="ts">
	import InnerGlowVisualizer from '$lib/visualizations/core/InnerGlowVisualizer.svelte';
	import Glow from '$lib/visualizations/core/Glow.svelte';
	import AudioFrequency from '$lib/visualizations/audio/AudioFrequency.svelte';
	import { WavRecorder, AudioFilePlayer } from '$lib/visualizations/wavtools';
	import CircleBarAudioVisualizer from '$lib/visualizations/audio/CircleBarAudioVisualizer.svelte';
	import BarAudioVisualizer from '$lib/visualizations/audio/BarAudioVisualizer.svelte';
	import { onMount } from 'svelte';

	export let file: File;
	export let player = new AudioFilePlayer();
	export let currentlyPlaying: WavRecorder | AudioFilePlayer | null = null;

	let paused = false;
	const analysisType: 'music' | 'voice' | 'frequency' = 'voice';

	onMount(async () => {
		await player.loadFile(file);
		startAudio();
	});

	async function startAudio() {
		if (!paused) {
			player.pause();
			paused = true;
			return;
		}

		player.play();
		currentlyPlaying = player;

		paused = false;
	}
</script>

<div class="relative h-full w-full">
	<AudioFrequency audio={currentlyPlaying} let:getValues {analysisType}>
		<div class="h-full w-full overflow-hidden rounded-xl border border-white/15 p-2">
			<Glow glow={10}>
				<InnerGlowVisualizer values={getValues(256)} startHue={0} endHue={120} />
			</Glow>
		</div>
	</AudioFrequency>

	<div
		class="absolute left-0 top-0 flex h-full w-full flex-col items-center justify-center rounded-xl"
	>
		<CircleBarAudioVisualizer
			audio={currentlyPlaying}
			startHue={120}
			endHue={120}
			rotate={2}
			{analysisType}
		/>
	</div>

	<div
		class="absolute left-0 top-1/4 flex h-1/2 w-full flex-col items-center justify-center rounded-xl border border-white/15 p-4 px-24 opacity-50 blur-lg"
	>
		<BarAudioVisualizer
			audio={currentlyPlaying}
			barSpacing={16}
			startHue={120}
			endHue={120}
			center
			{analysisType}
		/>
	</div>

	<button
		type="button"
		on:click={startAudio}
		class="absolute left-1/2 top-1/2 rounded-full px-3 py-2 text-sm font-semibold focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-amber-500 {paused
			? 'border border-stone-500/20 bg-stone-500/10 text-stone-500 hover:bg-stone-500/20'
			: 'border border-amber-500/20 bg-amber-500/10 text-amber-500 hover:bg-amber-500/20'}"
		>{paused ? 'Start ' : 'Pause '}music</button
	>
</div>
