<template>
  <v-form ref="form">
    <h3>Register</h3>
    <v-text-field v-model="username" :rules="[rules.required]" label="username"></v-text-field>
    <v-text-field :type="show1 ? 'text' : 'password'" :rules="[rules.required]" v-model="password" label="password"></v-text-field>
    <v-text-field :type="show1 ? 'text' : 'password'" :rules="[rules.required, rules.confirmation]" v-model="passwordConfirmation" label="Confirm Password"></v-text-field>
    <AlertVue :type="alert.type" :message="alert.message" v-if="alert.message" />
    <v-btn class="my-2" @click="handleSubmit">Register</v-btn>
  </v-form>
</template>

<style>

</style>

<script>
import axios from 'axios'
import AlertVue from './AlertVue.vue'

export default {
  name: 'RegisterVue',
  data () {
    return {
      username: '',
      password: '',
      passwordConfirmation: '',
      alert: {
        type: null,
        message: null
      },
      rules: {
        required: v => !!v || 'Required',
        confirmation: v => this.password === v || 'Password confirmation doesnot match original password'
      }
    }
  },
  methods: {
    async handleSubmit () {
      const { valid } = await this.$refs.form.validate()

      if (valid) {
        const data = {
          username: this.username,
          password: this.password,
          passwordConfirmation: this.passwordConfirmation
        }
        const response = await axios.post('/auth/register', data)
        if (response.data.register_status === 'fail') {
          this.alert.type = 'warning'
          this.alert.message = response.data.message
        } else {
          this.alert.type = 'success'
          this.alert.message = 'Registered! You can login now'
        }
      }
    }
  },
  components: {
    AlertVue
  }
}
</script>
