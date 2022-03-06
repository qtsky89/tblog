<template>
  <div>
    <b-navbar toggleable="lg" type="light" variant="light">
      <div class="main-navbar">
        <b-navbar-brand sticky=true>
          <NuxtLink class="main-link" to="/">Tblog</NuxtLink>
        </b-navbar-brand>
      </div>
    </b-navbar>
    <Nuxt />
  </div>
</template>

<style scoped>
.main-navbar {
  width: 70%;
  vertical-align: middle;
  margin: 0 auto;
}

.main-link {
  color: black;
  font-weight: bold;
  font-size: 1.5rem;
  font-family: "Quicksand", sans-serif;
}
</style>