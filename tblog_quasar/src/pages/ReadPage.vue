<template>
  <q-page class="q-pa-md post-card">
    <h5>{{ p.title }}</h5>
    <q-markdown :src="p.body" />
  </q-page>
</template>

<script lang="ts">
import { usePostStore } from 'stores/postStore'
import { useMeta } from 'quasar'

export default {
  async preFetch({ currentRoute }) {
    const p = usePostStore()
    await p.initialize(currentRoute.params.id as string)
  },
}
</script>
<script setup lang="ts">
const p = usePostStore()

// TODO: Optimize meta data (https://quasar.dev/quasar-plugins/meta)
useMeta(() => {
  return {
    title: p.title,
    meta: {
      description: { name: 'description', content: p.description },
      keywords: { name: 'keywords', content: p.tags },
      equiv: {
        'http-equiv': 'Content-Type',
        content: 'text/html; charset=UTF-8',
      },
      ogTitle: {
        property: 'og:title',
        template() {
          return p.title
        },
      },
    },
  }
})
</script>

<style scoped>
.post-card {
  width: 850px;
  margin: auto;
}
</style>
