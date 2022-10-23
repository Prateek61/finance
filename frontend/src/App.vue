<template>
  <nav-vue v-if="user"/>
  <div class="container-fluid py-5 text-center">
    <router-view/>
  </div>
</template>

<script>
import axios from 'axios'
import NavVue from '@/components/NavVue.vue'
import { mapGetters } from 'vuex'

export default {
  components: {
    NavVue
  },
  async created () {
    const response = await axios.get('/getuser')
    console.log(response.data.user)
    this.$store.dispatch('user', response.data.user)
  },
  computed: {
    ...mapGetters(['user'])
  }
}
</script>

<style>

</style>
