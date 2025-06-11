<template>
  <BackButton />
    <div class="min-h-screen bg-[#242424] flex flex-col justify-start px-6 py-4 font-poppins">

      <!-- Logo / titre -->
      <div class="mb-10 flex justify-center">
        <h2 class="font-carattere italic text-[50px] mb-2 text-center text-white">
          <span class="text-orange-400">R</span>eserv'<span class="text-orange-400">I</span>t
        </h2>
      </div>

      <!-- Titre -->
      <h2 class="text-start mb-4 text-2xl text-white">
        <span class="text-orange-400">C</span>reate your account
      </h2>

      <!-- Formulaire -->
      <form @submit.prevent="handleRegister" class="space-y-6">
        <!-- Prénom -->
         <div class="flex gap-2">
        <div>
          <input
            v-model="name"
            type="text"
            placeholder="First name"
            required
            class="w-full px-4 py-3 border border-gray-300 rounded-xl shadow-sm focus:ring-orange-500 focus:border-orange-500 bg-white"
          />
        </div>
        <!-- Nom -->
        <div>
          <input
            v-model="familyName"
            type="text"
            placeholder="Last name"
            required
            class="w-full px-4 py-3 border border-gray-300 rounded-xl shadow-sm focus:ring-orange-500 focus:border-orange-500 bg-white"
          />
        </div>
      </div>
        <!-- Email -->
        <div>
          <input
            v-model="email"
            type="email"
            placeholder="Email"
            required
            class="w-full px-4 py-3 border border-gray-300 rounded-xl shadow-sm focus:ring-orange-500 focus:border-orange-500 bg-white"
          />
        </div>

        <!-- Password -->
        <div>
          <input
            v-model="password"
            type="password"
            placeholder="Password"
            required
            class="w-full px-4 py-3 border border-gray-300 rounded-xl shadow-sm focus:ring-orange-500 focus:border-orange-500 bg-white"
          />
        </div>

        <!-- Confirm Password -->
        <div>
          <input
            v-model="confirmPassword"
            type="password"
            placeholder="Confirm password"
            required
            class="w-full px-4 py-3 border border-gray-300 rounded-xl shadow-sm focus:ring-orange-500 focus:border-orange-500 bg-white"
          />
        </div>

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

        <!-- Message d'erreur -->
        <div v-if="errorMessage" class="text-red-400 text-sm text-center">
          {{ errorMessage }}
        </div>

        <!-- Bouton s'enregistrer -->
        <div class="flex justify-center">
          <button
            type="submit"
            class="w-1/3 flex justify-center items-center py-3 px-4 border border-transparent rounded-full shadow-sm text-sm font-light text-white bg-orange-500 hover:bg-orange-600"
          >
            Continue
          </button>
        </div>
      </form>

    </div>
    <p class="fixed bottom-4 w-full text-center text-sm text-white">
      Already have an account ?
      <router-link to="/login" class="font-medium text-orange-500 hover:text-orange-600 underline">
        Login
      </router-link>
    </p>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import BackButton from '@/components/BackButton.vue'


const name = ref('')
const familyName = ref('')
const email = ref('')
const password = ref('')
const confirmPassword = ref('')
const errorMessage = ref('')
const router = useRouter()

const apiUrl = import.meta.env.VITE_API_URL;
console.log('API URL:', apiUrl);

const handleRegister = async () => {
  if (password.value !== confirmPassword.value) {
    errorMessage.value = 'Passwords do not match'
    return
  }

  try {
    const response = await axios.post(`${apiUrl}/users`, {
      name: name.value,
      
      family_name: familyName.value,
      email: email.value,
      password_hash: password.value, // Backend will hash this
      is_admin: false // always set to false by default
    })
    localStorage.setItem('user', JSON.stringify(response.data))
    errorMessage.value = ''
    router.push('/login')
  } catch (error) {
    if (error.response && error.response.data) {
      console.log(error.response.data)
      errorMessage.value = Object.values(error.response.data).flat().join(' ')
    } else {
      errorMessage.value = 'Registration failed'
    }
  }
}
</script>
