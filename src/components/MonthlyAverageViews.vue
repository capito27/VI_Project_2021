<template>
  <div v-if="$store.state.loading === 0">
    <highcharts :options="chartOptions" />
  </div>
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
