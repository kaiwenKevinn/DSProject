import Vue from 'vue'
import App from './App'
import 'es6-promise/auto'
import Vuex from "vuex"
import store from './store'
import '@/assets/css/global.css'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.use(Vuex)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: h => h(App),
  store:store,
  beforeCreate() {
    Vue.prototype.$bus=this
  }

})
