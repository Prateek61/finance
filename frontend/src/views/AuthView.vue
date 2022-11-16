<template>
  <AuthNav :clickedRegister="clickedRegister" :clickedLogin="clickedLogin" />

  <v-main>
    <v-container class="my-5 py-5">
      <v-row no-gutters justify="center">
        <v-col cols="10" xs="8" sm="6" lg="4">
          <login-form
            v-if="login"
            key="login-form-active"
          ></login-form>

          <register-form
            v-else
            key="register-form-active"
          ></register-form>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
import LoginForm from '@/components/LoginFrom.vue'
import RegisterForm from '@/components/RegisterForm.vue'
import AuthNav from '@/components/AuthNav.vue'

export default {
  name: 'AuthView',

  components: {
    LoginForm,
    RegisterForm,
    AuthNav
  },

  data () {
    return {
      login: true
    }
  },

  methods: {
    clickedRegister () {
      this.login = false
    },

    clickedLogin () {
      this.login = true
    }
  }
}

</script>
