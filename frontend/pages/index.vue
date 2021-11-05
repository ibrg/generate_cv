<template>
  <div class="">
    <h1>Index</h1>
    <p v-for="cv in getCV" :key="cv.id">
      {{ cv.title }}
    </p>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  computed: mapGetters(['getCV']),
  mounted () {
    // this.$store.dispatch("fetchPosts");
    this.loadCV()
  },
  methods: mapActions(['loadCV'])

}

</script>
