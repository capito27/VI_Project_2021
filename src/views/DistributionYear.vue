<template>
  <mdb-container id="distribution">
    <h2>Distribution</h2>
    <MonthlyAverageViews
      :labels="labels"
      :values="values"
    />
  </mdb-container>
</template>

<script>
import {
  mdbContainer,
} from 'mdbvue'
import MonthlyAverageViews from "@/components/MonthlyAverageViews";
import {mapActions, mapState} from 'vuex';

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
      tags: state => state.tags,
      values: state => {
        let values = {
          name: "Overall",
          data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        }
        // Loop over all ratings, incrementing based on the month of the rating
        for (const rating of state.ratings) {
          const date = new Date(rating.timestamp * 1000);
          values.data[date.getMonth()] += 1;
        }

        return [values];
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
