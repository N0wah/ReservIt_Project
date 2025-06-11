<template>
    <div
      v-if="visible"
      class="fixed inset-0 z-50 flex items-center justify-center backdrop-blur-sm bg-opacity-50"
    >
      <div class="bg-white text-center p-6 rounded-2xl shadow-xl w-11/12 max-w-sm text-black">
        <h2 class="text-xl font-semibold mb-2">It's Book !! ✅</h2>
        <p class="text-sm text-gray-600 mb-4">
          Your booking has been successfully registered. Thank you!
        </p>
        <button
          @click="$emit('close')"
          class="bg-orange-500 hover:bg-orange-600 text-white text-sm font-medium px-5 py-2 rounded-full transition"
        >
          OK
        </button>
      </div>
    </div>
  </template>
  
  <script setup>
  defineProps({
    visible: Boolean,
  })
  defineEmits(['close'])
  </script>
  