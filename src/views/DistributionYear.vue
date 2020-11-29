<template>
  <mdb-container id="distribution">
    <h2>Distribution</h2>
    <mdb-row>
      <mdb-col
        v-show="$store.state.loading === 0"
        col="12"
      >
        <AverageRatingsPerMonth
          v-show="$store.state.loading === 0"
          title="Average views per months"
          :values="RatingsPerMonth"
        />
        <LoadingSpinner v-show="$store.state.loading > 0" />
      </mdb-col>
      
      <mdb-col
        v-show="$store.state.loading === 0"
        col="12"
      >
        <AverageRatingsPerWeek
          v-show="$store.state.loading === 0"
          title="Average views per weeks of year"
          :values="RatingsPerWeek"
        />
        <LoadingSpinner v-show="$store.state.loading > 0" />
      </mdb-col>

      <mdb-col
        v-show="$store.state.loading === 0"
        col="12"
      >
        <AverageRatingsPerDayOfWeek
          v-show="$store.state.loading === 0"
          title="Average views per days of week"
          :values="RatingPerDayOfWeek"
        />
        <LoadingSpinner v-show="$store.state.loading > 0" />
      </mdb-col>
    </mdb-row>
  </mdb-container>
</template>

<script>
import {
  mdbContainer,
  mdbRow,
  mdbCol,
} from 'mdbvue'
import LoadingSpinner from "@/components/LoadingSpinner";
import AverageRatingsPerMonth from "@/components/AverageRatingsPerMonth";
import AverageRatingsPerWeek from "@/components/AverageRatingsPerWeek";
import AverageRatingsPerDayOfWeek from "@/components/AverageRatingsPerDayOfWeek";
import {mapActions, mapGetters, mapState} from 'vuex';

export default {
  name: "DistributionYear",
  components: {
    mdbContainer,
    mdbRow,
    mdbCol,
    LoadingSpinner,
    AverageRatingsPerMonth,
    AverageRatingsPerWeek,
    AverageRatingsPerDayOfWeek,
  },
  data: function () {
    return {}
  },
  computed: {
    ...mapState({
      name: state => state.name,
      links: state => state.links,
      movies: state => state.movies,
      ratings: state => state.ratings,
      tags: state => state.tags,
    }),
    ...mapGetters(['RatingsPerMonth', 'RatingsPerWeek', 'RatingPerDayOfWeek']),
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
