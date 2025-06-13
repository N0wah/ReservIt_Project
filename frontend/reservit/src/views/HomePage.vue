<template>
    <div class="bg-[#242424] min-h-screen text-white px-4 pt-6 pb-24">
      
      <!-- Logo / titre -->
      <div class="flex justify-center">
        <h2 class="font-carattere italic text-[50px] mb-2 text-center text-white">
          <span class="text-orange-400">H</span>ome
        </h2>
      </div>
      <p class="font-Poppins text-lg mb-4 text-left sm:text-left">
        Hey <span class="font-bold">{{ userName }}</span>!
      </p>
  
      <!-- Nav -->

  
      <!-- Hot Right Now -->
      <h3 class="text-lg mb-2">Hot Right Now</h3>
      <div class="grid grid-cols-2 gap-4">
        <router-link
          v-for="restaurant in restaurants"
          :key="restaurant.id"
          :to="`/restaurant/${restaurant.id}`"
          class="block"
        >
          <RestaurantCard
            :name="restaurant.name"
            :address="restaurant.address"
            :rating="restaurant.rating ? restaurant.rating : 'N/A'"
            :price="restaurant.price ? restaurant.price : '$$'"
            :image="restaurant.images"
          />
        </router-link>
      </div>
  
      <!-- Top Cannes -->
      <h3 class="text-lg mt-8 mb-2">Top Cannes</h3>
      <!--<img src="@/assets/images/restaurant2.jpg" alt="Top restaurant" class="w-full h-40 object-cover rounded-xl" />-->
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
import axios from 'axios'
import RestaurantCard from '../components/RestaurantsCard.vue'

const restaurants = ref([])
const userName = ref('')
const apiUrl = import.meta.env.VITE_API_URL;

onMounted(async () => {
  try {
    const response = await axios.get(`${apiUrl}/restaurants/`)
    restaurants.value = response.data
  } catch (error) {
    console.error('Failed to fetch restaurants:', error)
  }
  // Set userName from localStorage
  const userData = localStorage.getItem('user')
  if (userData) {
    const user = JSON.parse(userData)
    userName.value = user.name || ''
  }
})
  </script>
