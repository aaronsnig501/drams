<template>
  <main>
    <navigation></navigation>
    <section class="section">
      <div class="columns main-section">
        <div class="column is-1"></div>
        <div class="column is-11">
          <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
              <li>
                <NuxtLink :to="'/whiskey/'">Whiskies</NuxtLink>
              </li>
              <li class="is-active">
                <a href="#" aria-current="page">{{ data.brand }} {{ data.name }}</a>
              </li>
            </ul>
          </nav>
        </div>
      </div>
      <div class="columns">
        <div class="column is-1"></div>
        <div class="column is-3">
          <img v-bind:src="data.image">
        </div>
        <div class="column is-6">
          <h1 class="title is-size-2">{{ data.brand }} {{ data.name }}</h1>
          <p class="pt-4 is-size-5">{{ data.description }}</p>
        </div>
        <div class="column is-5"></div>
      </div>
      <div class="columns">
        <div class="column is-2"></div>
        <div class="column is-2 has-text-centered">
          <p>Age statement</p>
          <p class="pt-2 is-size-5">{{ data.age_statement }}</p>
        </div>
        <div class="column is-2 has-text-centered">
          <p>Proof
          <p class="pt-2 is-size-5">{{ data.proof }}</p>
        </div>
        <div class="column is-2 has-text-centered">
          <p>Colouring</p>
          <p class="pt-2 is-size-5">{{ is_coloured }}</p>
        </div>
        <div class="column is-2 has-text-centered">
          <p>Chill filtering</p>
          <p class="pt-2 is-size-5">{{ is_chill_filtered }}</p>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import Navigation from "~/components/Navigation";

export default {
  name: 'WhiskeyDetails',
  auth: false,

  components: {
    Navigation
  },

  async asyncData({ params, $axios }) {
    let { data } = await $axios.get(`/api/whiskey/${params.id}/`);
    console.log(data)
    return { data };
  },

  computed: {
    is_chill_filtered() {
      if (this.data.chill_filtered == 1) return "Chill filtered";
      if (this.data.chill_filtered == 2) return "Not chill filtered";
      return "Unknown";
    },

    is_coloured() {
      if (this.data.colour == 1) return "Artificial";
      if (this.data.colour == 2) return "Natural";
      return "Unknown";
    }
  }
}
</script>