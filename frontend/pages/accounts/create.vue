<template>
  <main>
    <navigation></navigation>
    <section class="section">
      <div class="columns">
        <div class="column is-1"></div>
        <div class="column is-11">
          <h1 class="title is-2">Create New Account</h1>
        </div>
      </div>
      <div class="columns main-section">
        <div class="column is-2"></div>
        <div class="column is-8">
          <form>
            <div class="field">
              <label class="label">Username</label>
              <div class="control has-icons-right">
                <input
                  name="username"
                  class="input"
                  type="text"
                  v-model="register.username"
                />
                <span class="icon is-small is-right">
                  <i class="fa fa-user"></i>
                </span>
              </div>
            </div>

            <div class="field">
              <label class="label">Email</label>
              <div class="control has-icons-right">
                <input
                  name="email"
                  class="input"
                  type="text"
                  v-model="register.email"
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
                  v-model="register.password"
                />
                <span class="icon is-small is-right">
                  <i class="fa fa-key"></i>
                </span>
              </div>
            </div>
            <div class="has-text-centered">
              <button
                class="button is-vcentered is-primary is-outlined"
                @click.prevent="createAccount"
              >
                Sign Up!
              </button>
            </div>
            <div class="has-text-centered">
              <NuxtLink to="/accounts/login">
                Already have an account? Log in now!
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
  name: 'Register',

  components: {
    Navigation
  },

  data() {
    return {
      loading: false,
      visibility: false,
      register: {
        username: "",
        email: "",
        password: ""
      }
    };
  },

  methods: {
    async createAccount() {
      this.loading = true;
      let data = this.register;

      try {
        let response = await this.$axios.post("/api/accounts/create/", data);
        console.log(response)
        this.$router.push("/login");
        this.loading = false;
        console.log({
          group: "success",
          title: "Success!",
          text: "Account created successfully!"
        });
      } catch (error) {
        this.loading = false;
        console.log({
          group: "error",
          title: "Error!",
          text: error.response
            ? error.response.data.error
            : "Sorry an error occured, check your internet"
        })
      }
    }
  }
};
</script>

<style scoped>
.main-section {
  margin-top: 5%;
}
</style>