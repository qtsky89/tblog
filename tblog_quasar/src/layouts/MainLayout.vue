<template>
  <q-layout view="hHh lpr lFr">
    <q-header reveal class="bg-grey-2 text-black">
      <q-toolbar>
        <q-toolbar-title class="q-ml-lg">
          <router-link class="main-link" to="/">Wonhee's Tech Blog</router-link>
        </q-toolbar-title>
        <ControlDropdown />
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import ControlDropdown from 'components/ControlDropdown.vue'

</script>

<style scoped>
.main-link {
  color: black;
  font-weight: bold;
  font-size: 1.5rem;
  font-family: 'Quicksand', sans-serif;
  text-decoration: none;
}
</style>
