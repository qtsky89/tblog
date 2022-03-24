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
          <b-card-text class="post-card-text">
            {{ post.summary }}
          </b-card-text>
          <!-- <a href="#" class="card-link">Card link</a>
          <b-link href="#" class="card-link">Another link</b-link> -->
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
  cursor: pointer;
  vertical-align: middle;
  margin: 0 auto;
  width: 800px;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  min-height: 110px;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  word-wrap: break-word;
}

.post-card:hover {
  background: #4093d2 !important;
}

.post-card-text {
  color: hsla(0, 0%, 0%, 0.801);
}

.tagbar {
  width: 800px;
  margin: 0 auto;
}

.tag {
  font-size: 12px;
  display: inline-block;
  padding: 4px 10px;
  margin: 15px 8px 10px 0;
  color: #959595;
  font-weight: 600;
  border: 1px solid #d1d1d1;
  border-radius: 14px;
  cursor: pointer;
}

.tag:hover {
  background: #4093d2 !important;
  color: #000000;
}
</style>
