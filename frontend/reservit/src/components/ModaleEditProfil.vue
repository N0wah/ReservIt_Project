<template>
    <div
      v-if="isOpen"
      class="fixed inset-0 z-50 flex items-center justify-center bg-opacity-50 backdrop-blur-sm"
    >
      <div class=" bg-white rounded-xl p-6 w-11/12 max-w-md text-black">
        <h2 class="text-xl font-semibold mb-4">Modifier le profil</h2>
  
        <form @submit.prevent="submit">
          <div class="mb-3">
            <input placeholder="LastName" v-model="form.lastName" class="w-full p-2 rounded-md bg-gray-100 focus:ring-2 focus:ring-orange-500 focus:outline-none shadow-md" required />
          </div>
  
          <div class="mb-3">
            
            <input  placeholder="FirstName" v-model="form.firstName" class="w-full p-2 rounded-md bg-gray-100 focus:ring-2 focus:ring-orange-500 focus:outline-none shadow-md" required />
          </div>
  
          <div class="mb-4">
            <input
            placeholder="Phone"
              v-model="form.phone"
              class="w-full p-2 rounded-md bg-gray-100 focus:ring-2 focus:ring-orange-500 focus:outline-none shadow-md"
              type="tel"
              required
            />
          </div>
  
          <div class="flex justify-end gap-2">
            <button
              type="button"
              @click="close"
              class="px-4 py-2 text-sm text-gray-700 bg-gray-200 rounded-full"
            >
              Cancel
            </button>
            <button
              type="submit"
              class="px-4 py-2 text-sm text-white bg-orange-500 hover:bg-orange-600 rounded-full"
            >
              Save
            </button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, defineEmits, defineProps } from 'vue'
  
  const emit = defineEmits(['close', 'save'])
  
  const props = defineProps({
    isOpen: Boolean,
  })
  
  const form = ref({
    lastName: '',
    firstName: '',
    phone: '',
  })
  
  function close() {
    emit('close')
  }
  
  function submit() {
    emit('save', form.value)
    close()
  }
  </script>
  