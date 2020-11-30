<template>
  <mdb-container id="distribution">
    <h2>Distribution</h2>
    <mdb-row>
      <mdb-col col="12">
        <AverageRatingsPerMonth
          v-show="$store.state.loading === 0"
          title="Average views per months"
          :values="perMonth"
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
import api from '../api'

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
  data() {
    return {
      perMonth: {
        name: "Overall",
        data: []
      }
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
    ...mapGetters(['ViewsPerWeek', 'ViewsPerDayOfWeek']),
  },
  mounted() {
    api.getViewsPerMonth()
        .then(response => {
          this.perMonth.data = response.data.data
        })
        .catch(reason => {
          // Error
        })
        .finally(() => {
          // Loading done
        })
  },
  methods: {
    ...
        mapActions([
          'getLinks',
          'getMovies',
          'getRatings',
          'getTags'
        ])
  }
  ,
}
</script>

<style scoped>
</style>
