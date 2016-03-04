// Vue itself
import Vue from 'vue'

// Plugins
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'

// Pages
import Main from './app.vue'
import Login from './login.vue'

// Config
import { configRouter } from './route-config'

// Assets
import 'bootstrap/dist/css/bootstrap.css'
import './styles.css'

Vue.config.debug = process.env.NODE_ENV !== 'production'

// install router
Vue.use(VueRouter)
// install resource
Vue.use(VueResource);

// create router
const router = new VueRouter({
  // remove the "!" in the URL
  hashbang: false,
  // remove the "/#/" in the URL
  history: true,
})

// configure router
configRouter(router)

// The default page to be loaded
const App = Vue.extend(Main)

// Define DOM hook for switching routes
router.start(App, 'body')

// just for debugging
window.router = router
