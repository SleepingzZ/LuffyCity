import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios";
import cookies from 'vue-cookies'
// 配置全局样式
import '@/assets/css/global.css'

// 全局配置
import settings from "@/assets/js/settings";

Vue.prototype.$url = settings;  // Vue.prototype --> JS 对象原型，相当于类

// axios 的全局配置
Vue.prototype.$axios = axios;

// cookies 的全局配置
Vue.prototype.$cookies = cookies;

// 配置 Element-UI
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);

// 配置 jQuery & Bootstrap
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
