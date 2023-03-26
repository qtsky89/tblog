import { defineStore } from 'pinia'
import { UserState, User } from 't-common'

export const useUserStore = defineStore('user', {
  state: (): UserState => ({
    user: defaultUser()
  }),
  actions: {
    login(email: string, picture: string, isSu: boolean, encodedJwt: string): void {
      this.user.email = email
      this.user.picture = picture
      this.user.isSu = isSu
      this.user.encodedJwt = encodedJwt
      localStorage.setItem('loginInfo', JSON.stringify(this.user))
    },
    logout(): void {
      this.user = defaultUser()
      localStorage.removeItem('loginInfo')
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
    picture: '',
    encodedJwt: ''
  }
}
