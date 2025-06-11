<template>
    <div class="min-h-screen bg-[#242424] flex flex-col justify-start px-6 py-8 font-poppins">
      
      <!-- Logo / titre -->
      <div class="flex justify-center">
        <h2 class="font-carattere italic text-[50px] mb-2 text-center text-white">
          <span class="text-orange-400">P</span>rofile
        </h2>
        
      </div>

      <div class="flex flex-col w-full items-center text-white">
        <div class="w-32 h-32 bg-white rounded-full">
        </div>
        <p>{{ user?.name || 'Nom' }}</p>
      </div>
      <h1 class="font-Poppins text-white ml-6 mt-4 font-light">Reservation</h1>
      <div class="flex flex-col w-full items-center text-white">
        <div class="h-28 w-full bg-[#242424] rounded-3xl flex justify-around items-center p-5 shadow-[0_2px_10.2px_rgba(0,0,0,0.25)]">
            <CalendarIcon class="w-12 h-12 text-white"/>
            <div class="w-[1px] h-14 bg-[#242424] shadow-[1px_3px_3.7px_rgba(0,0,0,0.25)]"></div>
            <div class="w-12 h-12 flex items-center justify-center">
      <p class="text-[#B7B7B7] text-3xl font-bold">6</p>
    </div>
        </div>
      </div>
      <h1 class="font-Poppins text-white ml-6 mt-4 font-light">General Information</h1>
      <div class="flex flex-col w-full items-center text-white">
        <div class=" w-full bg-[#242424] rounded-3xl flex flex-col justify-around items-center p-5 shadow-[0_2px_10.2px_rgba(0,0,0,0.25)]">
            <div class="flex justify-between w-full gap- items-center border-b border-[#474747]">
                <p class="font-Poppins text-[#B2B2B2]">email</p>
                <p class="text-sm text-white">{{ user?.email }}</p>
            </div>
            <div class="flex justify-between w-full gap- items-center border-b border-[#474747] pt-6">
                <p class="font-Poppins text-[#B2B2B2]">phone</p>
                <p class="text-sm text-white">{{ user?.phone || 'Non renseigné' }}</p>
            </div>
            <div class="flex justify-between w-full gap- items-center border-b border-[#474747] pt-6">
                <p class="font-Poppins text-[#B2B2B2]">country</p>
                <p class="text-sm text-white">{{ user?.country || 'Non renseigné' }}</p>
            </div>
        </div>
      </div>
      <h1 class="font-Poppins text-white ml-6 mt-4 font-light">Reservation History</h1>
      <ul class="liste-none flex flex-col gap-2">
        <li v-for="reservation in filteredReservations" :key="reservation.id">
          <BookitemsBooked :reservation="reservation" />
        </li>
      </ul>
      <button
        class="bg-red-500 hover:bg-red-600 text-white font-medium py-2 px-4 rounded-full shadow-md transition duration-200 my-10"
        @click="handleLogout"
      >
        Disconnect
      </button>
    </div>
    

</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { CalendarIcon } from '@heroicons/vue/24/solid'
import BookitemsBooked from '@/components/BookitemsBooked.vue'
import axios from 'axios'

const router = useRouter()
const user = ref(null)
const reservations = ref([])
const apiUrl = import.meta.env.VITE_API_URL;

onMounted(async () => {
  const token = localStorage.getItem('token')
  const userData = localStorage.getItem('user')
  if (!token || !userData) {
    router.push('/login')
  } else {
    user.value = JSON.parse(userData)
    try {
      const res = await axios.get(`${apiUrl}/reservations/?user_id=${user.value.id}`)
      const reservationsWithRestaurant = await Promise.all(res.data.map(async reservation => {
        try {
          const restRes = await axios.get(`${apiUrl}/restaurants/${reservation.restaurant}/`)
          return { ...reservation, restaurant: restRes.data }
        } catch {
          return { ...reservation, restaurant: {} }
        }
      }))
      reservations.value = reservationsWithRestaurant
    } catch (error) {
      reservations.value = []
    }
  }
})

const filteredReservations = computed(() =>
  reservations.value.filter(r => r && r.status && r.status.toLowerCase() === 'fini')
)

function handleLogout() {
  localStorage.removeItem('token')
  localStorage.removeItem('user')
  router.push('/home')
}
</script>