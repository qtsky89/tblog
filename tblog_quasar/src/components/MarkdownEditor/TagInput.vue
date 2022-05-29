<template>
  <div>
    <div v-for="(tag, index) in p.tags" :key="tag" class="tag-input">
      <span style="color: black" @click="deleteTag(index)">x </span>{{ tag }}
    </div>
    <q-input
      @keyup.enter="addTag"
      @keyup.space="addTag"
      @keyup.delete="deleteLastTag"
      label="tags"
    />
  </div>
</template>
<script setup lang="ts">
import { usePostStore } from 'src/stores/postStore'

const p = usePostStore()

function addTag(e: Event) {
  e.preventDefault()
  const val = (e.target as HTMLInputElement).value.trim()
  if (val.length > 0 && !p.tags.includes(val)) {
    p.tags.push(val)
    ;(e.target as HTMLInputElement).value = ''
  }
}

function deleteTag(index: number) {
  p.tags.splice(index, 1)
}

function deleteLastTag(e: Event) {
  e.preventDefault()
  if ((e.target as HTMLInputElement).value.length === 0) {
    deleteTag(p.tags.length - 1)
  }
}
</script>
<style scoped>
.tag-input {
  height: 30px;
  font-size: 14px;
  float: left;
  margin: 20px 8px 0px 0px;
  color: #959595;
  font-weight: 600;
  border: 1px solid #d1d1d1;
  background-color: #eee;
  line-height: 25px;
  padding: 0 5px;
  border-radius: 14px;
}

.tag-input > span {
  cursor: pointer;
  opacity: 0.4;
}
</style>
