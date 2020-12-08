<template>
  <highcharts
      ref="bargraph"
      :options="graphData"
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
    series: {
      type: Object,
      required: true,
    },
  },
  data: function () {
    return {
      chartOptions: {
        chart: {
          type: 'column',
        },
        title: {
          text: this.title
        },
        xAxis: {
          categories: [],
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
        series: []
      }
    };
  },
  computed: {
    graphData: function () {
      let data = this.chartOptions
      data.series = [{
        data: this.series.data,
        name: "Overall"
      }]
      data.xAxis.categories = this.series.labels
      return data
    }
  },
  mounted() {
  },
  methods: {
  }
}
</script>

<style>
</style>
