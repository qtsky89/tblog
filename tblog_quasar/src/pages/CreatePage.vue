<template>
  <q-page class="q-pa-md">
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
  </q-page>
</template>

<script setup>
import { onMounted, reactive } from 'vue'
import { useRoute } from 'vue-router'
import { api } from 'boot/axios'

onMounted(() => {
  const route = useRoute()
  console.log(route.params)
})

const data = reactive({
  title: '',
  body: '',
  description: '',
  tags: [],
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

async function publish() {
  try {
    await api.post('/api/v1/post', data)
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
  /* border: 1px solid #ced4da; */
}
</style>
