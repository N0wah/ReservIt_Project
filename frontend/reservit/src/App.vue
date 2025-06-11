<template>
  <div :class="!excludePathsMargin.includes(route.path) && !hideNavbar ? 'mb-10' : ''">
    <Navbar v-if="!hideNavbar" />
    <router-view />
  </div>

  <!-- Footer utilisateur -->
  <Navbar v-if="user?.role === 'user' && !excludePaths.includes(route.path) && !hideNavbar" />

  <!-- Footer restaurateur -->
  <RestaurantFooter v-if="user?.role === 'restaurant' && !excludePaths.includes(route.path) && !hideNavbar" />
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

const excludePathsMargin = [...excludePaths]

// Hide navbar on /login, /register, and /restaurant/:id
const hideNavbar = computed(() => {
  if (['/login', '/register'].includes(route.path)) return true
  // Masque la navbar sur les pages de détail restaurant
  if (/^\/restaurant\/[0-9]+$/.test(route.path)) return true
  return false
})
</script>
