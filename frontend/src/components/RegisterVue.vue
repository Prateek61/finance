<template>
  <form class="text-center" @submit.prevent="handleSubmit">
    <h3>Register</h3>

    <div class="mb-3">
      <input class="form-control mx-auto w-auto" placeholder="Username" type="text" v-model="Username">
    </div>
    <div class="mb-3">
      <input class="form-control mx-auto w-auto" type="password" placeholder="Password" v-model="Password">
    </div>

    <div class="mb-3">
      <input class="form-control mx-auto w-auto" type="password" placeholder="Confirm Password" v-model="Password_Confirmation">
    </div>

    <button class="btn btn-primary mx-auto w-auto">Register</button>
  </form>
</template>

<style>

</style>

<script>
import axios from 'axios'

export default {
  name: 'RegisterVue',
  data () {
    return {
      Username: '',
      Password: '',
      Password_Confirmation: ''
    }
  },
  methods: {
    async handleSubmit () {
      const data = {
        username: this.Username,
        password: this.Password,
        password_Confirmation: this.Password_Confirmation
      }
      console.log(data)
      const response = await axios.post('/auth/register', data)
      console.log(response)
    }
  }
}
</script>
