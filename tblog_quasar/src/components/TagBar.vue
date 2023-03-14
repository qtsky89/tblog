<template>
  <div>
    <span
      v-for="tag in props.tags"
      :key="tag"
      class="tag click"
      @click="click(tag)"
    >
      {{ tag }}
    </span>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{ tags: Array<string> }>()
const emits = defineEmits(['click:tag'])

function click(tag: string): void {
  emits('click:tag', tag)
}
</script>

<style scoped>
.tag {
  font-size: 14px;
  display: inline-block;
  padding: 4px 10px;
  margin: 15px 8px 10px 0;
  color: #959595;
  font-weight: 600;
  border: 1px solid #d1d1d1;
  border-radius: 14px;
  cursor: pointer;
}

.click {
  cursor: pointer;
}
.click:hover {
  background: #4093d2 !important;
}
</style>
