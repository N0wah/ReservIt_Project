<template>
  
  <div v-if="restaurant" class="bg-[#242424] text-white w-screen max-w-none relative h-screen ">
    <BackButton/>

    <!-- Main image -->
    <div class="relative overflow-hidden ">
      
      <img
        :src="mainImage"
        :alt="restaurant.name"
        class="w-full h-54 object-cover"
        loading="lazy"
      />
      <FavoriteButton :active="isFavorite" @click="toggleFavorite" />
      
    </div>

    <!-- Infos -->
    <div class=" space-y-3 sm:space-y-4 text-xs sm:text-sm bg-[#242424] p-4 rounded-3xl mt-[-4vh] z-50 relative  ">
      <div class="flex  sm:flex-row justify-between items-center gap-2">
        <div class="space-y-1">
          <h2 class="text-lg sm:text-xl font-bold leading-tight">
            {{ restaurant.name }},<span class="text-lg">{{restaurant.cities}}</span>
          </h2>
          <p class="text-gray-400 leading-snug break-words">{{ restaurant.address }}</p>
        </div>
        <div class="flex items-center text-yellow-400 text-base sm:text-lg">
          <i class="fas fa-star rotate-45"></i> <span class="ml-1">5</span>
        </div>
      </div>

      <!-- Description -->
      <div class="min-h-21">
        <p class="text-gray-300 leading-relaxed">
          <strong>Description</strong><br />
          {{ restaurant.description }}
        </p>
      </div>

      <!-- Prix -->
      <div>
        <p class="text-gray-300 text-lg"><strong>Avg. Prices:</strong> $$$</p>
      </div>

      <!-- Galerie -->
      <div v-if="photos.length > 0">
        <p class="text-gray-300 mb-2 underline"><strong>Photos</strong></p>
        <div class="flex space-x-2 overflow-x-auto pb-2">
          <img
            v-for="(photo, index) in photos"
            :key="index"
            :src="photo"
            :alt="`Photo ${index + 1} of ${restaurant.name}`"
            class="w-28 h-28 sm:w-24 sm:h-24 object-cover rounded-lg flex-shrink-0"
            loading="lazy"
          />
        </div>
      </div>

      <!-- Reservation button -->
      <div>
        <button
          class="w-full bg-orange-500 hover:bg-orange-600 text-white py-4 rounded-full font-semibold text-lg"
          @click="goToBooking"
        >
          Reserve It now
        </button>
      </div>
    </div>
  </div>

  <!-- Fallback loading -->
  <div v-else class="text-center text-white py-20">Loading...</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import BackButton from '../components/BackButton.vue'
import FavoriteButton from '@/components/FavoriteButton.vue'

const route = useRoute()
const router = useRouter()
const restaurant = ref(null)
const mainImage = ref('')
const photos = ref([])
const isFavorite = ref(false)
const apiUrl = import.meta.env.VITE_API_URL;

onMounted(async () => {
  try {
    const response = await axios.get(`${apiUrl}/restaurants/${route.params.id}/`)
    restaurant.value = response.data

    if (restaurant.value.images) {
      const basePath = restaurant.value.images.replace(/^\/public/, '')
      mainImage.value = basePath ? `${basePath}/goldenbeef1.webp` : '/img/GoldenBeef/goldenbeef1.webp'
      photos.value = [
        mainImage.value,
        `${basePath}/goldenbeef2.webp`,
        `${basePath}/goldenbeef3.webp`
      ]
    } else {
      mainImage.value = '/img/GoldenBeef/goldenbeef1.webp'
      photos.value = [mainImage.value]
    }

    // Check if this restaurant is a favorite for the current user (par l'id favori)
    const userData = localStorage.getItem('user')
    if (userData) {
      const user = JSON.parse(userData)
      const favRes = await axios.get(`${apiUrl}/favorites/?user_id=${user.id}&restaurant_id=${route.params.id}`)
      isFavorite.value = Array.isArray(favRes.data) && favRes.data.some(fav => fav.user_id === user.id && fav.restaurant_id === Number(route.params.id))
    } else {
      isFavorite.value = false
    }
  } catch (error) {
    console.error('Erreur lors du chargement du restaurant:', error)
    isFavorite.value = false
  }
})

function toggleFavorite() {
  isFavorite.value = !isFavorite.value
  const userData = localStorage.getItem('user')
  if (!userData) return
  const user = JSON.parse(userData)
  if (isFavorite.value) {
    // Ajoute en favori
    axios.post(`${apiUrl}/favorites/`, {
      user_id: user.id,
      restaurant_id: restaurant.value.id
    }).catch(err => {
      // Si déjà favori, ignore l'erreur unique_together
      if (err.response && err.response.status !== 400) {
        console.error('Erreur lors de l\'ajout en favori:', err)
      }
    })
  } else {
    // Supprime le favori (il faut l'id du favori)
    axios.get(`${apiUrl}/favorites/?user_id=` + user.id + '&restaurant_id=' + restaurant.value.id)
      .then(res => {
        if (res.data.length > 0) {
          const favId = res.data[0].id
          axios.delete(`${apiUrl}/favorites/` + favId + '/')
        }
      })
  }
}

function goToBooking() {
  // Stocke les infos du restaurant dans le localStorage pour la page de réservation
  localStorage.setItem('selectedRestaurant', JSON.stringify({
    name: restaurant.value.name,
    address: restaurant.value.address,
    cities: restaurant.value.cities || restaurant.value.city || '',
    id: restaurant.value.id // Enregistre aussi l'id du restaurant
  }))
  router.push({ name: 'BookingPage', params: { id: restaurant.value.id } })
}
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');


img {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
}
</style>
