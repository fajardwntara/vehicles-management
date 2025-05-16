<template>
  <div class="flex h-screen overflow-hidden">

    <!-- Modal Add/Update-->
    <transition name="fade">
      <div v-if="showModal || showEditModal"
        class="fixed inset-0 z-50 flex items-center justify-center backdrop-blur-sm bg-black/20">
        <div class="bg-white dark:bg-gray-900 rounded-2xl shadow-2xl w-full max-w-lg p-6 animate-fade-in">
          <h2 v-if="showModal" class="text-xs font-bold text-gray-800 dark:text-white mb-6">Add New User</h2>
          <h2 v-if="showEditModal" class="text-2xl font-bold text-gray-800 dark:text-white mb-6">Edit User</h2>

          <div class="space-y-4">
            <input v-model="form.username" type="text" :disabled="showEditModal" placeholder="Username"
              class="text-xs w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-slate-600 dark:bg-gray-800 dark:text-white disabled:bg-slate-200 dark:disabled:bg-gray-600" />
            <input v-model="form.email" type="email" placeholder="Email"
              class="text-xs w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-slate-600 dark:bg-gray-800 dark:text-white" />
            <input v-model="form.password" type="password" placeholder="Password"
              class="text-xs w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-slate-600 dark:bg-gray-800 dark:text-white" />
            <select v-model="form.role"
              class="text-xs w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-slate-600 dark:bg-gray-800 dark:text-white">
              <option disabled value="">Select Role</option>
              <option value="admin">Admin</option>
              <option value="staff">Staff</option>
            </select>
          </div>

          <div class="mt-6 flex justify-end space-x-4">
            <div v-if="showModal">
              <button @click="showModal = false"
                class="text-xs mx-2 cursor-pointer px-4 py-2 rounded-lg bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:text-white">
                Cancel
              </button>
              <button @click="addUser"
                class="text-xs cursor-pointer px-4 py-2 rounded-lg bg-slate-600 text-white hover:bg-slate-700">
                Save
              </button>
            </div>
            <div v-if="showEditModal">
              <button @click="showEditModal = false"
                class="text-xs mx-2 cursor-pointer px-4 py-2 rounded-lg bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:text-white">
                Cancel
              </button>
              <button @click="editUser"
                class="text-xs cursor-pointer px-4 py-2 rounded-lg bg-yellow-600 text-white hover:bg-yellow-700">
                Update
              </button>
            </div>
          </div>
        </div>
      </div>
    </transition>

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
              <h1 class="text-2xl md:text-3xl text-gray-800 dark:text-gray-100 font-bold">Users</h1>
            </div>

            <div class="grid grid-flow-col sm:auto-cols-max justify-start sm:justify-end gap-2">


            </div>

          </div>

          <!-- Body -->
          <div class="p-4 shadow-xl bg-white rounded-lg" v-if="users">

            <ListTable :data="users" :currentPage="currentPage" :pageSize="pageSize" :totalPages="totalPages"
              :prevPage="prevPage" :nextPage="nextPage" :columns="['username', 'role', 'email']"
              :headerColumns="['Username', 'Role', 'Email', 'Actions']">

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

                <button @click="deleteUser(data.id)"
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

          <Spinner v-else />

        </div>
      </main>


    </div>

  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'

import Sidebar from '../../partials/Sidebar.vue'
import Header from '../../partials/Header.vue'
import { getCurrentUser } from '@/data/User'

import { getListUser } from '@/data/User'
import { API_BASE_URL } from '../../config'
import ListTable from '../../components/Helpers/ListTable.vue'
const sidebarOpen = ref(false)
const users = ref([])
const currentPage = ref(1)
const totalPages = ref(1)
const pageSize = 5
const loading = ref(true)
const showModal = ref(false)
const showEditModal = ref(false)
const form = ref({
  username: '',
  email: '',
  role: '',
  password: '',
})
const userBeingEdited = ref(null)

// Clear form
const clearForm = () => {
  form.value.username = ""
  form.value.email = ""
  form.value.role = ""
  form.value.password = ""
}

const currentUserRole = ref('')

// fetch users
const fetchUsers = async () => {
  try {
    const response = await getListUser(currentPage.value, pageSize)

    users.value = response
    totalPages.value = Math.ceil(response.length / pageSize)

    if (response) {
      loading.value = false
    }
  } catch (err) {
    console.error("Error fetching users: ", err)
  }
}

const prevPage = () => {
  if (currentPage.value > 1) currentPage.value--
}
const nextPage = () => {
  if (currentPage.value < totalPages.value) currentPage.value++
}

// Add user
const addUser = async () => {

  if (
    !form.value.username.trim() ||
    !form.value.email.trim() ||
    !form.value.role.trim() ||
    !form.value.password.trim()
  ) {
    alert("Semua field wajib diisi!");
    return;
  }

  try {
    const token = sessionStorage.getItem('access_token')

    if (!token) {
      alert('Unauthorized: No access token found.')
      return
    }
    const res = await axios.post(`${API_BASE_URL}/api/users/create/`, form.value, {
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
    })
    users.value.push(res.data)
    showModal.value = false
    clearForm()
    alert("Successfully added new user.")
    await fetchUsers()
  } catch (err) {
    alert('Failed to add user')
    console.error(err)
  }
}

const showModalAdd = () => {
  showModal.value = true
  clearForm()
}

const openEditModal = (user) => {
  userBeingEdited.value = user
  form.value.username = user.username
  form.value.email = user.email
  form.value.role = user.role
  form.value.password = ''
  showEditModal.value = true
}

// Update user
const editUser = async () => {
  if (currentUserRole.value != 'admin') {
    alert("Only Admin role can use this action.")
    return
  }

  if (
    !form.value.username.trim() ||
    !form.value.email.trim() ||
    !form.value.role.trim() ||
    !form.value.password.trim()
  ) {
    alert("Semua field wajib diisi!");
    return;
  }


  try {
    const token = sessionStorage.getItem('access_token')
    if (!token) {
      alert('Unauthorized: No access token found.')
      return
    }
    let formEdited = {}
    if (form.value) {
      formEdited = {
        'email': form.value.email,
        'password': form.value.password,
        'role': form.value.role
      }
    }

    const res = await axios.put(`${API_BASE_URL}/api/users/update/${userBeingEdited.value.id}/`, formEdited, {
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
    })

    const index = users.value.findIndex(user => user.id === userBeingEdited.value.id)
    if (index !== -1) {
      users.value[index] = res.data
    }

    showEditModal.value = false
    alert("User updated successfully.")
    await fetchUsers()
    clearForm()
  } catch (err) {
    alert('Failed to update user: ')
    console.error(err)
  }
}

// Delete user
const deleteUser = async (id) => {
  if (currentUserRole.value != 'admin') {
    alert("Only Admin role can use this action.")
    return
  }
  const confirmed = confirm("Are you sure you want to delete this user?");
  if (!confirmed) return;

  try {
    const token = sessionStorage.getItem('access_token');
    if (!token) {
      alert('Unauthorized: No access token found.');
      return;
    }

    await axios.delete(`${API_BASE_URL}/api/users/delete/${id}/`, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    await fetchUsers();
    alert("User deleted successfully.");
  } catch (error) {
    console.error("Failed to delete user:", error);
    alert("Failed to delete user.");
  }
};

onMounted(async () => {
  fetchUsers()
  const currentUser = await getCurrentUser()
  currentUserRole.value = currentUser.role
})
watch(currentPage, fetchUsers)

</script>