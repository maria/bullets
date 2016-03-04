<template>
  <div class="main container">
    <div class="row">
      <div class="col-md-3">
        <sidebar></sidebar>
      </div>
      <div class="col-md-9">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
  import Sidebar from './modules/sidebar.vue'

  export default {
    replace: false,

    name: 'main',

    components: {
      Sidebar
    }
  }
</script>
