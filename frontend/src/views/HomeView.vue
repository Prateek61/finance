<template>
  <v-main>
    <v-container v-if="user">
      <v-row wrap>
        <v-col cols="12" lg="6">
          <bar-graph></bar-graph>
        </v-col>
        <v-col cols="12" lg="6">
          <pie-chart></pie-chart>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
import { mapGetters } from 'vuex'
import BarGraph from '@/components/BarGraph.vue'
import PieChart from '@/components/PieChart.vue'

export default {
  name: 'HomeView',

  components: {
    BarGraph,
    PieChart
  },

  computed: {
    ...mapGetters(['user'])
  }
}
</script>
