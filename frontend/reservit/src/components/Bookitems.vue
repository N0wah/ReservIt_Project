<template>
<!-- Top block -->
<div @click="toggleDetails" class="relative w-full bg-[#444444] rounded-2xl flex p-3 shadow-[0_3px_10.2px_rgba(0,0,0,0.25)] gap-4 items-center justify-between text-white font-Poppins z-1">
    <div class="flex gap-2">
  <div class="bg-white w-12 h-12 rounded-2xl overflow-hidden flex items-center justify-center">
    <img v-if="reservation && reservation.restaurant && reservation.restaurant.images" :src="reservation.restaurant.images + '/goldenbeef1.webp'" alt="Restaurant image" class="object-cover w-12 h-12" />
  </div>
  <div class="w-[150px]">
    <h1 class="text-sm sm:text-base md:text-lg ">
      <span >{{ name }}</span>
    </h1>
    <p class="text-[#BCBCBC] font-light text-base">Réservé par : {{ userName || 'Utilisateur inconnu' }}</p>
    <p class="text-[#BCBCBC] font-light text-base">{{ guestCount }} persons</p>
  </div>
    </div>
  <div class="flex flex-col items-end">
    <p class="font-thin">{{ reservation_date }}</p>
    <p class="font-thin">{{ reservation_time }}</p>
    <p class="font-thin">Status: {{ status }}</p>
  </div>
</div>

<!-- Bottom block -->
<div v-show="showDetails" class="relative w-full bg-[#444444] mt-[-12px] z-0 rounded-b-lg p-3 text-white">
  <h1 class="font-light mt-1 font-Poppins">
    Information:
  </h1>
  <p class="mt-1 text-xs font-s max-w-70">{{ reservation.information || 'No additional information.' }}</p>
  <div class="flex justify-between mt-2">
    <button  @click.stop="showModal = true" class="bg-[#B40000] px-4 py-2 rounded-full text-white flex items-center justify-center mt-2">
      Cancel
    </button>
    <Confirmation
      :visible="showModal"
      title="Reservation"
      message="Are you sure to cancel your booking?"
      @confirm="handleConfirm"
      @cancel="handleCancel"
    />
    <button
      v-if="reservation.restaurant && reservation.restaurant.lat && reservation.restaurant.lng"
      @click.stop="openMap"
      class="flex items-center gap-2 bg-[#F6F6F6] text-white font-medium px-3 py-2 rounded-full shadow-md"
    >
      <MapPinIcon class="w-6 h-6" />
    </button>
  </div>
</div>

</template>
<script setup>
defineProps({
  name: String,
  reservation: Object,
  userName: String,
  guestCount: Number,
  reservation_date: String,
  reservation_time: String,
  status: String
})
</script>

