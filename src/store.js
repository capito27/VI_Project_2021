import Vuex from "vuex";
import Vue from "vue";
import * as d3 from "d3";

Vue.use(Vuex)
export const store = new Vuex.Store({
    state: {
        name: 'Movie dataset',
        links: [],
        movies: [],
        ratings: [],
        tags: [],
        loading: 0
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
        },
        startLoading(state) {
            state.loading += 1;
        },
        doneLoading(state) {
            state.loading -= 1;
        }
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
        },
    },
    actions: {
        getLinks: ({commit}) => {
            commit('startLoading');
            d3.csv("../dataset/links.csv")
                .then(function (data) {
                    commit('setLinks', data)
                    commit('doneLoading');
                })
        },
        getMovies: ({commit}) => {
            commit('startLoading');
            d3.csv("../dataset/movies.csv")
                .then(function (data) {
                    commit('setMovies', data)
                    commit('doneLoading');
                })
        },
        getRatings: ({commit}) => {
            commit('startLoading');
            d3.csv("../dataset/ratings.csv")
                .then(function (data) {
                    commit('setRatings', data)
                    commit('doneLoading');
                })
        },
        getTags: ({commit}) => {
            commit('startLoading');
            d3.csv("../dataset/tags.csv")
                .then(function (data) {
                    commit('setTags', data)
                    commit('doneLoading');
                })
        }
    }
});