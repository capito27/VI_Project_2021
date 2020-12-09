<template>
  <div>
    <mdb-btn
      color="primary"
      @click.native="modal = true"
    >
      Filter Dataset
    </mdb-btn>
    <mdb-modal
      :show="modal"
      @close="close"
    >
      <mdb-modal-header>
        <mdb-modal-title>Dataset control pannel</mdb-modal-title>
      </mdb-modal-header>
      <mdb-modal-body>
        <h5>Chose dataset to use</h5>
        <toggle-button
          :value="fullDataset"
          :labels="{checked: 'Use Full Dataset', unchecked: 'Use Test Dataset'}"
          :width="120"
          @change="updateDatasetToUse"
        />
        <hr>
        <h5>Filter by review date</h5>
        <div class="container d-flex align-items-center justify-content-center">
          <div class="row">
            <div class="col-sm">
              From :
            </div>
            <div class="col-sm-6">
              <date-picker
                v-model="from"
                :config="options"
              />
            </div>
            <div class="col-sm">
              <mdb-btn
                color="primary"
                @click="resetFromBound"
              >
                Reset
              </mdb-btn>
            </div>
          </div>
          <div class="row ">
            <div class="col-sm">
              To :
            </div>
            <div class="col-sm-6">
              <date-picker
                v-model="to"
                :config="options"
              />
            </div>
            <div class="col-sm">
              <mdb-btn
                color="primary"
                @click="resetToBound"
              >
                Reset
              </mdb-btn>
            </div>
          </div>
        </div>
        <hr>
        <h5>Filter by movie genre</h5>
        <tbody>
          <tr
            v-for="(value, genre) in GenresFilter"
            :key="genre"
            :genre="genre"
            :value="value"
          >
            <td style="text-align: right">
              {{ genre }}
            </td>
            <td style="text-align: left">
              <TriStateButton
                :id="genre"
                :labels="['Include', 'Exclude', 'Ignore']"
                :initial="value"
                :callback="genreCallback"
              />
            </td>
          </tr>
        </tbody>
      </mdb-modal-body>
      <mdb-modal-footer>
        <mdb-btn
          color="secondary"
          @click="close"
        >
          Close
        </mdb-btn>
        <mdb-btn
          color="primary"
          @click="reload"
        >
          Reload data
        </mdb-btn>
      </mdb-modal-footer>
    </mdb-modal>
  </div>
</template>

<script>
import {
  mdbModal,
  mdbModalHeader,
  mdbModalTitle,
  mdbModalBody,
  mdbModalFooter,
  mdbBtn,
} from 'mdbvue';

import datePicker from 'vue-bootstrap-datetimepicker';
import 'pc-bootstrap4-datetimepicker/build/css/bootstrap-datetimepicker.css';


import {mapGetters, mapState} from "vuex";
import TriStateButton from "@/components/TriStateButton";

export default {
  name: "DatasetControllerModal",
  components: {
    TriStateButton,
    mdbModal,
    mdbModalHeader,
    mdbModalTitle,
    mdbModalBody,
    mdbModalFooter,
    mdbBtn,
    datePicker
  },
  data() {
    return {
      modal: false,
      change: false,
      from: null,
      to: null,
      options: {
        format: 'DD/MM/YYYY',
        useCurrent: false,
      }
    };
  },
  computed: {
    ...mapGetters(['GenresFilter', 'RatingsTimeRange']),
    ...mapState({
      fullDataset: state => state.useFullDataset
    })
  },
  watch: {
    from(newDate) {
      if (typeof newDate !== "string")
        return;
      const explodedDate = newDate.split("/");
      const date = new Date(explodedDate[2], explodedDate[1] - 1, explodedDate[0]);
      const timestamp = date.getTime() / 1000 / (60 * 60 * 24) * (60 * 60 * 24) + 60 * 60; // rounds to the day
      this.updateReviewRange(timestamp, null);
    },
    to(newDate) {
      if (typeof newDate !== "string")
        return;
      const explodedDate = newDate.split("/");
      const date = new Date(explodedDate[2], explodedDate[1] - 1, explodedDate[0]);
      const timestamp = date.getTime() / 1000 / (60 * 60 * 24) * (60 * 60 * 24) + 25 * 60 * 60; // rounds to the next day at midnight
      this.updateReviewRange(null, timestamp);
    }
  },
  methods: {
    close() {
      this.reload();
      this.modal = false;
    },
    reload() {
      // Only reload data if we're not currently reloading and there was any change
      if (!Object.values(this.$store.state.loading).some(v => v) && this.change) {
        //this.$store.dispatch('getRatings', ['Month', 'Week', 'DayOfMonth', 'DayOfWeek']);
        this.$store.dispatch('getViews', ['Month', 'Week', 'DayOfMonth', 'DayOfWeek']);
        this.change = false;
      }
    },
    genreCallback(filter, value) {
      this.change = true;
      this.$store.commit('setGenreFilter', {filter: filter, value: value});
    },
    updateReviewRange(from, to) {
      this.$store.commit('setRatingTimeRange', {from: from, to: to});
      this.change = true;
    },
    resetFromBound() {
      console.log(this.$store.state.ratingsTimeRange.min)
      this.$store.commit('setRatingTimeRange', {from: this.$store.state.ratingsTimeRange.min, to: null});
      this.change = true;
      this.from = new Date(this.$store.state.ratingsTimeRange.min * 1000);
    },
    resetToBound() {
      this.$store.commit('setRatingTimeRange', {to: this.$store.state.ratingsTimeRange.min, from: null});
      this.change = true;
      this.to = new Date(this.$store.state.ratingsTimeRange.max * 1000);
    },
    updateDatasetToUse(full) {
      this.$store.commit('setUseFullDataset', full.value);
      this.$store.dispatch('getRatingsTimeBounds');
      // We must also get the new bounds
      this.change = true;
    }
  }

}
</script>

<style scoped>

</style>