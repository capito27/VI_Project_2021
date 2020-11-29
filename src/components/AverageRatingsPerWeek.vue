<template>
  <div v-if="$store.state.loading === 0">
    <highcharts :options="chartOptions" />
  </div>
</template>

<script>
export default {
  name: "AverageRatingsPerWeek",
  props: {
    title: {
      type: String,
      required: true
    },
    values: {
      type: Array,
      required: true
    },
  },
  data: function () {
    return {}
  },
  computed: {
    labels: function () {
      let labels = []

      for (let i = 0; i < 52; i++) {
        labels[i] = i + 1
      }

      return labels
    },
    chartOptions: function () {
      return {
        chart: {
          type: 'column',
        },
        title: {
          text: this.title
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
