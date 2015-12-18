<template>
  <div class="col-md-4">
    <logo></logo>
  </div>
</template>

<script>
  export default {
    replace: false,
    data() {
      return {
        login: {
          username: '',
          password: ''
        }
      }
    },

    methods() {
      attemptLogin: () => {
        console.log('wat.');
      }
    }
  }
</script>
