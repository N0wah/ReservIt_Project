<template>
    <teleport to="body">
      <div
        v-if="visible"
        class="fixed inset-0 bg-opacity-20 backdrop-blur-sm z-50 flex items-center justify-center mt-[-100px]"
      >
        <div class="bg-[#FFAD66] rounded-xl p-6 w-80 text-center shadow-xl relative z-60 justify-center flex flex-col items-center">
          <h2 class="text-2xl font-semibold text-gray-800 mb-4">{{ title }}</h2>
          <p class="text-xl text-center font-light max-w-[150px] text-black mb-6">{{ message }}</p>
  
          <div class="flex justify-center gap-4">
            <button
              @click="cancel"
              class="px-8 py-2 bg-[#A6FF94] text-black rounded-full hover:bg-gray-300 shadow-[1px_3px_3.7px_rgba(0,0,0,0.25)]
"
            >
              No
            </button>
            <button
              @click="confirm"
              class="px-8 py-2 bg-[#FF5252] text-black rounded-full hover:bg-orange-600 shadow-[1px_3px_3.7px_rgba(0,0,0,0.25)]
"
            >
              YES
            </button>
          </div>
        </div>
      </div>
    </teleport>
  </template>
  
  <script setup>
  import { defineProps, defineEmits, watch, onMounted, onBeforeUnmount  } from 'vue'
  
  const props = defineProps({
    visible: Boolean,
    title: {
      type: String,
      default: 'Confirmation'
    },
    message: {
      type: String,
      default: 'Êtes-vous sûr de vouloir continuer ?'
    }
  })
  
  const emit = defineEmits(['confirm', 'cancel'])
  
  const confirm = () => emit('confirm')
  const cancel = () => emit('cancel')

  const disableScroll = () => document.body.style.overflow = 'hidden'
    const enableScroll = () => document.body.style.overflow = ''

  watch(() => props.visible, (val) => {
  document.body.style.overflow = val ? 'hidden' : ''
    })

    onBeforeUnmount(() => {
  enableScroll()
})
  </script>
  