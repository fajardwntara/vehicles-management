<template>
    <div class="flex h-screen overflow-hidden">

        <ModalForm v-model:visible="showModal" :title="isEdit ? `Edit ${activeTab}` : `Add New ${activeTab}`"
            :modelValue="activeTab == 'Motorcycles' ? motorForm : carForm"
            :fields="activeTab == 'Motorcycles' ? motorFields : carFields" :submitText="isEdit ? 'Update' : 'Save'"
            :submitClass="isEdit ? 'bg-yellow-600 hover:bg-yellow-700' : 'bg-slate-600 hover:bg-slate-700'"
            @submit="handleSubmit" />

        <!-- Sidebar -->
        <Sidebar :sidebarOpen="sidebarOpen" @close-sidebar="sidebarOpen = false" />

        <!-- Content area -->
        <div class="relative flex flex-col flex-1 overflow-y-auto overflow-x-hidden">

            <!-- Site header -->
            <Header :sidebarOpen="sidebarOpen" @toggle-sidebar="sidebarOpen = !sidebarOpen" />

            <main class="grow">
                <div class="px-4 sm:px-6 lg:px-8 py-8 w-full max-w-9xl mx-auto">

                    <!-- Dashboard actions -->
                    <div class="sm:flex sm:justify-between sm:items-center mb-8">
                        <!-- Left: Title -->
                        <div class="mb-4 sm:mb-0">
                            <!-- Tabs -->
                            <div class="flex border-b mb-4">
                                <button v-for="tab in tabs" :key="tab" @click="activeTab = tab" :class="[
                                    'px-4 py-2 text-sm font-medium border-b-2 cursor-pointer',
                                    activeTab === tab
                                        ? 'border-slate-700 text-slate-600'
                                        : 'border-transparent text-gray-500 hover:text-slate-900'
                                ]">
                                    {{ tab }}
                                </button>
                            </div>

                            <!-- Title -->
                            <h1 class="text-2xl text-gray-800 dark:text-gray-100 font-bold">
                                {{ activeTab }}
                            </h1>

                        </div>

                    </div>

                    <!-- Body -->
                    <div class="p-4 shadow-xl bg-white rounded-lg" v-if="activeTab === 'Motorcycles' && motors">

                        <ListTable :data="motors" :currentPage="motorCurrentPage" :pageSize="motorPageSize"
                            :totalPages="motorTotalPages" :prevPage="prevMotorPage" :nextPage="nextMotorPage"
                            :columns="['release_year', 'color', 'price', 'stock', 'machine', 'suspenssion_type', 'transmission_type']"
                            :headerColumns="['Release Year', 'Color', 'Price', 'Stock', 'Machine', 'Suspenssion', 'Transmission']">

                            <template #add-button>
                                <button @click="showModalAdd"
                                    class="m-3 py-2 cursor-pointer btn bg-gray-900 text-gray-100 hover:bg-gray-800 dark:bg-slate-700 dark:text-gray-100 dark:hover:bg-white">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24">
                                        <path fill="currentColor" d="M5 13v-1h6V6h1v6h6v1h-6v6h-1v-6z" />
                                    </svg>
                                    <span class="max-xs:sr-only ml-1 text-xs">New</span>
                                </button>
                            </template>

                            <template #button="{ data }">
                                <button @click="openEditModal(data)"
                                    class="bg-slate-100 cursor-pointer hover:bg-slate-200 shadow-xl p-2 text-white rounded-lg mx-1">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24"
                                        class="fill-yellow-700">
                                        <g>
                                            <path
                                                d="m12.593 23.258l-.011.002l-.071.035l-.02.004l-.014-.004l-.071-.035q-.016-.005-.024.005l-.004.01l-.017.428l.005.02l.01.013l.104.074l.015.004l.012-.004l.104-.074l.012-.016l.004-.017l-.017-.427q-.004-.016-.017-.018m.265-.113l-.013.002l-.185.093l-.01.01l-.003.011l.018.43l.005.012l.008.007l.201.093q.019.005.029-.008l.004-.014l-.034-.614q-.005-.018-.02-.022m-.715.002a.02.02 0 0 0-.027.006l-.006.014l-.034.614q.001.018.017.024l.015-.002l.201-.093l.01-.008l.004-.011l.017-.43l-.003-.012l-.01-.01z" />
                                            <path
                                                d="M13 3a1 1 0 0 1 .117 1.993L13 5H5v14h14v-8a1 1 0 0 1 1.993-.117L21 11v8a2 2 0 0 1-1.85 1.995L19 21H5a2 2 0 0 1-1.995-1.85L3 19V5a2 2 0 0 1 1.85-1.995L5 3zm6.243.343a1 1 0 0 1 1.497 1.32l-.083.095l-9.9 9.899a1 1 0 0 1-1.497-1.32l.083-.094z" />
                                        </g>
                                    </svg>
                                </button>

                                <button @click="deleteMotor(data.id)"
                                    class="shadow-xl bg-slate-100 cursor-pointer hover:bg-slate-200 p-2 text-white rounded-lg mx-1">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24"
                                        class="fill-red-500">
                                        <path
                                            d="M2 5.27L3.28 4L5 5.72l.28.28l1 1l2 2L16 16.72l2 2l2 2L18.73 22l-1.46-1.46c-.34.29-.77.46-1.27.46H8c-1.1 0-2-.9-2-2V9.27zM8 19h7.73L8 11.27zM18 7v9.18l-2-2V9h-5.18l-2-2zm-2.5-3H19v2H7.82l-2-2H8.5l1-1h5z" />
                                    </svg>

                                </button>
                            </template>

                        </ListTable>

                    </div>

                    <!-- Car -->
                    <div v-else-if="activeTab === 'Cars'" class="p-4 shadow-xl bg-white rounded-lg">
                        <ListTable :data="cars" :currentPage="carCurrentPage" :pageSize="carPageSize" :totalPages="carTotalPages"
                            :prevPage="prevCarPage" :nextPage="nextCarPage"
                            :columns="['release_year', 'color', 'price', 'stock', 'machine', 'passenger_cap', 'type']"
                            :headerColumns="['Release Year', 'Color', 'Price', 'Stock', 'Machine', 'Passenger Capacities', 'Type']">

                            <template #add-button>
                                <button @click="showModalAdd"
                                    class="m-3 py-2 cursor-pointer btn bg-gray-900 text-gray-100 hover:bg-gray-800 dark:bg-slate-700 dark:text-gray-100 dark:hover:bg-white">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24">
                                        <path fill="currentColor" d="M5 13v-1h6V6h1v6h6v1h-6v6h-1v-6z" />
                                    </svg>
                                    <span class="max-xs:sr-only ml-1 text-xs">New</span>
                                </button>
                            </template>

                            <template #button="{ data }">
                                <button @click="openEditModal(data)"
                                    class="bg-slate-100 cursor-pointer hover:bg-slate-200 shadow-xl p-2 text-white rounded-lg mx-1">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24"
                                        class="fill-yellow-700">
                                        <g>
                                            <path
                                                d="m12.593 23.258l-.011.002l-.071.035l-.02.004l-.014-.004l-.071-.035q-.016-.005-.024.005l-.004.01l-.017.428l.005.02l.01.013l.104.074l.015.004l.012-.004l.104-.074l.012-.016l.004-.017l-.017-.427q-.004-.016-.017-.018m.265-.113l-.013.002l-.185.093l-.01.01l-.003.011l.018.43l.005.012l.008.007l.201.093q.019.005.029-.008l.004-.014l-.034-.614q-.005-.018-.02-.022m-.715.002a.02.02 0 0 0-.027.006l-.006.014l-.034.614q.001.018.017.024l.015-.002l.201-.093l.01-.008l.004-.011l.017-.43l-.003-.012l-.01-.01z" />
                                            <path
                                                d="M13 3a1 1 0 0 1 .117 1.993L13 5H5v14h14v-8a1 1 0 0 1 1.993-.117L21 11v8a2 2 0 0 1-1.85 1.995L19 21H5a2 2 0 0 1-1.995-1.85L3 19V5a2 2 0 0 1 1.85-1.995L5 3zm6.243.343a1 1 0 0 1 1.497 1.32l-.083.095l-9.9 9.899a1 1 0 0 1-1.497-1.32l.083-.094z" />
                                        </g>
                                    </svg>
                                </button>

                                <button @click="deleteCar(data.id)"
                                    class="shadow-xl bg-slate-100 cursor-pointer hover:bg-slate-200 p-2 text-white rounded-lg mx-1">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24"
                                        class="fill-red-500">
                                        <path
                                            d="M2 5.27L3.28 4L5 5.72l.28.28l1 1l2 2L16 16.72l2 2l2 2L18.73 22l-1.46-1.46c-.34.29-.77.46-1.27.46H8c-1.1 0-2-.9-2-2V9.27zM8 19h7.73L8 11.27zM18 7v9.18l-2-2V9h-5.18l-2-2zm-2.5-3H19v2H7.82l-2-2H8.5l1-1h5z" />
                                    </svg>

                                </button>
                            </template>

                        </ListTable>

                    </div>

                    <Spinner v-if="loading" />

                </div>
            </main>


        </div>

    </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'

