import Vue from 'vue'
import App from './App.vue'
import router from './router'

import Buefy from 'buefy'
import vueHeadful from 'vue-headful'

import './assets/app.scss'

Vue.use(Buefy)

Vue.component('vue-headful', vueHeadful)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
