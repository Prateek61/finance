<template>
  <div>
    <table class="table">
      <thead>
        <tr>
          <th class="text-start">Category</th>
          <th class="text-end">Amount</th>
          <th class="text-end">Description</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="(item, index) in history" :key="index">
          <th class="text-start">{{ item.category }}</th>
          <th class="text-end">{{ item.amount }}</th>
          <th class="text-end">{{ item.description }}</th>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HistoryView',
  data () {
    return {
      history: null
    }
  },
  async created () {
    const response = await axios.get('/history')
    this.history = response.data.history
  }
}
</script>
