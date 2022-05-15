import { defineStore } from 'pinia'

interface Post {
  id: number
  title: string
  description: string
  create_date: string
  tags: Array<string>
}

export const usePostStore = defineStore('index', {
  state: () => ({
    posts: [],
    tags: [],
  }),
  getters: {
    doubleCount: (state) => state.counter * 2,
  },
  actions: {
    increment() {
      this.counter++
    },
  },
})