import Sidebar from '@/partials/Sidebar.vue'
import Header from '@/partials/Header.vue'
import ListTable from '@/components/Helpers/ListTable.vue'
import { API_BASE_URL } from '@/config'
import ModalForm from '@/components/Helpers/ModalForm.vue'

// Setup
const token = sessionStorage.getItem('access_token')
const tabs = ['Motorcycles', 'Cars']
const activeTab = ref('Motorcycles')

// General Setup
const sidebarOpen = ref(false)
const loading = ref(false)
const showModal = ref(false)
const isEdit = ref(false)

// Motor variables
const motorCurrentPage = ref(1)
const motorTotalPages = ref(1)
const motorPageSize = 5
const motors = ref([])
const defaultMotorForm = ref({
    release_year: 0,
    color: '',
    price: 0,
    stock: 0,
    machine: '',
    suspenssion_type: '',
    transmission_type: '',
})
const motorForm = ref({ ...defaultMotorForm.value })
const motorFields = [
    { model: 'release_year', label: 'Released Year', type: 'number', placeholder: 'Must be > 1900' },
    { model: 'color', label: 'Color' },
    { model: 'price', label: 'Price', type: 'number' },
    { model: 'stock', label: 'Stock', type: 'number' },
    { model: 'machine', label: 'Machine' },
    { model: 'suspenssion_type', label: 'Suspenssion Type' },
    { model: 'transmission_type', label: 'Transmission Type' }
]
const prevMotorPage = () => {
  if (motorCurrentPage.value > 1) motorCurrentPage.value--
}

