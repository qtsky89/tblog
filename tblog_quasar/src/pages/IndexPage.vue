<template>
  <div>{{ p.counter }}</div>
</template>

<script lang="ts">
import { usePostStore } from 'stores/postStore'

export default {
  preFetch({ store }) {
    const p = usePostStore(store)
    p.increment()
    p.increment()
    p.increment()
  },
}
</script>

<script setup lang="ts">
import { api } from 'boot/axios'
const p = usePostStore()

const res = await api.get('/api/v1/post')
console.log(res)
</script>
