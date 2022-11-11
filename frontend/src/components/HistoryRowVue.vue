<template>
  <v-card class="pa-3" flat v-ripple>
    <v-row :class="'status {{data.category}}'" :style="cssVars" wrap>
      <v-col cols="6" md="3">
        <div class="text-caption text-grey">Category</div>
        <v-icon class="icon" :style="cssVars">{{"mdi-" + style.icon}}</v-icon>
        <span class="text-capitalize">{{data.category}}</span>
      </v-col>

      <v-col  cols="6" sm="4" md="2">
        <div class="text-caption text-grey">Amount</div>
        <div> {{ data.amount }} </div>
      </v-col>

      <v-col  cols="6" sm="4" md="3">
        <div class="text-caption text-grey">Date Added</div>
        <div>2022/10/11</div>
      </v-col>

      <v-col  cols="12" sm=6 md="4">
        <div class="text-caption text-grey">Desciption</div>
        <div>{{ data.description }}</div>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
export default {
  name: 'HistoryRowVue',
  props: ['data', 'style'],
  computed: {
    cssVars () {
      return {
        '--icon-color': this.style.color
      }
    }
  }
}
</script>

<style>

.status {
  border-left: 4px solid var(--icon-color);
}

.icon {
  color: var(--icon-color);
}

</style>
