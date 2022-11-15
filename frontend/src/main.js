import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/en'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'

// collapse 展开折叠
import CollapseTransition from 'element-ui/lib/transitions/collapse-transition';


Vue.use(ElementUI, { locale })

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
