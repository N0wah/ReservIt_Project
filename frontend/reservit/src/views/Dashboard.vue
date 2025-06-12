<template>
    <RestaurantNav />
    <div class="bg-[#242424] min-h-screen text-white px-6 pt-6 pb-24">
        <div class="flex justify-center items-center gap-2">
      <div class="flex justify-center">
        <h2 class="font-carattere italic text-[50px] mb-2 text-center text-white">
          <span class="text-orange-400">D</span>ashboard
        </h2>
        
        </div>
        <p><span class="text-orange-400">A</span>dmin</p>
        </div>
        <section class="mb-3">
    <h1 class="font-Poppins text-lg">Weekly Reservation</h1>
    <RestaurantGraphic />
        </section>
        <section>
    <h1 class="font-Poppins text-lg">Latest Customers Reservation</h1>
    <ul>
        <!-- Conditional display to avoid rendering errors -->
        <li v-if="Array.isArray(reservations) && reservations.length" class="list-none flex flex-col gap-2 z-0">
            <RestaurantBookitems v-for="reservation in reservations" :key="reservation.id" :reservation="reservation" />
        </li>
        <li v-else class="text-gray-400">No recent reservations.</li>
    </ul>
    </section>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import RestaurantNav from '@/components/RestaurantNav.vue';
import RestaurantGraphic from '@/components/RestaurantGraphic.vue';
import RestaurantBookitems from '@/components/RestaurantBookitems.vue';
import axios from 'axios'

const reservations = ref([])
const apiUrl = import.meta.env.VITE_API_URL;

onMounted(async () => {
  try {
    const res = await axios.get(`${apiUrl}/reservations/`)
    let reservationsRaw = res.data.slice(-4).reverse() // Les 4 dernières

    // Récupère les restaurants nécessaires en une seule fois
    const restaurantIds = [...new Set(reservationsRaw.map(r => r.restaurant || r.restaurant_id))]
    const restaurantMap = {}
    for (const id of restaurantIds) {
      try {
        const restRes = await axios.get(`${apiUrl}/restaurants/${id}/`)
        restaurantMap[id] = restRes.data
      } catch { restaurantMap[id] = { name: 'Restaurant inconnu' } }
    }

    // Enrichit chaque réservation avec le restaurant et l'utilisateur
    for (const reservation of reservationsRaw) {
      reservation.restaurant = restaurantMap[reservation.restaurant] || restaurantMap[reservation.restaurant_id] || null
      try {
        const userRes = await axios.get(`${apiUrl}/users/${reservation.user_id}/`)
        reservation.user = userRes.data
      } catch { reservation.user = {} }
    }
    reservations.value = reservationsRaw
  } catch (e) {
    reservations.value = []
  }
})
</script>