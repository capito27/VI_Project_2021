<template>
  <svg />
</template>

<script>
import * as d3 from 'd3'

export default {
  name: "BarChart",
  props: {
    values: {
      type: Array,
      required: true
    },
  },
  data: function () {
    return {
      width: 300,
      height: 300,
      color: "darkgray",
      margin: ({top: 30, right: 0, bottom: 60, left: 40})
    }
  },
  mounted() {
    let x = d3.scaleBand()
        .domain(d3.range(this.values.length))
        .range([this.margin.left, this.width - this.margin.right])
        .padding(0.1)
    let y = d3.scaleLinear()
        .domain([0, d3.max(this.values, d => d.value)]).nice()
        .range([this.height - this.margin.bottom, this.margin.top])

    let xAxis = g => g
        .attr("transform", `translate(0,${this.height - this.margin.bottom})`)
        .call(d3.axisBottom(x).tickFormat(i => this.values[i].name).tickSizeOuter(0))
    let yAxis = g => g
        .attr("transform", `translate(${this.margin.left},0)`)
        .call(d3.axisLeft(y).tickSizeOuter(0))
        .call(g => g.select(".domain").remove())

    const svg = d3.select("svg")
        .attr("viewBox", [0, 0, this.width, this.height]);

    svg.append("g")
        .attr("fill", this.color)
        .selectAll("rect")
        .data(this.values)
        .join("rect")
        .attr("x", (d, i) => x(i))
        .attr("y", d => y(d.value))
        .attr("height", d => y(0) - y(d.value))
        .attr("width", x.bandwidth())

    svg.append("g")
        .call(xAxis)
        .selectAll("text")
        .attr("y", 0)
        .attr("x", 9)
        .attr("dy", ".35em")
        .attr("transform", "rotate(90)")
        .style("text-anchor", "start");

    svg.append("g")
        .call(yAxis)
  },
  methods: {}
}
</script>

<style>
</style>
