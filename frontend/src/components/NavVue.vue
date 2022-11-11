<template>
  <nav>
    <v-toolbar flat app>
      <v-btn selected to="/">Home</v-btn>
      <v-btn to="/add">Add</v-btn>
      <v-btn to="/history">History</v-btn>

      <v-spacer />
      <div class="center-add">
        <AddVue />
      </div>
      <v-btn @click="handleLogout">
        <span class="font-weight-light">Sign Out</span>
      </v-btn>
    </v-toolbar>
  </nav>
</template>

<script>
import AddVue from '@/components/AddVue.vue'

export default {
  name: 'NavVue',
  components: {
    AddVue
  },
  methods: {
    handleLogout () {
      this.$store.dispatch('logout')
      this.$router.push('/auth')
    }
  }
}
</script>

<style>
.center-add{
  display: flex;
  margin-right: 16pt;
}
</style>
