<template>
    <div class="h-screen bg-[#242424] flex flex-col justify-start px-6 py-8 font-poppins">
      
      <!-- Logo / titre -->
      <div class="flex justify-center">
        <h2 class="font-carattere italic text-[50px] mb-2 text-center text-white">
          <span class="text-orange-400">R</span>eservation
        </h2>
      </div>

      <ul v-if="isAuthenticated" class="list-none flex flex-col gap-2 z-0">
        <li v-for="reservation in reservations" :key="reservation.id">
          <Bookitems :reservation="reservation" />    
        </li>
      </ul>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Bookitems from '../components/Bookitems.vue'
import axios from 'axios'

const isAuthenticated = ref(false)
const reservations = ref([])
const apiUrl = import.meta.env.VITE_API_URL;

onMounted(async () => {
  const userData = localStorage.getItem('user')
  if (!userData) {
    isAuthenticated.value = false
    return
  }
  isAuthenticated.value = true
  const user = JSON.parse(userData)
  try {
    const res = await axios.get(`${apiUrl}/reservations/?user_id=${user.id}`)
    // Filtrer les réservations qui ne sont pas "Finished"
    reservations.value = res.data.filter(r => r.status && r.status.toLowerCase() !== 'fini' && r.status.toLowerCase() !== 'finished')
  } catch (error) {
    reservations.value = []
  }
})
</script>