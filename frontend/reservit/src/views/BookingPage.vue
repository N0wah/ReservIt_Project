<template>
  <BackButton />

  <div class="relative min-h-screen bg-[#2E2E2E] px-10 pt-16 text-white flex flex-col gap-4 overflow-x-hidden pb-10">

    <!-- Profil Header -->
    <section class="w-full bg-[#444444] rounded-2xl p-3 shadow-[0_2px_10.2px_rgba(0,0,0,0.25)]">
      <div class="flex justify-between items-center w-full">
        <div class="flex items-center gap-2">
            <img
            v-if="userInfo.avatar_path"
            :src="userInfo.avatar_path"
            alt="User avatar"
            class="w-10 h-10 bg-white rounded-full object-cover"
            />
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
        <Calendar @dayclick="handleDateSelect" />
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
      <QuantitySelector @update:guestCount="handleGuestCountChange" />
    </section>

    <!-- Message -->
    <section class="w-full">
      <h2 class="text-xl mb-2">Message</h2>
      <MessageTexteArea v-model="message" />
    </section>

    <!-- Table Selection -->
    <section class="w-full">
      <h2 class="text-xl mb-2">Table</h2>
      <div v-if="loadingTables" class="text-gray-400">Loading tables...</div>
      <div v-else-if="tableError" class="text-red-400">{{ tableError }}</div>
      <div v-else-if="availableTables.length === 0" class="text-gray-400">No table available for this slot.</div>
      <div v-else class="flex flex-wrap gap-3">
        <button
          v-for="table in availableTables"
          :key="table.id"
          :class="[
            'px-5 py-3 rounded-2xl font-semibold transition-all duration-200',
            'shadow-[0_2px_8px_rgba(0,0,0,0.15)]',
            selectedTableId === table.id
              ? 'bg-orange-500 text-white scale-105 border-2 border-orange-400'
              : 'bg-[#444444] text-white hover:bg-orange-400 hover:text-black border border-[#666]'
          ]"
          @click="selectedTableId = table.id"
        >
          Table {{ table.table_number }}<br>
          <span class="text-xs font-normal">({{ table.capacity }} pers)</span>
        </button>
      </div>
    </section>

    <!-- Reserve Button -->
    <div class="w-full flex flex-col gap-4 justify-center items-center">
      <button
        @click="handleReserve"
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
import { ref, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router'
import BackButton from '@/components/BackButton.vue'
import Calendar from '@/components/Calendar.vue'
import TimeSlotSelector from '@/components/SelectHours.vue'
import QuantitySelector from '@/components/Guestcount.vue'
import MessageTexteArea from '@/components/MessageTexteArea.vue'
import EditProfileModal from '@/components/ModaleEditProfil.vue'
import SuccessModal from '@/components/BookingConfirmation.vue'
import { PencilIcon, CheckIcon } from '@heroicons/vue/24/outline'
import axios from 'axios'

// États
const selectedTime = ref(null)
const showEditModal = ref(false)
const showSuccess = ref(false)
const reservationDate = ref('')
const guestCount = ref(1)
const message = ref('')
const availableTables = ref([])
const selectedTableId = ref(null)
const loadingTables = ref(false)
const tableError = ref('')

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
const apiUrl = import.meta.env.VITE_API_URL;

onMounted(async () => {
  const userData = localStorage.getItem('user')
  if (userData) {
    const user = JSON.parse(userData)
    userInfo.value.firstName = user.name || ''
    userInfo.value.lastName = user.family_name || ''
    userInfo.value.phone = user.phone || ''
    userInfo.value.email = user.email || ''
    userInfo.value.avatar_path = user.avatar_path || ''
  }
  // Prend les infos du restaurant depuis le localStorage si elles existent
  const storedRestaurant = localStorage.getItem('selectedRestaurant')
  if (storedRestaurant) {
    try {
      const data = JSON.parse(storedRestaurant)
      restaurantInfo.value = {
        name: data.name || '',
        address: data.address || '',
        cities: data.cities || data.city || '',
        id: data.id || data.pk || '' // Ajout de l'id si présent
      }
    } catch {
      // fallback API si parsing échoue
    }
  } else if (route.params.id) {
    // fallback API si pas dans le localStorage
    try {
      const res = await fetch(`${apiUrl}/restaurants/${route.params.id}/`)
      if (res.ok) {
        const data = await res.json()
        restaurantInfo.value = {
          name: data.name || '',
          address: data.address || '',
          cities: data.cities || data.city || '',
          id: data.id || data.pk || '' // Ajout de l'id si présent
        }
      }
    } catch {}
  }

  // Fetch all tables (not filtered by restaurant)
  loadingTables.value = true
  try {
    const res = await axios.get(`${apiUrl}/tables/`)
    availableTables.value = res.data
    if (availableTables.value.length > 0) {
      selectedTableId.value = availableTables.value[0].id
    }
  } catch (e) {
    tableError.value = 'Error loading tables.'
    availableTables.value = []
  } finally {
    loadingTables.value = false
  }
})

function handleTimeSelect(time) {
  selectedTime.value = time + ':00'
}

function updateProfile(newData) {
  userInfo.value = { ...userInfo.value, ...newData }
}

// Synchronisation du nombre de personnes avec le composant QuantitySelector
const guestCountFromSelector = ref(1)

function handleGuestCountChange(newCount) {
  guestCount.value = newCount
}

// Gère la sélection de la date
function handleDateSelect(date) {
  reservationDate.value = date
}

// Réserve la table sélectionnée
function reserveTable() {
  if (!selectedTableId.value) {
    alert('Please select a table.')
    return
  }
  // Logique de réservation de table ici
}

// Ajout de la logique de réservation
function handleReserve() {
  const userData = localStorage.getItem('user')
  if (!userData) {
    alert('You must be logged in to make a reservation.')
    return
  }
  const user = JSON.parse(userData)
  if (!selectedTime.value) {
    alert('Please select a time slot.')
    return
  }
  if (!reservationDate.value) {
    alert('Please select a date.')
    return
  }
  if (!selectedTableId.value) {
    alert('Please select a table.')
    return
  }

  // Format reservation_date as YYYY-MM-DD
  let formattedDate = ''
  if (reservationDate.value instanceof Date) {
    formattedDate = reservationDate.value.toISOString().slice(0, 10)
  } else if (typeof reservationDate.value === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(reservationDate.value)) {
    formattedDate = reservationDate.value
  } else {
    // Try to parse string to Date
    const d = new Date(reservationDate.value)
    if (!isNaN(d.getTime())) {
      formattedDate = d.toISOString().slice(0, 10)
    } else {
      alert('Invalid date format. Please select a valid date.')
      return
    }
  }

  

  // Ensure table_id is a number and not null/undefined
  const tableId = Number(selectedTableId.value)
  if (!tableId || isNaN(tableId)) {
    alert('Please select a valid table.')
    return
  }

  // Ensure restaurant is a number (id) and not null/undefined
  const restaurantId = Number(restaurantInfo.value.id)
  if (!restaurantId || isNaN(restaurantId)) {
    alert('Restaurant information is missing.')
    return
  }

  // DEBUG: Log all values before sending
  console.log('Reservation debug:', {
    user_id: user.id,
    restaurant: restaurantId,
    table_id: tableId,
    guest_count: guestCount.value,
    reservation_time: selectedTime.value,
    reservation_date: formattedDate,
    status: 'Pending',
    information: message.value
  })



  axios.post(`${apiUrl}/reservations/`, {
    user_id: user.id,
    restaurant: restaurantId, // must be a number and not null
    table_id: tableId, // must be a number
    guest_count: guestCount.value,
    reservation_time: selectedTime.value,
    reservation_date: formattedDate,
    status: 'Pending',
    information: message.value || ''
  })
    .then(() => {
      showSuccess.value = true
      // Update the table in availableTables to is_reserved = true
      const reservedTable = availableTables.value.find(t => t.id === tableId)
      if (reservedTable) reservedTable.is_reserved = true
    })
    .catch((error) => {
      if (error.response && error.response.data) {
        alert('Error: ' + JSON.stringify(error.response.data))
      } else {
        alert('Reservation failed. Please try again.')
      }
    })
}

function handleLogout() {
  // Logique de déconnexion
  localStorage.removeItem('user')

}
</script>
