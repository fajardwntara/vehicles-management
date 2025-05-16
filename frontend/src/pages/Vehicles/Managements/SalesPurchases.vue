<template>
    <div class="flex h-screen overflow-hidden">

        <!-- Custom Modal -->
        <!-- <transition name="fade">
            <div v-if="showModal"
                class="fixed inset-0 z-50 flex items-center justify-center backdrop-blur-sm bg-black/20">
                <div class="bg-white dark:bg-gray-900 rounded-2xl shadow-2xl w-full max-w-lg p-6 animate-fade-in">

                    <h2 class="text-xs sm:text-2xl font-bold text-gray-800 dark:text-white mb-6">
                        Add New {{ activeTab }}
                    </h2>

                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                        <div class="block" v-for="field in purchaseFields" :key="field.model">
                            <span class="text-xs">{{ field.label }}</span>
                            <input v-model="purchaseForm[field.model]" :type="field.type || 'text'"
                                :placeholder="field.placeholder || field.label" :disabled="field.disabled"
                                class="text-xs w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-slate-600 dark:bg-gray-800 dark:text-white disabled:bg-slate-200 dark:disabled:bg-gray-600" />
                        </div>
                    </div>

                    <div class="mt-6 flex justify-end space-x-4">
                        <button @click="onCancel"
                            class="cursor-pointer text-xs mx-2 px-4 py-2 rounded-lg bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:text-white">
                            Cancel
                        </button>
                        <button @click="onSubmit" class="cursor-pointer text-xs px-4 py-2 rounded-lg text-white"
                            :class="submitClass">
                            {{ submitText }}
                        </button>
                    </div>

                </div>
            </div>
        </transition> -->

        <ModalForm v-model:visible="showModal" :title="isEdit ? `Edit ${activeTab}` : `Add New ${activeTab}`"
            :modelValue="activeTab == 'Sales' ? saleForm : purchaseForm"
            :fields="activeTab == 'Sales' ? saleFields : purchaseFields" :submitText="isEdit ? 'Update' : 'Save'"
            :submitClass="isEdit ? 'bg-yellow-600 hover:bg-yellow-700' : 'bg-slate-600 hover:bg-slate-700'"
            @submit="handleSubmit">

            <template #add-input>
                <div class="block">
                    <span class="text-xs">Vehicle</span>
                    <input v-model="purchaseForm.vehicle" placeholder="Choose One" class="text-xs w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-slate-600 dark:bg-gray-800 dark:text-white disabled:bg-slate-200 dark:disabled:bg-gray-600" />
                </div>
            </template>
        </ModalForm>


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
                    <div class="p-4 shadow-xl bg-white rounded-lg" v-if="activeTab === 'Sales' && sales">

                        <ListTable :data="sales" :currentPage="motorCurrentPage" :pageSize="motorPageSize"
                            :totalPages="motorTotalPages" :prevPage="prevMotorPage" :nextPage="nextMotorPage"
                            :columns="['vehicle_type', 'release_year', 'machine', 'price', 'purchase_date', 'qty', 'status']"
                            :headerColumns="['Vehicle Type', 'Release Year', 'Machine', 'Price', 'Purchase Date', 'Quantity', 'Status']">

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

                    <!-- Purchases -->
                    <div v-else-if="activeTab === 'Purchases'" class="p-4 shadow-xl bg-white rounded-lg">
                        <ListTable :data="purchases" :currentPage="purchaseCurrentPage" :pageSize="purchasePageSize"
                            :totalPages="purchaseTotalPages" :prevPage="prevPurchasePage" :nextPage="nextPurchasePage"
                            :columns="['vehicle_type', 'release_year', 'machine', 'purchase_price', 'purchase_date', 'qty', 'status']"
                            :headerColumns="['Vehicle Type', 'Release Year', 'Machine', 'Purchase Price', 'Purchase Date', 'Quantity', 'Status']">

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
const tabs = ['Sales', 'Purchases']
const activeTab = ref('Sales')

// General Setup
const sidebarOpen = ref(false)
const loading = ref(false)
const showModal = ref(false)
const isEdit = ref(false)

