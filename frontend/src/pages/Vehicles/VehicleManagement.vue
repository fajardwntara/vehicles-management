<template>
    <div class="flex h-screen overflow-hidden">

        <Sidebar :sidebarOpen="sidebarOpen" @close-sidebar="sidebarOpen = false" />

        <!-- Content area -->
        <div class="relative flex flex-col flex-1 overflow-y-auto overflow-x-hidden">

            <!-- Site header -->
            <Header :sidebarOpen="sidebarOpen" @toggle-sidebar="sidebarOpen = !sidebarOpen" />

            <main class="grow">
                <div class="px-4 sm:px-6 lg:px-8 py-8 w-full max-w-9xl mx-auto">

                    <!-- Body -->
                    <div class="p-4 rounded-lg">
                        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 px-4 py-8">
                            <div v-for="menu in menus" :key="menu.title" @click="navigateTo(menu.path)"
                                class="cursor-pointer group bg-white dark:bg-gray-200 shadow-md rounded-2xl p-6 hover:shadow-xl transition duration-300">
                                <div
                                    class="flex items-center justify-center w-14 h-14 rounded-full bg-slate-100 dark:bg-gray-800 mb-4">
                                    <component :is="menu.icon" class="w-6 h-6 text-slate-700 dark:text-white" />
                                </div>
                                <h3
                                    class="text-lg font-semibold text-gray-800 group-hover:text-slate-600">
                                    {{ menu.title }}
                                </h3>
                                <p class="text-sm text-gray-500">{{ menu.description }}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
        </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import Sidebar from '@/partials/Sidebar.vue'
import Header from '@/partials/Header.vue'

// Icon
import Car from '@/icons/Car.vue'
import SalesPurchases from '@/icons/SalesPurchases.vue'

const router = useRouter()

const sidebarOpen = ref(false)

const menus = [
    {
        title: 'Vehicles',
        description: 'Vehicle management stock and prices',
        path: '/vehicle-management/motor',
        icon: Car
    },
    {
        title: 'Sales & Purchases',
        description: 'Vehicle transactions',
        path: '/vehicle-management/sales-purchases',
        icon: SalesPurchases
    },
    {
        title: 'Reports',
        description: 'Financial and activity reports',
        path: '/reports',
    }
]

const navigateTo = (path) => {
    router.push(path)
}

</script>