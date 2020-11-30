<template>
  <mdb-container id="distribution">
    <h2>Distribution</h2>
    <mdb-row>
      <mdb-col col="12">
        <AverageRatingsPerMonth
          v-show="$store.state.loading === 0"
          title="Average views per months"
          :values="ViewsPerMonth"
        />
        <LoadingSpinner v-show="$store.state.loading > 0" />
      </mdb-col>
      
      <mdb-col col="12">
        <AverageRatingsPerWeek
          v-show="$store.state.loading === 0"
          title="Average views per weeks of year"
          :values="ViewsPerWeek"
        />
        <LoadingSpinner v-show="$store.state.loading > 0" />
      </mdb-col>

      <mdb-col col="12">
        <AverageRatingsPerDayOfWeek
          v-show="$store.state.loading === 0"
          title="Average views per days of week"
          :values="ViewsPerDayOfWeek"
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
    ...mapGetters(['ViewsPerMonth', 'ViewsPerWeek', 'ViewsPerDayOfWeek']),
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
