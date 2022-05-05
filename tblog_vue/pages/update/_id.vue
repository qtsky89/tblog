<template>
  <Editor />
</template>

<script lang="ts">
import Editor from '@/components/Editor.vue'

export default {
  components: { Editor },
  async mounted() {
    const id = this.$route.params.id
    const res = await this.$axios.get(`/api/v1/post/${id}`)
    console.log(res.data.data[0])
  },
}
</script>
