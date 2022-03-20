<template>
  <div>
    <b-row>
      <div class="tagbar">
        <span v-for="tag in tags" class="tag">{{ tag }}</span>
      </div>
    </b-row>
    <b-row>
      <b-col cols="12">
        <b-card
          v-for="post in posts"
          :key="post.id"
          sm="4"
          class="mt-3 mb-3 post-card"
          title="post.title"
          @click="postClick"
        >
          <b-card-text>
            {{ post.body }}
          </b-card-text>
          <a href="#" class="card-link">Card link</a>
          <b-link href="#" class="card-link">Another link</b-link>
        </b-card>
      </b-col>
    </b-row>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'IndexPage',
  async asyncData({ $axios, $config: { djangoURL } }) {
    try {
      const [postsRes, tagRes] = await Promise.all([
        $axios.get(`${djangoURL}/api/v1/post`),
        $axios.get(`${djangoURL}/api/v1/tag`),
      ])
      return {
        posts: postsRes.data.data,
        tags: tagRes.data.data,
      }
    } catch (error) {
      console.error(error)
    }
  },
  data() {
    return {
      posts: [],
    }
  },
  methods: {
    postClick() {
      this.$router.push('/funHo')
    },
  },
})
</script>

<style scoped>
.post-card {
  border: 1px solid;
  cursor: pointer;
  vertical-align: middle;
  margin: 0 auto;
  width: 800px;
}

.post-card:hover {
  background: #4093d2 !important;
}

.tagbar {
  width: 800px;
  margin: 0 auto;
}

.tag {
  font-size: 1.5rem;
  display: inline-block;
  padding: 0.25rem 0.5rem;
  margin: 5px 5px 5px;
  color: rgb(33, 37, 41);
  background: rgb(241, 243, 245);
  font-weight: 600;
  border-radius: 1rem;
  cursor: pointer;
}

.tag:hover {
  background: #4093d2 !important;
}
</style>
