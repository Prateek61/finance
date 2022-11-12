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
          <h4 v-if="errorMessage">{{errorMessage}}</h4>
          <v-form class="px3" ref="form">
            <v-select :items="categories" label="Category" :rules="rules.category" v-model="selected"></v-select>
            <v-text-field label="Amount" :rules="rules.amount" v-model.number="amount"></v-text-field>
            <v-text-field label="Description" :rules="rules.description" v-model="description"></v-text-field>
            <v-btn color="primary" @click="handleSubmit">Add</v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import axios from 'axios'

export default {
  name: 'AddVue',
  data () {
    return {
      dialog: false,
      categories: null,
      selected: null,
      amount: null,
      description: '',
      errorMessage: null,
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
        this.errorMessage = response.data.message
      }
    }
  },
  async created () {
    const response = await axios.get('/getcategories')
    this.categories = response.data.categories
  }
}
</script>
