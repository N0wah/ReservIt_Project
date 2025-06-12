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
    <form class="space-y-6" @submit="handleSubmit">
      <!-- Nom du restaurant -->
      <div>
        <label class="block text-sm text-gray-300 mb-1">Nom du restaurant</label>
        <input type="text" v-model="name" class="w-full bg-white text-black rounded-xl px-4 py-2" placeholder="Ex : La Table d'Or" />
      </div>

      <!-- Adresse, Ville, Pays -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div>
          <label class="block text-sm text-gray-300 mb-1">Adresse</label>
          <input type="text" v-model="address" class="w-full bg-white text-black rounded-xl px-4 py-2" placeholder="Ex : 123 Rue Principale" />
        </div>
        <div>
          <label class="block text-sm text-gray-300 mb-1">Ville</label>
          <input type="text" v-model="city" class="w-1/2 bg-white text-black rounded-xl px-4 py-2" placeholder="Ex : Paris" />
        </div>
        <div>
          <label class="block text-sm text-gray-300 mb-1">Pays</label>
          <input type="text" v-model="country" class="w-1/2 bg-white text-black rounded-xl px-4 py-2" placeholder="Ex : France" />
        </div>
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
        <input
          type="file"
          multiple
          accept="image/*"
          class="w-full text-sm file:mr-2 file:py-1 file:px-3 file:rounded-full file:border-0 file:text-sm file:bg-orange-500 file:text-white"
          @change="handlePhotoChange"
        />
        <div v-if="photoError" class="text-red-400 text-sm mt-1">{{ photoError }}</div>

        <!-- Prévisualisation des photos enregistrées -->
        <div class="mt-4 grid grid-cols-3 gap-4">
          <div
            v-for="(photo, index) in savedPhotos"
            :key="index"
            class="relative rounded-xl overflow-hidden"
          >
            <img :src="photo.url" class="w-full h-full object-cover" />
            <div class="absolute top-0 right-0 flex gap-2 p-2">
              <button @click="editPhoto(index)" class="bg-white text-black rounded-full p-2 text-sm">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width={2} d="M15.232 5.232a4.5 4.5 0 010 6.364M9.879 9.879a4.5 4.5 0 006.364 0M5.232 15.232a4.5 4.5 0 010-6.364M18.364 18.364a4.5 4.5 0 01-6.364 0M12 12l2.121 2.121a4.5 4.5 0 006.364 0M12 12l-2.121 2.121a4.5 4.5 0 01-6.364 0" />
                </svg>
              </button>
              <button @click="deletePhoto(index)" class="bg-red-500 text-white rounded-full p-2 text-sm">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width={2} d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Email et Téléphone -->
      <div>
        <label class="block text-sm text-gray-300 mb-1">Email</label>
        <input type="email" v-model="email" class="w-full bg-white text-black rounded-xl px-4 py-2" placeholder="Ex : contact@restaurant.com" />
      </div>
      <div>
        <label class="block text-sm text-gray-300 mb-1">Téléphone</label>
        <input type="text" v-model="phoneNumber" class="w-full bg-white text-black rounded-xl px-4 py-2" placeholder="Ex : 0601020304" />
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
import { ref, computed } from 'vue'
import RestaurantNav from '@/components/RestaurantNav.vue'
import axios from 'axios'

const name = ref('')
const openTime = ref('')
const closeTime = ref('')
const description = ref('')
const address = ref('')
const city = ref('')
const country = ref('')
const email = ref('')
const phoneNumber = ref('')
const selectedDays = ref([])
const photoError = ref('')

const days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']

// Simule les photos déjà enregistrées (remplace par ton fetch API si besoin)
const savedPhotos = ref([
  // { url: 'https://via.placeholder.com/150' },
  // { url: 'https://via.placeholder.com/150/0000FF' }
])

const apiUrl = import.meta.env.VITE_API_URL;

const selectedDaysString = computed(() => selectedDays.value.map(i => days[i]).join(';'))
print(selectedDaysString.value)

const toggleDay = (index) => {
  if (selectedDays.value.includes(index)) {
    selectedDays.value = selectedDays.value.filter(d => d !== index)
  } else {
    selectedDays.value.push(index)
  }
}

const handlePhotoChange = (event) => {
  const files = Array.from(event.target.files)
  if (files.length + savedPhotos.value.length > 3) {
    photoError.value = 'Vous ne pouvez télécharger que 3 photos maximum.'
    event.target.value = ''
    return
  }
  photoError.value = ''
  // Ajoute les nouvelles photos à la liste (affichage local, à adapter pour upload réel)
  files.forEach(file => {
    const reader = new FileReader()
    reader.onload = (e) => {
      savedPhotos.value.push({ url: e.target.result, file })
    }
    reader.readAsDataURL(file)
  })
}

const deletePhoto = (idx) => {
  savedPhotos.value.splice(idx, 1)
}

const editPhoto = (idx) => {
  // Ici tu peux ouvrir une modale ou un input pour remplacer la photo
  alert('Fonction de modification à implémenter')
}

const handleSubmit = async (e) => {
  e.preventDefault();
  const userData = localStorage.getItem('user');
  if (!userData) {
    alert('Vous devez être connecté pour créer un restaurant.');
    return;
  }
  const user = JSON.parse(userData);
  const payload = {
    name: name.value,
    address: address.value,
    city: city.value,
    country: country.value,
    description: description.value,
    email: email.value,
    phone_number: phoneNumber.value,
    images: savedPhotos.value.length > 0 ? savedPhotos.value.map(p => p.url).join(',') : '',
    owner_id: user.id,
    opening_days: selectedDaysString.value
  };
  try {
    await axios.post(`${apiUrl}/restaurants/`, payload);
    alert('Restaurant créé avec succès !');
  } catch (err) {
    if (err.response && err.response.data) {
      alert('Erreur: ' + JSON.stringify(err.response.data));
    } else {
      alert('Erreur lors de la création du restaurant.');
    }
  }
};
</script>
