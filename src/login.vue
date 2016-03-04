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
          <input type="text" v-model="loginData.username" placeholder="username" class="form-control input-lg" />
        </div>
        <div class="form-group">
          <input type="password" v-model="loginData.password" placeholder="password" class="form-control input-lg" />
        </div>
        <button type="submit" @click="attemptLogin" name="loginSubmit" class="btn btn-primary btn-block btn-lg">Login</button>
      </div>
    </div>
  </div>
</template>

<script>
  import Logo from './modules/logo.vue';
  import {apiURL} from './settings.js';

  export default {
    replace: false,

    name: 'authentication',

    components: {
      Logo
    },

    data() {
      return {
        loginData: {
          username: '',
          password: '',
        }
      }
    },

    methods: {
      attemptLogin() {
        this.$http.post(`${apiURL}/login`, this.loginData)
        .then((response) => {
          // do stuff
        }, () => {
          return 'Login failed';
        });

      }
    },
  }
</script>
