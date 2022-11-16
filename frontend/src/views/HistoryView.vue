<template>
  <v-container class="my-5">
    <h4>Expenditure History</h4>
    <history-row
      v-for="(item, index) in history"
      :key="index"
      :data="item"
      :style="icon[item.category]"
    ></history-row>
  </v-container>
</template>

<script>
import axios from 'axios'
import HistoryRow from '@/components/HistoryRow.vue'
import icons from '@/assets/icons.json'

export default {
  name: 'HistoryView',

  components: {
    HistoryRow
  },

  data () {
    return {
      history: null,
      icon: icons
    }
  },

  async created () {
    const response = await axios.get('/history')
    this.history = response.data.history
  }
}
</script>
