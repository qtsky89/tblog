<template>
  <div>
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
        <q-item
          v-for="item in items"
          :key="item.label"
          :to="item.to"
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
  to: string
  color: string
  label: string
}
</script>

<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'
//var items = ['/create', '/update', 'delete']

const r = useRoute()
console.log(r.path)
let items = computed(() => {
  let ret: Array<ControlItem> = [
    { to: '/create', color: 'blue-10', label: 'Create' },
  ]
  if (r.name === 'read') {
    ret.push({
      to: `/update/${r.params.id}`,
      color: 'green-10',
      label: 'Update',
    })
  }
  return ret
})
</script>
