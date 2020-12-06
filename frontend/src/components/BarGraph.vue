<template>
  <highcharts
    ref="bargraph"
    :options="chartOptions"
  />
</template>

<script>
export default {
  name: "BarGraph",
  props: {
    title: {
      type: String,
      required: true,
    },
    data: {
      type: Object,
      required: true
    },
  },
  computed: {
    chartOptions: function () {
      return {
        chart: {
          type: 'column',
        },
        title: {
          text: this.title
        },
        xAxis: {
          categories: this.data.labels,
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
        series: this.data
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