// Motor variables
const saleCurrentPage = ref(1)
const saleTotalPages = ref(1)
const salePageSize = 5
const sales = ref([])
const defaultSaleForm = ref({
    release_year: 0,
    color: '',
    price: 0,
    stock: 0,
    machine: '',
    suspenssion_type: '',
    transmission_type: '',
})
const saleForm = ref({ ...defaultSaleForm.value })
const saleFields = [
    { model: 'release_year', label: 'Released Year', type: 'number', placeholder: 'Must be > 1900' },
    { model: 'color', label: 'Color' },
    { model: 'price', label: 'Price', type: 'number' },
    { model: 'stock', label: 'Stock', type: 'number' },
    { model: 'machine', label: 'Machine' },
    { model: 'suspenssion_type', label: 'Suspenssion Type' },
    { model: 'transmission_type', label: 'Transmission Type' }
]
const prevSalePage = () => {
    if (saleCurrentPage.value > 1) saleCurrentPage.value--
}

const nextSalePage = () => {
    if (saleCurrentPage.value < saleTotalPages.value) saleCurrentPage.value++
}

// Cars variables
const purchaseCurrentPage = ref(1)
const purchaseTotalPages = ref(1)
const purchasePageSize = 5
const purchases = ref([])
const defaultPurchaseForm = ref({
    purchase_date: '',
    seller_name: '',
    seller_phone: '',
    purchase_price: 0,
    qty: 0
})
const purchaseForm = ref({ ...defaultPurchaseForm.value })
const purchaseFields = [
    // { model: 'vehicle', label: 'Vehicle', placeholder: 'Choose one' },
    { model: 'purchase_date', label: 'Purchase Date', placeholder: "YYYY-MM-DD" },
    { model: 'seller_name', label: 'Seller Name' },
    { model: 'seller_phone', label: 'Seller Phone' },
    { model: 'purchase_price', label: 'Price', type: "Number" },
    { model: 'qty', label: 'Quantity', type: "Number" },
]

const prevPurchasePage = () => {
    if (purchaseCurrentPage.value > 1) purchaseCurrentPage.value--
}

const nextPurchasePage = () => {
    if (purchaseCurrentPage.value < purchaseTotalPages.value) purchaseCurrentPage.value++
}

/* ================================ */
const handleSubmit = (data) => {
    console.log("active Tab : ", activeTab)
    if (isEdit.value) {
        if (activeTab.value == "Sales") {
            editSale(data)
        } else {
            editPurchase(data)
        }
    } else {
        if (activeTab.value == "Purchases") {
            addSale(data)
        } else {
            addPurchase(data)
        }
    }

}

// Clear Form
const clearForm = () => {
    saleForm.value = { ...defaultSaleForm.value }
}

const openEditModal = (data) => {
    isEdit.value = true
    if (activeTab.value == 'Sales') {
        saleForm.value = { ...data }
    } else {
        purchaseForm.value = { ...data }
    }
    showModal.value = true
}

const showModalAdd = () => {
    showModal.value = true
    clearForm()
}

/* ========== Functions =========== */
const fetchData = async (type, page, size, targetListRef, totalPageRef, targetPageSize) => {
    loading.value = true
    try {
        const response = await axios.get(`${API_BASE_URL}/api/sales-purchases/${type}/lists`, {
            params: { page, size },
            headers: { Authorization: `Bearer ${token}` }
        })
        targetListRef.value = response.data
        totalPageRef.value = Math.ceil(response.data.length / targetPageSize)
    } catch (error) {
        console.error(`Error fetching ${type}: `, error)
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
// const fetchMotors = () => fetchData('motorcycle', motorCurrentPage.value, motorPageSize, motors, motorTotalPages, motorPageSize)

// const addMotor = (data) => addData('motorcycle', data, fetchMotors)

// const editMotor = (data) => editData('motorcycle', data, fetchMotors)

// const deleteMotor = (id) => deleteData('motorcycle', id, fetchMotors)

// /* Purchase */
const fetchPurchases = () => fetchData('purchases', purchaseCurrentPage.value, purchasePageSize, purchases, purchaseTotalPages, purchasePageSize)

// const addCar = (data) => addData('car', data, fetchCars)

// const editCar = (data) => editData('car', data, fetchCars)

// const deleteCar = (id) => deleteData('car', id, fetchCars)


/* Configs */
onMounted(() => {
    //   fetchMotors()
    fetchPurchases()
})

// watch(motorCurrentPage, () => {
//   fetchMotors()
// })

watch(purchaseCurrentPage, () => {
    fetchPurchases()
})

</script>