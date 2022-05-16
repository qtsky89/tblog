import { defineStore } from 'pinia'
import { IndexState } from 'components/models'

export const useIndexStore = defineStore('index', {
  state: (): IndexState => ({
    posts: [],
    tags: [],
  }),
  getters: {
    doubleCount: (state) => 1 * 2,
  },
  actions: {
    async initialize() {
      try {
        const [postsRes, tagRes] = await Promise.all([
          this.api.get('/api/v1/post'),
          this.api.get('/api/v1/tag'),
        ])
        this.posts = postsRes.data.data
        this.tags = tagRes.data.data
      } catch (error) {
        console.error(error)
      }
    },
  },
})
