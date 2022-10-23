<template>
  <nav class="bg-light border navbar navbar-expand-md navbar-light">
    <div class="container-fluid">
      <RouterLink class="navbar-brand" to="/"><span class="red">Home</span></RouterLink>
      <button aria-controls="navbar" aria-expand="false" aria-label="Toggle navigation" class="navbar-toggler" data-bs-target="#navbar" data-bs-toggle="collapse" type="button">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbar">
        <ul class="navbar-nav me-auto mt-2">
          <li class="nav-item"><RouterLink class="nav-link" to="/add">Add</RouterLink></li>
          <li class="nav-item"><RouterLink class="nav-link" to="/history">History</RouterLink></li>
          <li class="nav-item"><a class="nav-link" href="https://www.youtube.com/watch?v=j5a0jTc9S10">###</a></li>
        </ul>
        <ul class="navbar-nav ms-auto mt-2">
          <li class="nav-item"><a class="nav-link" href="#" @click.prevent="handleLogout">Log Out</a></li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavVue',
  methods: {
    handleLogout () {
      this.$store.dispatch('logout')
      this.$router.push('/auth')
    }
  }
}
</script>
