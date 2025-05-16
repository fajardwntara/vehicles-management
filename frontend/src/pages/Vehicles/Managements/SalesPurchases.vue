<template>
    <div class="flex h-screen overflow-hidden">
        <!-- Custom Modal for Vehicle -->
        <transition name="fade">
            <div v-if="vehicleModal"
                class="fixed inset-0 z-50 flex items-center justify-center backdrop-blur-sm bg-black/20">
                <div class="bg-white dark:bg-gray-900 rounded-2xl shadow-2xl w-full max-w-3xl p-6 animate-fade-in">
                    <!-- Header Modal -->
                    <div class="flex items-center justify-between mb-4">
                        <h1 class="text-base font-semibold text-gray-800 dark:text-white">
                            Choose the Vehicle
                        </h1>
                        <button @click="closeVehicleModal" class="text-gray-500 hover:text-slate-600 text-lg font-bold">
                            &times;
                        </button>
                    </div>

                    <!-- Scrollable Content -->
                    <div class="overflow-y-auto max-h-[60vh]">
                        <!-- Table Header -->
                        <div
                            class="text-center grid grid-cols-5 gap-2 text-xs font-semibold text-slate-800 dark:text-gray-300 border-b pb-2 mb-2">
                            <div>Type</div>
                            <div>Name</div>
                            <div>Machine</div>
                            <div>Year</div>
                            <div>Price</div>
                        </div>

                        <!-- Table Rows -->
                        <div v-for="vehicle in vehicleData" :key="vehicle.id" @click="selectVehicle(vehicle)"
                            class="text-center grid grid-cols-5 gap-2 text-xs items-center border rounded-lg px-4 py-2 mb-2 cursor-pointer hover:bg-gray-100 dark:hover:bg-gray-800 transition">
                            <div class="text-gray-600 dark:text-white">{{ vehicle.vehicle_type }}</div>
                            <div class="text-gray-600 dark:text-white">{{ vehicle.name }}</div>
                            <div class="text-gray-600 dark:text-white">{{ vehicle.machine }}</div>
                            <div class="text-gray-600 dark:text-white">{{ vehicle.release_year }}</div>
                            <div class="text-gray-600 dark:text-white">{{ vehicle.price }}</div>
                        </div>
                    </div>
                </div>
            </div>
        </transition>

        <ModalForm v-model:visible="showModal" v-if="activeTab == 'Sales'" v-model:modelValue="saleForm"
            :title="isEdit ? `Edit Sales` : 'Add New Sales'" :fields="saleFields"
            :submitText="isEdit ? 'Update' : 'Save'"
            :submitClass="isEdit ? 'bg-yellow-600 hover:bg-yellow-700' : 'bg-slate-600 hover:bg-slate-700'"
            @submit="handleSubmit">
            <template #add-input>
                <div class="block">
                    <button @click="showVehicleModal"
                        class="cursor-pointer text-xs bg-slate-700 text-white px-4 py-2 rounded-lg hover:bg-slate-800 transition">
                        Choose Vehicle
                    </button>

                    <div class="mt-2 text-xs text-gray-700 dark:text-white">
                        <div class="font-medium">Selected:</div>
                        <div>
                            <span v-if="selectedVehicleLabel">{{ selectedVehicleLabel }}</span>
                            <span v-else class="italic text-gray-400">Not selected yet</span>
                        </div>
                    </div>
                </div>
            </template>
        </ModalForm>

        <ModalForm v-model:visible="showModal" v-else v-model:modelValue="purchaseForm"
            :title="isEdit ? `Edit Purchase` : 'Add New Purchase'" :fields="purchaseFields"
            :submitText="isEdit ? 'Update' : 'Save'"
            :submitClass="isEdit ? 'bg-yellow-600 hover:bg-yellow-700' : 'bg-slate-600 hover:bg-slate-700'"
            @submit="handleSubmit">
            <template #add-input>
                <div class="block">
                    <button @click="showVehicleModal"
                        class="cursor-pointer text-xs bg-slate-700 text-white px-4 py-2 rounded-lg hover:bg-slate-800 transition">
                        Choose Vehicle
                    </button>

                    <div class="mt-2 text-xs text-gray-700 dark:text-white">
                        <div class="font-medium">Selected:</div>
                        <div>
                            <span v-if="selectedVehicleLabel">{{ selectedVehicleLabel }}</span>
                            <span v-else class="italic text-gray-400">Not selected yet</span>
                        </div>
                    </div>
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

                        <!-- Sales -->
                        <ListTable :data="sales" :currentPage="saleCurrentPage" :pageSize="salePageSize"
                            :totalPages="saleTotalPages" :prevPage="prevSalePage" :nextPage="nextSalePage"
                            :columns="['vehicle_type', 'name', 'release_year', 'machine', 'price', 'sale_date', 'qty', 'status']"
                            :headerColumns="['Type', 'Name', 'Release Year', 'Machine', 'Price', 'Sale Date', 'Quantity', 'Status']">

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
                                <button @click="confirmSale(data)"
                                    class="bg-slate-100 cursor-pointer hover:bg-slate-200 shadow-xl p-2 text-white rounded-lg mx-1">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24">
                                        <g fill="none" stroke="#0ed700" stroke-linecap="round" stroke-linejoin="round"
                                            stroke-width="2">
                                            <path
                                                d="M3 12c0 -4.97 4.03 -9 9 -9c4.97 0 9 4.03 9 9c0 4.97 -4.03 9 -9 9c-4.97 0 -9 -4.03 -9 -9Z" />
                                            <path d="M8 12l3 3l5 -5" />
                                        </g>
                                    </svg>
                                </button>

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

                                <button @click="cancelSale(data)"
                                    class="shadow-xl bg-slate-100 cursor-pointer hover:bg-slate-200 p-2 text-white rounded-lg mx-1">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 48 48">
                                        <path fill="#d50000"
                                            d="M24 6C14.1 6 6 14.1 6 24s8.1 18 18 18s18-8.1 18-18S33.9 6 24 6m0 4c3.1 0 6 1.1 8.4 2.8L12.8 32.4C11.1 30 10 27.1 10 24c0-7.7 6.3-14 14-14m0 28c-3.1 0-6-1.1-8.4-2.8l19.6-19.6C36.9 18 38 20.9 38 24c0 7.7-6.3 14-14 14" />
                                    </svg>
                                </button>

                                <button @click="deleteSale(data)"
                                    class="shadow-xl bg-slate-100 cursor-pointer hover:bg-slate-200 p-2 text-white rounded-lg mx-1">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24">
                                        <path fill="none" stroke="#e30000" stroke-linecap="round"
                                            stroke-linejoin="round" stroke-width="1.5"
                                            d="m18 9l-.84 8.398c-.127 1.273-.19 1.909-.48 2.39a2.5 2.5 0 0 1-1.075.973C15.098 21 14.46 21 13.18 21h-2.36c-1.279 0-1.918 0-2.425-.24a2.5 2.5 0 0 1-1.076-.973c-.288-.48-.352-1.116-.48-2.389L6 9m7.5 6.5v-5m-3 5v-5m-6-4h4.615m0 0l.386-2.672c.112-.486.516-.828.98-.828h3.038c.464 0 .867.342.98.828l.386 2.672m-5.77 0h5.77m0 0H19.5" />
                                    </svg>
                                </button>
                            </template>

                        </ListTable>

                    </div>

                    <!-- Purchases -->
                    <div v-else-if="activeTab === 'Purchases'" class="p-4 shadow-xl bg-white rounded-lg">
                        <ListTable :data="purchases" :currentPage="purchaseCurrentPage" :pageSize="purchasePageSize"
                            :totalPages="purchaseTotalPages" :prevPage="prevPurchasePage" :nextPage="nextPurchasePage"
                            :columns="['vehicle_type', 'name', 'release_year', 'machine', 'purchase_price', 'purchase_date', 'qty', 'status']"
                            :headerColumns="['Type', 'Name', 'Release Year', 'Machine', 'Purchase Price', 'Purchase Date', 'Quantity', 'Status']">

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
                                <button @click="confirmPurchase(data)"
                                    class="bg-slate-100 cursor-pointer hover:bg-slate-200 shadow-xl p-2 text-white rounded-lg mx-1">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24">
                                        <g fill="none" stroke="#0ed700" stroke-linecap="round" stroke-linejoin="round"
                                            stroke-width="2">
                                            <path
                                                d="M3 12c0 -4.97 4.03 -9 9 -9c4.97 0 9 4.03 9 9c0 4.97 -4.03 9 -9 9c-4.97 0 -9 -4.03 -9 -9Z" />
                                            <path d="M8 12l3 3l5 -5" />
                                        </g>
                                    </svg>
                                </button>

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

                                <button @click="cancelPurchase(data)"
                                    class="shadow-xl bg-slate-100 cursor-pointer hover:bg-slate-200 p-2 text-white rounded-lg mx-1">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 48 48">
                                        <path fill="#d50000"
                                            d="M24 6C14.1 6 6 14.1 6 24s8.1 18 18 18s18-8.1 18-18S33.9 6 24 6m0 4c3.1 0 6 1.1 8.4 2.8L12.8 32.4C11.1 30 10 27.1 10 24c0-7.7 6.3-14 14-14m0 28c-3.1 0-6-1.1-8.4-2.8l19.6-19.6C36.9 18 38 20.9 38 24c0 7.7-6.3 14-14 14" />
                                    </svg>
                                </button>

                                <button @click="deletePurchase(data)"
                                    class="shadow-xl bg-slate-100 cursor-pointer hover:bg-slate-200 p-2 text-white rounded-lg mx-1">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24">
                                        <path fill="none" stroke="#e30000" stroke-linecap="round"
                                            stroke-linejoin="round" stroke-width="1.5"
                                            d="m18 9l-.84 8.398c-.127 1.273-.19 1.909-.48 2.39a2.5 2.5 0 0 1-1.075.973C15.098 21 14.46 21 13.18 21h-2.36c-1.279 0-1.918 0-2.425-.24a2.5 2.5 0 0 1-1.076-.973c-.288-.48-.352-1.116-.48-2.389L6 9m7.5 6.5v-5m-3 5v-5m-6-4h4.615m0 0l.386-2.672c.112-.486.516-.828.98-.828h3.038c.464 0 .867.342.98.828l.386 2.672m-5.77 0h5.77m0 0H19.5" />
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
import moment from 'moment'
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
const vehicleModal = ref(false)
const vehicleData = ref([])
const selectedVehicleLabel = ref('')
const selectVehicleID = ref(-1)

