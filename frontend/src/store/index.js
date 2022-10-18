import { createStore } from 'vuex'

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
    }
  },
  actions: {
    user: (context, user) => {
      context.commit('user', user)
    },
    logout: (context) => {
      context.commit('logout')
    }
  },
  modules: {
  }
})
