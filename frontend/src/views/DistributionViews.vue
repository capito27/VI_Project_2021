<template>
  <mdb-container id="distribution">
    <h2>Distribution</h2>
    <mdb-row>
      <mdb-col col="12">
        <BarGraph
          v-show="!loading.viewsPerMonth"
          title="Average views per months"
          :series="ViewsPerMonth"
        />
        <LoadingSpinner v-show="loading.viewsPerMonth" />
      </mdb-col>

      <mdb-col col="12">
        <BarGraph
          v-show="!loading.viewsPerWeek"
          title="Average views per weeks of year"
          :series="ViewsPerWeek"
        />
        <LoadingSpinner v-show="loading.viewsPerWeek" />
      </mdb-col>

      <mdb-col col="12">
        <BarGraph
          v-show="!loading.viewsPerDayOfWeek"
          title="Average views per days of week"
          :series="ViewsPerDayOfWeek"
        />
        <LoadingSpinner v-show="loading.viewsPerDayOfWeek" />
      </mdb-col>
      <mdb-col col="12">
        <TriStateButton />
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
import {mapGetters, mapState} from 'vuex';
import BarGraph from "@/components/BarGraph";
import TriStateButton from "@/components/TriStateButton";

export default {
  name: "DistributionViews",
  components: {
    TriStateButton,
    mdbContainer,
    mdbRow,
    mdbCol,
    LoadingSpinner,
    BarGraph,
  },
  data() {
    return {}
  },
  computed: {
    ...mapState({
      loading: state => state.loading,
    }),
    ...mapGetters(['ViewsPerWeek', 'ViewsPerDayOfWeek', 'ViewsPerMonth']),
  },
  mounted() {
  },
  methods: {}
}
</script>

<style scoped>
</style>
