import router from '@/router'
import axios from 'axios'
import store from '../store'

axios.defaults.baseURL = 'http://localhost:5000'
axios.defaults.headers.common['x-access-token'] = localStorage.getItem('token')

axios.interceptors.response.use((response) => {
  return response
}, (error) => {
  if (error.response.status === 401) {
    store.dispatch('logout')
    router.push('/auth')
    return Promise.reject(error)
  }
  return error
})
