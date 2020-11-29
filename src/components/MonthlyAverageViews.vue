<template>
  <highcharts :options="chartOptions" />
</template>

<script>
export default {
  name: "MonthlyAverageViews",
  props: {
    labels: {
      type: Array,
      required: true
    },
    values: {
      type: Array,
      required: true
    },
  },
  data: function () {
    return {
      chartOptions: {
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
