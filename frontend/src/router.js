import { createRouter, createWebHistory } from 'vue-router'
import Login from './pages/Login.vue'
import User from './pages/User/UserManagement.vue'
import VehicleManagement from './pages/Vehicles/VehicleManagement.vue'
import Vehicle from '@/pages/Vehicles/Managements/Vehicle.vue'

const routerHistory = createWebHistory()

const router = createRouter({
  history: routerHistory,
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/login',
      component: Login
    },
    {
      path: '/user',
      component: User
    },
    // Vehicles
    {
      path: '/vehicle-management',
      component: VehicleManagement
    },
    {
      path: '/vehicle-management/motor',
      component: Vehicle
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: '/login'
    }
  ]
})

export default router
