<template>
    <!-- Premier bloc : au-dessus -->
    <div @click="toggleDetails" class="relative w-full bg-[#242424] rounded-2xl flex p-3 shadow-[0_3px_10.2px_rgba(0,0,0,0.25)] gap-4 items-center justify-between text-white font-Poppins z-10">
        <div class="flex gap-2">
      <div class="bg-white w-12 h-12 rounded-2xl flex items-center justify-center overflow-hidden">
        <img v-if="reservation.restaurant && reservation.restaurant.images" :src="reservation.restaurant.images + '/goldenbeef1.webp'" alt="" class="object-cover w-12 h-12" />
      </div>
      <div class="max-w-[250px]">
        <h1 class="text-sm sm:text-base md:text-lg ">
          {{ reservation.restaurant?.name || 'Restaurant' }}, {{ reservation.restaurant?.address || '' }}
        </h1>
        <p class="text-[#BCBCBC] font-light text-base">
          {{ reservation.guest_count }} persons
        </p>
      </div>
        </div>
      <p class="font-thin text-end">
      {{ reservation.reservation_date }} {{ reservation.reservation_time }}
      </p>
    </div>
    
    <!---BLoc de dessous-->
    <div v-show="showDetails" class="relative w-full bg-[#242424] mt-[-12px] z-0 rounded-b-lg p-3 text-white shadow-[0_3px_10.2px_rgba(0,0,0,0.25)]">
      <h1 class="font-light mt-1 font-Poppins ">
        Information :
      </h1>
      <p class="mt-1 text-xs font-s max-w-70">
      {{ reservation.information || 'No description.' }}
      </p>
      <div class="flex justify-center">
    
    <button
        @click.stop="openMap"
        class="flex items-center gap-2 bg=[#242424] text-white font-medium px-3 py-2 rounded-full shadow-md"
      >
        <MapPinIcon class="w-6 h-6" />
      </button>
      </div>
    </div>
    
    </template>
    <script setup>
    import { MapPinIcon } from '@heroicons/vue/24/solid'
    import { ref, computed } from 'vue'
    
    const props = defineProps({
      reservation: {
        type: Object,
        required: true
      }
    })
    
    const showDetails = ref(false)
    const toggleDetails = () => {
      showDetails.value = !showDetails.value
    }
    
    const openMap = () => {
      if (props.reservation.restaurant && props.reservation.restaurant.address) {
        const address = encodeURIComponent(props.reservation.restaurant.address)
        const url = `https://www.google.com/maps?q=${address}`
        window.open(url, '_blank')
      }
    }
    </script>