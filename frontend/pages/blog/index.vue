<template>
  <main>
    <navigation></navigation>
    <section class="section">
      <div class="columns">
        <div class="column is-1"></div>
        <div class="column is-11">
          <h1 class="title is-2">The Whiskey Blog</h1>
        </div>
      </div>
      <div class="columns main-section">
        <div class="column is-2"></div>
        <div class="column is-8">
          <div class="columns is-multiline">
            <div class="column is-4" v-for="post in posts" :key="post.id">
              <NuxtLink :to="'/blog/' + post.id">
                <div class="card">
                  <p class="subtitle is-2">{{ post.title }}</p>
                  <p>{{ post.excerpt }}</p>
                </div>
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import Navigation from '~/components/Navigation'

export default {
  name: 'Blog',
  auth: false,

  components: {
    Navigation
  },

  data() {
    return {
      posts: []
    }
  },

  async asyncData({ $axios }) {
    let { data } = await $axios.get("/blog/");
    return { posts: data };
  },
}
</script>

<style scoped>
.main-section {
  margin-top: 5%;
}
</style>