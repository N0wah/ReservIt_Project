<template>
    <div class="bg-gray-800 rounded-xl overflow-hidden shadow-md text-xs sm:text-sm">
      <img :src="image" alt="Restaurant" class="w-full h-24 object-cover" />
      <div class="p-2">
        <h4 class="font-bold text-white text-sm">{{ name }}</h4>
        <p class="text-gray-400">{{ address }}</p>
        <div class="flex justify-between mt-2">
          <span class="text-white">{{ rating }}</span>
          <span class="text-white">{{ price }}</span>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  defineProps({
    name: String,
    address: String,
    rating: String,
    price: String,
    image: String
  })
  </script>
  