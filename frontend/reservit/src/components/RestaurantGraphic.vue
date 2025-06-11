<template>
    <div class="bg-black rounded-xl w-full">
    <div class="bg-white rounded-xl p-2 shadow-[1px_3px_3.7px_rgba(0,0,0,0.25)] w-full ">
        <Line :data="chartData" :options="chartOptions" />
    </div>
  </div>
</template>

<script setup>
import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Tooltip,
  Legend
} from 'chart.js'
import { Line } from 'vue-chartjs'

// Enregistre les composants nécessaires
ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement, Tooltip, Legend)

// Données du graphique (vide ici, tu peux remplir)
const chartData = {
  labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
  datasets: [
    {
      label: 'Réservations',
      data: [12, 30, 25,10,20,30,50], // ← ajoute des valeurs ici
      borderColor: '#FFAD66',
      backgroundColor: '#FFAD66',
      tension: 0.4,
    }
  ]
}

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: {
      min: 0,
      max: 60,
      ticks: {
        stepSize: 10,
        color: '#333'
      },
      grid: {
        drawTicks: false,
        color: '#e5e5e5'
      }
    },
    x: {
      ticks: {
        color: '#333'
      },
      grid: {
        display: false
      }
    }
  },
  plugins: {
    legend: { display: false },
    tooltip: { enabled: true }
  }
}
</script>

<style scoped>
/* Pour forcer la hauteur comme sur ton image */
div {
  height: 200px;
}
</style>
