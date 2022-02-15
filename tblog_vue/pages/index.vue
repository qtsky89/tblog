<template>
<div>
  <!-- Tutorial/ -->
  <!-- <nuxt-link to="/">Home page!</nuxt-link> -->

  <b-navbar class="main-navbar" toggleable="lg" type="light" variant="light">
    <b-navbar-brand href="#" sticky=true>Tech Blog</b-navbar-brand>
  </b-navbar>
  <b-row
    class="card-row"
  >
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
    </b-col>
    <b-col class="mt-3" md="4">
      <b-card img-src="https://placekitten.com/1000/500" img-alt="Card image" img-top>
        <b-card-text>
          Some quick example text to build on the card and make up the bulk of the card's content.
        </b-card-text>
      </b-card>
    </b-col>

  </b-row>
</div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'IndexPage'
})
</script>

<style scoped>

.main-navbar {
  padding-left: 3.5rem !important;
}

.card-row {
  padding-left: 10rem;
  padding-right: 10rem;
}
</style>