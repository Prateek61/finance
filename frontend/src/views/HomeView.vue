<template>
  <div>
    <div v-if="user">
      <h1>{{user.username}}  {{user.public_id}}</h1>
    </div>
    <div v-else>
      <h1>Not logged in</h1>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'HomeView',
  data () {
    return {
    }
  },
  methods: {
  },
  computed: {
    ...mapGetters(['user'])
  }
}
</script>
