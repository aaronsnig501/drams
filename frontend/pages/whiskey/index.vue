<template>
  <main>
    <navigation></navigation>

    <section class="section">
      <div class="columns">
        <div class="column is-12">
          <h1 class="title is-3">Whiskies</h1>
        </div>
      </div>
      <div class="columns main-section is-8">
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
                  @click.prevent="searchWhiskies"
                >
                  Search whiskey
                </button>
              </li>
            </ul>
            <p class="menu-label">
              Administration
            </p>
            <ul class="menu-list">
              <li><a>Team Settings</a></li>
              <li>
                <a class="is-active">Manage Your Team</a>
                <ul>
                  <li><a>Members</a></li>
                  <li><a>Plugins</a></li>
                  <li><a>Add a member</a></li>
                </ul>
              </li>
              <li><a>Invitations</a></li>
              <li><a>Cloud Storage Environment Settings</a></li>
              <li><a>Authentication</a></li>
            </ul>
            <p class="menu-label">
              Transactions
            </p>
            <ul class="menu-list">
              <li><a>Payments</a></li>
              <li><a>Transfers</a></li>
              <li><a>Balance</a></li>
            </ul>
          </aside>
        </div>
        <div class="column is-9">
          <div v-if="whiskies.length == 0">
            <p class="is-size-5 mt-5 ml-6">
              Sorry, there are no whiskies that match your query
            </p>
          </div>
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
      search: {
        textSearch: "",
      },
      whiskies: []
    }
  },

  async fetch() {
    this.whiskies = await this.$store.dispatch("getWhiskies");
  },

  methods: {
    async searchWhiskies() {
      this.whiskies = await this.$store.dispatch(
        "getWhiskies", this.search.textSearch);
    }
  }
}
</script>
