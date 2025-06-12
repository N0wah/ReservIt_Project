<template>
    <div class="w-full">
      <textarea
        v-model="message"
        maxlength="200"
        placeholder="Enter your message\n200 characters max"
        class="w-full h-46 bg-gray-100 rounded-xl p-3 text-black resize-none focus:outline-none focus:ring-2 focus:ring-gray-300 shadow-[1px_3px_3.7px_rgba(0,0,0,0.25)]
"
      ></textarea>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const message = ref('')
  </script>
