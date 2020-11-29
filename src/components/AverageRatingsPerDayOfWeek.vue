<template>
  <div v-if="$store.state.loading === 0">
    <highcharts :options="chartOptions" />
  </div>
</template>

<script>
export default {
  name: "AverageRatingsPerDayOfWeek",
  props: {
    values: {
      type: Array,
      required: true
    },
  },
  data: function () {
    return {
      labels: [
          "Monday",
          "Tuesday",
          "Wednesday",
          "Thursday",
          "Friday",
          "Saturday",
          "Sunday",
      ]
    }
  },
  computed: {
    chartOptions: function () {
      return {
        chart: {
          type: 'column',
        },
        title: {
          text: "Day of week average views"
        },
        xAxis: {
          categories: this.labels,
          crosshair: true,
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
