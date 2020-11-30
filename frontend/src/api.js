import axios from "axios"

const API_ROOT = "http://localhost:5000/"

const API_ALL_MOVIES = API_ROOT + "movies"
const API_ALL_GENRES = API_ROOT + "genres"

const API_VIEWS_PER_MONTH = API_ROOT + "views/per_month"
const API_VIEWS_PER_WEEK = API_ROOT + "views/per_week"
const API_VIEWS_PER_DAY_OF_WEEK = API_ROOT + "views/per_day_of_week"

export default new class {
    getViewsPerMonth(full = false) {
        return axios.get(API_VIEWS_PER_MONTH)
    }
}