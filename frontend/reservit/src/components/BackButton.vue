<template>
  <button
    @click="goBack"
    class="absolute top-4 left-2 flex items-center justify-center text-white text-sm font-medium hover:underline aspect-square bg-[#FFAD66] p-2 rounded-full z-50"
  >
    <ChevronLeftIcon class="w-6 h-6 text-white stroke-[5]" />
  </button>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ChevronLeftIcon } from '@heroicons/vue/24/outline'

const router = useRouter()

const goBack = () => {
  if (window.history.length > 1) {
    router.back()
  } else {
    router.push('/home')
  }
}
</script>

<style scoped>
.go-back {
  text-decoration: none;
  display: inline-block;
  padding: 10px 20px;
  background-color: lightgreen;
  color: black;
  transition: background-color 0.3s;
}

.go-back:hover {
  background-color: lightgray;
  color: black;
}
</style>
