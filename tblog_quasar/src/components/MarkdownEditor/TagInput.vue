<template>
  <div>
    <div v-for="(tag, index) in tags" :key="tag" class="tag-input">
      <span @click="deleteTag(index)">x</span>{{ tag }}
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
import { ref } from 'vue'
import type { Ref } from 'vue'

const tags: Ref<string[]> = ref([])

function addTag(e: Event) {
  e.preventDefault()
  const val = (e.target as HTMLInputElement).value.trim()
  if (val.length > 0 && !tags.value.includes(val)) {
    tags.value.push(val)
    ;(e.target as HTMLInputElement).value = ''
  }
}

function deleteTag(index: number) {
  tags.value.splice(index, 1)
}

function deleteLastTag(e: Event) {
  e.preventDefault()
  if ((e.target as HTMLInputElement).value.length === 0) {
    deleteTag(tags.value.length - 1)
  }
}
</script>
<style scoped>
/* .tag-input {
  width: 100%;
  border: 1px solid #eee;
  font-size: 1em;
  height: 70px;
  box-sizing: border-box;
  padding: 0 10px;
} */

.tag-input {
  height: 30px;
  float: left;
  margin-right: 10px;
  background-color: #eee;
  margin-top: 16px;
  line-height: 30px;
  padding: 0 5px;
  border-radius: 5px;
}

.tag-input > span {
  cursor: pointer;
  opacity: 0.75;
}

/* .tag-input__text {
  border: none;
  outline: none;
  font-size: 0.9em;
  line-height: 50px;
  background: none;
} */
</style>
