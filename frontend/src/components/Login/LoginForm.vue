<template>
    <div class="mx-auto flex w-full max-w-sm flex-col">
        <h1 class="mt-8 text-2xl font-semibold text-gray-700 lg:mt-0">
            Login
        </h1>

        <!-- Username -->
        <p class="mt-5 text-sm font-semibold text-gray-500">Username</p>
        <input @keyup.enter="handleLogin" v-model="username" class="mt-1 rounded border py-1 px-3 text-sm shadow focus:border-slate-700" />

        <!-- Password -->
        <p class="mt-5 text-sm font-semibold text-gray-500">Password</p>
        <input @keyup.enter="handleLogin" v-model="password" class="mt-1 rounded border py-1 px-3 text-sm text-sm shadow focus:border-slate-700" type="password" />

        <button @click="handleLogin"
            class="mt-5 rounded border bg-slate-700 py-2 px-5 text-sm text-sm font-semibold text-slate-50 shadow hover:bg-slate-800 hover:duration-300">
            Sign in
        </button>
    </div>

    <Spinner v-if="loading"/>
</template>

<script setup>

import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { API_BASE_URL } from '../../config'

const username = ref('')
const password = ref('')
const loading = ref(false)
const router = useRouter()

const handleLogin = async () => {
    if (username.value === '' || password.value === '') {
        alert("Email and/or password must be filled.")
        return
    }

    loading.value = true

    try {
        const response = await axios.post(`${API_BASE_URL}/api/users/login/`, {
            username: username.value,
            password: password.value
        })

        const data = response.data

        sessionStorage.setItem('access_token', data.access)
        sessionStorage.setItem('refresh_token', data.refresh)

        if ((data.access && data.refresh) ) {
            router.push('/dashboard')
        }

    } catch (err) {
        alert(err.response?.data?.detail || 'Login failed')
    } finally {
        loading.value = false
    }
}
</script>