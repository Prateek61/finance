<template>
  <div :class="type">{{message}}</div>
</template>

<script>
export default {
  name: 'AlertVue',

  props: {
    type: {
      type: String,
      required: false,
      validator: (value) => {
        return [
          'error',
          'success',
          'warning'
        ].includes(value)
      }
    },

    message: {
      type: String,
      required: true
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

.warning{
  text-align: center;
  color: #FFC107;
}
</style>
