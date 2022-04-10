<template>
  <div class="total">
    <b-container class="editor-container">
      <b-row>
        <b-form-input
          v-model="title"
          class="mt-3"
          size="lg"
          placeholder="Enter the post title"
        >
        </b-form-input>
      </b-row>
      <b-row>
        <b-form-tags
          v-model="tags"
          class="mt-3"
          size="lg"
          tag-pills
          tag-variant="primary"
          placeholder="Enter the post tags"
        ></b-form-tags
      ></b-row>
      <b-row>
        <no-ssr>
          <mavon-editor
            v-model="body"
            class="editor mt-3"
            :toolbars="toolbarOption"
            language="en"
            font-size="15px"
            placeholder="Enter the post body"
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
}
</style>
