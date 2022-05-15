<template>
  <p>create page</p>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRoute } from 'vue-router'

onMounted(() => {
  const route = useRoute()
  console.log(route.params)
})
</script>
