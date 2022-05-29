<template>
  <q-page class="q-pa-md post-cards row">
    <TagBar :tags="s.tags" />
    <q-card
      v-for="post in s.posts"
      :key="post.id"
      class="col-12 q-mt-sm q-mb-sm post-card"
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
      <q-card-actions class="q-mt-sm">
        <span v-for="t in post.tags" :key="t" class="card-tags click"
          >{{ t }}
        </span>
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
function postClick(id: number) {
  r.push(`/post/${id}`)
}
</script>

<style scoped>
.post-cards {
  width: 850px;
  margin: auto;
}

.card-tags {
  font-size: 14px;
  display: inline-block;
  padding: 0px 5px;
  margin: 0px 8px 10px 0px;
  color: #959595;
  font-weight: 600;
  border: 1px solid #d1d1d1;
  border-radius: 14px;
  cursor: pointer;
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
