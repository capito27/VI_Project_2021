<template>
  <div v-if="$store.state.loading === 0">
    <highcharts :options="chartOptions" />
  </div>
</template>

<script>

export default {
  name: "AverageRatingsPerMonth",
  props: {
    values: {
      type: Array,
      required: true
    }
  },
  data: function () {
    return {
      labels: [
        "January",
        "February",
        "March",
        "April",
        "Mai",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
      ],
    }
  },
  computed: {
    chartOptions: function () {
      return {
        chart: {
          type: 'column',
        },
        title: {
          text: "Monthly Average Views"
        },
        xAxis: {
          categories: this.labels,
          crosshair: true
        },
        yAxis: {
          min: 0,
          title: {
            text: "Views"
          }
        },
        plotOptions: {
          column: {
            pointPadding: 0.2,
            borderWidth: 0
          }
        },
        series: this.values
      }
    }
  },
  mounted() {
  },
  methods: {}
}
</script>

<style>
</style>
