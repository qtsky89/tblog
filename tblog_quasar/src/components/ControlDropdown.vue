<template>
  <div>
    <!-- TODO: add control feature (create, update, delete, login, logout)-->
    <q-btn-dropdown class="q-btn--flat">
      <template #label>
        <q-avatar>
          <img
            v-if="u.isLoggedIn"
            class="bg-black"
            :src="u.user.picture"
          />
          <img
            v-else
            class="bg-black"
            src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg"
          />
        </q-avatar>
      </template>

      <q-list>
        <q-item
          v-for="item in items"
          :key="item.label"
          @click="controlClick(item.action)"
          clickable
          v-close-popup
        >
          <q-item-section avatar>
            <q-avatar
              :color="item.color"
              size="25px"
              icon="add"
              text-color="white"
            />
          </q-item-section>
          <q-item-section>
            <q-item-label>{{ item.label }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-btn-dropdown>
  </div>
</template>

<script lang="ts">
interface ControlItem {
  action: string
  color: string
  label: string
}
</script>

<script setup lang="ts">
import { api } from 'src/boot/axios'
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { googleOneTap, decodeCredential } from 'vue3-google-login';
import { useUserStore } from 'stores/userStore'
import { decodeCredentialResponse } from './types';

const route = useRoute()
const router = useRouter()
const u = useUserStore()

let items = computed(() => {
  let ret: Array<ControlItem> = []

  if (!u.isLoggedIn) {
    ret.push({action: 'login', color: 'green-10', label: 'Login'})
  } else {
    ret.push({action: 'logout', color: 'red-10', label: 'Logout'})
  }

  if (u.user.isSu) {
    ret.push({ action: 'create', color: 'blue-10', label: 'Create' })
    if (route.name === 'read') {
      ret.push(
        { action: 'update', color: 'green-10', label: 'Update' },
        { action: 'delete', color: 'red-10', label: 'Delete' }
      )
    }
  }
  return ret
})

function controlClick(action: string): void {
  switch (action) {
    case 'login': {
      login()
      break
    }
    case 'logout': {
      logout()
      break
    }
    case 'create':
      router.push('/create')
      break
    case 'update':
      router.push(`/update/${route.params.id}`)
      break
    case 'delete':
      try {
        api.delete(`/api/v1/post/${route.params.id}`)
        router.push('/')
      } catch (error) {
        console.error(error)
      }
  }
}

async function login(): Promise<void> {
  try {
    const r1 = await googleOneTap()
    const r2 = decodeCredential(r1.credential) as decodeCredentialResponse
    const r3 = await api.post('/api/v1/login', {email: r2.email})
    u.login(r2.email, r2.picture, r3.data.data[0].isSu)
  } catch (e) {
    console.error(e)
  }
}

function logout() {
  try {
    u.logout()
  } catch (e) {
    console.error(e)
  }
}

</script>
