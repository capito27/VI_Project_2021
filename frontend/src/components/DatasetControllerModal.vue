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
      scrollable
    >
      <mdb-modal-header>
        <mdb-modal-title>Dataset control pannel</mdb-modal-title>
      </mdb-modal-header>

      <mdb-modal-body>
        <mdb-row>
          <mdb-col col="12">
            <mdb-row>
              <mdb-col col="12">
                <h5> Chose dataset to use </h5>
              </mdb-col>
              <mdb-col col="12">
                <toggle-button
                  :value="fullDataset"
                  :labels="{checked: 'Use Full Dataset', unchecked: 'Use Test Dataset'}"
                  :width="150"
                  :height="30"
                  @change="updateDatasetToUse"
                />
              </mdb-col>
            </mdb-row>
            <hr>
          </mdb-col>

          <mdb-col col="12">
            <mdb-row>
              <mdb-col col="12">
                <h5>Filter by review date</h5>
              </mdb-col>
              <mdb-col col="12">
                <mdb-row>
                  <mdb-col
                    col="2"
                    class="my-auto text-left"
                  >
                    From :
                  </mdb-col>
                  <mdb-col class="my-auto">
                    <date-picker
                      v-model="from"
                      :config="options"
                    />
                  </mdb-col>
                  <mdb-col
                    col="auto"
                    class="my-auto"
                  >
                    <mdb-btn
                      color="primary"
                      @click="resetFromBound"
                    >
                      Reset
                    </mdb-btn>
                  </mdb-col>
                </mdb-row>
              </mdb-col>
              <mdb-col col="12">
                <mdb-row>
                  <mdb-col
                    col="2"
                    class="my-auto text-left"
                  >
                    To :
                  </mdb-col>
                  <mdb-col class="my-auto">
                    <date-picker
                      v-model="to"
                      :config="options"
                    />
                  </mdb-col>
                  <mdb-col
                    col="auto"
                    class="my-auto"
                  >
                    <mdb-btn
                      color="primary"
                      @click="resetToBound"
                    >
                      Reset
                    </mdb-btn>
                  </mdb-col>
                </mdb-row>
              </mdb-col>
            </mdb-row>
            <hr>
          </mdb-col>

          <mdb-col col="12">
            <mdb-col col="12">
              <h5>Filter by movie genre</h5>
            </mdb-col>
            <mdb-col col="12">
              <mdb-row
                v-for="(value, genre) in GenresFilter"
                :key="genre"
                class="justify-content-start my-1"
                :genre="genre"
                :value="value"
                col="12"
              >
                <mdb-col
                  col="6"
                  class="my-auto text-left"
                >
                  {{ genre }}
                </mdb-col>
                <mdb-col
                  col="6"
                  class="my-auto text-left"
                >
                  <TriStateButton
                    :id="genre"
                    :labels="['Include', 'Exclude', 'Ignore']"
                    :initial="value"
                    :callback="genreCallback"
                  />
                </mdb-col>
              </mdb-row>
            </mdb-col>
          </mdb-col>
        </mdb-row>
      </mdb-modal-body>

      <mdb-modal-footer center>
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
  mdbAccordion,
  mdbAccordionPane,
  mdbRow,
  mdbCol,
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
    mdbAccordion,
    mdbAccordionPane,
    mdbRow,
    mdbCol,
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