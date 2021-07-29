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
            <div class="buttons">
              <a href="" class="button is-dark">Register</a>
              <a href="" class="button is-link">Login</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {}
</script>
