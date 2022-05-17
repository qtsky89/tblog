import { defineStore } from 'pinia'
import { IndexState } from 't-common'
import { api } from 'boot/axios'

export const useIndexStore = defineStore('index', {
  state: (): IndexState => ({
    posts: [],
    tags: [],
  }),
  actions: {
    async initialize() {
      try {
        const [postsRes, tagRes] = await Promise.all([
          api.get('/api/v1/post'),
          api.get('/api/v1/tag'),
        ])
        this.posts = postsRes.data.data
        this.tags = tagRes.data.data
      } catch (error) {
        console.error(error)
      }
    },
  },
})
