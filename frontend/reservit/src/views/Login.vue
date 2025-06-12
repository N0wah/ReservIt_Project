<template>
  <BackToHome />
  <div class="min-h-screen bg-[#242424] flex flex-col justify-start relative px-6 py-4">
    
    <div class="mb-10 flex justify-center itemstar">
      
      <h2 class="font-carattere italic text-[50px] mb-2 text-center sm:text-left text-white">
      <span class="text-orange-400">R</span>eserv'<span class="text-orange-400">I</span>t
    </h2>
    </div>



  
    <!-- Title -->
    <h2 class="text-start mb-4 text-2xl  text-white"><span class="text-orange-400">L</span>ogin to your account</h2>

  
    <!-- Form -->
    <form @submit.prevent="handleLogin" class="space-y-10">
      <div>
        <input
          v-model="email"
          id="email"
          type="email"
          placeholder="Email"
          autocomplete="email"
          required
          class="mt-1 block w-full px-4 py-3 border border-gray-300 rounded-xl shadow-sm focus:ring-orange-500 focus:border-orange-500 bg-white"
        />
      </div>
      <div>
        <input
          v-model="password"
          id="password"
          type="password"
          placeholder="Password"
          autocomplete="current-password"
          required
          class="mt-1 block w-full px-4 py-3 border border-gray-300 rounded-xl shadow-sm focus:ring-orange-500 focus:border-orange-500 bg-white"
        />
      </div>
      <div>
        <button
          type="submit"
          class="w-1/3 mx-auto flex justify-center items-center py-3 px-4 border border-transparent rounded-full shadow-sm text-sm font-light text-white bg-orange-500 hover:bg-orange-600 focus:outline-none"
        >
          Login
        </button>
      </div>
    </form>
    <p class="fixed bottom-4 w-full text-center text-sm text-white">
      No account?
      <router-link to="/register" class="underline text-orange-400">Create one</router-link>
    </p>
    <RestaurantNav v-if="showRestaurantNav" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import BackToHome from '@/components/BackToHome.vue'
import RestaurantNav from '@/components/RestaurantNav.vue'

const email = ref('')
const password = ref('')
const errorMessage = ref('')
const router = useRouter()
const apiUrl = import.meta.env.VITE_API_URL;
const showRestaurantNav = ref(false)

const handleLogin = async () => {
  try {
    const response = await axios.post(`${apiUrl}/login/`, {
      email: email.value,
      password: password.value,
    })
    if (response.data.token) {
      localStorage.setItem('token', response.data.token)
      localStorage.setItem('user', JSON.stringify(response.data.user))
      if (response.data.user.is_admin === true) {
        window.location.replace('/dashboard')
      } else {
        window.location.replace('/profile')
      }
    } else {
      errorMessage.value = 'Invalid credentials'
    }
  } catch (error) {
    errorMessage.value = 'Connection error'
  }
}
</script>
