<template>
  <div>
    <span>{{ post.body }}</span>
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

<style></style>
