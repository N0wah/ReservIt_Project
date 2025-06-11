<template>

      <div
        ref="scrollContainer"
        class="overflow-x-auto cursor-grab active:cursor-grabbing select-none"
        @mousedown="startDrag"
        @mousemove="onDrag"
        @mouseup="stopDrag"
        @mouseleave="stopDrag"
      >
        <div class="flex flex-nowrap space-x-2 pb-2 w-max">
          <button
            v-for="(time, index) in timeSlots"
            :key="index"
            @click="selectTime(time)"
            :class="[
              'min-w-[5.5rem] h-11 sm:min-w-[5rem] sm:h-10 bg-[#444444] text-white rounded-full shadow-[1px_3px_3.7px_rgba(0,0,0,0.25)] flex-shrink-0',
              selectedTime === time ? 'bg-[#666666]' : 'hover:bg-[#666666]'
            ]"
          >
            {{ time }}
          </button>
        </div>
      </div>
  </template>
  
  <script setup>
  import { ref, defineEmits } from 'vue'
  
  const emit = defineEmits(['update:selectedTime'])
  const selectedTime = ref(null)
  
  const timeSlots = [
    '18:00', '18:30', '19:00', '19:30', '20:00',
    '20:30', '21:00', '21:30', '22:00', '22:30',
    '23:00', '23:30', '00:00'
  ]
  
  function selectTime(time) {
    selectedTime.value = time
    emit('update:selectedTime', time)
  }
  
  // --- Scroll horizontal à la souris ---
  const scrollContainer = ref(null)
  let isDown = false
  let startX
  let scrollLeft
  
  function startDrag(e) {
    isDown = true
    startX = e.pageX - scrollContainer.value.offsetLeft
    scrollLeft = scrollContainer.value.scrollLeft
  }
  
  function onDrag(e) {
    if (!isDown) return
    e.preventDefault()
    const x = e.pageX - scrollContainer.value.offsetLeft
    const walk = x - startX
    scrollContainer.value.scrollLeft = scrollLeft - walk
  }
  
  function stopDrag() {
    isDown = false
  }
  </script>
  