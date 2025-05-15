import { createRouter, createWebHistory } from 'vue-router'
import VehicleManagement from './pages/Vehicles/VehicleManagement.vue'
import Login from './pages/Login.vue'
import User from './pages/User/UserManagement.vue'

const routerHistory = createWebHistory()

const router = createRouter({
  history: routerHistory,
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/vehicle-management',
      component: VehicleManagement
    },
    {
      path: '/login',
      component: Login
    },
    {
      path: '/user',
      component: User
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: '/login'
    }
  ]
})

export default router
