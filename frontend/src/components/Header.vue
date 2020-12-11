<template>
  <mdb-navbar
    color="indigo"
    dark
  >
    <mdb-container>
      <mdb-navbar-brand
        router
        to="/"
        waves
      >
        Movies Statistics
      </mdb-navbar-brand>

      <mdb-form-inline>
        <DatasetControllerModal />
      </mdb-form-inline>
    </mdb-container>
  </mdb-navbar>
</template>

<script>
import {
  mdbContainer,
  mdbNavbar,
  mdbNavbarBrand,
  mdbFormInline,
} from 'mdbvue';
import DatasetControllerModal from "@/components/DatasetControllerModal";

export default {
  name: "Header",
  components: {
    DatasetControllerModal,
    mdbContainer,
    mdbNavbar,
    mdbNavbarBrand,
    mdbFormInline,
  }
}
</script>

<style scoped>

</style>
