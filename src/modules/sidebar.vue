<template>
  <div class="col-md-4">
    <logo></logo>
    <h3>Hello, {{ user }}!</h3>
    <a href="#" v-show="isLoggedIn">Logout</a>
    <ul>
      <li><a v-link="{ path: '/groups' }">Groups</a></li>
      <li><a v-link="{ path: '/about' }">About</a></li>
    </ul>
  </div>
</template>

<script>
  import logo from './logo.vue'

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
