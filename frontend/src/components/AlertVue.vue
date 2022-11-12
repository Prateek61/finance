<template>
  <div :class="type">{{message}}</div>
</template>

<script>
export default {
  name: 'AlertVue',
  props: ['type', 'message'],
  data () {
    return {

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
