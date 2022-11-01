<template>
  <v-form>
    <h3>Register</h3>
    <ErrorVue :error="errorMessage" v-if="errorMessage" />

    <v-text-field v-model="username" label="username"></v-text-field>
    <v-text-field :type="show1 ? 'text' : 'password'" v-model="password" label="password"></v-text-field>
    <v-text-field :type="show1 ? 'text' : 'password'" v-model="passwordConfirmation" label="Confirm Password"></v-text-field>
    <v-btn @click="handleSubmit">Register</v-btn>

    <h4 v-if="registered">Registered, you can now log in</h4>
  </v-form>
</template>

<style>

</style>

<script>
import axios from 'axios'
import ErrorVue from './ErrorVue.vue'

export default {
  name: 'RegisterVue',
  data () {
    return {
      username: '',
      password: '',
      passwordConfirmation: '',
      errorMessage: '',
      registered: false
    }
  },
  methods: {
    async handleSubmit () {
      if (!this.username || !this.password || !this.passwordConfirmation) {
        this.errorMessage = 'Form not filled completely'
        return
      } else if (this.password !== this.passwordConfirmation) {
        this.errorMessage = 'passwords does not match'
        return
      }

      const data = {
        username: this.username,
        password: this.password,
        passwordConfirmation: this.passwordConfirmation
      }
      const response = await axios.post('/auth/register', data)
      if (response.data.register_status === 'fail') {
        this.errorMessage = response.data.message
      } else {
        this.registered = true
      }
    }
  },
  components: {
    ErrorVue
  }
}
</script>
