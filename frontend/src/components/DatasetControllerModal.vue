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
  mdbCollapse,
  mdbContainer
} from 'mdbvue';
import {mapGetters} from "vuex";
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
  },
  data() {
    return {
      modal: false,
      change: false
    };
  },
  computed: {
    ...mapGetters(['GenresFilter', 'RatingsTimeRange']),
  },
  methods: {
    close(){
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
      console.log(this.$store.state.genres_filter)
    }
  }

}
</script>

<style scoped>

</style>