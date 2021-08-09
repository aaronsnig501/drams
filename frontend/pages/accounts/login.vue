<template>
  <main>
    <navigation></navigation>
    <section class="section">
      <div class="columns">
        <div class="column is-1"></div>
        <div class="column is-11">
          <h1 class="title is-2">Login</h1>
        </div>
      </div>
      <div class="columns main-section">
        <div class="column is-2"></div>
        <div class="column is-8">
          <form>

            <div class="field">
              <label class="label">Email</label>
              <div class="control has-icons-right">
                <input
                  name="email"
                  class="input"
                  type="text"
                  v-model="login.email"
                />
                <span class="icon is-small is-right">
                  <i class="fa fa-envelope"></i>
                </span>
              </div>
            </div>

            <div class="field">
              <label class="label">Password</label>
              <div class="control has-icons-right">
                <input
                  name="password"
                  class="input"
                  type="password"
                  v-model="login.password"
                />
                <span class="icon is-small is-right">
                  <i class="fa fa-key"></i>
                </span>
              </div>
            </div>
            <div class="has-text-centered">
              <button
                class="button is-vcentered is-primary is-outlined"
                @click.prevent="loginUser"
              >
                Login!
              </button>
            </div>
            <div class="has-text-centered">
              <NuxtLink to="/accounts/login">
                Don't have an account? Create one!
              </NuxtLink>
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
  name: 'Login',
  auth: false,

  components: {
    Navigation
  },

  data() {
    return {
      loading: false,
      visibility: false,
      login: {
        email: "",
        password: ""
      }
    };
  },

  methods: {

    /**
     * Log the user in using Nuxt auth.
     *
     * This was tedious, and there's probably a better way doing this, but for now the
     * login is performed using `$auth.loginWith` which will retrieve the auth tokens.
     * These tokens will then be set, and then used to retrieve the user profile.
     *
     * Once that is complete the user will be redirected to the home page
     */
    async loginUser() {
      let data = this.login;
      this.$nuxt.$loading.start();
      let auth = await this.$auth.loginWith("local", {
          data
      });
      this.loading = false;

      const tokens = auth.data;

      this.$auth.setUserToken(tokens.access, tokens.refresh).then(
        () => this.$auth.fetchUser())

      this.$axios.setHeader(`Authorization: Bearer {tokens.access}`)
      let user = await this.$axios.get("/api/accounts/me/");
      await this.$auth.setUser(user.data);

      this.$router.push("/");
    }
  }
};
</script>

<style scoped>
.main-section {
  margin-top: 5%;
}
</style>