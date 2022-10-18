<template>
  <form class="text-center" @submit.prevent="handleSubmit">
    <h3>Login</h3>

    <div class="mb-3">
      <input class="form-control mx-auto w-auto" placeholder="Username" type="text" v-model="Username" />
    </div>

    <div class="mb-3">
      <input class="form-control mx-auto w-auto" placeholder="Password" type="password" v-model="Password" />
    </div>

    <button class="btn btn-primary">Login</button>
  </form>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginFormVue',
  data () {
    return {
      Username: '',
      Password: ''
    }
  },
  methods: {
    async handleSubmit () {
      const token = btoa(`${this.Username}:${this.Password}`)
      const header = {
        Authorization: `Basic ${token}`,
        'Content-Type': 'application/json'
      }
      const response = await axios.get('/auth/login', {
        headers: header
      })
      console.log(response.data.user)

      localStorage.setItem('token', response.data.token)
      this.$store.dispatch('user', response.data.user)

      this.$router.push('/')
    }
  }
}
</script>
