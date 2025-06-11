<template>
    <button
      @click="toggleFavorite"
      class="absolute top-4 right-2 p-1 rounded-full bg-white/80 hover:bg-white shadow-md z-20"
    >
      <component
        :is="isFavorite ? HeartSolidIcon : HeartIcon"
        class="w-8 h-8 text-red-500 transition-transform duration-200"
      />
    </button>
  </template>
  
  <script setup>
  import { computed } from 'vue'
  import { HeartIcon } from '@heroicons/vue/24/outline'
  import { HeartIcon as HeartSolidIcon } from '@heroicons/vue/24/solid'
  
  const props = defineProps({
    active: {
      type: Boolean,
      default: false,
    }
  })
  
  const emit = defineEmits(['click'])
  
  // Utilise directement la prop active, sans état local
  const isFavorite = computed(() => props.active)
  
  const toggleFavorite = () => {
    emit('click')
  }
  </script>
