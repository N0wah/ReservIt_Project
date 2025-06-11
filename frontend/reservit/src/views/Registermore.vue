<template>
  <BackButton />
    <div class="min-h-screen bg-[#242424] flex flex-col justify-start px-6 py-12 font-poppins">
      
      <!-- Logo / titre -->
      <div class="mb-10 flex justify-center">
        <h2 class="font-carattere italic text-[50px] mb-2 text-center text-white">
          <span class="text-orange-400">R</span>eserv'<span class="text-orange-400">I</span>t
        </h2>
      </div>
  
      <!-- Titre -->
      <h2 class="text-start mb-4 text-2xl text-white">
        <span class="text-orange-400">P</span>rofile details
      </h2>
  
      <!-- Formulaire -->
      <form @submit.prevent="handleSubmit" class="space-y-6">
        <!-- Nom d'utilisateur -->
        <div>
          <input
            v-model="username"
            type="text"
            placeholder="Nom d'utilisateur"
            required
            class="w-full px-4 py-3 border border-gray-300 rounded-xl shadow-sm focus:ring-orange-500 focus:border-orange-500 bg-white"
          />
        </div>
  
        <!-- Téléphone -->
        <div>
          <input
            v-model="phone"
            type="tel"
            placeholder="Numéro de téléphone"
            required
            class="w-full z-100 px-4 py-3 border border-gray-300 rounded-xl shadow-sm focus:ring-orange-500 focus:border-orange-500 bg-white"
          />
        </div>
        
        <!-- Ajout de l'avatar de profil -->
        <div class="flex flex-col items-center">
          <label for="avatar" class="mb-2 text-white">Avatar de profil</label>
          <input
            id="avatar"
            type="file"
            accept="image/*"
            @change="onAvatarChange"
            class="block w-full text-sm text-gray-500
              file:mr-4 file:py-2 file:px-4
              file:rounded-full file:border-0
              file:text-sm file:font-semibold
              file:bg-orange-50 file:text-orange-700
              hover:file:bg-orange-100
              mb-2"
          />
          <div v-if="avatarPreview" class="mt-2">
            <img :src="avatarPreview" alt="Aperçu de l'avatar" class="w-20 h-20 rounded-full object-cover border-2 border-orange-400" />
          </div>
        </div>
        <!-- Bouton terminer -->
        <div class="flex justify-center">
          <button
            type="submit"
            class="w-1/3 flex justify-center items-center py-3 px-4 border border-transparent rounded-full shadow-sm text-sm font-light text-white bg-orange-500 hover:bg-orange-600"
          >
            Terminer
          </button>
        </div>
      </form>
    </div>
    <p class="fixed bottom-4 w-full text-center text-sm text-white z-0">
      Already have an account ?
      <router-link to="/login" class="font-medium text-orange-500 hover:text-orange-600 underline">
        Login
      </router-link>
    </p>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import BackButton from '@/components/BackButton.vue'

  const lastName = ref('')
  const firstName = ref('')
  const username = ref('')
  const phone = ref('')
  
  const handleSubmit = () => {
    console.log('Profil complété :', {
      lastName: lastName.value,
      firstName: firstName.value,
      username: username.value,
      phone: phone.value,
    })
  
    // Ici tu peux faire un appel API ou router.push('/home') par exemple
  }
  </script>
  