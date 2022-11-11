<template>
  <v-btn color="primary" @click.stop="dialog = true">
    Add
  </v-btn>

  <v-row>
    <v-dialog v-model="dialog" max-width="600">
      <v-card>
        <v-card-title>
          <h2>Add</h2>
        </v-card-title>

        <v-card-text>
          <v-form class="px3">
            <v-text-field label="Title"></v-text-field>
          </v-form>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
  name: 'AddVue',
  data () {
    return {
      dialog: false
    }
  }
}
</script>
