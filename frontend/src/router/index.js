import Vue from "vue"
import Router from "vue-router"
import Home from "@/views/Home"
import Evolution from "@/views/Evolution";
import DistributionViews from "@/views/DistributionViews";

Vue.use(Router)

export default new Router({
    routes: [
        {path: "/", name: "home", component: Home},
        {path: "/evolution", name: "evolution", component: Evolution},
        {path: "/distribution", name: "distribution_views", component: DistributionViews},
    ]
})
