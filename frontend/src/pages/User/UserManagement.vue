<template>
  <div class="flex h-screen overflow-hidden">

    <!-- Modal Add/Update-->
    <transition name="fade">
      <div v-if="showModal || showEditModal"
        class="fixed inset-0 z-50 flex items-center justify-center backdrop-blur-sm bg-black/20">
        <div class="bg-white dark:bg-gray-900 rounded-2xl shadow-2xl w-full max-w-lg p-6 animate-fade-in">
          <h2 v-if="showModal" class="text-2xl font-bold text-gray-800 dark:text-white mb-6">Add New User</h2>
          <h2 v-if="showEditModal" class="text-2xl font-bold text-gray-800 dark:text-white mb-6">Edit User</h2>

          <div class="space-y-4">
            <input v-model="form.username" type="text" :disabled="showEditModal" placeholder="Username"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-800 dark:text-white disabled:bg-slate-200 dark:disabled:bg-gray-600" />
            <input v-model="form.email" type="email" placeholder="Email"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-800 dark:text-white" />
            <input v-model="form.password" type="password" placeholder="Password"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-800 dark:text-white" />
            <select v-model="form.role"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-800 dark:text-white">
              <option disabled value="">Select Role</option>
              <option value="admin">Admin</option>
              <option value="staff">Staff</option>
            </select>
          </div>

          <div class="mt-6 flex justify-end space-x-4">
            <div v-if="showModal">
              <button @click="showModal = false"
                class="mx-2 cursor-pointer px-4 py-2 rounded-lg bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:text-white">
                Cancel
              </button>
              <button @click="addUser"
                class=" cursor-pointer px-4 py-2 rounded-lg bg-slate-600 text-white hover:bg-slate-700">
                Save
              </button>
            </div>
            <div v-if="showEditModal">
              <button @click="showEditModal = false"
                class="mx-2 cursor-pointer px-4 py-2 rounded-lg bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:text-white">
                Cancel
              </button>
              <button @click="editUser"
                class=" cursor-pointer px-4 py-2 rounded-lg bg-yellow-600 text-white hover:bg-yellow-700">
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

            <!-- Table -->
            <div class="overflow-x-auto">
              <button @click="showModalAdd"
                class="m-3 py-2.5 cursor-pointer btn bg-gray-900 text-gray-100 hover:bg-gray-800 dark:bg-slate-700 dark:text-gray-100 dark:hover:bg-white">
                <svg class="dark:fill-gray-100 fill-gray-100" version="1.1" id="Layer_1"
                  xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                  width="1em" height="1.2em" viewBox="0 0 122.879 122.879" enable-background="new 0 0 122.879 122.879"
                  xml:space="preserve">
                  <g>
                    <path
                      d="M56.573,4.868c0-0.655,0.132-1.283,0.37-1.859c0.249-0.6,0.61-1.137,1.056-1.583C58.879,0.545,60.097,0,61.44,0 c0.658,0,1.287,0.132,1.863,0.371c0.012,0.005,0.023,0.011,0.037,0.017c0.584,0.248,1.107,0.603,1.543,1.039 c0.881,0.88,1.426,2.098,1.426,3.442c0,0.03-0.002,0.06-0.006,0.089v51.62l51.619,0c0.029-0.003,0.061-0.006,0.09-0.006 c0.656,0,1.285,0.132,1.861,0.371c0.014,0.005,0.025,0.011,0.037,0.017c0.584,0.248,1.107,0.603,1.543,1.039 c0.881,0.88,1.428,2.098,1.428,3.441c0,0.654-0.133,1.283-0.371,1.859c-0.248,0.6-0.609,1.137-1.057,1.583 c-0.445,0.445-0.98,0.806-1.58,1.055v0.001c-0.576,0.238-1.205,0.37-1.861,0.37c-0.029,0-0.061-0.002-0.09-0.006l-51.619,0.001 v51.619c0.004,0.029,0.006,0.06,0.006,0.09c0,0.656-0.133,1.286-0.371,1.861c-0.006,0.014-0.012,0.025-0.018,0.037 c-0.248,0.584-0.602,1.107-1.037,1.543c-0.883,0.882-2.1,1.427-3.443,1.427c-0.654,0-1.283-0.132-1.859-0.371 c-0.6-0.248-1.137-0.609-1.583-1.056c-0.445-0.444-0.806-0.98-1.055-1.58h-0.001c-0.239-0.575-0.371-1.205-0.371-1.861 c0-0.03,0.002-0.061,0.006-0.09V66.303H4.958c-0.029,0.004-0.059,0.006-0.09,0.006c-0.654,0-1.283-0.132-1.859-0.371 c-0.6-0.248-1.137-0.609-1.583-1.056c-0.445-0.445-0.806-0.98-1.055-1.58H0.371C0.132,62.726,0,62.097,0,61.44 c0-0.655,0.132-1.283,0.371-1.859c0.249-0.6,0.61-1.137,1.056-1.583c0.881-0.881,2.098-1.426,3.442-1.426 c0.031,0,0.061,0.002,0.09,0.006l51.62,0l0-51.62C56.575,4.928,56.573,4.898,56.573,4.868L56.573,4.868z" />
                  </g>
                </svg>
                <span class="max-xs:sr-only ml-2">New</span>
              </button>

              <table class="min-w-full divide-y divide-gray-200">
                <thead class="bg-white">
                  <tr>
                    <th
                      class="px-6 py-3 text-left text-md font-medium text-gray-700 dark:text-gray-600 uppercase tracking-wider">
                      #</th>
                    <th
                      class="px-6 py-3 text-left text-md font-medium text-gray-700 dark:text-gray-600 uppercase tracking-wider">
                      Username</th>
                    <th
                      class="px-6 py-3 text-left text-md font-medium text-gray-700 dark:text-gray-600 uppercase tracking-wider">
                      Email
                    </th>
                    <th
                      class="px-6 py-3 text-left text-md font-medium text-gray-700 dark:text-gray-600 uppercase tracking-wider">
                      Role
                    </th>
                    <th
                      class="px-6 py-3 text-left text-md font-medium text-gray-700 dark:text-gray-600 uppercase tracking-wider">
                      Actions
                    </th>
                  </tr>
                </thead>

                <tbody class="bg-white divide-y divide-gray-200" v-if="users && users.length > 0">

                  <tr v-for="(user, index) in paginatedUsers" :key="user.id">
                    <td class="px-6 py-4 whitespace-nowrap dark:bg-slate-50">
                      {{ (currentPage - 1) * pageSize + index + 1 }}
                    </td>
                    <td class="px-6 py-4 text-md whitespace-nowrap dark:bg-slate-50 dark:text-gray-700">{{ user.username
                      }}</td>
                    <td class="px-6 py-4 text-md whitespace-nowrap dark:bg-slate-50 dark:text-gray-700">{{ user.email }}
                    </td>
                    <td class="px-6 py-4 text-md whitespace-nowrap dark:bg-slate-50 dark:text-gray-700">{{ user.role }}
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap dark:bg-slate-50">

                      <!-- Edit -->
                      <button @click="openEditModal(user)"
                        class="bg-slate-100 cursor-pointer hover:bg-slate-200 shadow-xl p-2 text-white rounded-lg mx-2">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" class="fill-yellow-700">
                          <g>
                            <path
                              d="m12.593 23.258l-.011.002l-.071.035l-.02.004l-.014-.004l-.071-.035q-.016-.005-.024.005l-.004.01l-.017.428l.005.02l.01.013l.104.074l.015.004l.012-.004l.104-.074l.012-.016l.004-.017l-.017-.427q-.004-.016-.017-.018m.265-.113l-.013.002l-.185.093l-.01.01l-.003.011l.018.43l.005.012l.008.007l.201.093q.019.005.029-.008l.004-.014l-.034-.614q-.005-.018-.02-.022m-.715.002a.02.02 0 0 0-.027.006l-.006.014l-.034.614q.001.018.017.024l.015-.002l.201-.093l.01-.008l.004-.011l.017-.43l-.003-.012l-.01-.01z" />
                            <path
                              d="M13 3a1 1 0 0 1 .117 1.993L13 5H5v14h14v-8a1 1 0 0 1 1.993-.117L21 11v8a2 2 0 0 1-1.85 1.995L19 21H5a2 2 0 0 1-1.995-1.85L3 19V5a2 2 0 0 1 1.85-1.995L5 3zm6.243.343a1 1 0 0 1 1.497 1.32l-.083.095l-9.9 9.899a1 1 0 0 1-1.497-1.32l.083-.094z" />
                          </g>
                        </svg>
                      </button>

                      <!-- Delete -->
                      <button @click="deleteUser(user.id)"
                        class="shadow-xl bg-slate-100 cursor-pointer hover:bg-slate-200 p-2 text-white rounded-lg">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" class="fill-red-500">
                          <path
                            d="M2 5.27L3.28 4L5 5.72l.28.28l1 1l2 2L16 16.72l2 2l2 2L18.73 22l-1.46-1.46c-.34.29-.77.46-1.27.46H8c-1.1 0-2-.9-2-2V9.27zM8 19h7.73L8 11.27zM18 7v9.18l-2-2V9h-5.18l-2-2zm-2.5-3H19v2H7.82l-2-2H8.5l1-1h5z" />
                        </svg>

                      </button>

                    </td>
                  </tr>
                </tbody>
                <tbody v-else>
                  <tr>
                    <td colspan="3" class="text-center px-6 py-4 text-gray-500">No data found.</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <!-- Pagination -->
            <div class="mt-4 flex justify-center gap-5 items-center">
              <button @click="prevPage" :disabled="currentPage === 1"
                class="px-4 py-2 bg-slate-600 text-white rounded hover:bg-slate-700 disabled:opacity-50">
                < </button>

                  <span class="text-sm dark:text-gray-900 text-gray-600">Page {{ currentPage }} of {{ totalPages
                    }}</span>

                  <button @click="nextPage" :disabled="currentPage === totalPages"
                    class="px-4 py-2 bg-slate-600 text-white rounded hover:bg-slate-700 disabled:opacity-50">
                    >
                  </button>
            </div>
          </div>

          <Spinner v-else />

        </div>
      </main>


    </div>

  </div>
</template>

<script setup>
import { ref, onMounted, watch, computed } from 'vue'
import axios from 'axios'

import Sidebar from '../../partials/Sidebar.vue'
import Header from '../../partials/Header.vue'
import { getListUser } from '@/data/User'
import { API_BASE_URL } from '../../config'
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

const paginatedUsers = computed(() => {
  const start = (currentPage.value - 1) * pageSize
  const end = start + pageSize
  return users.value.slice(start, end)
})

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
  console.log("userBeingEdited.value : ", userBeingEdited.value.id)
  try {
    const token = sessionStorage.getItem('access_token')
    if (!token) {
      alert('Unauthorized: No access token found.')
      return
    }
    console.log("form val : ", form.value)
    let formEdited = {}
    if (form.value) {
      console.log("sene")
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

onMounted(fetchUsers)
watch(currentPage, fetchUsers)

</script>