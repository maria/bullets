import Vue from 'vue'
import app from './app.vue'
import login from './login.vue'
import VueRouter from 'vue-router'
import { configRouter } from './route-config'

import 'bootstrap/dist/css/bootstrap.css'
import './styles.css'

Vue.config.debug = process.env.NODE_ENV !== 'production'

// install router
Vue.use(VueRouter)

// create router
const router = new VueRouter({
  hashbang: false
})

// configure router
configRouter(router)

const App = Vue.extend(login)

router.start(App, 'body')

// just for debugging
window.router = router
