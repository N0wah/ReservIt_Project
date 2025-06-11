<template>
  <div class="bg-[#242424] min-h-screen text-white px-6 pt-6 pb-32 space-y-8">
    <!-- Titre -->
    <div class="flex justify-center items-center gap-2">
      <h2 class="font-carattere italic text-[50px] text-white">
        <span class="text-orange-400">S</span>etting
      </h2>
      <p><span class="text-orange-400">A</span>dmin</p>
    </div>

    <!-- Formulaire de gestion -->
    <form class="space-y-6">
      <!-- Nom du restaurant -->
      <div>
        <label class="block text-sm text-gray-300 mb-1">Nom du restaurant</label>
        <input type="text" v-model="name" class="w-full bg-white text-black rounded-xl px-4 py-2" placeholder="Ex : La Table d'Or" />
      </div>

      <!-- Heures d’ouverture -->
      <div>
        <label class="block text-sm text-gray-300 mb-1">Heures d’ouverture</label>
        <div class="flex gap-2">
          <input type="time" v-model="openTime" class="bg-white text-black rounded-xl px-3 py-2" />
          <span class="text-gray-400">à</span>
          <input type="time" v-model="closeTime" class="bg-white text-black rounded-xl px-3 py-2" />
        </div>
      </div>

      <!-- Jours d’ouverture -->
      <div>
        <label class="block text-sm text-gray-300 mb-1">Jours d’ouverture</label>
        <div class="flex flex-wrap gap-2">
          <button
            v-for="(day, i) in days"
            :key="i"
            @click.prevent="toggleDay(i)"
            :class="[
              'px-4 py-1 rounded-full text-sm',
              selectedDays.includes(i)
                ? 'bg-orange-500 text-white'
                : 'bg-white text-black'
            ]"
          >
            {{ day }}
          </button>
        </div>
      </div>

      <!-- Description -->
      <div>
        <label class="block text-sm text-gray-300 mb-1">Description</label>
        <textarea v-model="description" class="w-full bg-white text-black rounded-xl px-4 py-2 h-24" placeholder="Décris ton restaurant ici..."></textarea>
      </div>

      <!-- Photos -->
      <div>
        <label class="block text-sm text-gray-300 mb-1">Photos</label>
        <input type="file" multiple class="w-full text-sm file:mr-2 file:py-1 file:px-3 file:rounded-full file:border-0 file:text-sm file:bg-orange-500 file:text-white" />
      </div>

      <!-- Bouton Enregistrer -->
      <button type="submit" class="w-full bg-orange-500 hover:bg-orange-600 text-white font-medium py-3 rounded-full">
        Enregistrer les modifications
      </button>
    </form>
  </div>

  <RestaurantNav />
</template>

<script setup>
import { ref } from 'vue'
import RestaurantNav from '@/components/RestaurantNav.vue'

const name = ref('')
const openTime = ref('')
const closeTime = ref('')
const description = ref('')
const selectedDays = ref([])

const days = ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim']

const toggleDay = (index) => {
  if (selectedDays.value.includes(index)) {
    selectedDays.value = selectedDays.value.filter(d => d !== index)
  } else {
    selectedDays.value.push(index)
  }
}
</script>
