<style scoped>
  .panel-body {
    text-align: center;
  }

  figure {
    margin: 40px;
  }
</style>

<template>
  <div class="panel panel-default">
    <div class="panel-body">
      <logo></logo>
      <h3>Hello, {{ user }}!</h3>
      <ul class="nav nav-pills nav-stacked">
        <li><a v-link="{ name: 'groups' }">Groups</a></li>
        <li><a v-link="{ name: 'about' }">About</a></li>
        <li>&nbsp;</li>
        <li><a href="#" v-show="isLoggedIn">Logout</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
  import logo from './logo.vue'

  export default {
    replace: false,
    data() {
      return {
        user: ''
      }
    },

    methods: {
      isLoggedIn: () => {
      }
    },

    components: {
      logo
    }
  }
</script>
