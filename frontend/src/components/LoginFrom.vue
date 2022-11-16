<template>
  <v-form class="px-3" ref="form">
    <h3>Login</h3>
    <v-text-field v-model="username" :rules="rules.usernameRequired" label="Username"></v-text-field>
    <v-text-field :type="show1 ? 'text' : 'password'" :rules="rules.passwordRequired" v-model="password" label="Password"></v-text-field>
    <AlertText :type="alert.type" :message="alert.message" v-if="alert.message" />
    <v-btn class="my-2" @click="loginFormSubmit">Log In</v-btn>
  </v-form>
</template>

<script>
import axios from 'axios'
import AlertText from './AlertText.vue'

export default {
  name: 'LoginFormVue',

  components: {
    AlertText
  },

  data () {
    return {
      username: '',
      password: '',

      alert: {
        type: null,
        message: null
      },

      rules: {
        usernameRequired: [
          v => !!v || 'Username Required'
        ],

        passwordRequired: [
          v => !!v || 'Password Required'
        ]
      }
    }
  },

  methods: {
    async loginFormSubmit () {
      const { valid } = await this.$refs.form.validate()

      if (valid) {
        const token = btoa(`${this.username}:${this.password}`)
        const header = {
          Authorization: `Basic ${token}`,
          'Content-Type': 'application/json'
        }
        const response = await axios.get('/auth/login', {
          headers: header
        })

        if (response.data.login_status === 'fail') {
          this.alert.type = 'error'
          this.alert.message = response.data.message
        } else {
          this.$store.dispatch('user', response.data.user)
          this.$store.dispatch('login', response.data.token)
          this.$router.push('/')
        }
      }
    }
  }
}
</script>
