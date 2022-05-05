<template>
  <div>
    <b-navbar class="pl-0" toggleable="lg" type="light" variant="light" sticky>
      <b-container class="main-navbar">
        <b-navbar-brand>
          <NuxtLink class="main-link" to="/">Tblog</NuxtLink>
        </b-navbar-brand>
        <b-navbar-nav>
          <b-nav-item-dropdown right no-caret>
            <template #button-content>
              <b-avatar class="rounded-circle"></b-avatar>
            </template>
            <b-dropdown-item to="/create">Create</b-dropdown-item>
            <b-dropdown-item v-if="isReadPage" :to="`/update/${readPageId}`"
              >Update
            </b-dropdown-item>
            <b-dropdown-item to="/logout">Log out</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-container>
    </b-navbar>
    <Nuxt />
  </div>
</template>
<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  computed: {
    isReadPage(): boolean {
      return this.$route.name === 'post-id'
    },
    readPageId(): number {
      return this.$route.params.id
    },
  },
})
</script>

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

.dropdown-action {
  color: black;
  font-weight: bold;
  text-decoration: none;
}
</style>
