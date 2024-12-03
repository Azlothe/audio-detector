<div class="box flex h-full w-full flex-col items-center justify-center space-y-12">
	<span class="flex items-center space-x-5 text-gray-500">
		<span class="flex h-12 w-12 items-center justify-center">
			<svg viewBox="0 0 500 500" class="h-full w-full">
				<circle
					cx="249.9"
					cy="250.4"
					r="204.7"
					stroke="#808080"
					stroke-width="22"
					stroke-miterlimit="10"
					fill="none"
				/>
				<g>
					<line
						fill="none"
						stroke="#808080"
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-miterlimit="10"
						stroke-width="22"
						x1="250"
						x2="250"
						y1="123"
						y2="372"
					/>
					<line
						fill="none"
						stroke="#808080"
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-miterlimit="10"
						stroke-width="22"
						x1="374"
						x2="126"
						y1="247"
						y2="247"
					/>
				</g>
			</svg>
		</span>
		<h1>Upload Audio</h1>
	</span>

	<span class="flex items-center space-x-5 text-gray-500">
		<h2>Accepted file formats: <code>.mp3</code> <code>.m4a</code></h2>
	</span>
</div>

<style>
	.box {
		--b: 1rem;
		--c: rgba(128, 128, 128, 0.2);
		--w: 5rem;
		--r: 1.5rem;
		padding: var(--b);
		position: relative;
	}

	.box::before {
		content: '';
		position: absolute;
		inset: 0;
		background: var(--c);
		padding: var(--b);
		border-radius: var(--r);

		mask:
			linear-gradient(0deg, #000 calc(2 * var(--b)), #0000 0) 50% var(--b) /
				calc(100% - 2 * var(--w)) 100% repeat-y,
			linear-gradient(-90deg, #000 calc(2 * var(--b)), #0000 0) var(--b) 50% / 100%
				calc(100% - 2 * var(--w)) repeat-x,
			linear-gradient(#000 0 0) content-box,
			linear-gradient(#000 0 0);
		-webkit-mask:
			linear-gradient(0deg, #000 calc(2 * var(--b)), #0000 0) 50% var(--b) /
				calc(100% - 2 * var(--w)) 100% repeat-y,
			linear-gradient(-90deg, #000 calc(2 * var(--b)), #0000 0) var(--b) 50%/100%
				calc(100% - 2 * var(--w)) repeat-x,
			linear-gradient(#000 0 0) content-box,
			linear-gradient(#000 0 0);
		-webkit-mask-composite: destination-out;
		mask-composite: exclude;
	}
</style>
