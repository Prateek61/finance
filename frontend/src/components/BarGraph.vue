<template>
    <Bar
    v-if="loaded"
      :chart-options="chartOptions"
      :chart-data="chartData"
    />
</template>

<script>
import axios from 'axios'
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',

  components: {
    Bar
  },

  data () {
    return {
      loaded: false,

      chartData: {
        labels: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],

        datasets: [
          {
            label: 'Expenditure',
            data: [],

            backgroundColor: [
              '#F44336',
              '#E91E63',
              '#9C27B0',
              '#3F51B5',
              '#00BCD4',
              '#8BC34A',
              '#FFC107'
            ]
          }
        ]
      },

      chartOptions: {
        responsive: true,

        plugins: {
          title: {
            display: true,
            text: 'Expenditure in every day of week'
          },

          legend: {
            display: false
          }
        }
      }
    }
  },

  async mounted () {
    const response = await axios.get('/bargraph')
    const list = []
    const data = response.data.chartData

    this.chartData.labels.forEach((item, index) => {
      list.push(data[item])
    })
    this.chartData.datasets[0].data = list
    this.loaded = true
  }
}
</script>
