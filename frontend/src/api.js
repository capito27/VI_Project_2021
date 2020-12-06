import axios from "axios"

const API_ROOT = "http://localhost:5000/"

const API_ALL_GENRES = API_ROOT + "genres"
const API_RATING_RANGE = API_ROOT + "ratings/timestamp/bounds"

const API_VIEWS = API_ROOT + "views"
const API_RATINGS = API_ROOT + "ratings"

export default new class {
    async getGenres() {
        return axios.get(API_ALL_GENRES)
    }

    async getPeriodRange(full = false) {
        return axios.post(API_RATING_RANGE, {
            full: full
        })
    }

    async getViews(full = false, genres = null, period = {from: 0, to: Number.MAX_SAFE_INTEGER}, queries = null) {
        return axios.post(API_VIEWS, {
            full: full,
            filters: {
                genres: genres,
                period: period,
            },
            queries: queries,
        })
    }

    async getRatings(full = false, genres = null, period = {from: 0, to: Number.MAX_SAFE_INTEGER}, queries = null) {
        return axios.post(API_RATINGS, {
            full: full,
            filters: {
                genres: genres,
                period: period,
            },
            queries: queries,
        })
    }
}