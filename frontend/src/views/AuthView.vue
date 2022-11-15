<template>
  <AuthNavVueVue :clickedRegister="clickedRegister" :clickedLogin="clickedLogin" />

  <v-main>
    <v-container class="my-5 py-5">
      <v-row no-gutters justify="center">
        <v-col cols="10" xs="8" sm="6" lg="4">
          <LoginFormVue v-if="login" />
          <RegisterVue v-else />
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
import LoginFormVue from '@/components/LoginFromVue.vue'
import RegisterVue from '@/components/RegisterVue.vue'
import AuthNavVueVue from '@/components/AuthNavVue.vue'

export default {
  name: 'AuthView',
  components: {
    LoginFormVue,
    RegisterVue,
    AuthNavVueVue
  },
  methods: {
    clickedRegister () {
      this.login = false
    },
    clickedLogin () {
      this.login = true
    }
  },
  data () {
    return {
      login: true
    }
  }
}

</script>
