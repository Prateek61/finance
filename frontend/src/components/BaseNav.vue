<template>
  <nav>
    <v-toolbar flat app>
      <v-btn selected to="/">Home</v-btn>
      <v-btn to="/history">History</v-btn>

      <v-spacer></v-spacer>
      <div class="center-add">
        <add-transaction></add-transaction>
      </div>
      <v-btn @click="baseNavLogout">
        <span class="font-weight-light">Sign Out</span>
      </v-btn>
    </v-toolbar>
  </nav>
</template>

<script>
import AddTransaction from '@/components/AddTransaction.vue'

export default {
  name: 'BaseNav',

  components: {
    AddTransaction
  },

  methods: {
    baseNavLogout () {
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
