import { defineStore } from 'pinia'
import { UserState } from 't-common'

export const useUserStore = defineStore('user', {
  state: (): UserState => ({
    user: defaultUserState()
  }),
  actions: {
    login(emailAddress: string, picture: string): void {
      this.user.emailAddress = emailAddress
      this.user.picture = picture
    },
    logout(): void {
      this.user = defaultUserState()
    }
  },
  getters: {
    isLoggedIn(): boolean {
      return this.user.emailAddress !== ''
    }
  }
})

function defaultUserState() {
  return {
    emailAddress: '',
    isSu: false,
    picture: ''
  }
}
