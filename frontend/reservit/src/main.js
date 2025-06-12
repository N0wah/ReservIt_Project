import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/main.css'
import '@fortawesome/fontawesome-free/css/all.css'

import VCalendar from 'v-calendar'
import 'v-calendar/style.css';


const app = createApp(App)

app.use(router)
app.use(VCalendar, {}) 

app.mount('#app')

import { registerSW } from 'virtual:pwa-register'

const updateSW = registerSW({
  onNeedRefresh() {
    if (confirm("Une nouvelle version est disponible. Mettre à jour ?")) {
      updateSW(true)
    }
  },
  onOfflineReady() {
    console.log("L'application est prête à fonctionner hors ligne.")
  }
})
