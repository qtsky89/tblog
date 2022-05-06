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
          <router-link class="main-link" to="/">Wonhee's Tech Blog</router-link>
        </q-toolbar-title>

        <!-- TODO: add control feature (create, update, delete, login, logout)-->
        <q-btn-dropdown class="q-btn--flat">
          <template #label>
            <q-avatar>
              <img
                class="bg-black"
                src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg"
              />
            </q-avatar>
          </template>

          <q-list>
            <q-item clickable v-close-popup to="/create">
              <q-item-section avatar>
                <q-avatar
                  size="25px"
                  icon="add"
                  color="blue-10"
                  text-color="white"
                />
              </q-item-section>
              <q-item-section>
                <q-item-label>Create</q-item-label>
              </q-item-section>
            </q-item>

            <q-item clickable v-close-popup to="/update">
              <q-item-section avatar>
                <q-avatar
                  size="25px"
                  icon="edit"
                  color="green-10"
                  text-color="white"
                />
              </q-item-section>
              <q-item-section>
                <q-item-label>Update</q-item-label>
              </q-item-section>
            </q-item>
          </q-list>

          <q-item clickable v-close-popup to="/delete">
            <q-item-section avatar>
              <q-avatar
                size="25px"
                icon="add"
                color="red-10"
                text-color="white"
              />
            </q-item-section>
            <q-item-section>
              <q-item-label>Delete</q-item-label>
            </q-item-section>
          </q-item>
        </q-btn-dropdown>
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
