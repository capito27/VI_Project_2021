import '@fortawesome/fontawesome-free/css/all.min.css'
import 'bootstrap-css-only/css/bootstrap.min.css'
import 'mdbvue/lib/css/mdb.min.css'

import Vue from 'vue'
import Vuex, {mapState} from 'vuex'
import HighchartsVue from "highcharts-vue";
import Highcharts from 'highcharts'
import More from 'highcharts/highcharts-more'
import ToggleButton from 'vue-js-toggle-button'



More(Highcharts)

import App from './App.vue'
import router from './router'
import {store} from './store'

import './utils.js'

Vue.config.productionTip = false

Vue.use(Vuex)
Vue.use(HighchartsVue);
Vue.use(ToggleButton);

new Vue({
    el: '#app',
    router,
    store: store,
    render: h => h(App),
}).$mount('#app')
