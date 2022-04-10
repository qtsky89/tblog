<template>
  <div class="total">
    <b-container class="editor-container">
      <b-row>
        <no-ssr>
          <mavon-editor
            v-model="editorData"
            class="editor"
            :toolbars="toolbarOption"
            language="en"
            font-size="15px"
            placeholder="Please enter the post body"
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
      editorData: '',
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
  height: 100%;
}
</style>
