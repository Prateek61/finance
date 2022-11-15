<template>
    <Bar
      :chart-data="chartData"
      :width=50
      :height=25
    />
</template>

<script>
import axios from 'axios'
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: { Bar },
  data () {
    return {
      chartData: {
        labels: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
        datasets: [{ label: 'Expenditure', data: [] }]
      },
      chartOptions: {
        responsive: true
      }
    }
  },
  async created () {
    const response = await axios.get('/bargraph')
    const list = []
    const data = response.data.chartData
    console.log(data)

    this.chartData.labels.forEach((item, index) => {
      list.push(data[item])
    })
    console.log(list)
    this.chartData.datasets[0].data = list
  }
}
</script>
