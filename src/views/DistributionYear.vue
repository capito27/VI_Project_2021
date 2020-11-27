<template>
  <mdb-container id="distribution">
    <h2>Distribution</h2>
    <BarChart
      :values="values"
      width="50%"
      height="50%"
    />
  </mdb-container>
</template>

<script>
import {
  mdbContainer,
} from 'mdbvue'
import BarChart from "@/components/BarChart";

export default {
  name: "DistributionYear",
  components: {
    BarChart,
    mdbContainer,
  },
  data: function () {
    return {
      values: [
        {name: "January", value: 20},
        {name: "February", value: 34},
        {name: "March", value: 23},
        {name: "April", value: 56},
        {name: "Mai", value: 10},
        {name: "June", value: 15},
        {name: "July", value: 40},
        {name: "August", value: 60},
        {name: "September", value: 23},
        {name: "October", value: 10},
        {name: "November", value: 30},
        {name: "December", value: 80},
      ]
    };
  }
}
</script>

<style scoped>

</style>
