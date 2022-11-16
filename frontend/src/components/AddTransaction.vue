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
          <v-form class="px3" ref="form">
            <v-select :items="categories" label="Category" :rules="rules.category" v-model="selected"></v-select>
            <v-text-field label="Amount" :rules="rules.amount" v-model.number="amount"></v-text-field>
            <v-text-field label="Description" :rules="rules.description" v-model="description"></v-text-field>
            <AlertText :type="alert.type" :message="alert.message" v-if="alert.message" />
            <v-btn class="align-center" color="primary" @click="handleSubmit">Add</v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import axios from 'axios'
import AlertText from '@/components/AlertText.vue'

export default {
  name: 'AddTransaction',

  components: {
    AlertText
  },

  data () {
    return {
      dialog: false,

      categories: null,

      selected: null,
      amount: null,
      description: '',

      alert: {
        type: null,
        message: null
      },

      rules: {
        category: [
          v => !!v || 'Must select a category',
          v => this.categories.includes(v) || 'Must select a valid category'
        ],

        amount: [
          v => !!v || 'Must enter a amount',
          v => (Number.isInteger(v) && parseInt(v) > 0) || 'Must be a valid integer amount'
        ],

        description: [
          v => !!v || 'Must enter description'
        ]
      }
    }
  },

  async created () {
    const response = await axios.get('/getcategories')
    this.categories = response.data.categories
  },

  methods: {
    async handleSubmit () {
      const { valid } = await this.$refs.form.validate()
      if (valid) {
        const data = {
          category: this.selected,
          amount: this.amount,
          description: this.description
        }

        const response = await axios.post('/add', data)

        if (response.data.status === 'success') {
          this.alert = { type: 'success', message: response.data.message }
          this.selected = null
          this.amount = null
          this.description = null
        } else if (response.data.status === 'fail') {
          this.alert = { type: 'error', message: response.data.message }
        }
      }
    }
  }
}
</script>

<style>

.error{
  text-align: center;
  color: #B00020;
}
.success{
  text-align: center;
  color: #4CAF50;
}

</style>
