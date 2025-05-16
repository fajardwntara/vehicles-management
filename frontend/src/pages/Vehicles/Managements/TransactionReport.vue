<template>
    <div class="flex h-screen overflow-hidden">
        
        <Sidebar :sidebarOpen="sidebarOpen" @close-sidebar="sidebarOpen = false" />

        <!-- Content area -->
        <div class="relative flex flex-col flex-1 overflow-y-auto overflow-x-hidden">

            <!-- Site header -->
            <Header :sidebarOpen="sidebarOpen" @toggle-sidebar="sidebarOpen = !sidebarOpen" />

            <main class="grow">
                <div class="px-4 sm:px-6 lg:px-8 py-8 w-full max-w-9xl mx-auto">
                    <h1 class="text-2xl text-gray-800 dark:text-gray-100 font-bold">
                        Transaction Report
                    </h1>
                    <!-- Body -->
                    <div class="p-4 rounded-lg">
                        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 px-4 py-8">
                            <div v-for="transaction in transactions" :key="transaction.title"
                                class="group bg-white dark:bg-gray-200 shadow-md rounded-2xl p-6 hover:shadow-xl transition duration-300">
                                <h3 class="text-lg font-semibold text-gray-800 group-hover:text-slate-600">
                                    {{ transaction.title }}
                                </h3>
                                <p class="text-sm text-gray-500">{{ transaction.price }}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
        </div>
    </div>
</template>

<script setup>

import { ref, onMounted, computed } from 'vue'
import Sidebar from '@/partials/Sidebar.vue'
import Header from '@/partials/Header.vue'
import { API_BASE_URL } from '@/config'
import axios from 'axios'

import { formatValueRupiah } from '@/utils/Utils'

// Icon
import Car from '@/icons/Car.vue'
import SalesPurchases from '@/icons/SalesPurchases.vue'


const token = sessionStorage.getItem('access_token')

const sidebarOpen = ref(false)

const totalPurchase = ref(0)
const totalSale = ref(0)
const totalIncome = ref(0)

const loading = ref(false)

const fetchTotalPurchase = async () => {
    loading.value = true
    try {
        const response = await axios.get(`${API_BASE_URL}/api/sales-purchases/transaction/total-transaction/`, {
            headers: { Authorization: `Bearer ${token}` }
        })
        totalPurchase.value = response.data['total_purchase']
        totalSale.value = response.data['total_sale']
        totalIncome.value = response.data['total_income']
    } catch (error) {
        console.error(`Error fetching: `, error)
    } finally {
        loading.value = false
    }
}

const transactions = computed(() => [
    {
        title: 'Total Purchase',
        price: formatValueRupiah(totalPurchase.value)
    },
    {
        title: 'Total Sales',
        price: formatValueRupiah(totalSale.value)
    },
    {
        title: 'Total Income',
        price: formatValueRupiah(totalIncome.value)
    },
])

onMounted(() => {
    fetchTotalPurchase()
})
</script>