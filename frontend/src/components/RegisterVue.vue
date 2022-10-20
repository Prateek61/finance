<template>
  <form class="text-center" @submit.prevent="handleSubmit">
    <h3>Register</h3>
    <ErrorVue :error="errorMessage" v-if="errorMessage" />
    <div class="mb-3">
      <input class="form-control mx-auto w-auto" placeholder="Username" type="text" v-model="username">
    </div>
    <div class="mb-3">
      <input class="form-control mx-auto w-auto" type="password" placeholder="Password" v-model="password">
    </div>

    <div class="mb-3">
      <input class="form-control mx-auto w-auto" type="password" placeholder="Confirm Password" v-model="passwordConfirmation">
    </div>

    <button class="btn btn-primary mx-auto w-auto">Register</button>
    <div v-if="registered">User registered, you can login</div>
  </form>
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
