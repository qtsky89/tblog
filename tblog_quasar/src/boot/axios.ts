import { boot } from 'quasar/wrappers'
import axios, { AxiosInstance } from 'axios'
import { json } from 'body-parser'
import { User } from 't-common'

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $axios: AxiosInstance
  }
}

// Be careful when using SSR for cross-request state pollution
// due to creating a Singleton instance here;
// If any client changes this (global) instance, it might be a
// good idea to move this instance creation inside of the
// "export default () => {}" function below (which runs individually
// for each client)
const api = axios.create({ baseURL: process.env.DJANGO_URL })

// https://gusrb3164.github.io/web/2022/08/07/refresh-with-axios-for-client/
api.interceptors.request.use((config) => {
  if(!config.headers) {
    return config
  }

  const user = localStorage.getItem('loginInfo')
  if (user !== null) {
    const u: User = JSON.parse(user)
    config.headers.Authorization = `Bearer ${u.encodedJwt}`;
  }

  return config
})

export default boot(({ app, store }) => {
  // for use inside Vue files (Options API) through this.$axios and this.$api

  app.config.globalProperties.$axios = axios
  // ^ ^ ^ this will allow you to use this.$axios (for Vue Options API form)
  //       so you won't necessarily have to import axios in each vue file

  app.config.globalProperties.$api = api
  // ^ ^ ^ this will allow you to use this.$api (for Vue Options API form)
  //       so you can easily perform requests against your app's API

  store.use(({ store }) => {
    store.api = api
  })
})

export { api }
