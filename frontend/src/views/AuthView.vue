<template>
  <nav class="bg-light border navbar navbar-expand-md navbar-light">
      <div class="container-fluid">
          <a class="navbar-brand" href="#"><span class="red">Hello</span></a>
          <button aria-controls="navbar" aria-expanded="false" aria-label="Toggle navigation" class="navbar-toggler" data-bs-target="#navbar" data-bs-toggle="collapse" type="button">
              <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbar">
                  <ul class="navbar-nav ms-auto mt-2">
                      <li class="nav-item"><a class="btn" @click="() => {login = false}">Register</a></li>
                      <li class="nav-item"><a class="btn" @click="() => {login = true}">Log In</a></li>
                  </ul>
          </div>
      </div>
  </nav>

  <LoginFormVue v-if="login" />
  <RegisterVue v-else />
</template>

<script>
import LoginFormVue from '@/components/LoginFromVue.vue'
import RegisterVue from '@/components/RegisterVue.vue'

export default {
  name: 'AuthView',
  components: {
    LoginFormVue,
    RegisterVue
  },
  data () {
    return {
      login: true
    }
  }
}

</script>