const fetchVehicles = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/api/vehicles/lists`, {
            headers: { Authorization: `Bearer ${token}` }
        })
        vehicleData.value = response.data
    } catch (error) {
        console.error(`Error fetching ${type}: `, error)
    } finally {
        loading.value = false
    }
}

const showVehicleModal = () => {
    showModal.value = false
    vehicleModal.value = true
}

const closeVehicleModal = () => {
    showModal.value = true
    vehicleModal.value = false
}

function selectVehicle(vehicle) {
    selectVehicleID.value = vehicle.id
    selectedVehicleLabel.value = `${vehicle.vehicle_type} - ${vehicle.name} - ${vehicle.release_year}`
    showModal.value = true
}

const showModalAdd = () => {
    showModal.value = true
    clearForm()
}


// Motor variables
const saleCurrentPage = ref(1)
const saleTotalPages = ref(1)
const salePageSize = 5
const sales = ref([])
const defaultSaleForm = ref({
    sale_date: moment().format('YYYY-MM-DDTHH:mm'),
    buyer_name: '',
    buyer_phone: '',
    qty: 0
})
const saleForm = ref({ ...defaultSaleForm.value })
const saleFields = [
    { model: 'sale_date', label: 'Purchase Date', placeholder: "YYYY-MM-DD", type: "Date" },
    { model: 'buyer_name', label: 'Seller Name' },
    { model: 'buyer_phone', label: 'Seller Phone' },
    { model: 'qty', label: 'Quantity', type: "Number" },
]
const prevSalePage = () => {
    if (saleCurrentPage.value > 1) saleCurrentPage.value--
}

const nextSalePage = () => {
    if (saleCurrentPage.value < saleTotalPages.value) saleCurrentPage.value++
}

// Purchase variables
const purchaseCurrentPage = ref(1)
const purchaseTotalPages = ref(1)
const purchasePageSize = 5
const purchases = ref([])
const defaultPurchaseForm = ref({
    purchase_date: moment().format('YYYY-MM-DDTHH:mm'),
    seller_name: '',
    seller_phone: '',
    purchase_price: 0,
    qty: 0
})
const purchaseForm = ref({ ...defaultPurchaseForm.value })
const purchaseFields = [
    { model: 'purchase_date', label: 'Purchase Date', placeholder: "YYYY-MM-DD", type: "Date" },
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
    if (isEdit.value) {
        if (activeTab.value == "Sales") {
            editSale(data)
        } else {
            editPurchase(data)
        }
    } else {
        if (activeTab.value == "Sales") {
            addSale(data)
        } else {
            addPurchase(data)
        }
    }

}

// Clear Form
const clearForm = () => {
    saleForm.value = { ...defaultSaleForm.value }
    purchaseForm.value = { ...defaultPurchaseForm.value }
    selectedVehicleLabel.value = ''
}

const openEditModal = (data) => {

    if (data.status == 'confirm') {
        alert('You can only cancel the data')
        return
    } else if (data.status == 'cancel') {
        alert('Data has already been canceled')
        return
    }

    const keys = Object.keys(defaultPurchaseForm.value)
    const dataUpdated = {}

    keys.forEach(key => {
        dataUpdated[key] = key === 'purchase_date'
            ? moment(data[key]).format('YYYY-MM-DDTHH:mm')
            : data[key]
    })

    if (activeTab.value === 'Sales') {
        selectedVehicleLabel.value = `${data.vehicle_type} - ${data.name} - ${data.release_year}`
        saleForm.value = { ...data }
    } else {
        selectedVehicleLabel.value = `${data.vehicle_type} - ${data.name} - ${data.release_year}`
        purchaseForm.value = { ...data }
    }

    isEdit.value = true
    showModal.value = true
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
        vehicleModal.value = false
    } catch (error) {
        console.error(`Error fetching ${type}: `, error)
    } finally {
        loading.value = false
    }
}

const addData = async (type, data, fetchFunc) => {
    if (!token) {
        alert('Unauthorized: No access token found.')
        return
    }
    data.vehicle = selectVehicleID.value
    try {
        await axios.post(`${API_BASE_URL}/api/sales-purchases/${type}/create/`, data, {
            headers: {
                Authorization: `Bearer ${token}`,
                'Content-Type': 'application/json',
            }
        })
        alert('Successfully added new data.')
        clearForm()
        fetchFunc()
    } catch (error) {
        alert('Failed to add new data')
        console.error(error)
    }
}

const editData = async (type, data, fetchFunc) => {
    if (!token) {
        alert('Unauthorized: No access token found.')
        return
    }

    let updatedData = {}

    if (type == 'sales') {
        updatedData = {
            "vehicle": selectVehicleID.value,
            "sale_date": data.sale_date,
            "buyer_phone": data.buyer_phone,
            "buyer_name": data.buyer_name,
            "status": data.status
        }
    } else {
        updatedData = {
            "vehicle": selectVehicleID.value,
            "purchase_date": data.purchase_date,
            "seller_phone": data.seller_phone,
            "seller_name": data.seller_name,
            "purchase_price": data.purchase_price,
            "status": data.status
        }
    }

    try {
        await axios.put(`${API_BASE_URL}/api/sales-purchases/${type}/update/${data.id}/`, updatedData, {
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

const confirmData = async (type, data, fetchFunc) => {
    if (!token) {
        alert('Unauthorized: No access token found.')
        return
    }

    if (data.status == 'confirm') {
        alert("The status is confirm.\nYou can only cancel the data")
        return
    } else if (data.status == 'cancel') {
        alert("The data has already been canceled.")
        return
    }

    const confirmed = confirm('Are you sure you want to confirm this data?')
    if (!confirmed) return

    let updatedData = {}

    if (type == 'sales') {
        updatedData = {
            "vehicle": data.vehicle_id,
            "sale_date": data.sale_date,
            "buyer_phone": data.buyer_phone,
            "buyer_name": data.buyer_name,
            "status": 'confirm'
        }
    } else {
        updatedData = {
            "vehicle": data.vehicle_id,
            "purchase_date": data.purchase_date,
            "seller_phone": data.seller_phone,
            "seller_name": data.seller_name,
            "purchase_price": data.purchase_price,
            "status": 'confirm'
        }
    }

    try {
        await axios.put(`${API_BASE_URL}/api/sales-purchases/${type}/update/${data.id}/`, updatedData, {
            headers: {
                Authorization: `Bearer ${token}`,
                'Content-Type': 'application/json',
            }
        })
        alert('Data updated successfully.')
        fetchFunc()
    } catch (error) {
        alert('Failed to confirm data.\nMake sure your quantity is not ouf of stock\nYou can purchase for adding the stock with the product you selected.')
        console.error(error)
    }
}

const cancelData = async (type, data, fetchFunc) => {
    if (!token) {
        alert('Unauthorized: No access token found.')
        return
    }

    if (data.status == 'draft') {
        alert("You need to confirm the data.")
        return
    } else if (data.status == 'cancel') {
        alert("Data has already been canceled.")
        return
    }

    const confirmed = confirm('Are you sure you want to cancel this data?')
    if (!confirmed) return

    let updatedData = {}

    if (type == 'sales') {
        updatedData = {
            "vehicle": data.vehicle_id,
            "sale_date": data.sale_date,
            "buyer_phone": data.buyer_phone,
            "buyer_name": data.buyer_name,
            "status": 'cancel'
        }
    } else {
        updatedData = {
            "vehicle": data.vehicle_id,
            "purchase_date": data.purchase_date,
            "seller_phone": data.seller_phone,
            "seller_name": data.seller_name,
            "purchase_price": data.purchase_price,
            "status": 'cancel'
        }
    }


    try {
        await axios.put(`${API_BASE_URL}/api/sales-purchases/${type}/update/${data.id}/`, updatedData, {
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

const deleteData = async (type, data, fetchFunc) => {
    const confirmed = confirm('Are you sure you want to delete this data?')
    if (!confirmed) return

    if (!token) {
        alert('Unauthorized: No access token found.')
        return
    }

    if (data.status != 'draft') {
        alert("Only 'draft' status that can be deleted.")
        return
    }

    try {
        await axios.delete(`${API_BASE_URL}/api/sales-purchases/${type}/delete/${data.id}/`, {
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
const fetchSales = () => fetchData('sales', saleCurrentPage.value, salePageSize, sales, saleTotalPages, salePageSize)

const addSale = (data) => addData('sales', data, fetchSales)

const editSale = (data) => editData('sales', data, fetchSales)

const confirmSale = (data) => confirmData('sales', data, fetchSales)

const cancelSale = (data) => cancelData('sales', data, fetchSales)

const deleteSale = (data) => deleteData('sales', data, fetchSales)

// /* Purchase */
const fetchPurchases = () => fetchData('purchases', purchaseCurrentPage.value, purchasePageSize, purchases, purchaseTotalPages, purchasePageSize)

const addPurchase = (data) => addData('purchases', data, fetchPurchases)

const editPurchase = (data) => editData('purchases', data, fetchPurchases)

const confirmPurchase = (data) => confirmData('purchases', data, fetchPurchases)

const cancelPurchase = (data) => cancelData('purchases', data, fetchPurchases)

const deletePurchase = (data) => deleteData('purchases', data, fetchPurchases)

/* Configs */
onMounted(() => {
    fetchSales()
    fetchPurchases()

})

watch(saleCurrentPage, () => {
    fetchSales()
})

watch(purchaseCurrentPage, () => {
    fetchPurchases()
})

watch(() => {
    fetchVehicles()
})

</script>