import { createRouter, createWebHistory } from 'vue-router'

import LoadingScreen from '@/views/LoadingScreen.vue'
import Intro from '@/views/Intro.vue'
import HomePage from '@/views/HomePage.vue'
import RestaurantDetail from '@/views/RestaurantDetail.vue'
import Search from '@/views/Search.vue'
import Favorites from '@/views/Favorites.vue'
import List from '@/views/List.vue'
import Profile from '@/views/Profile.vue'
import Login from '@/views/Login.vue'
import Register from '@/views/Register.vue'
import RegisterDetails from '@/views/Registermore.vue'
import Dashboard from '@/views/Dashboard.vue'
import RestaurantReservationList from '@/views/RestaurantReservationList.vue'
import RestaurantSetting from '@/views/RestaurantSetting.vue'
import BookingPage from '@/views/BookingPage.vue'

const routes = [
  {
    path: '/',
    name: 'Loading',
    component: LoadingScreen,
  },
  {
    path: '/intro',
    name: 'Intro',
    component: Intro,
  },
  {
    path: '/home',
    name: 'Home',
    component: HomePage,
  },
  {
    path: '/restaurant/:id',
    name: 'RestaurantDetail',
    component: RestaurantDetail,
  },
  {
    path: '/search',
    name: 'Search',
    component: Search,
  },
  {
    path: '/favorites',
    name: 'Favorites',
    component: Favorites,
  },
  {
    path: '/list',
    name: 'List',
    component: List,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
  {
    path: '/registerdetails',
    name: 'RegisterDetails',
    component: RegisterDetails,
  },
  {
    path: '/test',
    name: 'BookingPage',
    component: BookingPage,
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: { requiresRestaurant: true }
  },
  {
    path: '/reservations',
    name: 'RestaurantReservationList',
    component: RestaurantReservationList,
    meta: { requiresRestaurant: true }
  },
  {
    path: '/settings',
    name: 'RestaurantSetting',
    component: RestaurantSetting,
    meta: { requiresRestaurant: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
