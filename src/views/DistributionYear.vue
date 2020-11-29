<template>
  <mdb-container id="distribution">
    <h2>Distribution</h2>
    <MonthlyAverageViews
      :labels="labels"
      :values="RatingsPerMonth"
    />
  </mdb-container>
</template>

<script>
import {
  mdbContainer,
} from 'mdbvue'
import MonthlyAverageViews from "@/components/MonthlyAverageViews";
import {mapActions, mapGetters, mapState} from 'vuex';

export default {
  name: "DistributionYear",
  components: {
    MonthlyAverageViews,
    mdbContainer,
  },
  data: function () {
    return {
      labels: [
        "January",
        "February",
        "March",
        "April",
        "Mai",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
      ],
    }
  },
  computed: {
    ...mapState({
      name: state => state.name,
      links: state => state.links,
      movies: state => state.movies,
      ratings: state => state.ratings,
      tags: state => state.tags
    }),
    ...mapGetters(['RatingsPerMonth']),
  },
  beforeMount() {
    // Uncomment below to load required data if missing
    //if (this.$store.state.links.length === 0)
    //  this.$store.dispatch('getLinks');
    //if (this.$store.state.movies.length === 0)
    //  this.$store.dispatch('getMovies');
    if (this.$store.state.ratings.length === 0)
      this.$store.dispatch('getRatings');
    //if (this.$store.state.tags.length === 0)
    //  this.$store.dispatch('getTags')
  },
  methods: {
    ...mapActions([
      'getLinks',
      'getMovies',
      'getRatings',
      'getTags'
    ])
  },
}
</script>

<style scoped>

</style>
