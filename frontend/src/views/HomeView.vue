<template>
  <v-main>
    <v-container v-if="user">
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