const nextMotorPage = () => {
  if (motorCurrentPage.value < motorTotalPages.value) motorCurrentPage.value++
}

// Cars variables
const carCurrentPage = ref(1)
const carTotalPages = ref(1)
const carPageSize = 5
const cars = ref([])
const defaultCarForm = ref({
    release_year: 0,
    color: '',
    price: 0,
    stock: 0,
    machine: '',
    suspenssion_type: '',
    transmission_type: '',
})
const carForm = ref({ ...defaultCarForm.value })
const carFields = [
    { model: 'release_year', label: 'Released Year', type: 'number', placeholder: 'Must be > 1900' },
    { model: 'color', label: 'Color' },
    { model: 'price', label: 'Price', type: 'number' },
    { model: 'stock', label: 'Stock', type: 'number' },
    { model: 'machine', label: 'Machine' },
    { model: 'passenger_cap', label: 'Passenger Capacities' },
    { model: 'type', label: 'Type' }
]

const prevCarPage = () => {
  if (carCurrentPage.value > 1) carCurrentPage.value--
}

const nextCarPage = () => {
  if (carCurrentPage.value < carTotalPages.value) carCurrentPage.value++
}

/* ================================ */
const handleSubmit = (data) => {
    console.log("active Tab : ", activeTab)
    if (isEdit.value) {
        if (activeTab.value == "Motorcycles") {
            editMotor(data)
        } else {
            editCar(data)
        }
    } else {
        if (activeTab.value == "Motorcycles") {
            addMotor(data)
        } else {
            addCar(data)
        }
    }

}

