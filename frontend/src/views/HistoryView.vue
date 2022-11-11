<template>
  <v-content>
    <v-container class="my-5">
      <h4>History</h4>
      <HistoryRowVue v-for="(item, index) in history" :key="index" :data="item" :style="icon[item.category]"/>
    </v-container>
  </v-content>
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
