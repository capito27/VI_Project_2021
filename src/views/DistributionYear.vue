<template>
  <mdb-container id="distribution">
    <h2>Distribution</h2>
    <MonthlyAverageViews
      :values="RatingsPerMonth"
    />
    <WeeklyAverageViews
      :values="RatingsPerWeek"
    />
  </mdb-container>
</template>

<script>
import {
  mdbContainer,
} from 'mdbvue'
import MonthlyAverageViews from "@/components/MonthlyAverageViews";
import WeeklyAverageViews from "@/components/WeeklyAverageViews";
import {mapActions, mapGetters, mapState} from 'vuex';

export default {
  name: "DistributionYear",
  components: {
    MonthlyAverageViews,
    WeeklyAverageViews,
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
    }),
    ...mapGetters(['RatingsPerMonth', 'RatingsPerWeek']),
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
