<template>
  <nav class="text-left">
    <v-toolbar flat app>
      <v-toolbar-title>Auth</v-toolbar-title>
      <v-spacer></v-spacer>

      <v-btn link selected @click="clickedLogin">Login</v-btn>
      <v-btn link @click="clickedRegister">Register</v-btn>
    </v-toolbar>
  </nav>
</template>

<script>
export default {
  name: 'AuthNavVue',
  props: ['clickedRegister', 'clickedLogin']
}
</script>
