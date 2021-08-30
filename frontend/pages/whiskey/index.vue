<template>
  <main>
    <navigation></navigation>
    <section class="section">
      <div class="columns">
        <div class="column is-1"></div>
        <div class="column is-11">
          <h1 class="title is-2">Whiskies</h1>
        </div>
      </div>
      <div class="columns main-section">
        <div class="column is-2"></div>
        <div class="column is-8">
          <div class="box" v-for="whiskey in whiskies" :key="whiskey.id">
            <article class="media">
              <div class="media-left">
                <figure class="image is-128x128">
                  <img v-bind:src="whiskey.image" alt="Image">
                </figure>
              </div>
              <div class="media-content">
                <div class="content">
                  <p class="is-size-4">
                    <strong>{{ whiskey.name }}</strong>
                    <small>{{ whiskey.brand }}</small>
                    <small class="is-size-5"> - {{ whiskey.age_statement }} years old</small>
                  </p>
                  <p>
                    {{ whiskey.description }}
                  </p>
                </div>
                <nav class="level">
                  <div class="level-left">
                    <a class="level-item" aria-label="reply">
                      <font-awesome-icon :icon="['fas', 'reply']"  />
                    </a>
                    <a class="level-item" aria-label="retweet">
                      <span class="icon is-small">
                        <i class="fas fa-retweet" aria-hidden="true"></i>
                      </span>
                    </a>
                    <a class="level-item" aria-label="like">
                      <span class="icon is-small">
                        <i class="fas fa-heart" aria-hidden="true"></i>
                      </span>
                    </a>
                  </div>
                </nav>
              </div>
            </article>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import Navigation from '~/components/Navigation'

export default {
  name: 'Whiskey',
  auth: false,

  components: {
    Navigation
  },

  data() {
    return {
      whiskies: []
    }
  },

  async fetch() {
    let { data } = await this.$axios.get("/api/whiskey/");
    this.whiskies = data;
    console.log(this.whiskies);
  },
}
</script>
