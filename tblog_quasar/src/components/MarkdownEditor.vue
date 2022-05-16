<template>
  <div class="editor-container">
    <q-input class="input-form" v-model="data.title" label="title">
      <template v-slot:after>
        <q-btn round @click="publish" icon="send" />
      </template>
    </q-input>
    <q-input
      class="input-form"
      v-model="data.description"
      label="description"
    />
    <!-- TODO: add tag form -->
    <q-no-ssr>
      <mavon-editor
        v-model="data.body"
        class="editor q-mt-lg"
        :toolbars="editorOption"
        language="en"
        font-size="16px"
        :box-shadow="true"
      />
    </q-no-ssr>
  </div>
</template>

<script setup lang="ts">
import { reactive, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { api } from 'boot/axios'

// interface
interface Post {
  id: number
  title: string
  body: string
  description: string
  create_date: string
  tags: Array<string>
}
interface Prop {
  data: Post
}
//

let data: Post = reactive({
  id: 0,
  title: '',
  body: '',
  description: '',
  tags: [],
  create_date: '',
})

const props = defineProps<Prop>()
onMounted(async () => {
  console.log('child')
  console.log(props.data)
})

const editorOption = {
  bold: true,
  italic: true,
  header: true,
  underline: true,
  strikethrough: true,
  mark: true,
  superscript: true,
  subscript: true,
  quote: true,
  ol: true,
  ul: true,
  link: true,
  imagelink: true,
  code: true,
  table: true,
  fullscreen: true,
  readmodel: true,
  htmlcode: true,
  help: true,
  undo: true,
  redo: true,
  trash: true,
  navigation: true,
  alignleft: true,
  aligncenter: true,
  alignright: true,
  subfield: true,
  preview: true,
}

const router = useRouter()
async function publish() {
  try {
    await api.post('/api/v1/post', data)
    router.push('/')
  } catch (error) {
    console.error(error)
  }
}
</script>

<style scoped>
.input-form {
  width: 100%;
}
.editor-container {
  width: 1000px;
  margin: auto;
}

.editor {
  width: 100%;
  height: 65vh;
}
</style>
