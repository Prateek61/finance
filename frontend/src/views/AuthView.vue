<template>
  <NavVue />
  <LoginFormVue />
</template>

<script>
import NavVue from '@/components/NavVue.vue'
import LoginFormVue from '@/components/LoginFromVue.vue'

export default {
  name: 'AuthView',
  components: {
    NavVue,
    LoginFormVue
  }
}

</script>
