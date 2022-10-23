import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    user: null
  },
  getters: {
    user: (state) => {
      return state.user
    }
  },
  mutations: {
    user: (state, user) => {
      state.user = user
    },
    logout: (state) => {
      state.user = null
      localStorage.removeItem('token')
      axios.defaults.headers.common['x-access-token'] = null
    },
    login: (state, token) => {
      console.log(token)
      axios.defaults.headers.common['x-access-token'] = token
      localStorage.setItem('token', token)
    }
  },
  actions: {
    user: (context, user) => {
      context.commit('user', user)
    },
    logout: (context) => {
      context.commit('logout')
    },
    login: (context, token) => {
      context.commit('login', token)
    }
  },
  modules: {
  }
})
