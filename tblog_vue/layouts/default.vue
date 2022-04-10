<template>
  <div>
    <b-navbar class="pl-0" toggleable="lg" type="light" variant="light" sticky>
      <b-container class="main-navbar">
        <b-navbar-brand>
          <NuxtLink class="main-link" to="/">Tblog</NuxtLink>
        </b-navbar-brand>
        <b-button variant="outline-primary" pill size="md">
          <NuxtLink to="/create">Create</NuxtLink>
        </b-button>
      </b-container>
    </b-navbar>
    <Nuxt />
  </div>
</template>

<style scoped>
.main-navbar {
  width: 100%;
}

.main-link {
  color: black;
  font-weight: bold;
  font-size: 1.5rem;
  font-family: 'Quicksand', sans-serif;
  text-decoration: none;
}
</style>
