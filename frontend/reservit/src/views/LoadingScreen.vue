<template>
   <div class="min-h-screen bg-[#242424] flex flex-col justify-center items-center gap-34  px-6 py-12">

<div class="mb-10 flex justify-center itemstar">
  <h2 class="font-carattere italic text-[70px] mb-2 text-center sm:text-left text-white">
  <span class="text-orange-400">R</span>eserv'<span class="text-orange-400">I</span>t
</h2>
</div>
<div class="w-16 h-16 border-4 border-t-transparent border-orange-500 rounded-full animate-spin"></div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
onMounted(() => {
  setTimeout(() => {
    router.push('/intro') // ou '/home' selon ton choix
  }, 2000) // 2 secondes d'attente
})
</script>









