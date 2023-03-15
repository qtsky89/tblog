<template>
  <q-page class="q-pa-sm post-card">
    <h3 class="q-mt-lg">{{ p.title }}</h3>
    <span>{{ formatYYYYMMDD(p.created_date) }}</span>
    <TagBar :tags="p.tags" @click:tag="tagClick" />
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
import { useIndexStore } from 'stores/indexStore'
import TagBar from 'components/TagBar.vue'
import { useRouter } from 'vue-router'
import { formatYYYYMMDD } from '../utils/day'

const p = usePostStore()
const s = useIndexStore()
const r = useRouter()

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

function tagClick(tag: string) {
  s.selectedTag = tag
  r.push('/')
}
</script>

<style scoped>
.post-card {
  width: 850px;
  margin: auto;
}
</style>
