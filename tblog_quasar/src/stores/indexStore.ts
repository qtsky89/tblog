import { defineStore } from 'pinia'
import { IndexState, Post } from 't-common'
import { api } from 'boot/axios'

export const useIndexStore = defineStore('index', {
  state: (): IndexState => ({
    posts: [],
    tags: [],
    selectedTag: '',
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

  getters: {
    selectedPosts(): Post[] {
      if (this.selectedTag !== '') {
        return this.posts.filter((p) => p.tags.includes(this.selectedTag))
      }
      return this.posts
    },
    selectedTags(): string[] {
      if (this.selectedTag !== '') {
        return [this.selectedTag]
      }
      return this.tags
    },
  },
})
