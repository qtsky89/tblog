import { boot } from 'quasar/wrappers'
import vue3GoogleLogin from 'vue3-google-login'

export default boot(({ app }) => {
  app.use(vue3GoogleLogin, {
    clientId:
      '287549598528-jmrn0f9k69t1k7f5i1002bpm5192rtdt.apps.googleusercontent.com',
  })
})
