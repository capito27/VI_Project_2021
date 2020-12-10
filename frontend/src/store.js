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
        ratingsTimeRange: {
            min: 0,
            max: Number.MAX_SAFE_INTEGER,
            from: 0,
            to: Number.MAX_SAFE_INTEGER,
        },
        ratingsFilter: {
            min: 0.5,
            max: 5,
        },
        useFullDataset: false,
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
        setGenreFilter(state, payload) {
            state.genres_filter[payload.filter] = payload.value
        },
        setRatingTimeRange(state, payload) {
            if (payload.from)
                state.ratingsTimeRange.from = payload.from;
            if (payload.to)
                state.ratingsTimeRange.to = payload.to;
        },
        setRatingTimeBounds(state, payload) {
            state.ratingsTimeRange.min = payload.min;
            state.ratingsTimeRange.max = payload.max;
        },
        startLoading(state, prop) {
            if (state.loading.hasOwnProperty(prop))
                state.loading[prop] = true;
        },
        doneLoading(state, prop) {
            if (state.loading.hasOwnProperty(prop))
                state.loading[prop] = false;
        },
        setUseFullDataset(state, isFull) {
            state.useFullDataset = isFull;
        },
        setRatingsFilter(state, payload) {
            if (payload.min)
                state.ratingsFilter.min = payload.min;
            if (payload.max)
                state.ratingsFilter.max = payload.max;
        }
    },
    getters: {
        ViewsPerMonth: state => state.viewsPerMonth,
        ViewsPerWeek: state => state.viewsPerWeek,
        ViewsPerDayOfMonth: state => state.viewsPerDayOfMonth,
        ViewsPerDayOfWeek: state => state.viewsPerDayOfWeek,
        RatingsPerMonth: state => state.ratingsPerMonth,
        RatingsPerWeek: state => state.ratingsPerWeek,
        RatingsPerDayOfMonth: state => state.ratingsPerDayOfMonth,
        RatingsPerDayOfWeek: state => state.ratingsPerDayOfWeek,
        GenresFilter: state => state.genres_filter,
        RatingsTimeRange: state => state.ratingsTimeRange,
        RatingsTimeRangeMin: state => new Date(state.ratingsTimeRange.min * 1000),
        RatingsTimeRangeMax: state => new Date(state.ratingsTimeRange.max * 1000),
    },
    actions: {
        async getViews(ctx, queries) {
            let timeRange = ctx.state.ratingsTimeRange;
            delete timeRange.min;
            delete timeRange.max;
            for (let query of queries)
                ctx.commit('startLoading', "viewsPer" + query);
            let res = await api.getViews(ctx.state.useFullDataset, ctx.state.genres_filter, timeRange, queries.map(v => v.toLowerCase()), ctx.state.ratingsFilter);

            for (let query of queries) {
                if (res.status === 200) {
                    ctx.commit('setViews', {query: query, data: res.data[query.toLowerCase()]});
                }
                ctx.commit('doneLoading', "viewsPer" + query);
            }
        },
        async getRatings(ctx, queries) {
            let timeRange = ctx.state.ratingsTimeRange;
            delete timeRange.min;
            delete timeRange.max;
            for (let query of queries)
                ctx.commit('startLoading', "ratingsPer" + query);

            let res = await api.getRatings(ctx.state.useFullDataset, ctx.state.genres_filter, timeRange, queries.map(v => v.toLowerCase()));

            for (let query of queries) {
                if (res.status === 200) {
                    ctx.commit('setRatings', {query: query, data: res.data[query.toLowerCase()]});
                }
                ctx.commit('doneLoading', "ratingsPer" + query);
            }
        },
        async getGenres(ctx) {
            let res = await api.getGenres();
            if (res.status === 200) {
                ctx.commit('initGenreFilter', res.data);
            }
        },
        async getRatingsTimeBounds(ctx) {
            let res = await api.getRatingsTimeRange(ctx.state.useFullDataset);
            console.log(res);
            if (res.status === 200) {
                ctx.commit('setRatingTimeBounds', res.data);
            }
        }
    }
});