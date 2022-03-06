<template>
  <div>
    <b-navbar class="main-navbar" toggleable="lg" type="light" variant="light">
      <b-navbar-brand sticky=true>
        <NuxtLink to="/">Home page</NuxtLink>
      </b-navbar-brand>
    </b-navbar>
    <Nuxt />
  </div>
</template>

<style scoped>
.main-navbar {
  padding-left: 10rem !important;
  padding-right: 10rem !important;
}
</style>