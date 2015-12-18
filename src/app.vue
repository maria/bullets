<template>
  <div class="main container">
    <div class="row">
      <div class="col-md-4">
        <sidebar></sidebar>
      </div>
    </div>
    <div class="row">
      <div class="col-md-8">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
  import sidebar from './sidebar.vue'

    export default {
    components: {
      sidebar
    }
  }
</script>
