import Vue from 'vue'
import app from './app.vue'
import VueRouter from 'vue-router'
import { configRouter } from './route-config'

import 'bootstrap/dist/css/bootstrap.css'
import './styles.css'

Vue.config.debug = process.env.NODE_ENV !== 'production'

// install router
Vue.use(VueRouter)

// create router
const router = new VueRouter({
  history: true,
  saveScrollPosition: true
})

// configure router
configRouter(router)

const App = Vue.extend(app)

router.start(App, 'body')

// just for debugging
window.router = router
