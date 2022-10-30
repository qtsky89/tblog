<template>
  <q-layout view="hHh lpr lFr">
    <q-header reveal class="bg-grey-2 text-black">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />
        <q-toolbar-title>
          <router-link class="main-link" to="/">Test</router-link>
        </q-toolbar-title>
        <GoogleLogin :callback="callback" prompt />
        <ControlDropdown />
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" side="left" bordered overlay>
      <q-list>
        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import EssentialLink from 'components/EssentialLink.vue'
import ControlDropdown from 'components/ControlDropdown.vue'
import { decodeCredential } from 'vue3-google-login'

const essentialLinks = [
  {
    title: 'Docs',
    caption: 'quasar.dev',
    icon: 'school',
    link: 'https://quasar.dev',
  },
]
const leftDrawerOpen = ref(false)
function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value
}

const callback = (response) => {
  // This callback will be triggered when the user selects or login to
  // his Google account from the popup
  console.log('Handle the response', response)

  const userData = decodeCredential(response.credential)
  console.log(userData)
}
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
