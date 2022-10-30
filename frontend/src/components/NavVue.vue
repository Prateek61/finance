<template>
  <nav>
    <v-toolbar flat app>
      <v-btn selected to="/">Home</v-btn>
      <v-btn to="/add">Add</v-btn>
      <v-btn to="/history">History</v-btn>

      <v-spacer/>

      <v-btn @click="handleLogout">
        <span class="font-weight-light">Sign Out</span>
      </v-btn>
    </v-toolbar>
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
