<template>
  <nav class="text-left">
    <v-toolbar flat app>
      <v-toolbar-title>Auth</v-toolbar-title>
      <v-spacer></v-spacer>

      <v-btn link selected
        @click="clickedLogin"
      >Login</v-btn>

      <v-btn link
        @click="clickedRegister"
      >Register</v-btn>
    </v-toolbar>
  </nav>
</template>

<script>
export default {
  name: 'AuthNav',

  props: {
    /**
     * Gets called when user clicks on register
     */
    clickedRegister: {
      type: Function,
      required: true
    },
    /**
     * Gets called when user clicks on login
     */
    clickedLogin: {
      type: Function,
      required: true
    }
  }
}
</script>
