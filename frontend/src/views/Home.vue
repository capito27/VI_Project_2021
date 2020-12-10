<template>
  <mdb-container>
    <mdb-tabs
      default
      :active="0"
      :links="tabLinks"
    >
      <template :slot="'per_month'">
        <RadarGraph
          v-show="!loading.viewsPerMonth"
          title="Average views per months"
          :series="ViewsPerMonth"
        />
        <LoadingSpinner v-show="loading.viewsPerMonth" />
      </template>

      <template :slot="'per_day_of_month'">
        <BarGraph
          v-show="!loading.viewsPerDayOfMonth"
          title="Average views per day of month"
          :series="ViewsPerDayOfMonth"
        />
        <LoadingSpinner v-show="loading.viewsPerDayOfMonth" />
      </template>

      <template :slot="'per_week'">
        <BarGraph
          v-show="!loading.viewsPerWeek"
          title="Average views per weeks of year"
          :series="ViewsPerWeek"
        />
        <LoadingSpinner v-show="loading.viewsPerWeek" />
      </template>

      <template :slot="'per_day_of_week'">
        <BarGraph
          v-show="!loading.viewsPerDayOfWeek"
          title="Average views per days of week"
          :series="ViewsPerDayOfWeek"
        />
        <LoadingSpinner v-show="loading.viewsPerDayOfWeek" />
      </template>
    </mdb-tabs>
  </mdb-container>
</template>

<script>
import {
  mdbTabs,
  mdbContainer,
} from 'mdbvue'
import BarGraph from "@/components/BarGraph";
import RadarGraph from "@/components/RadarGraph";
import LoadingSpinner from "@/components/LoadingSpinner";
import {mapGetters, mapState} from 'vuex';

export default {
  name: "Home",
  components: {
    BarGraph,
    RadarGraph,
    LoadingSpinner,
    mdbContainer,
    mdbTabs,
  },
  data() {
    return {
      tabLinks: [
        {text: "Per month", slot: "per_month"},
        {text: "Per day of month", slot: "per_day_of_month"},
        {text: "Per week", slot: "per_week"},
        {text: "Per day of week", slot: "per_day_of_week"},
      ]
    }
  },
  computed: {
    ...mapState({
      loading: state => state.loading,
    }),
    ...mapGetters(['ViewsPerWeek', 'ViewsPerDayOfWeek', 'ViewsPerMonth', 'ViewsPerDayOfMonth']),
  }
}
</script>

<style scoped>

</style>
