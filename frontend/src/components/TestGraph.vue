<template>
  <highcharts
      ref="test-graph"
      :options="graphData"
  />
</template>

<script>

export default {
  name: "TestGraph",
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
        chart: {},
        title: {
          text: this.title
        },
        xAxis: {
          categories: [],
        },
        yAxis: {
          min: 0,
          title: {
            text: "Views"
          }
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
      data.series = [
        {
          type: "column",
          name: "Column",
          data: this.series.data,
          visible: false
        },
        {
          type: "line",
          name: "Line",
          data: this.series.data,
          visible: false
        },
        {
          type: "spline",
          name: "Spline",
          data: this.series.data,
          visible: false
        },
        {
          type: "spline",
          name: "Area",
          data: this.series.data,
          visible: false
        },
        {
          type: "areaspline",
          name: "Area spline",
          data: this.series.data,
          visible: false
        },
        {
          type: "areaspline",
          name: "Area spline",
          data: this.series.data,
          visible: true
        },
      ]
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