<template>
  <v-container class="my-5">
    <h4>Expenditure History</h4>
    <HistoryRowVue v-for="(item, index) in history.slice().reverse()" :key="index" :data="item" :style="icon[item.category]" />
  </v-container>
</template>

<script>
import axios from 'axios'
import HistoryRowVue from '@/components/HistoryRowVue.vue'
import icons from '@/assets/icons.json'

export default {
  name: 'HistoryView',
  components: {
    HistoryRowVue
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
