<template>
  <q-page class="q-pa-md"> <MarkdownEditor /> </q-page>
</template>

<script setup lang="ts">
import MarkdownEditor from 'components/MarkdownEditor.vue'
import { useRoute } from 'vue-router'
import { onMounted } from 'vue'
import { usePostStore } from 'stores/postStore'

onMounted(async () => {
  const p = usePostStore()
  const r = useRoute()
  try {
    await p.initialize(r.params.id as string)
  } catch (error) {
    console.error(error)
  }
})
</script>
