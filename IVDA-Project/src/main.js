// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import axios from 'axios';
import VueAxios from 'vue-axios';
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/en'
import App from './App'
import L from 'leaflet'
import * as d3 from 'd3'
import 'leaflet/dist/leaflet.css'
// import './registerServiceWorker'
import router from './router'
import store from './store'
import iFrameResize from 'iframe-resizer/js/iframeResizer'

// collapse 展开折叠
import CollapseTransition from 'element-ui/lib/transitions/collapse-transition';

Vue.use(ElementUI, { locale });
Vue.use(L);
Vue.use(d3);
Vue.use(VueAxios, axios);
axios.defaults.baseURL='/api';

Vue.config.productionTip = false;

Vue.directive('resize', {
  bind: function(el, { value = {} }) {
    el.addEventListener('load', () => iFrameResize(value, el))
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
