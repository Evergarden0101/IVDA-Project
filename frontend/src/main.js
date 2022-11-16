import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/en'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import iFrameResize from 'iframe-resizer/js/iframeResizer'

// collapse 展开折叠
import CollapseTransition from 'element-ui/lib/transitions/collapse-transition';


Vue.use(ElementUI, { locale })

Vue.config.productionTip = false

Vue.directive('resize', {
  bind: function(el, { value = {} }) {
    el.addEventListener('load', () => iFrameResize(value, el))
  }
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
