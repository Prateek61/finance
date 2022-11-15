<template>
  <v-main>
    <v-container v-if="user">
      <p>Hello, welcome {{user.username}}</p>
      <BarGraphVue />
    </v-container>
  </v-main>
</template>

<script>
import { mapGetters } from 'vuex'
import BarGraphVue from '@/components/BarGraphVue.vue'

export default {
  name: 'HomeView',
  data () {
    return {
    }
  },
  methods: {
  },
  computed: {
    ...mapGetters(['user'])
  },
  components: {
    BarGraphVue
  }
}
</script>
