<template>
  <div>
    <tag-bar :tags="post.tags" />
    <b-container class="post-body mt-3">
      <span>{{ post.body }}</span>
    </b-container>
  </div>
</template>

<script lang="ts">
import TagBar from '@/components/TagBar.vue'

export default {
  components: {
    TagBar,
  },
  async asyncData({ params, $axios }) {
    try {
      const [postRes] = await Promise.all([
        $axios.get(`/api/v1/post/${params.id}`),
      ])
      return {
        post: postRes.data.data[0],
      }
    } catch (error) {
      console.error(error)
    }
  },
}
</script>

<style scoped>
.post-body {
  width: 800px;
}
</style>
