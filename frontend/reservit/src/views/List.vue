<template>
  <div class="h-screen bg-[#242424] flex flex-col justify-start px-6 py-8 font-poppins">
    <!-- Logo / titre -->
    <div class="flex justify-center">
      <h2 class="font-carattere italic text-[50px] mb-2 text-center text-white">
        <span class="text-orange-400">R</span>eservation
      </h2>
    </div>

    <ul v-if="isAuthenticated" class="list-none flex flex-col gap-2 z-0">
      <li v-for="reservation in reservations" :key="reservation.id" class="bg-white rounded-lg p-4 flex gap-4 items-center">
        <img
          v-if="reservation.restaurant && reservation.restaurant.images"
          :src="reservation.restaurant.images + '/goldenbeef1.webp'"
          alt="Image restaurant"
          class="w-24 h-24 object-cover rounded"
        />
        <div>
          <h3 class="text-xl font-bold">{{ reservation.restaurant?.name || 'Inconnu' }}</h3>
          <p class="text-gray-600">{{ reservation.restaurant?.address || '' }}</p>
          <p class="text-yellow-500">Note : {{ reservation.restaurant?.rating || 'N/A' }}</p>
          <p class="text-green-600">Prix : {{ reservation.restaurant?.price || 'N/A' }}</p>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
// Pas besoin de defineProps ici, car tu utilises les données de reservation
</script>
