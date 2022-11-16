<template>
  <v-app class="bg-grey-lighten-4">
    <base-nav v-if="notAuth"></base-nav>
    <v-main :class="{'py-5': user}">
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import axios from 'axios'
import BaseNav from '@/components/BaseNav.vue'
import { mapGetters } from 'vuex'

export default {
  components: {
    BaseNav
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
  },

  async created () {
    const response = await axios.get('/getuser')
    this.$store.dispatch('user', response.data.user)
  }
}
</script>

<style>
</style>
