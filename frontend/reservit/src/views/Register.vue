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
          <label class="mb-2 text-white">Choose your avatar</label>
          <div class="flex flex-wrap gap-4 justify-center mb-2">
            <img
              v-for="n in 4" :key="n"
              :src="`/img/avatar/avatar${n}.png`"
              :alt="`Avatar ${n}`"
              :class="[
                'w-20 h-20 rounded-full object-cover border-2 cursor-pointer',
                selectedAvatar === `/img/avatar/avatar${n}.png` ? 'border-orange-500 ring-2 ring-orange-400' : 'border-gray-300'
              ]"
              @click="selectAvatar(`/img/avatar/avatar${n}.png`)"
            />
          </div>
          <div v-if="selectedAvatar" class="mt-2">
            <span class="text-white">Selected avatar:</span>
            <img :src="selectedAvatar" alt="Selected avatar" class="w-12 h-12 rounded-full inline-block ml-2 border-2 border-orange-400" />
          </div>
        </div>

        <!-- Error message -->
        <div v-if="errorMessage" class="text-red-400 text-sm text-center">
          {{ errorMessage }}
        </div>

        <!-- Register button -->
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
      Already have an account?
      <router-link to="/login" class="underline text-orange-400">Log in</router-link>
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
const selectedAvatar = ref('')
const router = useRouter()

const apiUrl = import.meta.env.VITE_API_URL;

const handleRegister = async () => {
  if (password.value !== confirmPassword.value) {
    errorMessage.value = 'Passwords do not match'
    return
  }
  if (!selectedAvatar.value) {
    errorMessage.value = 'Please select an avatar.'
    return
  }
  try {
    const response = await axios.post(`${apiUrl}/users/`, {
      name: name.value,
      family_name: familyName.value,
      email: email.value,
      password_hash: password.value,
      is_admin: false, 
      created_at: new Date().toISOString(),
      avatar: selectedAvatar.value // send avatar path
    })
    // If backend does not return avatar, patch it
    let userData = response.data
    if (!userData.avatar && selectedAvatar.value) {
      userData.avatar = selectedAvatar.value
    }
    localStorage.setItem('user', JSON.stringify(userData))
    errorMessage.value = ''
    router.push('/login')
  } catch (error) {
    if (error.response && error.response.data) {
      errorMessage.value = Object.values(error.response.data).flat().join(' ')
    } else {
      errorMessage.value = 'Registration failed'
    }
  }
}

function selectAvatar(path) {
  selectedAvatar.value = path
}
</script>
