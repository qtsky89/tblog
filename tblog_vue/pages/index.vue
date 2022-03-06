<template>
<div>
  <b-row>
    <b-card v-for="post in posts" :key="post.id" sm="4" class="mt-2 mb-2 post-card" title=post.title @click="postClick">
      <b-card-text>
        {{ post.body }}
      </b-card-text>
      <a href="#" class="card-link">Card link</a>
      <b-link href="#" class="card-link">Another link</b-link>
    </b-card>
  </b-row>
</div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'IndexPage',
  async asyncData({ $axios, $config: { djangoURL }}) {
    try {
    const res = await $axios.get(`${djangoURL}/api/v1/post`)
    const posts = res.data.data
    return { posts }
    } catch (error) {
      console.error(error)
    }
  },
  data () {
    return  {
      posts: []
    }
  },
  methods: {
    postClick () {
      this.$router.push('/funHo')
    }
  },
})
</script>

<style scoped>

.post-card {
  border: 1px solid;
  cursor: pointer;
  vertical-align: middle;
  margin: 0 auto;
  width: 70%;
}

.post-card:hover {
  background: #4093d2 !important;
}
</style>