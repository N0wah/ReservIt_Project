<template>
  <div class="min-h-screen bg-[#242424] flex flex-col justify-start px-6 py-8 font-poppins">
    <!-- Logo / titre -->
    <div class="flex justify-center">
      <h2 class="font-carattere italic text-[50px] mb-2 text-center text-white">
        <span class="text-orange-400">E</span>xploration
      </h2>
    </div>

    <!-- Liste des restaurants -->
    <div class="grid grid-cols-2 gap-4 mt-6 texte-white">
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
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import RestaurantCard from '../components/RestaurantsCard.vue'

const restaurants = ref([])
const apiUrl = import.meta.env.VITE_API_URL;

onMounted(async () => {
  try {
    const response = await axios.get(`${apiUrl}/restaurants/`)
    restaurants.value = response.data
  } catch (error) {
    console.error('Failed to fetch restaurants:', error)
  }
})
</script>