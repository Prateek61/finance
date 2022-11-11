<template>
  <v-app class="bg-grey-lighten-4">
    <nav-vue v-if="notAuth"/>
    <v-main v-bind:class="{'py-5': user}">
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import axios from 'axios'
import NavVue from '@/components/NavVue.vue'
import { mapGetters } from 'vuex'
export default {
  components: {
    NavVue
  },
  data () {
    return {
    }
  },
  async created () {
    const response = await axios.get('/getuser')
    this.$store.dispatch('user', response.data.user)
  },
  computed: {
    ...mapGetters(['user']),
    notAuth () {
      if (this.$route.name === 'Auth') {
        return false
      } else {
        return true
      }
    }
  }
}
</script>

<style>
</style>
