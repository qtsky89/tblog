<template>
  <q-page class="q-pa-md post-card">
    <h5>{{ p.title }}</h5>
    <mavon-editor
      v-model="p.body"
      class="editor q-mt-lg"
      language="en"
      font-size="16px"
      :box-shadow="false"
      :toolbarsFlag="false"
      :subfield="false"
      defaultOpen="preview"
  /></q-page>
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

<style scoped>
.post-card {
  width: 850px;
  margin: auto;
}
</style>
