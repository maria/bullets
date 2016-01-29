<template>
  <div class="main container">
    <div class="row">
        <div class="col-md-4 col-md-offset-4">
          <div class="text-center uMB-30 uMT-30">
            <logo></logo>
          </div>
        </div>
      </div>
    <div class="row">
      <div class="col-md-4 col-md-offset-4">
        <div class="form-group">
          <input type="text" v-model="login.username" placeholder="username" class="form-control input-lg" />
        </div>
        <div class="form-group">
          <input type="password" v-model="login.password" placeholder="password" class="form-control input-lg" />
        </div>
        <button type="submit" v-on:click="attemptLogin" name="loginSubmit" class="btn btn-primary btn-block btn-lg">Login</button>
      </div>
    </div>
  </div>
</template>

<script>
  import logo from './modules/logo.vue'

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

    methods: {
      attemptLogin: () => {
      }
    },

    components: {
      logo
    }
  }
</script>
