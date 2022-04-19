<template>
  <div>
    <b-container class="tagbar">
      <span v-for="tag in tags" :key="tag" class="tag">{{ tag }}</span>
    </b-container>
  </div>
</template>

<script lang="ts">
export default {
  name: 'TagBar',
  props: {
    tags: {
      type: Array,
      default: () => [],
    },
  },
}
</script>

<style scoped>
.tagbar {
  width: 800px;
}

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
</style>
