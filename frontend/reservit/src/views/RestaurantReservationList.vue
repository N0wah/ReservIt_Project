<template>
     <div class="bg-[#242424] min-h-screen text-white px-4 pt-6 pb-24">
      
      <!-- Logo / titre -->
       <div class="flex justify-center items-center gap-2">
      <div class="flex justify-center">
        <h2 class="font-carattere italic text-[50px] mb-2 text-center text-white">
          <span class="text-orange-400">R</span>eservation
        </h2>
        
        </div>
        <p><span class="text-orange-400">A</span>dmin</p>
        </div>
        <ul class="list-none flex flex-col gap-2 z-0">
      <li v-for="reservation in reservations" :key="reservation.id">
        <Bookitems :reservation="reservation" />
      </li>
    </ul>



    </div>
    <RestaurantNav />
</template>
<script setup>
import { ref, onMounted } from 'vue'
import Bookitems from '@/components/RestaurantBookitems.vue';
import RestaurantNav from '@/components/RestaurantNav.vue';
import axios from 'axios'

const reservations = ref([])
const apiUrl = import.meta.env.VITE_API_URL;

onMounted(async () => {
  const userData = localStorage.getItem('user')
  if (!userData) return
  const user = JSON.parse(userData)
  // Récupère les restaurants de l'admin
  const restRes = await axios.get(`${apiUrl}/restaurants/?owner_id=${user.id}`)
  const adminRestaurants = restRes.data
  if (!Array.isArray(adminRestaurants) || adminRestaurants.length === 0) return
  const restaurantIds = adminRestaurants.map(r => r.id)
  // Récupère toutes les réservations pour ces restaurants
  const resRes = await axios.get(`${apiUrl}/reservations/`)
  reservations.value = resRes.data.filter(r => restaurantIds.includes(r.restaurant))
})
</script>