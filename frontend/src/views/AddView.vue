<template>
  <div>
    <form @submit.prevent="handleSubmit">
      <div class="mb-3">
        <select class="form-select mx-auto w-auto" name="category" v-model="selectedCategory">
          <option disabled selected>Category</option>
          <option v-for="(category, index) in categories" :key="index" :value="category">{{ category }}</option>
        </select>
      </div>

      <div class="mb-3">
        <input class="form-control mx-auto w-auto" name="amount" placeholder="Amount" type="number" min="0" v-model="amount">
      </div>
      <div class="mb-3">
        <input autocomplete="off" class="form-control mx-auto w-auto" name="description" placeholder="Description" type="text" v-model="description" />
      </div>

      <ErrorVue v-if="errorMessage" :error="errorMessage"/>

      <button class="btn btn-primary" type="submit">Add</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import ErrorVue from '@/components/ErrorVue.vue'

export default {
  name: 'AddView',
  components: {
    ErrorVue
  },
  data () {
    return {
      categories: null,
      selectedCategory: 'Category',
      amount: null,
      description: null,
      errorMessage: null
    }
  },
  methods: {
    async handleSubmit () {
      const data = {
        category: this.selectedCategory,
        amount: this.amount,
        description: this.description
      }
      console.log(data)
      if (!this.isValid(data)) {
        this.errorMessage = 'Please complete the form properly'
        return
      }

      const response = await axios.post('/add', data)
      this.errorMessage = response.data.message
    },
    isValid (data) {
      if (!(data.category && data.amount && data.description)) {
        return false
      } else if (!Number.isInteger(data.amount) || parseInt(data.amount) < 0) {
        return false
      } else if (!this.categories.includes(data.category)) {
        return false
      }

      return true
    }
  },
  async created () {
    const response = await axios.get('/getcategories')
    this.categories = response.data.categories
    console.log(this.categories)
  }
}
</script>
