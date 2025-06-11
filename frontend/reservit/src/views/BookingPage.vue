<template>
  <BackButton />

  <div class="relative min-h-screen bg-[#2E2E2E] px-10 pt-16 text-white flex flex-col gap-4 overflow-x-hidden pb-10">

    <!-- Profil Header -->
    <section class="w-full bg-[#444444] rounded-2xl p-3 shadow-[0_2px_10.2px_rgba(0,0,0,0.25)]">
      <div class="flex justify-between items-center w-full">
        <div class="flex items-center gap-2">
          <div class="w-10 h-10 bg-white rounded-full" />
          <div>
            <h1 class="text-white">{{ userInfo.firstName }} {{ userInfo.lastName }}</h1>
            <div class="flex gap-2 items-center mt-1">
              <span>{{ userInfo.email || 'No email' }}</span>
            </div>
          </div>
        </div>
        <button
          class="text-white text-sm w-10 h-10 bg-white rounded-full flex justify-center items-center"
          @click="showEditModal = true"
        >
          <PencilIcon class="w-6 h-6 text-black" />
        </button>
      </div>
    </section>

    <!-- Restaurant Info -->
    <section class="w-full">
      <div class="space-y-0 mb-2">
        <h2 class="text-3xl font-light leading-tight">
          {{ restaurantInfo.name }}<span v-if="restaurantInfo.cities" class="text-lg">, {{ restaurantInfo.cities }}</span>
        </h2>
        <p class="text-gray-400 text-sm leading-snug break-words -mt-1">{{ restaurantInfo.address }}</p>
      </div>
    </section>

    <!-- Date -->
    <section class="w-full">
      <h2 class="text-xl mb-2">Date</h2>
      <div class="flex justify-center">
        <Calendar />
      </div>
    </section>

    <!-- Hours -->
    <section class="w-full">
      <h2 class="text-xl mb-2">Hours</h2>
      <TimeSlotSelector @update:selectedTime="handleTimeSelect" />
    </section>

    <!-- Guest -->
    <section class="w-full">
      <h2 class="text-xl mb-2">Guest</h2>
      <QuantitySelector />
    </section>

    <!-- Message -->
    <section class="w-full">
      <h2 class="text-xl mb-2">Message</h2>
      <MessageTexteArea />
    </section>

    <!-- Reserve Button -->
    <div class="w-full flex justify-center">
      <button
        @click="showSuccess = true"
        class="bg-orange-500 w-full hover:bg-orange-600 text-white font-light text-2xl py-3 px-10 rounded-full transition duration-200 shadow-[1px_3px_3.7px_rgba(0,0,0,0.25)]"
      >
        Reserve It now
      </button>
    </div>
  </div>

  <!-- Modales -->
  <EditProfileModal
    :isOpen="showEditModal"
    @close="showEditModal = false"
    @save="updateProfile"
  />

  <SuccessModal
    :visible="showSuccess"
    @close="showSuccess = false"
  />
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import BackButton from '@/components/BackButton.vue'
import Calendar from '@/components/Calendar.vue'
import TimeSlotSelector from '@/components/SelectHours.vue'
import QuantitySelector from '@/components/Guestcount.vue'
import MessageTexteArea from '@/components/MessageTexteArea.vue'
import EditProfileModal from '@/components/ModaleEditProfil.vue'
import SuccessModal from '@/components/BookingConfirmation.vue'
import { PencilIcon } from '@heroicons/vue/24/outline'

// États
const selectedTime = ref(null)
const showEditModal = ref(false)
const showSuccess = ref(false)

// Infos utilisateur dynamiques
const userInfo = ref({
  firstName: '',
  lastName: '',
  phone: '',
  email: ''
})
const contactMethod = ref('phone') // 'phone' ou 'email'

const route = useRoute()
const restaurantInfo = ref({ name: '', address: '', cities: '' })

onMounted(async () => {
  const userData = localStorage.getItem('user')
  if (userData) {
    const user = JSON.parse(userData)
    userInfo.value.firstName = user.name || ''
    userInfo.value.lastName = user.family_name || ''
    userInfo.value.phone = user.phone || ''
    userInfo.value.email = user.email || ''
  }
  // Prend les infos du restaurant depuis le localStorage si elles existent
  const storedRestaurant = localStorage.getItem('selectedRestaurant')
  if (storedRestaurant) {
    try {
      const data = JSON.parse(storedRestaurant)
      restaurantInfo.value = {
        name: data.name || '',
        address: data.address || '',
        cities: data.cities || data.city || ''
      }
    } catch {
      // fallback API si parsing échoue
    }
  } else if (route.params.id) {
    // fallback API si pas dans le localStorage
    try {
      const res = await fetch(`http://127.0.0.1:8000/api/restaurants/${route.params.id}/`)
      if (res.ok) {
        const data = await res.json()
        restaurantInfo.value = {
          name: data.name || '',
          address: data.address || '',
          cities: data.cities || data.city || ''
        }
      }
    } catch {}
  }
})

function handleTimeSelect(time) {
  selectedTime.value = time
}

function updateProfile(newData) {
  userInfo.value = { ...userInfo.value, ...newData }
}
</script>
