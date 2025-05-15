import { API_BASE_URL } from '../config'
import axios from 'axios'

/* Get User Profile */
export const getCurrentUser = async () => {
    const token = sessionStorage.getItem('access_token')

    if (!token) {
        throw new Error('no_token_found')
    }

    try {
        const response = await axios.get(`${API_BASE_URL}/api/users/current/`, {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        })

        return response.data

    } catch (error) {
        alert("Token has been expired. Please refresh/login again.")
        sessionStorage.clear()
        window.location.href = '/login'
        console.error('Failed to fetch users:', error)
    }
}

// Get List of Users
export const getListUser = async (page, pageSize) => {
    const token = sessionStorage.getItem('access_token')
    try {
        const response = await axios.get(`${API_BASE_URL}/api/users/`, {
            params: {
                page: page,
                page_size: pageSize,
            },
            headers: {
                Authorization: `Bearer ${token}`,
            },
        })

        return response.data
    } catch (error) {
        console.error('Failed to fetch users:', error)
    }
}