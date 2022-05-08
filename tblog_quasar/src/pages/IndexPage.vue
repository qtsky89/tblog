<template>
  <div>{{ c.counter }}</div>
</template>

<script lang="ts">
import { useCounterStore } from 'stores/example-store'

export default {
  preFetch({ store }) {
    const c = useCounterStore(store)
    c.increment()
    c.increment()
    c.increment()
  },
}
</script>

<script setup lang="ts">
import { api } from 'boot/axios'
const c = useCounterStore()

const res = await api.get('/api/v1/post')
console.log(res)
</script>
