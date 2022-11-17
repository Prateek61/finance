<template>
  <div :class="type">{{message}}</div>
</template>

<script>
export default {
  name: 'AlertText',

  props: {
    /**
     * The type of alert
     * @values error, success, warning
     */
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
    /**
     * The message in the alert
     */
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
