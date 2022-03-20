<template>
  <div>
    <b-navbar class="pl-0" toggleable="lg" type="light" variant="light" sticky>
      <div class="main-navbar">
        <b-navbar-brand>
          <NuxtLink class="main-link" to="/">Tblog</NuxtLink>
        </b-navbar-brand>
      </div>
    </b-navbar>
    <Nuxt />
  </div>
</template>

<style scoped>
.main-navbar {
  width: 800px;
  vertical-align: middle;
  margin: 0 auto;
  padding-left: 10px;
}

.main-link {
  color: black;
  font-weight: bold;
  font-size: 1.5rem;
  font-family: 'Quicksand', sans-serif;
  text-decoration: none;
}
</style>
