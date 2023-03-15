<template>
  <q-page class="q-pa-md post-cards">
    <TagBar :tags="s.selectedTags" @click:tag="tagClick" />
    <q-card
      v-for="post in s.selectedPosts"
      :key="(post.id as number)"
      class="col-12 q-mt-sm q-mb-sm"
    >
      <div class="click" @click="postClick(post.id as number)">
        <q-card-section>
          <div class="text-h6">{{ post.title }}</div>
        </q-card-section>
        <q-card-section class="q-pt-none description-text">
          {{ post.description }}
        </q-card-section>
      </div>

      <q-separator inset />
      <q-card-actions>
        <TagBar :tags="post.tags" @click:tag="tagClick" />
      </q-card-actions>
    </q-card>
  </q-page>
</template>

<script lang="ts">
import { useIndexStore } from 'stores/indexStore'
import TagBar from 'components/TagBar.vue'

export default {
  async preFetch() {
    const p = useIndexStore()
    await p.initialize()
  },
}
</script>

<script setup lang="ts">
import { useRouter } from 'vue-router'
const s = useIndexStore()
const r = useRouter()

function tagClick(tag: string) {
  s.selectedTag = tag
}

function postClick(id: number) {
  r.push(`/post/${id}`)
}
</script>

<style scoped>
.post-cards {
  width: 850px;
  margin: auto;
}
.description-text {
  color: hsla(0, 0%, 0%, 0.55);
}

.click {
  cursor: pointer;
}
.click:hover {
  background: #4093d2 !important;
}
</style>
