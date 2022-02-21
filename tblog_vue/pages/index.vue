<template>
<div>
  <b-row
    class="card-row"
  >
  <div v-for="post in posts" class="mt-2 mb-2 post-card">
    <b-card title=post.title>
      <b-card-text>
        {{ post.body }}
      </b-card-text>
      <a href="#" class="card-link">Card link</a>
      <b-link href="#" class="card-link">Another link</b-link>
    </b-card>
  </div>

  <!-- <div v-for="post in posts">
    {{ post }}
  </div> -->

    <!-- <b-col class="mt-3" md="4">
      <b-card img-src="https://placekitten.com/1000/500" img-alt="Card image" img-top>
        <b-card-text>
          Some quick example text to build on the card and make up the bulk of the card's content.
        </b-card-text>
      </b-card>
    </b-col>
    <b-col class="mt-3" md="4">
      <b-card img-src="https://placekitten.com/1000/500" img-alt="Card image" img-top>
        <b-card-text>
          Some quick example text to build on the card and make up the bulk of the card's content.
        </b-card-text>
      </b-card>
    </b-col>
    <b-col class="mt-3" md="4">
      <b-card img-src="https://placekitten.com/1000/500" img-alt="Card image" img-top>
        <b-card-text>
          Some quick example text to build on the card and make up the bulk of the card's content.
        </b-card-text>
      </b-card>
    </b-col>
    <b-col class="mt-3" md="4">
      <b-card img-src="https://placekitten.com/1000/500" img-alt="Card image" img-top>
        <b-card-text>
          Some quick example text to build on the card and make up the bulk of the card's content.
        </b-card-text>
      </b-card>
    </b-col> -->

  </b-row>
</div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'IndexPage',
  data () {
    return  {
      posts: []
    }
  },
    async fetch() {
      const res = await this.$axios.get('http://csh61127.nfra.io:8000/api/v1/post')
      this.posts = res.data.data
    }
})
</script>

<style scoped>
.card-row {
  padding-left: 25rem;
  padding-right: 25rem;
}

.post-card {
  width: 100%;
}
</style>