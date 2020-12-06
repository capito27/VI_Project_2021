import Vuex from "vuex";
import Vue from "vue";
import api from "@/api";

Vue.use(Vuex)
export const store = new Vuex.Store({
    state: {
        name: 'Movie dataset',
        viewsPerMonth: {data: [], labels: []},
        viewsPerWeek: {data: [], labels: []},
        viewsPerDayOfMonth: {data: [], labels: []},
        viewsPerDayOfWeek: {data: [], labels: []},
        ratingsPerMonth: {data: [], labels: []},
        ratingsPerWeek: {data: [], labels: []},
        ratingsPerDayOfMonth: {data: [], labels: []},
        ratingsPerDayOfWeek: {data: [], labels: []},
        genres_filter: {},
        periods_filter: {
            min: 0,
            max: Number.MAX_SAFE_INTEGER,
            from: 0,
            to: Number.MAX_SAFE_INTEGER,
        },
        useFullDataset: true,
        loading: {
            viewsPerMonth: false,
            viewsPerWeek: false,
            viewsPerDayOfMonth: false,
            viewsPerDayOfWeek: false,
            ratingsPerMonth: false,
            ratingsPerWeek: false,
            ratingsPerDayOfMonth: false,
            ratingsPerDayOfWeek: false,
        }
    },
    mutations: {
        setViews(state, payload) {
            state["viewsPer" + payload.query] = payload.data
        },
        setRatings(state, payload) {
            state["ratingsPer" + payload.query] = payload.data
        },
        initGenreFilter(state, fields) {
            for (let field of fields) {
                state.genres_filter[field] = null;
            }
        },
        setGenreFilter(state, filter, value) {
            state.genres_filter[filter] = value
        },
        startLoading(state, prop) {
            if (state.loading.hasOwnProperty(prop))
                state.loading[prop] = true;
        },
        doneLoading(state, prop) {
            if (state.loading.hasOwnProperty(prop))
                state.loading[prop] = false;
        }
    },
    getters : {
        ViewsPerMonth: state => state.viewsPerMonth,
        ViewsPerWeek: state => state.viewsPerWeek,
        ViewsPerDayOfMonth: state => state.viewsPerDayOfMonth,
        ViewsPerDayOfWeek: state => state.viewsPerDayOfWeek,
        RatingsPerMonth: state => state.ratingsPerMonth,
        RatingsPerWeek: state => state.ratingsPerWeek,
        RatingsPerDayOfMonth: state => state.ratingsPerDayOfMonth,
        RatingsPerDayOfWeek: state => state.ratingsPerDayOfWeek,
    },
    actions: {
        async getViews(ctx, queries) {
            let period = ctx.state.periods_filter;
            delete period.min;
            delete period.max;
            for (let query of queries)
                ctx.commit('startLoading', "viewsPer" + query);

            let res = await api.getViews(ctx.state.useFullDataset, ctx.state.genres_filter, period, queries.map(v => v.toLowerCase()));

            for (let query of queries) {
                if (res.status === 200) {
                    ctx.commit('setViews', {query: query, data: res.data[query.toLowerCase()]});
                }
                ctx.commit('doneLoading', "viewsPer" + query);
            }
        },
        async getRatings(ctx, queries) {
            let period = ctx.state.periods_filter;
            delete period.min;
            delete period.max;
            for (let query of queries)
                ctx.commit('startLoading', "ratingsPer" + query);

            let res = await api.getRatings(ctx.state.useFullDataset, ctx.state.genres_filter, period, queries.map(v => v.toLowerCase()));

            for (let query of queries) {
                if (res.status === 200) {
                    ctx.commit('setRatings', {query: query, data: res.data[query.toLowerCase()]});
                }
                ctx.commit('doneLoading', "ratingsPer" + query);
            }
        },
        async getGenres(ctx) {
            let res = await api.getGenres();
            for (let genre of res.data) {
                ctx.state.genres_filter[genre] = null
            }
            console.log(ctx.state.genres_filter)
        },
    }
});