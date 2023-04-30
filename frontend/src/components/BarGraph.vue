<template>
    <Bar
      v-if="loaded"
      :chart-options="chartOptions"
      :chart-data="chartData"
    />
</template>

<script>
import axios from 'axios'
import materialColors from '@/assets/material-colors.json'
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

      monthName: null,
      total: null,

      chartData: null,

      chartOptions: {
        responsive: true,

        plugins: {
          title: {
            display: true,
            text: ''
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
    const data = response.data
    const label = []
    const colorList = []

    for (let i = 1; i <= data.chartData.length; i++) {
      label.push((i - 1).toString())
      colorList.push(pickRandomColor())
    }

    this.monthName = data.monthName
    this.total = data.total
    this.chartData = {
      labels: label,
      datasets: [
        {
          data: data.chartData,
          backgroundColor: colorList
        }
      ]
    }
    this.chartOptions.plugins.title.text = `Expenditure in ${this.monthName}: ${this.total}`
    this.loaded = true
  }
}

function pickRandomColor () {
  return pickRandomProperty(pickRandomProperty(materialColors))
}

function pickRandomProperty (obj) {
  const keys = Object.keys(obj)
  const randKey = keys[keys.length * Math.random() << 0]
  if (['50', '100', '200', '300', 'grey', 'bluegrey'].includes(randKey)) {
    return pickRandomProperty(obj)
  } else {
    return obj[randKey]
  }
}

</script>
