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
                class="m-3 py-2.5 cursor-pointer btn bg-gray-900 text-gray-100 hover:bg-gray-800 dark:bg-gray-100 dark:text-gray-800 dark:hover:bg-white">
                <svg class="dark:fill-gray-900 fill-gray-100" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg"
                  xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="1em" height="1.2em"
                  viewBox="0 0 122.879 122.879" enable-background="new 0 0 122.879 122.879" xml:space="preserve">
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
                      <button @click="openEditModal(user)"
                        class="bg-slate-100 cursor-pointer hover:bg-slate-200 shadow-xl p-2 text-white rounded-lg mx-2">
                        <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg"
                          xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="2em" height="2em"
                          viewBox="0 0 122.879 122.879" enable-background="new 0 0 122.879 122.879"
                          xml:space="preserve">
                          <g>
                            <path fill-rule="evenodd" clip-rule="evenodd" fill="#dfad2d"
                              d="M61.44,0c33.93,0,61.44,27.51,61.44,61.44c0,33.93-27.51,61.44-61.44,61.44S0,95.37,0,61.44 C0,27.51,27.51,0,61.44,0L61.44,0z M52.56,84c-1.82,0.61-3.68,1.17-5.5,1.77c-1.82,0.61-3.64,1.21-5.5,1.82 c-4.34,1.4-6.71,2.19-7.23,2.33c-0.51,0.14-0.19-1.86,0.89-6.06l3.45-13.19l26.01-27.04l13.85,13.33L52.56,84L52.56,84L52.56,84z M78.48,33.84c-0.65-0.61-1.4-0.93-2.24-0.89c-0.84,0-1.59,0.33-2.19,0.98l-4.94,5.13l13.85,13.38l4.99-5.22 c0.61-0.61,0.84-1.4,0.84-2.24c0-0.84-0.33-1.63-0.93-2.19L78.48,33.84L78.48,33.84L78.48,33.84z" />
                          </g>
                        </svg>
                      </button>

                      <button @click="deleteUser(user.id)"
                        class="shadow-xl bg-slate-100 cursor-pointer hover:bg-slate-200 p-2 text-white rounded-lg">
                        <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg"
                          xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="2em" height="2em"
                          viewBox="0 0 122.879 122.879" enable-background="new 0 0 122.879 122.879"
                          xml:space="preserve">
                          <g>
                            <path fill-rule="evenodd" clip-rule="evenodd" fill="#FF4141"
                              d="M61.44,0c33.933,0,61.439,27.507,61.439,61.439 s-27.506,61.439-61.439,61.439C27.507,122.879,0,95.372,0,61.439S27.507,0,61.44,0L61.44,0z M73.451,39.151 c2.75-2.793,7.221-2.805,9.986-0.027c2.764,2.776,2.775,7.292,0.027,10.083L71.4,61.445l12.076,12.249 c2.729,2.77,2.689,7.257-0.08,10.022c-2.773,2.765-7.23,2.758-9.955-0.013L61.446,71.54L49.428,83.728 c-2.75,2.793-7.22,2.805-9.986,0.027c-2.763-2.776-2.776-7.293-0.027-10.084L51.48,61.434L39.403,49.185 c-2.728-2.769-2.689-7.256,0.082-10.022c2.772-2.765,7.229-2.758,9.953,0.013l11.997,12.165L73.451,39.151L73.451,39.151z" />
                          </g>
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
  password: '',
  role: ''
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
    console.log("form : ", form.value)
    const res = await axios.put(`${API_BASE_URL}/api/users/update/${userBeingEdited.value.id}/`, form.value, {
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