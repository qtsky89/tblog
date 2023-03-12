import { defineStore } from 'pinia'
import { UserState, User } from 't-common'

export const useUserStore = defineStore('user', {
  state: (): UserState => ({
    user: defaultUser()
  }),
  actions: {
    login(email: string, picture: string, isSu: boolean): void {
      this.user.email = email
      this.user.picture = picture
      this.user.isSu = isSu
    },
    logout(): void {
      this.user = defaultUser()
    }
  },
  getters: {
    isLoggedIn(): boolean {
      return this.user.email !== ''
    }
  }
})

function defaultUser(): User {
  return {
    email: '',
    isSu: false,
    picture: ''
  }
}
