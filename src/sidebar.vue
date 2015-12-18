<template>
  <div class="col-md-4">
    <logo></logo>
    <h3>Hello, {{ user }}!</h3>
    <a href="#" v-show="isLoggedIn">Logout</a>
  </div>
</template>

<script>
  import logo from './modules/logo.vue'

  export default {
    data() {
      return {
        user: ''
      }
    },

    methods: {
      isLoggedIn: () => {
        console.log('woot.');
      }
    },

    components: {
      logo
    }
  }
</script>
