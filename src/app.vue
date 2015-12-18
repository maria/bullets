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
  import sidebar from './modules/sidebar.vue'

  export default {
    replace: false,
    components: {
      sidebar
    }
  }
</script>
