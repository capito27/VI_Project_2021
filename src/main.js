import '@fortawesome/fontawesome-free/css/all.min.css'
import 'bootstrap-css-only/css/bootstrap.min.css'
import 'mdbvue/lib/css/mdb.min.css'

import Vue from 'vue'
import Vuex from 'vuex'
import HighchartsVue from "highcharts-vue";

import App from './App.vue'
import router from './router'
import * as d3 from 'd3'

Vue.config.productionTip = false

Vue.use(Vuex)
Vue.use(HighchartsVue);
// Default store, containing the dataset

export const store = new Vuex.Store({
    state: {
        name: 'Movie dataset',
        links: [],
        movies: [],
        ratings: [],
        tags: [],
    },
    getters: {
        RatingsPerMonth: state => {
            let values = {
                name: "Overall",
                data: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            }
            // Loop over all ratings, incrementing based on the month of the rating
            for (const rating of state.ratings) {
                const date = new Date(rating.timestamp * 1000);
                values.data[date.getMonth()] += 1;
            }
            return [values];
        }
    },
    mutations: {
        setLinks(state, data) {
            state.links = data
        },
        setMovies(state, data) {
            state.movies = data
        },
        setRatings(state, data) {
            state.ratings = data
        },
        setTags(state, data) {
            state.tags = data
        }
    },
    actions: {
        getLinks: ({commit}) => {
            d3.csv("../dataset/links.csv")
                .then(function (data) {
                    commit('setLinks', data)
                })
        },
        getMovies: ({commit}) => {
            d3.csv("../dataset/movies.csv")
                .then(function (data) {
                    commit('setMovies', data)
                })
        },
        getRatings: ({commit}) => {
            d3.csv("../dataset/ratings.csv")
                .then(function (data) {
                    commit('setRatings', data)
                })
        },
        getTags: ({commit}) => {
            d3.csv("../dataset/tags.csv")
                .then(function (data) {
                    commit('setTags', data)
                })
        }
    }
});

new Vue({
    el: '#app',
    router,
    render: h => h(App),
    store: store
}).$mount('#app')
