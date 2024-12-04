<script lang="ts">
	import UploadAudio from '$lib/components/upload/UploadAudio.svelte';
	import PlayAudio from '$lib/components/play/PlayAudio.svelte';

	let uploadedAudio: File | null = null;

	$: if (uploadedAudio) {
		console.log(uploadedAudio);
	}
</script>

<div class="h-screen w-screen">
	{#if uploadedAudio}
		<div class="h-full w-full bg-black">
			<PlayAudio file={uploadedAudio} />
		</div>
	{:else}
		<div class="h-full p-12">
			<UploadAudio onFileSelect={(file) => (uploadedAudio = file)} />
		</div>
	{/if}
</div>