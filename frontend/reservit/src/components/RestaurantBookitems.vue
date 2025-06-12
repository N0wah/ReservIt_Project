<template>
<!-- Premier bloc : au-dessus -->
<div @click="toggleDetails" class="relative w-full bg-[#444444] rounded-2xl flex p-3 shadow-[0_3px_10.2px_rgba(0,0,0,0.25)] gap-4 items-center justify-between text-white font-Poppins z-1">
    <div class="flex gap-2">
  <div class="bg-white w-12 h-12 rounded-2xl">
    <!-- Affiche une image si disponible -->
    <img v-if="reservation && reservation.restaurant && reservation.restaurant.images" :src="reservation.restaurant.images + '/goldenbeef1.webp'" alt="" class="object-cover w-12 h-12" />
  </div>
  <div class="w-[150px]">
    <h1 class="text-sm sm:text-base md:text-lg ">
      {{ reservation && reservation.restaurant ? (reservation.restaurant.name || 'Restaurant') : 'Restaurant' }}, {{ reservation && reservation.restaurant ? (reservation.restaurant.cities || '') : '' }}
    </h1>
    <p class="text-[#BCBCBC] font-light text-base">{{ reservation?.guest_count || '' }} personnes</p>
  </div>
    </div>
    <div>
        <p class="font-thin text-sm">{{ reservation?.reservation_date || '' }}</p>
        <p class="font-light text-sm">{{ reservation?.reservation_time || '' }}</p>
    </div>
</div>

<!---BLoc de dessous-->
<div v-show="showDetails" class="relative w-full bg-[#444444] mt-[-3vh] z-0 rounded-b-lg p-3 text-white">
  <h1 class="font-light mt-1 font-Poppins">
    Information :
  </h1>
  <div class="flex justify-between w-full gap- items-center border-b border-[#474747] p-2">
        <div class=" flex flex-col w-full justify-around items-center ">
            <div class="flex justify-between w-full gap- items-center border-b border-[#474747] pt-2">
                <p class="font-Poppins text-[#B2B2B2]">email</p>
                <p class="text-sm text-white">{{ reservation?.user?.email || 'Non renseigné' }}</p>
            </div>
            <div class="flex justify-between w-full gap- items-center border-b border-[#474747] pt-6">
                <p class="font-Poppins text-[#B2B2B2]">phone</p>
                <p class="text-sm text-white">{{ reservation?.user?.phone || 'Non renseigné' }}</p>
            </div>
            <div class="flex justify-between w-full gap- items-center border-b border-[#474747] pt-6">
                <p class="font-Poppins text-[#B2B2B2]">country</p>
                <p class="text-sm text-white">{{ reservation?.user?.country || 'Non renseigné' }}</p>
            </div>
        </div>
    </div>
<h1>Message :</h1>
  <p class="mt-1 text-xs font-s max-w-70">{{ reservation?.information || 'Aucune information.' }}</p>
  <div class="flex justify-end">
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

  </div>
</div>

</template>
<script setup>
import { ref } from 'vue'
import Confirmation from '@/components/Confirmation.vue'

defineProps({
  label: {
    type: String,
    default: 'Voir sur la carte'
  },
  lat: {
    type: Number,
    required: true
  },
  lng: {
    type: Number,
    required: true
  },
  reservation: {
    type: Object,
    required: true
  }
})

const openMap = () => {
  const url = `https://www.google.com/maps?q=${props.lat},${props.lng}`
  window.open(url, '_blank')
}

const showDetails = ref(false)

const toggleDetails = () => {
  showDetails.value = !showDetails.value
}

const showModal = ref(false)

const handleConfirm = () => {
  showModal.value = false
  console.log('Action confirmée !')
}

const handleCancel = () => {
  showModal.value = false
}
</script>

