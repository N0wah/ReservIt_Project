<template>
    <nav class="fixed bottom-0 w-full bg-zinc-900 text-white flex justify-between items-center px-4 py-3 z-50 max-w-[512px]">
      <button @click="goTo('/home')" class="flex-1 flex justify-center">
      <div :class="isActive('/home') ? activeClass : ''" class="p-2 rounded-full">
        <HomeIcon class="w-6 h-6 text-white" />
      </div>
    </button>
      <button @click="goTo('/search')" class="flex-1 flex justify-center">
        <div :class="isActive('/search') ? activeClass : ''" class="p-2 rounded-full">
  <MagnifyingGlassIcon class="w-6 h-6 text-white" />
</div>
</button>

      <div class="relative flex-1 flex justify-center">
        <button @click="goTo('/list')"
          class="bg-orange-400 p-4 rounded-xl rotate-45 z-10"
          style="margin-top: -50px;"
        >
          <div class="rotate-[-45deg]">
            <DocumentIcon class="w-5 h-5 text-white" />
          </div>
        </button>
      </div>
      
      <button @click="goTo('/favorites')" class="flex-1 flex justify-center">
        <div :class="isActive('/favorites') ? activeClass : ''" class="p-2 rounded-full">
        <HeartIcon class="w-6 h-6 text-white" />   
       </div>
      </button>

      <button @click="goTo('/profile')" class="flex-1 flex justify-center">
        <div :class="isActive('/profile') ? activeClass : ''" class="p-2 rounded-full">
        <UserIcon class="w-6 h-6 text-white" />
      </div>
      </button>
    </nav>
  </template>
  

<script setup>
import { useRoute, useRouter } from 'vue-router'
import { 
  HomeIcon, 
  MagnifyingGlassIcon, 
  DocumentIcon, 
  HeartIcon, 
  UserIcon 
} from '@heroicons/vue/24/solid'
const route = useRoute()
const router = useRouter()

const isActive = (path) => route.path === path

const activeClass = 'bg-[#FFAD66] text-black'


const goTo = (path) => {
  router.push(path)
}

</script>
