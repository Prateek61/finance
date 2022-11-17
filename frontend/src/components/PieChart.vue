<template>
  <Pie
    v-if="loaded"
    :chart-data="chartData"
    :chart-options="chartOptions"
  />
</template>

<script>
import axios from 'axios'
import icons from '@/assets/icons.json'
import { Pie } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement, CategoryScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale)

export default {
  name: 'PieChart',

  components: {
    Pie
  },

  data () {
    return {
      loaded: false,
      total: null,
      chartData: null,

      chartOptions: {
        responsive: true,

        plugins: {
          title: {
            display: true,
            text: 'Expenditure in each category'
          }
        }
      }
    }
  },

  async mounted () {
    const response = await axios.get('/piechart')
    const dataList = []
    const colorList = []
    const labelList = []
    const data = response.data.chartData

    for (const [key, value] of Object.entries(data)) {
      dataList.push(value)
      labelList.push(key)
      colorList.push(icons[key].color)
    }

    this.chartData = {
      labels: labelList,
      datasets: [
        {
          data: dataList,
          backgroundColor: colorList
        }
      ]
    }
    this.total = response.data.total
    this.chartOptions.plugins.title.text += `   [Total: ${this.total}]`
    this.loaded = true
  }
}
</script>
