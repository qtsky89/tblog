<template>
  <q-layout view="hHh lpr lFr">
    <q-header reveal class="bg-grey-2 text-black">
      <q-toolbar>
        <q-toolbar-title class="q-ml-lg">
          <span class="main-link click" @click="mainClick()">
            Wonhee's Tech Blog
          </span>
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
import { useRouter } from 'vue-router'
import { useIndexStore } from 'stores/indexStore'

const r = useRouter()
const s = useIndexStore()
function mainClick(): void {
  s.selectedTag = ''
  r.push('/')
}
</script>

<style scoped>
.main-link {
  color: black;
  font-weight: bold;
  font-size: 1.5rem;
  font-family: 'Quicksand', sans-serif;
  text-decoration: none;
  cursor: pointer;
}
</style>
