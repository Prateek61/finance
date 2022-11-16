<template>
  <v-main>
    <v-container v-if="user">
      <v-row wrap>
        <v-col cols="12" lg="6">
          <BarGraphVue />
        </v-col>
        <v-col cols="12" lg="6">
          <PieChartVue />
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
import { mapGetters } from 'vuex'
import BarGraphVue from '@/components/BarGraphVue.vue'
import PieChartVue from '@/components/PieChartVue.vue'

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
    BarGraphVue,
    PieChartVue
  }
}
</script>
