<template>
  <div class="flex w-full justify-center bg-black">
    <div class="max-w-[512px] w-full">
      <router-view />
      <!-- Navbar classique : affichée pour tous sauf admin et sauf sur intro -->
      <Navbar
        v-if="route.name !== '/intro' && user.value.is_admin !== true"
      />
      <!-- Navbar restaurant : affichée uniquement pour admin -->
      <RestaurantFooter v-if="user.value.is_admin === true" />
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { computed } from 'vue'
import Navbar from './components/NavComposant.vue'
import RestaurantFooter from './components/RestaurantNav.vue'

const route = useRoute()
const user = computed(() => {
  try {
    return JSON.parse(localStorage.getItem('user') || '{}')
  } catch {
    return {}
  }
})
</script>