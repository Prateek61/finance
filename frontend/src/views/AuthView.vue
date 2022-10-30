<template>
  <AuthNavVueVue :clickedRegister="clickedRegister" :clickedLogin="clickedLogin" />

  <div class="container-fluid py-5">
    <LoginFormVue v-if="login" />
    <RegisterVue v-else />
  </div>
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
