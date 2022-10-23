<template>
  <form class="text-center" @submit.prevent="handleSubmit">
    <h3>Login</h3>
    <ErrorVue :error="errorMessage" v-if="errorMessage" />
    <div class="mb-3">
      <input class="form-control mx-auto w-auto" placeholder="Username" type="text" v-model="username" />
    </div>

    <div class="mb-3">
      <input class="form-control mx-auto w-auto" placeholder="Password" type="password" v-model="password" />
    </div>

    <button class="btn btn-primary">Login</button>
  </form>
</template>

<script>
import axios from 'axios'
import ErrorVue from './ErrorVue.vue'

export default {
  name: 'LoginFormVue',
  data () {
    return {
      username: '',
      password: '',
      errorMessage: ''
    }
  },
  methods: {
    async handleSubmit () {
      if (!this.username || !this.password) {
        this.errorMessage = 'username and password not provided'
        return
      }
      console.log(this.username, this.password)
      const token = btoa(`${this.username}:${this.password}`)
      const header = {
        Authorization: `Basic ${token}`,
        'Content-Type': 'application/json'
      }
      let response = null
      response = await axios.get('/auth/login', {
        headers: header
      })
      console.log(response)
      if (response.data.login_status === 'fail') {
        this.errorMessage = response.data.message
        return
      }

      this.$store.dispatch('user', response.data.user)
      this.$store.dispatch('login', response.data.token)
      this.$router.push('/')
    }
  },
  components: {
    ErrorVue
  }
}
</script>
