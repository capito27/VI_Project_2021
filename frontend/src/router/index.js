import Vue from "vue"
import Router from "vue-router"
import DistributionViews from "@/views/DistributionViews";

Vue.use(Router)

export default new Router({
    routes: [
        {path: "/", name: "home", component: DistributionViews},
    ]
})
