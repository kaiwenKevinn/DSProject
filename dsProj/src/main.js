import Vue from 'vue'
import App from './App'

import '@/assets/css/global.css'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.config.productionTip = false
Vue.use(ElementUI)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>',
  beforeCreate() {
    Vue.prototype.$bus=this
  }
})
