<template>
  <div class="total">
    <b-container class="editor-container">
      <b-row class="title">
        <b-col sm="5" class="p-0">
          <b-form-input
            v-model="title"
            class="mt-3"
            size="md"
            placeholder="Enter the post title"
          />
        </b-col>
        <b-col>
          <b-button
            class="publish-button mt-3"
            pill
            variant="outline-info"
            @click="publish"
            >Publish</b-button
          >
        </b-col>
      </b-row>
      <b-row>
        <b-form-input
          v-model="description"
          class="mt-3"
          size="md"
          placeholder="Enter the post description"
        />
      </b-row>
      <b-row>
        <b-form-tags
          v-model="tags"
          class="mt-3"
          size="md"
          tag-pills
          tag-variant="primary"
          placeholder="Enter the post tags"
        />
      </b-row>
      <b-row>
        <client-only>
          <mavon-editor
            v-model="body"
            class="editor mt-3"
            :toolbars="toolbarOption"
            language="en"
            font-size="16px"
            placeholder="Enter the post body"
            :box-shadow="false"
          />
        </client-only>
      </b-row>
    </b-container>
  </div>
</template>

<script lang="ts">
interface publishData {
  title: string
  body: string
  description: string
  tags: Array<string>
}

export default {
  props: {
    form: {
      type: Object,
      default: () => {},
    },
  },
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
        navigation: true,
        alignleft: true,
        aligncenter: true,
        alignright: true,
        subfield: true,
        preview: true,
      },
    }
  },
  mounted() {
    console.log(this.form)
    console.log(this.$route.name)
  },
  methods: {
    async publish() {
      try {
        const data: publishData = {
          title: this.title,
          body: this.body,
          description: this.description,
          tags: this.tags,
        }
        await this.$axios.post('/api/v1/post', data)
        this.$router.push('/')
      } catch (error) {
        console.error(error)
      }
    },
  },
}
</script>

<style scoped>
.editor-container {
  width: 100%;
}

.editor {
  width: 100%;
  height: 65vh;
  border: 1px solid #ced4da;
}

.publish-button {
  float: right;
}

.title {
  justify-content: space-between;
}
</style>
