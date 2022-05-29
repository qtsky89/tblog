import { defineStore } from 'pinia'
import { Post } from 't-common'
import { api } from 'boot/axios'

export const usePostStore = defineStore('post', {
  state: (): Post => ({
    id: null,
    title: '',
    body: '',
    description: '',
    create_date: '',
    tags: [],
  }),
  actions: {
    reset() {
      this.title = ''
      this.body = ''
      this.description = ''
      this.create_date = ''
      this.tags = []
    },
    async initialize(id: string) {
      try {
        const res = await api.get(`/api/v1/post/${id}`)
        this.title = res.data.data[0].title
        this.body = res.data.data[0].body
        this.description = res.data.data[0].description
        this.create_date = res.data.data[0].create_date
        this.tags = res.data.data[0].tags
      } catch (error) {
        console.error(error)
      }
    },
  },
})
