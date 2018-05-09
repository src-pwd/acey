/* eslint-disable */
import Vue from 'vue'
import { sync } from 'vuex-router-sync'
import jwt_decode from 'jwt-decode'
import Element from 'element-ui'
import App from 'components/App' // require components using webpack alias
import { router } from './router' // Vue Router
import store from './store' // Vuex store
import locale from 'element-ui/lib/locale/lang/en'
import 'normalize.css' // normalize
import 'whatwg-fetch' // polyfill
import 'material-design-icons' // material icons, because Element-UI icons set is incomplete
import 'styles/index.scss' // require styles using webpack alias
import '../theme/index.css'
import fontawesome from '@fortawesome/fontawesome'




sync(store, router)
Vue.use(Element, { locale })

const BASE_URL = 'http://localhost:8000'

const app = new Vue({
  router,
  store,
  ...App
})

export { app, router, store }
