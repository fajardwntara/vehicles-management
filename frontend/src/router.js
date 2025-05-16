import { createRouter, createWebHistory } from 'vue-router'
import Login from './pages/Login.vue'
import User from './pages/User/UserManagement.vue'
import VehicleManagement from './pages/Vehicles/VehicleManagement.vue'
import Vehicle from '@/pages/Vehicles/Managements/Vehicle.vue'
import SalesPurchases from '@/pages/Vehicles/Managements/SalesPurchases.vue'
import TransactionReport from '@/pages/Vehicles/Managements/TransactionReport.vue'
import NotFound from '@/pages/NotFound.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', redirect: '/login' },
    { path: '/login', component: Login },
    { path: '/user', component: User },
    { path: '/vehicle-management', component: VehicleManagement },
    { path: '/vehicle-management/vehicle', component: Vehicle },
    { path: '/vehicle-management/sales-purchases', component: SalesPurchases },
    { path: '/vehicle-management/transaction-report', component: TransactionReport },
    { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFound }
  ]
})

router.beforeEach((to, from, next) => {
  const token = sessionStorage.getItem('access_token')

  if (!token && to.path !== '/login') {
    return next('/login')
  }

  if (token && to.path === '/login') {
    return next('/user')
  }

  next()
})

export default router
