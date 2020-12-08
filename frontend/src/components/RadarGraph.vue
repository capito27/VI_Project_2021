<template>
    <highcharts
        ref="radar-graph"
        :options="graphData"
    />
</template>

<script>

export default {
  name: "RadarGraph",
  props: {
    title: {
      type: String,
      required: true,
    },
    series: {
      type: Object,
      required: true,
    }
  },
  data: function () {
    return {
      chartOptions: {
        chart: {
          polar: true
        },
        title: {
          text: this.title
        },
        pane: {
          startAngle: 0,
          endAngle: 360
        },
        xAxis: {
          tickInterval: 1,
          min: 0,
          max: 12
        },
        yAxis: {
          min: 0
        },
        plotOptions: {
          series: {
            pointStart: 0,
            pointInterval: 1
          },
          column: {
            pointPadding: 0.05,
            groupPadding: 0
          }
        },
        series: []
      }
    }
  },
  computed: {
    graphData: function () {
      let data = this.chartOptions
      data.series = [{
        type: "column",
        name: "Overall",
        data: this.series.data,
      }]
      data.xAxis.categories = this.series.labels
      return data
    }
  },
  mounted() {
  }
}
</script>

<style scoped>

</style>