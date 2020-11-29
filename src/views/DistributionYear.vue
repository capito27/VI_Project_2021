<template>
  <mdb-container id="distribution">
    <h2>Distribution</h2>
    <BarChart
      :values="values"
      width="50%"
      height="50%"
    />
  </mdb-container>
</template>

<script>
import {
  mdbContainer,
} from 'mdbvue'
import BarChart from "@/components/BarChart";
import {mapActions, mapState} from 'vuex';

export default {
  name: "DistributionYear",
  components: {
    BarChart,
    mdbContainer,
  },
  data: function () {
    return {
    }
  },
  computed: {
    ...mapState({
      name: state => state.name,
      links: state => state.links,
      movies: state => state.movies,
      ratings: state => state.ratings,
      tags: state => state.tags,
      values: state => {
        let values = [
          {name: "January", value: 0},
          {name: "February", value: 0},
          {name: "March", value: 0},
          {name: "April", value: 0},
          {name: "Mai", value: 0},
          {name: "June", value: 0},
          {name: "July", value: 0},
          {name: "August", value: 0},
          {name: "September", value: 0},
          {name: "October", value: 0},
          {name: "November", value: 0},
          {name: "December", value: 0},
        ]
        // Loop over all ratings, incrementing based on the month of the rating
        for (const rating of state.ratings) {
          const date = new Date(rating.timestamp * 1000);
          values[date.getMonth()].value += 1;
        }
        return values;
      }
    })
  },
  methods: {
    ...mapActions([
      'getLinks',
      'getMovies',
      'getRatings',
      'getTags'
    ])
  },
  beforeMount() {
    // Uncomment below to load required data
    // this.$store.dispatch('getLinks');
    // this.$store.dispatch('getMovies');
    this.$store.dispatch('getRatings');
    // this.$store.dispatch('getTags')
  },
}
</script>

<style scoped>

</style>
