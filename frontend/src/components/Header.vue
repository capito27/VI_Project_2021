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

      <mdb-navbar-toggler>
        <mdb-navbar-nav>
          <mdb-nav-item
            router
            to="/distribution"
            waves
          >
            Distribution in year
          </mdb-nav-item>
          <mdb-nav-item
            router
            to="/evolution"
            waves
          >
            Evolution
          </mdb-nav-item>
        </mdb-navbar-nav>
      </mdb-navbar-toggler>
    </mdb-container>
  </mdb-navbar>
</template>

<script>
import {
  mdbContainer,
  mdbNavbar,
  mdbNavbarBrand,
  mdbNavbarToggler,
  mdbNavbarNav,
  mdbNavItem,
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
    mdbNavbarToggler,
    mdbNavbarNav,
    mdbNavItem,
    mdbFormInline,
  }
}
</script>

<style scoped>

</style>
