<template>
<!-- Premier bloc : au-dessus -->
<div @click="toggleDetails" class="relative w-full bg-[#444444] rounded-2xl flex p-3 shadow-[0_3px_10.2px_rgba(0,0,0,0.25)] gap-4 items-center justify-between text-white font-Poppins z-1">
    <div class="flex gap-2">
  <div class="bg-white w-12 h-12 rounded-2xl">
    <img src="" alt="">
  </div>
  <div class="w-[150px]">
    <h1 class="text-sm sm:text-base md:text-lg ">Restaurant, Cities,📍</h1>
    <p class="text-[#BCBCBC] font-light text-base">number Persons</p>
  </div>
    </div>
  <p class="font-thin">02/03</p>
</div>

<!---BLoc de dessous-->
<div v-show="showDetails" class="relative w-full bg-[#444444] mt-[-12px] z-0 rounded-b-lg p-3 text-white">
  <h1 class="font-light mt-1 font-Poppins">
    information :
  </h1>
  <p class="mt-1 text-xs font-s max-w-70">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi eget molestie ipsum. In sagit cor.</p>
  <div class="flex justify-between">
    <button  @click="showModal = true" class="bg-[#B40000] px-4 py-2 rounded-full text-white flex items-center justify-center mt-2">
  Cancel
</button>
<Confirmation
    :visible="showModal"
    title="Reservation"
    message="Are you sure to cancel your booking ?"
    @confirm="handleConfirm"
    @cancel="handleCancel"
  />

<button
    @click="openMap"
    class="flex items-center gap-2 bg=[#F6F6F6] text-white font-medium px-3 py-2 rounded-full shadow-md"
  >
    <MapPinIcon class="w-6 h-6" />
  </button>
  </div>
</div>

</template>
<script setup>
import { MapPinIcon } from '@heroicons/vue/24/solid'
import { ref } from 'vue'
import Confirmation from '@/components/Confirmation.vue'
import axios from 'axios'

const props = defineProps({
  reservation: {
    type: Object,
    required: true
  }
})

const openMap = () => {
  if (props.reservation && props.reservation.restaurant && props.reservation.restaurant.lat && props.reservation.restaurant.lng) {
    const url = `https://www.google.com/maps?q=${props.reservation.restaurant.lat},${props.reservation.restaurant.lng}`
    window.open(url, '_blank')
  }
}

const showDetails = ref(false)
const toggleDetails = () => {
  showDetails.value = !showDetails.value
}
const showModal = ref(false)

const handleConfirm = async () => {
  showModal.value = false
  try {
    // Call the backend route to delete reservation and free the table
    await axios.delete(`${import.meta.env.VITE_API_URL}/reservations/delete_and_free/${props.reservation.id}/`)
    window.location.reload()
  } catch (e) {
    alert('Failed to cancel the reservation or free the table.')
  }
}

const handleCancel = () => {
  showModal.value = false
}
</script>

