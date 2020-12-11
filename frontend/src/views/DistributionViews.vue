<template>
  <mdb-container id="distribution" class="mt-4">
    <h1>Movie views visualisation</h1>
    <mdb-row class="mt-4">
      <mdb-col
        col="12"
        class="mb-3"
      >
        <mdb-card>
          <mdb-card-body>
            <RadarGraph
              v-show="!loading.viewsPerMonth"
              title="Average views per months"
              :series="ViewsPerMonth"
            />
            <LoadingSpinner v-show="loading.viewsPerMonth" />
          </mdb-card-body>
        </mdb-card>
      </mdb-col>

      <mdb-col
        col="12"
        class="mb-3"
      >
        <mdb-card>
          <mdb-card-body>
            <BarGraph
              v-show="!loading.viewsPerDayOfMonth"
              title="Average views per day of months"
              :series="ViewsPerDayOfMonth"
            />
            <LoadingSpinner v-show="loading.viewsPerDayOfMonth" />
          </mdb-card-body>
        </mdb-card>
      </mdb-col>

      <mdb-col
        col="12"
        class="mb-3"
      >
        <mdb-card>
          <mdb-card-body>
            <BarGraph
              v-show="!loading.viewsPerWeek"
              title="Average views per weeks of year"
              :series="ViewsPerWeek"
            />
            <LoadingSpinner v-show="loading.viewsPerWeek" />
          </mdb-card-body>
        </mdb-card>
      </mdb-col>

      <mdb-col
        col="12"
        class="mb-3"
      >
        <mdb-card>
          <mdb-card-body>
            <BarGraph
              v-show="!loading.viewsPerDayOfWeek"
              title="Average views per days of week"
              :series="ViewsPerDayOfWeek"
            />
            <LoadingSpinner v-show="loading.viewsPerDayOfWeek" />
          </mdb-card-body>
        </mdb-card>
      </mdb-col>
    </mdb-row>
  </mdb-container>
</template>

<script>
import {
  mdbContainer,
  mdbRow,
  mdbCol,
  mdbCard,
  mdbCardBody,
  mdbCardTitle,
} from 'mdbvue'
import LoadingSpinner from "@/components/LoadingSpinner";
import {mapGetters, mapState} from 'vuex';
import BarGraph from "@/components/BarGraph";
import RadarGraph from "@/components/RadarGraph";
import TriStateButton from "@/components/TriStateButton";

export default {
  name: "DistributionViews",
  components: {
    mdbContainer,
    mdbRow,
    mdbCol,
    mdbCard,
    mdbCardBody,
    mdbCardTitle,
    LoadingSpinner,
    BarGraph,
    RadarGraph,
  },
  data() {
    return {}
  },
  computed: {
    ...mapState({
      loading: state => state.loading,
    }),
    ...mapGetters(['ViewsPerWeek', 'ViewsPerDayOfWeek', 'ViewsPerMonth', 'ViewsPerDayOfMonth']),
  },
  mounted() {
  },
  methods: {}
}
</script>

<style scoped>
</style>
