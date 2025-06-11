<template>
  <div>
    <router-view />
  </div>

  <!-- Affiche la Navbar pour toutes les routes sauf celles exclues, si l'user n'est pas restaurant, si on n'est pas sur BookingPage et pas sur une page de détail restaurant -->
  <Navbar
    v-if="
      !excludePaths.includes(route.path) &&
      user?.role !== 'restaurant' &&
      route.name !== 'BookingPage' &&
      !/^\/restaurant\/[0-9]+$/.test(route.path)
    "
  />

  <!-- Footer restaurateur -->
  <RestaurantFooter v-if="showFooter && user?.role === 'restaurant'" />
</template>

<script setup>
import { useRoute } from 'vue-router'
import { computed } from 'vue'
import Navbar from './components/NavComposant.vue'
import RestaurantFooter from './components/RestaurantNav.vue'

const route = useRoute()
const user = JSON.parse(localStorage.getItem('user') || '{}')

// Routes à exclure (connexion, intro, etc.)
const excludePaths = [
  '/intro', '/', '/login', '/register',
  '/registerdetails', '/loginrestaurant',
  '/registerrestaurant',
  '/restaurantdetail',
  ''
]

// Masque le footer restaurateur sur les pages exclues et détail restaurant
const showFooter = computed(() => {
  if (excludePaths.includes(route.path)) return false
  if (/^\/restaurant\/[0-9]+$/.test(route.path)) return false
  return true
})
</script>
