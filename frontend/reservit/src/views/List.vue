<template>
    <div class="h-screen bg-[#242424] flex flex-col justify-start px-6 py-8 font-poppins">
      
      <!-- Logo / titre -->
      <div class="flex justify-center">
        <h2 class="font-carattere italic text-[50px] mb-2 text-center text-white">
          <span class="text-orange-400">R</span>eservation
        </h2>
      </div>

      <div v-if="!isAuthenticated" class="text-white text-center w-full h-full mt-[-15vh] flex flex-col items-center justify-center gap-4">
        Please log in to view your reservations.
        <router-link
          to="/login"
          class="bg-orange-500 hover:bg-orange-600 text-white font-semibold py-2 px-6 rounded-full transition duration-200"
        >
          Log in
        </router-link>
      </div>

      <ul v-else class="list-none flex flex-col gap-2 z-0">
        <li>
            <Bookitems :lat="48.8584" :lng="2.2945"  />
        </li>
        <li>
            <Bookitems :lat="48.8584" :lng="2.2945"  />
        </li>
        <li>
            <Bookitems :lat="48.8584" :lng="2.2945"  />
        </li>
        <li>
            <Bookitems :lat="48.8584" :lng="2.2945"  />
        </li>
        <li>
            <Bookitems :lat="48.8584" :lng="2.2945"  />
        </li>
      </ul>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Bookitems from '../components/Bookitems.vue'

const isAuthenticated = ref(false)

onMounted(() => {
  const userData = localStorage.getItem('user')
  isAuthenticated.value = !!userData
})
</script>