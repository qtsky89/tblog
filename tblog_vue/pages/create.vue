<template>
  <div class="total">
    <b-container class="editor-container">
      <b-row>
        <b-col sm="5" class="p-0">
          <b-form-input
            v-model="title"
            class="mt-3"
            size="lg"
            placeholder="Enter the post title"
          />
        </b-col>
      </b-row>
      <b-row>
        <b-form-input
          v-model="description"
          class="mt-3"
          size="lg"
          placeholder="Enter the post description"
        />
      </b-row>
      <b-row>
        <b-form-tags
          v-model="tags"
          class="mt-3"
          size="lg"
          tag-pills
          tag-variant="primary"
          placeholder="Enter the post tags"
        />
      </b-row>
      <b-row>
        <no-ssr>
          <mavon-editor
            v-model="body"
            class="editor mt-3"
            :toolbars="toolbarOption"
            language="en"
            font-size="16px"
            placeholder="Enter the post body"
            :box-shadow="false"
          />
        </no-ssr>
      </b-row>
    </b-container>
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      title: '',
      body: '',
      description: '',
      tags: [],
      toolbarOption: {
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
        save: true,
        navigation: true,
        alignleft: true,
        aligncenter: true,
        alignright: true,
        subfield: true,
        preview: true,
      },
    }
  },
}
</script>

<style scoped>
.editor-container {
  width: 100%;
}

.editor {
  width: 100%;
  height: 70vh;
  border: 1px solid #ced4da;
}
</style>
