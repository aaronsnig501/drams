<template>
  <nav class="navbar">
    <div class="container">
      <div id="navMenu" class="navbar-menu">
        <div class="navbar-start">
          <NuxtLink to="/" class="navbar-item">
            Home
          </NuxtLink>
          <NuxtLink to="/whiskey" class="navbar-item">
            Whiskies
          </NuxtLink>
          <a href="" class="navbar-item">
            Blends
          </a>
          <a href="" class="navbar-item">
            Recipes
          </a>
          <NuxtLink to="/blog/" class="navbar-item">
            Blog
          </NuxtLink>
        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons" v-if="!auth.loggedIn">
              <a class="button is-primary" @click.prevent="showLoginModal">
                Enter site
              </a>
            </div>

            <div class="buttons" v-if="auth.loggedIn">
              <p>{{ auth.user.email }}</p>
              <a class="button is-link" @click.prevent="logOut">
                Logout
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <section>
      <b-modal
        v-model="isModalActive"
        has-modal-card
        trap-focus
        :destroy-on-hide="false"
        aria-role="dialog"
        aria-label="Login form"
        aria-modal
      >
        <div class="modal-card" style="width: auto">
          <header class="modal-card-head">
            <p class="modal-card-title">Enter Drams!</p>
            <button
              type="button"
              class="delete"
              @click="$emit('close')"
            />
          </header>
          <section class="modal-card-body">
            <b-field class="email-input" label="Email">
              <b-input
                v-model="email"
                type="email"
                :value="email"
                placeholder="Your email"
                required>
              </b-input>
            </b-field>
            <p class="notification is-success is-light"></p>
            <b-field class="token-input" label="Token">
              <b-input
                v-model="token"
                type="number"
                :value="token"
                placeholder="Your Token"
                required>
              </b-input>
            </b-field>
          </section>
          <footer class="modal-card-foot">
            <b-button
              label="Close"
              @click="$emit('close')"
            />
            <b-button
              class="send-token"
              label="Continue"
              type="is-primary"
              @click="sendToken"
            />
            <b-button
              class="login"
              label="Login"
              type="is-success"
              @click="login"
            />
          </footer>
        </div>
      </b-modal>
    </section>
  </nav>
</template>

<style scoped>
.token-input {
  display: none;
}

.notification {
  display: none;
}

.login {
  display: none;
}
</style>

<script>
import { mapState } from "vuex";
export default {

  data() {
    return {
      isModalActive: false,
      email: "",
      token: ""
    };
  },
  computed: {
    ...mapState(["auth"])
  },
  methods: {
    logOut() {
      this.$auth.logout();
    },

    showLoginModal() {
      this.isModalActive = true;
    },

    async sendToken() {
      const data = {
        email: this.email
      }
      try {
        let response = await this.$api.post("api/auth/email/", data);

        document.querySelector(".email-input").style.display = "none";
        document.querySelector(".send-token").style.display = "none";
        document.querySelector(".token-input").style.display = "block";
        document.querySelector(".login").style.display = "block";

        const message = document.querySelector(".notification");
        message.style.display = "block";
        message.innerText =
          `${response.data.detail} Please use this token to get access.`;
      } catch (error) {
        console.log(error.response)
      }
    },

    async login() {
      const data = {
        email: this.email,
        token: this.token
      }

      const auth = await this.$api.post("/api/auth/token/", data);

      this.$auth.setUserToken(auth.data.token).then(
        () => this.$auth.fetchUser());

      console.log(auth.data.token)

      this.$axios.setHeader(`Authorization: Token ${auth.data.token}`);
      let user = await this.$axios.get("/api/accounts/me/");
      await this.$auth.setUser(user.data);

      this.isModalActive = false;
    }
  }
}
</script>
