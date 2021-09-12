<template>
  <main>
    <navigation></navigation>

    <section class="section">
      <div class="columns">
        <div class="column is-1"></div>
        <div class="column is-3">
          <h1 class="title is-3">Whiskies</h1>
        </div>
        <div class="column is-2">
          <div class="navbar-menu">
          <b-dropdown
            append-to-body
            aria-role="menu"
            scrollable
            max-height="200"
            trap-focus
          >
            <template #trigger>
              <b-button
                label="Order results by:"
                type="is-primary is-outlined"
                :icon-right="active ? 'menu-up' : 'menu-down'" />
            </template>

            <b-dropdown-item
              v-for="option in sortingOptions"
              :key="option.value"
              aria-role="listitem"
              @click="searchWhiskies('ordering', option.value)"
            >
              {{ option.text }}
            </b-dropdown-item>
          </b-dropdown>
          </div>
        </div>
      </div>
      <div class="columns main-section is-8">
        <div class="column is-1"></div>
        <div class="column is-3">
          <aside class="menu is-4">
            <p class="menu-label">
              General Search
            </p>
            <ul class="menu-list">
              <li>
                <input
                  name="username"
                  class="input"
                  type="text"
                  v-model="search.textSearch"
                />
              </li>
              <li>
                <button
                  class="button is-vcentered is-primary is-outlined is-fullwidth mt-3"
                  @click.prevent="searchWhiskies('search', search.textSearch)"
                >
                  Search whiskey
                </button>
              </li>
            </ul>
            <p class="menu-label">
              Quick Filters
            </p>
            <ul class="menu-list">
              <li>Type
                <ul>
                  <li v-for="type in types" :key="type">
                    <a @click.prevent="searchWhiskies('search', type)">{{ type }}</a>
                  </li>
                </ul>
              </li>
              <li>Colouring
                <ul>
                  <li v-for="colouring in colourings" :key="colouring.id">
                    <a @click.prevent="searchWhiskies('colour', colouring.id)">
                      {{ colouring.value }}
                    </a>
                  </li>
                </ul>
              </li>
              <li>Chill filtering
                <ul>
                  <li v-for="filtering in filterings" :key="filtering.id">
                    <a @click.prevent="searchWhiskies('chill_filtered', filtering.id)">
                      {{ filtering.value }}
                    </a>
                  </li>
                </ul>
              </li>
              <li>Proof
                <ul>
                  <li>
                    <input
                      name="username"
                      class="input"
                      type="text"
                      v-model="search.proofSearch"
                    />
                    <button
                      class="button is-vcentered is-primary is-outlined is-fullwidth mt-3"
                      @click.prevent="searchWhiskies('proof', search.proofSearch)"
                    >
                      Search by proof
                    </button>
                  </li>
                </ul>
              </li>
            </ul>
          </aside>
        </div>
        <div class="column is-7">
          <div v-if="whiskies.length == 0">
            <p class="is-size-5 mt-5 ml-6">
              Sorry, there are no whiskies that match your query
            </p>
          </div>
          <div class="box" v-for="whiskey in whiskies" :key="whiskey.id">
            <article class="media">
              <div class="media-left">
                <figure class="image is-128x128">
                  <NuxtLink  :to="'/whiskey/' + whiskey.id">
                    <img v-bind:src="whiskey.image" alt="Image">
                  </NuxtLink>
                </figure>
              </div>
              <div class="media-content">
                <div class="content">
                  <p class="is-size-4">
                    <NuxtLink :to="'/whiskey/' + whiskey.id">
                      <strong class="has-text-black">{{ whiskey.name }}</strong>
                      <small class="has-text-black">{{ whiskey.brand }}</small>
                      <small class="has-text-black is-size-5">
                        - {{ whiskey.age_statement }} years old
                      </small>
                    </NuxtLink>
                  </p>
                  <p>
                    {{ whiskey.description }}
                  </p>
                </div>
                <nav class="level">
                  <div class="level-left">
                    <a class="level-item" aria-label="reply">
                      <font-awesome-icon :icon="['fas', 'reply']" />
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
        <div class="create-button">
          <b-tooltip
            label="Add a new whiskey"
            type="is-dark"
            position="is-left"
          >
            <NuxtLink :to="'/whiskey/create'" class="button is-primary is-outlined">
              <font-awesome-icon :icon="['fas', 'plus']" />
            </NuxtLink>
          </b-tooltip>

        </div>
      </div>
    </section>
  </main>
</template>

<style scoped>
.menu {
  position: sticky;
  display: inline-block;
  vertical-align: top;
  max-height: 100vh;
  overflow-y: auto;
  width: 100%;
  top: 0;
  bottom: 0;
  padding: 30px;
}

.create-button {
  position: absolute;
  right: 3.5%;
  bottom: 7.5%;
}

.create-button .button {
  height: 50px;
  width: 50px;
  border-radius: 50%;
}
</style>

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
      active: false,
      search: {
        textSearch: "",
        proofSearch: ""
      },
      types: [
        "Bourbon",
        "Rye",
        "Scotch",
        "Irish",
        "Japanese",
        "Canadian"
      ],
      colourings: [
        {"id": "1", "value": "Coloured"},
        {"id": "2", "value": "Natural"}
      ],
      filterings: [
        {"id": "1", "value": "Chill-filtered"},
        {"id": "2", "value": "Non-chill-filtered"}
      ],
      sortingOptions: [
        {"value": "name", "text": "Name Ascending"},
        {"value": "-name", "text": "Name Descending"},
        {"value": "brand__name", "text": "Brand Name Ascending"},
        {"value": "-brand__name", "text": "Brand Name Descending"},
        {"value": "type__name", "text": "Type Name Ascending"},
        {"value": "-type__name", "text": "Type Name Descending"},
        {"value": "proof", "text": "Proof Ascending"},
        {"value": "-proof", "text": "Proof Descending"},
        {"value": "age_statement", "text": "Age Statement Ascending"},
        {"value": "-age_statement", "text": "Age Statement Descending"},
      ],
      whiskies: []
    }
  },

  async fetch() {
    await this.searchWhiskies();
  },

  methods: {
    async searchWhiskies(paramName, value) {
      let params = {[paramName]: value};
      this.whiskies = await this.$store.dispatch("getWhiskies", params);
    }
  }
}
</script>
