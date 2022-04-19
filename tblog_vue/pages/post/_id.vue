<template>
  <div>
    <b-container class="post-body">
      <span>{{ post.body }}</span>
    </b-container>
  </div>
</template>

<script lang="ts">
export default {
  async asyncData({ params, $axios, $config: { djangoURL } }) {
    try {
      const [postRes] = await Promise.all([
        $axios.get(`${djangoURL}/api/v1/post/${params.id}`),
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
}
</style>
