import { boot } from 'quasar/wrappers'
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'

// "async" is optional;
// more info on params: https://v2.quasar.dev/quasar-cli/boot-files
export default boot(({ app }) => {
  app.use(mavonEditor)
})
