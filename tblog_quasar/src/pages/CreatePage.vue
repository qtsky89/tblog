<template>
  <q-page class="q-pa-md"> <MarkdownEditor /> </q-page>
</template>

<script setup>
import MarkdownEditor from 'components/MarkdownEditor/MarkdownEditor.vue'
import { onMounted, nextTick } from 'vue'
import { usePostStore } from 'stores/postStore'

onMounted(() => {
  nextTick(() => {
    const p = usePostStore()
    p.reset()
  })
})
</script>
