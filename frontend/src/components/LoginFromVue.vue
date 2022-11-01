<template>
  <v-form>
    <h3>Login</h3>
    <ErrorVue :error="errorMessage" v-if="errorMessage" />
    <v-text-field v-model="username" label="Username"></v-text-field>
    <v-text-field :type="show1 ? 'text' : 'password'" v-model="password" label="Password"></v-text-field>
    <v-btn @click="handleSubmit">Log In</v-btn>
  </v-form>
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
