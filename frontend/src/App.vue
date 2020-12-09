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
    this.$store.dispatch('getGenres');
    this.$store.dispatch('getRatingsTimeBounds');
    //this.$store.dispatch('getRatings', ['Month', 'Week', 'DayOfMonth', 'DayOfWeek']);
    this.$store.dispatch('getViews', ['Month', 'Week', 'DayOfMonth', 'DayOfWeek']);
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
