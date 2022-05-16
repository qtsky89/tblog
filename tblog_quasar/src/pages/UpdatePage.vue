<template>
  <q-page class="q-pa-md"> <MarkdownEditor :data="data" /> </q-page>
</template>

<script setup lang="ts">
import MarkdownEditor from 'components/MarkdownEditor.vue'
import { Post } from 'components/models'
import { useRoute } from 'vue-router'
import { onBeforeMount } from 'vue'
import { api } from 'boot/axios'

let data: Post = {
  id: 0,
  title: '',
  body: '',
  description: '',
  create_date: '',
  tags: [],
}
onBeforeMount(async () => {
  const r = useRoute()
  try {
    const res = await api.get(`/api/v1/post/${r.params.id}`)
    data = res.data.data[0]
  } catch (error) {
    console.error(error)
  }

  console.log('parent')
  console.log(data)
})
</script>
