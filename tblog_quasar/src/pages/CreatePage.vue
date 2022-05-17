<template>
  <q-page class="q-pa-md"> <MarkdownEditor /> </q-page>
</template>

<script setup>
import MarkdownEditor from 'components/MarkdownEditor.vue'
import { onMounted } from 'vue'
import { usePostStore } from 'stores/postStore'

onMounted(() => {
  const p = usePostStore()
  p.reset()
})
</script>
