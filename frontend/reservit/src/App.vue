<template>
  <div class="flex w-full justify-center bg-black">
    <div class="max-w-[512px] w-full">
      <router-view />
      <!-- Navbar pour tous sauf admin -->
      <Navbar
        v-if="!user?.is_admin"
      />
      <!-- Footer restaurateur : affiché uniquement si l'utilisateur est admin -->
      <RestaurantFooter v-if="user?.is_admin === true" />
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import Navbar from './components/NavComposant.vue'
import RestaurantFooter from './components/RestaurantNav.vue'

const route = useRoute()
const user = JSON.parse(localStorage.getItem('user') || '{}')
</script>