// Clear Form
const clearForm = () => {
    motorForm.value = { ...defaultMotorForm.value }
}

const openEditModal = (data) => {
    isEdit.value = true
    if (activeTab == 'Motorcycles') {
        motorForm.value = { ...data }
    } else {
        carForm.value = { ...data }
    }
    showModal.value = true
}

const showModalAdd = () => {
    showModal.value = true
    clearForm()
}

/* ========== Functions =========== */
const fetchData = async (vehicleType, page, size, targetListRef, totalPageRef, targetPageSize) => {
    loading.value = true
    try {
        const response = await axios.get(`${API_BASE_URL}/api/vehicles/${vehicleType}/lists`, {
            params: { page, size },
            headers: { Authorization: `Bearer ${token}` }
        })
        targetListRef.value = response.data
        totalPageRef.value = Math.ceil(response.data.length / targetPageSize)
    } catch (error) {
        console.error(`Error fetching ${vehicleType}: `, error)
    } finally {
        loading.value = false
    }
}

const addData = async (vehicleType, data, fetchFunc) => {
    if (!token) {
        alert('Unauthorized: No access token found.')
        return
    }

    try {
        await axios.post(`${API_BASE_URL}/api/vehicles/${vehicleType}/create`, data, {
            headers: {
                Authorization: `Bearer ${token}`,
                'Content-Type': 'application/json',
            }
        })
        alert('Successfully added new data.')
        fetchFunc()
    } catch (error) {
        alert('Failed to add new data')
        console.error(error)
    }
}

const editData = async (vehicleType, data, fetchFunc) => {
    if (!token) {
        alert('Unauthorized: No access token found.')
        return
    }

    try {
        await axios.put(`${API_BASE_URL}/api/vehicles/${vehicleType}/update/${data.id}/`, data, {
            headers: {
                Authorization: `Bearer ${token}`,
                'Content-Type': 'application/json',
            }
        })
        alert('Data updated successfully.')
        fetchFunc()
    } catch (error) {
        alert('Failed to update data')
        console.error(error)
    }
}

const deleteData = async (vehicleType, id, fetchFunc) => {
    const confirmed = confirm('Are you sure you want to delete this data?')
    if (!confirmed) return

    if (!token) {
        alert('Unauthorized: No access token found.')
        return
    }

    try {
        await axios.delete(`${API_BASE_URL}/api/vehicles/${vehicleType}/delete/${id}/`, {
            headers: { Authorization: `Bearer ${token}` }
        })
        alert('Data deleted successfully.')
        fetchFunc()
    } catch (error) {
        alert('Failed to delete data')
        console.error(error)
    }
}

/* Motors */
const fetchMotors = () => fetchData('motorcycle', motorCurrentPage.value, motorPageSize, motors, motorTotalPages, motorPageSize)

const addMotor = (data) => addData('motorcycle', data, fetchMotors)

const editMotor = (data) => editData('motorcycle', data, fetchMotors)

const deleteMotor = (id) => deleteData('motorcycle', id, fetchMotors)

/* Cars */
const fetchCars = () => fetchData('car', carCurrentPage.value, carPageSize, cars, carTotalPages, carPageSize)

const addCar = (data) => addData('car', data, fetchCars)

const editCar = (data) => editData('car', data, fetchCars)

const deleteCar = (id) => deleteData('car', id, fetchCars)


/* Configs */
onMounted(() => {
  fetchMotors()
  fetchCars()
})

watch(motorCurrentPage, () => {
  fetchMotors()
})

watch(carCurrentPage, () => {
  fetchCars()
})
</script>