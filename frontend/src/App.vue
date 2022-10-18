<template>
  <router-view/>
</template>

<script>
import axios from 'axios'

export default {
  async created () {
    const response = await axios.get('/getuser')
    console.log(response.data.user)
    this.$store.dispatch('user', response.data.user)
  }
}
</script>

<style>

</style>
