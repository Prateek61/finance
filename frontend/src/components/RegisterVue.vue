<template>
  <form @submit.prevent="handlesubmit">
    <h3>Sign Up</h3>

    <div class="form-group">
      <label>Username</label>
      <input type="text" class="form-control" v-model="Username" placeholder="Username"/>
    </div>

    <div class="form-group">
      <label>Password</label>
      <input type="password" class="form-control" v-model="Password" placeholder="Password"/>
    </div>

    <div class="form-group">
      <label>Confirm Password</label>
      <input type="password" class="form-control" v-model="Password_Confirmation" placeholder="Confirm Password"/>
    </div>

    <button class="btn btn-primary btn-block">Register</button>
  </form>
</template>

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
    async handlesubmit () {
      const data = {
        username: this.Username,
        password: this.Password,
        password_Confirmation: this.Password_Confirmation
      }
      console.log(data)
      const response = await axios.post('/register', data)
      console.log(response)
    }
  }
}
</script>
