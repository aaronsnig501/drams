<template>
  <main>
    <section class="hero is-success is-fullheight">
      <div class="hero-head">
        <navigation></navigation>
      </div>

      <div class="hero-body">
        <div class="container">
          <p>Welcome to</p>
          <h1 class="">Drams</h1>
          <form class="">
            <div class="field has-addons">
              <div class="control">
                <div class="select is-large">
                  <select v-model="selected" @change="onChange($event)">
                    <option v-for="option in options" v-bind:key="option.type" v-bind:value="option.type">
                      {{ option.name }}
                    </option>
                  </select>
                </div>
              </div>
              <div class="control is-expanded">
                <b-field expanded>
                  <b-autocomplete
                    size="is-large"
                    :data="whiskies"
                    :placeholder="'Find a ' + selected"
                    field="title"
                    :check-infinite-scroll="true"
                    @typing="getWhiskies"
                    @select="option => selected = option"
                  >
                    <template slot-scope="props">
                      <NuxtLink :to="'/whiskey/' + props.option.id">
                        <div class="media">
                          <div class="media-left">
                            <img width="32" :src="`${props.option.image}`">
                          </div>
                          <div class="media-content">
                            {{ props.option.name }}
                            <br>
                            <small>
                              {{ props.option.brand }}
                            </small>
                          </div>
                        </div>
                      </NuxtLink>
                    </template>
                  </b-autocomplete>
                </b-field>
              </div>
            </div>
          </form>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import Navigation from '~/components/Navigation'

export default {
  name: 'HomePage',
  auth: false,

  components: {
    Navigation,
  },

  data() {
    return {
      selected: "whisky",
      options: [
        {
          type: "whisky",
          name: "Whiskies"
        },
        {
          type: "blend",
          name: "Blends"
        },
        {
          type: "recipe",
          name: "Recipies"
        }
      ],
      whiskies: [],
    }
  },

  methods: {
    onChange(event) {
      this.selected = event.target.value;
    },

    async getWhiskies(name) {
      let params = {search: name}
      let response = await this.$store.dispatch("getWhiskies", params);
      this.whiskies = response.results;
    }
  }
}
</script>

<style>
.hero {
  background-image: url(~/assets/hero.jpg);
  background-size: cover;
  height: 100%;
  background-position: center;
  background-repeat: no-repeat;
}

.hero.is-success .tabs.is-boxed li.is-active a {
  color: #000 !important;
}

.hero h1 {
  margin-bottom: 2.5%;
  font-size: 5em;
}

.hero p {
  font-size: 1.15em;
  margin-left: 0.03%;
}

.hero .hero-body form {
  margin-bottom: 12.5%;
}
</style>
