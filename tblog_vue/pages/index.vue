<template>
<div>
  <b-row class="card-row">
    <b-card v-for="post in posts" :key="post.id" class="mt-2 mb-2 post-card" title=post.title @click="postClick">
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
  async asyncData({ $axios, $config: { djangoURL}}) {
    const res = await $axios.get(`${djangoURL}/api/v1/post`)
    const posts = res.data.data
    return { posts }
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
.card-row {
  padding-left: 25rem;
  padding-right: 25rem;
}

.post-card {
  width: 100%;
  border: 1px solid;
  cursor: pointer;
}

.post-card:hover {
  background: #4093d2 !important;
}
</style>