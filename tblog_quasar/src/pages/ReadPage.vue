<template>
  <q-page class="q-pa-md"> {{ p.title }} </q-page>
</template>

<script lang="ts">
import { usePostStore } from 'stores/postStore'

export default {
  async preFetch({ currentRoute }) {
    const p = usePostStore()
    await p.initialize(currentRoute.params.id as string)
  },
}
</script>
<script setup lang="ts">
const p = usePostStore()
</script>
