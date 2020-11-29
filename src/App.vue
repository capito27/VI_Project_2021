<template>
  <div id="app">
    <Header />
    <router-view />
  </div>
</template>

<script>
import Header from "@/components/Header";

export default {
  name: 'App',
  components: {
    Header,
  },
  beforeMount() {
    // Uncomment below to load required data if missing
    //if (this.$store.state.links.length === 0)
    //  this.$store.dispatch('getLinks');
    //if (this.$store.state.movies.length === 0)
    //  this.$store.dispatch('getMovies');
    if (this.$store.state.ratings.length === 0)
      this.$store.dispatch('getRatings');
    //if (this.$store.state.tags.length === 0)
    //  this.$store.dispatch('getTags')
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap');

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
