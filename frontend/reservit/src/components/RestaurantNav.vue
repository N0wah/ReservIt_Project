<template>
    <nav class="fixed bottom-0 w-full bg-zinc-900 text-white flex justify-around items-center px-4 py-3 z-50 max-w-[512px]">
      <button @click="goTo('/dashboard')" class="flex-1 flex p-1 justify-center">
        <HomeIcon class="w-6 h-6 text-white" />
      </button>
      <div class="relative flex-1 flex justify-center">
        <button @click="goTo('/reservations')"
          class="bg-orange-400 p-4 rounded-xl rotate-45 z-10"
          style="margin-top: -50px;"
        >
          <div class="rotate-[-45deg]">
            <DocumentIcon class="w-5 h-5 text-white" />
          </div>
        </button>
      </div>
      <button @click="goTo('/settings')" class="flex-1 flex justify-center">
        <Cog6ToothIcon class="w-6 h-6 text-white" />
      </button>
    </nav>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router'
  import { HomeIcon, DocumentIcon, Cog6ToothIcon } from '@heroicons/vue/24/solid'
  
  const router = useRouter()
  const goTo = (path) => router.push(path)
  </script>
  