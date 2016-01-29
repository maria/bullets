import Vue from 'vue'
import app from './app.vue'
import login from './login.vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import { configRouter } from './route-config'

import 'bootstrap/dist/css/bootstrap.css'
import './styles.css'

Vue.config.debug = process.env.NODE_ENV !== 'production'

// install router
Vue.use(VueRouter)
// install resource
Vue.use(VueResource);

// create router
const router = new VueRouter({
  hashbang: false
})

// configure router
configRouter(router)

const App = Vue.extend(app)

router.start(App, 'body')

// just for debugging
window.router = router

Vue.use(require('vue-resource'));
