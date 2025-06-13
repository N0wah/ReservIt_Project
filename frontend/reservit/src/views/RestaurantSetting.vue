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
      <!-- Restaurant name -->
      <div>
        <label class="block text-sm text-gray-300 mb-1">Restaurant name</label>
        <input type="text" v-model="name" class="w-full bg-white text-black rounded-xl px-4 py-2" placeholder="e.g. The Golden Table" />
      </div>

      <!-- Adresse, Ville, Pays -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div>
          <label class="block text-sm text-gray-300 mb-1">Address</label>
          <input type="text" v-model="address" class="w-full bg-white text-black rounded-xl px-4 py-2" placeholder="e.g. 123 Main Street" />
        </div>
        <div>
          <label class="block text-sm text-gray-300 mb-1">City</label>
          <input type="text" v-model="city" class="w-1/2 bg-white text-black rounded-xl px-4 py-2" placeholder="e.g. Paris" />
        </div>
        <div>
          <label class="block text-sm text-gray-300 mb-1">Country</label>
          <input type="text" v-model="country" class="w-1/2 bg-white text-black rounded-xl px-4 py-2" placeholder="e.g. France" />
        </div>
      </div>

      <!-- Opening hours -->
      <div>
        <label class="block text-sm text-gray-300 mb-1">Opening hours</label>
        <div class="flex gap-2">
          <input type="time" v-model="openTime" class="bg-white text-black rounded-xl px-3 py-2" />
          <span class="text-gray-400">to</span>
          <input type="time" v-model="closeTime" class="bg-white text-black rounded-xl px-3 py-2" />
        </div>
      </div>

      <!-- Opening days -->
      <div>
        <label class="block text-sm text-gray-300 mb-1">Opening days</label>
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
        <textarea v-model="description" class="w-full bg-white text-black rounded-xl px-4 py-2 h-24" placeholder="Describe your restaurant here..."></textarea>
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

        <!-- Preview of saved photos -->
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

      <!-- Email and Phone -->
      <div>
        <label class="block text-sm text-gray-300 mb-1">Email</label>
        <input type="email" v-model="email" class="w-full bg-white text-black rounded-xl px-4 py-2" placeholder="e.g. contact@restaurant.com" />
      </div>
      <div>
        <label class="block text-sm text-gray-300 mb-1">Phone</label>
        <input type="text" v-model="phoneNumber" class="w-full bg-white text-black rounded-xl px-4 py-2" placeholder="e.g. 0601020304" />
      </div>

      <!-- Save button -->
      <button type="submit" class="w-full bg-orange-500 hover:bg-orange-600 text-white font-medium py-3 rounded-full">
        Save changes
      </button>
      <button type="button" @click="logout" class="w-full mt-2 bg-red-500 hover:bg-red-600 text-white font-medium py-3 rounded-full">
        Logout
      </button>
    </form>
  </div>

  <RestaurantNav />
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
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

const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

// Simulate already saved photos (replace with your API fetch if needed)
const savedPhotos = ref([
  // { url: 'https://via.placeholder.com/150' },
  // { url: 'https://via.placeholder.com/150/0000FF' }
])

const apiUrl = import.meta.env.VITE_API_URL;

const selectedDaysString = computed(() => selectedDays.value.map(i => days[i]).join(','))

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
    photoError.value = 'You can only upload up to 3 photos.'
    event.target.value = ''
    return
  }
  photoError.value = ''
  // Add new photos to the list (local display, adapt for real upload)
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
  // Here you can open a modal or input to replace the photo
  alert('Edit photo feature to be implemented')
}

const handleSubmit = async (e) => {
  e.preventDefault();
  const userData = localStorage.getItem('user');
  if (!userData) {
    alert('You must be logged in to create or edit a restaurant.');
    return;
  }
  const user = JSON.parse(userData);

  // 1. Check if restaurant exists (edit mode)
  let restaurantId = null;
  try {
    const res = await axios.get(`${apiUrl}/restaurants/owner_id/${user.id}/`);
    if (Array.isArray(res.data) && res.data.length > 0) {
      restaurantId = res.data[0].id;
    }
  } catch {}

  // 2. If there are new images to upload, send them to backend
  let uploadedImagePaths = [];
  const filesToUpload = savedPhotos.value.filter(p => p.file).map(p => p.file);
  if (filesToUpload.length > 0) {
    if (!restaurantId) {
      // Need to create restaurant first to get ID
      const payload = {
        name: name.value,
        address: address.value,
        city: city.value,
        country: country.value,
        description: description.value,
        email: email.value,
        phone_number: phoneNumber.value,
        images: '',
        owner_id: user.id,
        opening_days: selectedDaysString.value
      };
      const createRes = await axios.post(`${apiUrl}/restaurants/`, payload);
      restaurantId = createRes.data.id;
    }
    const formData = new FormData();
    filesToUpload.forEach(f => formData.append('images', f));
    try {
      const uploadRes = await axios.post(`${apiUrl}/restaurants/${restaurantId}/upload_images/`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      uploadedImagePaths = uploadRes.data.images;
    } catch (err) {
      alert('Image upload failed.');
      return;
    }
  }

  // 3. Prepare payload for restaurant update
  const payload = {
    name: name.value,
    address: address.value,
    city: city.value,
    country: country.value,
    description: description.value,
    email: email.value,
    phone_number: phoneNumber.value,
    images: uploadedImagePaths.length > 0
      ? uploadedImagePaths.join(',')
      : savedPhotos.value.filter(p => !p.file).map(p => p.url).join(','),
    owner_id: user.id,
    opening_days: selectedDaysString.value
  };

  try {
    if (restaurantId) {
      await axios.put(`${apiUrl}/restaurants/${restaurantId}/`, payload);
      alert('Restaurant updated successfully!');
    } else {
      await axios.post(`${apiUrl}/restaurants/`, payload);
      alert('Restaurant created successfully!');
    }
  } catch (err) {
    if (err.response && err.response.data) {
      alert('Error: ' + JSON.stringify(err.response.data));
    } else {
      alert('Error while creating or updating the restaurant.');
    }
  }
};

const logout = () => {
  localStorage.removeItem('user');
  window.location.href = '/login';
}

onMounted(async () => {
  const userData = localStorage.getItem('user');
  if (!userData) return;
  const user = JSON.parse(userData);
  try {
    const res = await axios.get(`${apiUrl}/restaurants/owner_id/${user.id}/`);
    if (Array.isArray(res.data) && res.data.length > 0) {
      const r = res.data[0];
      name.value = r.name || '';
      address.value = r.address || '';
      city.value = r.city || '';
      country.value = r.country || '';
      description.value = r.description || '';
      email.value = r.email || '';
      phoneNumber.value = r.phone_number || '';
      // Fill opening days
      if (r.opening_days) {
        const daysArr = r.opening_days.split(',').map(d => d.trim());
        selectedDays.value = daysArr.map(day => days.indexOf(day)).filter(i => i !== -1);
      }
      // Fill images if present
      if (r.images) {
        savedPhotos.value = r.images.split(',').map(url => ({ url }));
      }
    }
  } catch (e) {
    // ignore
  }
});
</script>
