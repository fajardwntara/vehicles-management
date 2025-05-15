import { API_BASE_URL } from '@/config'
import axios from 'axios'

const token = sessionStorage.getItem('access_token')

export const getListMotor = async (page, pageSize) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/api/vehicles/motorcycle/lists`, {
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
        console.error('Failed to fetch motors:', error)
    }
}
