<template>
  <div class="flex w-full justify-center bg-black">
    <div class="max-w-[512px] w-full">
      <router-view />
      <!-- Navbar classique : affichée pour tous sauf admin et sauf sur intro -->
      <Navbar
        v-if="route.name !== 'Intro' && !(user.value && user.value.is_admin === true)"
      />
      <!-- Navbar restaurant : affichée uniquement pour admin -->
      <RestaurantFooter v-if="user.value && user.value.is_admin === true" />
    </div>
  </div>
</template>

<script setup>
import { useRoute, onBeforeRouteUpdate } from 'vue-router'
import { computed, ref, watch } from 'vue'
import Navbar from './components/NavComposant.vue'
import RestaurantFooter from './components/RestaurantNav.vue'

const route = useRoute()
const user = ref(getUser())

function getUser() {
  try {
    return JSON.parse(localStorage.getItem('user') || '{}')
  } catch {
    return {}
  }
}

// Met à jour user à chaque navigation
watch(route, () => {
  user.value = getUser()
})
</script>