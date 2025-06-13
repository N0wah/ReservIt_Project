<template>
  <div class="h-screen bg-[#242424] flex flex-col justify-start px-6 py-8 font-poppins">
    <!-- Logo / titre -->
    <div class="flex justify-center">
      <h2 class="font-carattere italic text-[50px] mb-2 text-center text-white">
        <span class="text-orange-400">R</span>eservation
      </h2>
    </div>

    <div v-if="!isAuthenticated" class="text-white text-center w-full h-screen mt-[-15vh] flex flex-col items-center justify-center gap-4">
      Please log in to view your reservations.
      <router-link
        to="/login"
        class="bg-orange-500 hover:bg-orange-600 text-white font-semibold py-2 px-6 rounded-full transition duration-200"
      >
        Log in
      </router-link>
    </div>
    <div v-else>
      <div v-if="filteredReservations.length === 0" class="text-white text-center my-8">
        You have not made any reservations.
      </div>
      <ul v-else class="list-none flex flex-col gap-2 z-0">
        <li v-for="reservation in filteredReservations" :key="reservation.id">
          <BookitemsBooked :reservation="reservation" />
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { computed, ref, onMounted } from 'vue'
import axios from 'axios'
import BookitemsBooked from '@/components/BookitemsBooked.vue'

const reservations = ref([])
const isAuthenticated = computed(() => {
  const user = localStorage.getItem('user')
  return !!user
})

onMounted(async () => {
  const userData = localStorage.getItem('user')
  if (userData) {
    const user = JSON.parse(userData)
    try {
      const apiUrl = import.meta.env.VITE_API_URL
      // Fetch all reservations for the user using the new backend route
      const res = await axios.get(`${apiUrl}/reservations/user_id/${user.id}/`)
      // Optionally, fetch restaurant details for each reservation
      const reservationsWithRestaurant = await Promise.all(res.data.map(async reservation => {
        try {
          const restRes = await axios.get(`${apiUrl}/restaurants/${reservation.restaurant}/`)
          return { ...reservation, restaurant: restRes.data }
        } catch {
          return { ...reservation, restaurant: {} }
        }
      }))
      reservations.value = reservationsWithRestaurant
    } catch (e) {
      reservations.value = []
    }
  }
})

const filteredReservations = computed(() => {
  return reservations.value.filter(r =>
    r.status === 'Pending' || r.status === 'Booked'
  )
})
</script>
