<template>
    <div class="flex items-center justify-between w-full h-12 bg-gray-200 rounded-xl px-4">
      <button @click="decrement" class="text-2xl font-medium text-black">-</button>
      <span class="text-lg font-medium text-black">{{ count }}</span>
      <button @click="increment" class="text-2xl font-medium text-black">+</button>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const count = ref(2)
  
  function increment() {
    count.value++
  }
  
  function decrement() {
    if (count.value > 0) count.value--
  }
  </script>
  