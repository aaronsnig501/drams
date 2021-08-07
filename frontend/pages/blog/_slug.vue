<template>
	<main>
		<navigation></navigation>
		<section class="section">
			<div class="columns main-section">
        <div class="column is-2"></div>
        <div class="column is-8">
					<h1 class="title is-2">{{ data.title }}</h1>
				</div>
			</div>
		</section>
	</main>
</template>

<script>
import Navigation from "~/components/Navigation";

export default {
	name: 'Post',
	auth: false,

	components: {
		Navigation
	},

	async asyncData({ params, $axios }) {
		let { data } = await $axios.get(`/blog/${params.slug}/`);
    return { data };
	},

}
</script>