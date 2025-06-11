<template>
    <div class="min-h-screen bg-[#242424] flex flex-col justify-start px-6 py-8  font-poppins">
      
      <!-- Logo / titre -->
      <div class="flex justify-center">
        <h2 class="font-carattere italic text-[50px] mb-2 text-center text-white">
          <span class="text-orange-400">F</span>avorite
        </h2>
      </div>
      <div class="grid grid-cols-2 gap-4 text-white">
        <router-link
          v-for="restaurant in favoriteRestaurants"
          :key="restaurant.id"
          :to="`/restaurant/${restaurant.id}`"
          class="block"
        >
          <RestaurantCard
            :name="restaurant.name"
            :address="restaurant.address"
            :rating="restaurant.rating ? restaurant.rating : 'N/A'"
            :price="restaurant.price ? restaurant.price : '$$'"
            :image="restaurant.images + '/goldenbeef1.webp'"
          />
        </router-link>
        <div v-if="favoriteRestaurants.length === 0" class="text-white text-center w-full mt-8">
          Aucun restaurant favori pour le moment.
        </div>
      </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import RestaurantCard from '../components/RestaurantsCard.vue'

const favoriteRestaurants = ref([])

onMounted(async () => {
  const userData = localStorage.getItem('user')
  if (!userData) return

  const user = JSON.parse(userData)
  try {
    // Récupère tous les favoris de cet utilisateur
    const favRes = await axios.get(`http://127.0.0.1:8000/api/favorites/?user_id=${user.id}`)
    const favoriteList = favRes.data
    if (!Array.isArray(favoriteList) || favoriteList.length === 0) {
      favoriteRestaurants.value = []
      return
    }
    // Pour chaque favori, récupère le restaurant associé
    const requests = favoriteList.map(fav =>
      axios.get(`http://127.0.0.1:8000/api/restaurants/${fav.restaurant_id}/`).then(res => res.data)
    )
    favoriteRestaurants.value = await Promise.all(requests)
  } catch (error) {
    favoriteRestaurants.value = []
    console.error('Erreur lors du chargement des favoris :', error)
  }
})
</script>