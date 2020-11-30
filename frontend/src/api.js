import axios from "axios"

const API_ROOT = "http://localhost:5000/"
const API_VIEWS_PER_MONTH = API_ROOT + "views/per_month"
const API_VIEWS_PER_WEEK = API_ROOT + "views/per_week"
const API_VIEWS_PER_DAY = API_ROOT + "views/per_day"

export default new class {
    getViewsPerMonth(full = false) {
        return axios.get(API_VIEWS_PER_MONTH)
    }
}