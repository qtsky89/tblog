<template>
  <div>
    <tag-bar :tags="tags" />
    <b-container class="post-cards">
      <b-row>
        <b-col cols="12">
          <b-card
            v-for="post in posts"
            :key="post.id"
            sm="4"
            class="mt-3 mb-3 post-card"
            :title="post.title"
            @click="postClick(post.id)"
          >
            <b-card-text class="post-card-text">
              {{ post.description }}
            </b-card-text>
            <template #footer>
              <span v-for="t in post.tags" :key="t" class="card-tag"
                >{{ t }}
              </span>
            </template>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import TagBar from '@/components/TagBar.vue'

export default Vue.extend({
  name: 'IndexPage',
  components: {
    TagBar,
  },
  async asyncData({ $axios }) {
    try {
      const [postsRes, tagRes] = await Promise.all([
        $axios.get('/api/v1/post'),
        $axios.get('/api/v1/tag'),
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
    postClick(id: string) {
      this.$router.push(`/post/${id}`)
    },
  },
})
</script>

<style scoped>
.card-footer {
  padding: 11px 0px 0px 16px;
  background-color: rgba(0, 0, 0, 0);
}

.post-cards {
  width: 800px;
}
.post-card {
  cursor: pointer;
  overflow: hidden;
  text-overflow: ellipsis;
  min-height: 150px;
  word-wrap: break-word;
}

.post-card:hover {
  background: #4093d2 !important;
}

.post-card-text {
  color: hsla(0, 0%, 0%, 0.801);
}

.card-tag {
  font-size: 14px;
  display: inline-block;
  padding: 0px 5px;
  margin: 0px 8px 10px 0px;
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
