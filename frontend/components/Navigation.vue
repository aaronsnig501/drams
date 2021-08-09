<template>
  <nav class="navbar">
    <div class="container">
      <div id="navMenu" class="navbar-menu">
        <div class="navbar-start">
          <NuxtLink to="/" class="navbar-item">
            Home
          </NuxtLink>
          <NuxtLink to="/inspire" class="navbar-item">
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
             <NuxtLink to="/accounts/create" class="button is-dark">
                Register
              </NuxtLink>
              <NuxtLink to="/accounts/login" class="button is-link">
                Login
              </NuxtLink>
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
  </nav>
</template>

<script>
import { mapState } from "vuex";
export default {

  data() {
    return {};
  },
  computed: {
    ...mapState(["auth"])
  },
  methods: {
    logOut() {
      console.log(this.$auth.strategies)
      this.$auth.logout();
      console.log("logged out")
    }
  }
}
</script>
