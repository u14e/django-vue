<template>
  <div class="login-page">
    <div class="login-title">八斗教育</div>
    <form>
      <div class="form-group">
        <input type="text" v-model="username" class="form-control" placeholder="请输入您的手机号">        
      </div>
      <div class="form-group">
        <input type="password" v-model="password" class="form-control" placeholder="请输入您的密码">        
      </div>
      <button @click.prevent="handle_login" class="btn btn-block">登录</button>      
    </form>
    <div class="login-footer">
      <router-link class="register-link" to="/register">注册</router-link>
    </div>
  </div>
</template>

<script>
import { login } from '@/api/user'
import store from 'store'

export default {
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    handle_login () {
      const form = {
        username: this.username,
        password: this.password
      }
      login(form).then(data => {
        store.set('user', {
          token: data.token
        })
        this.$router.push({ name: 'user' })
      })
    }
  }
}
</script>


<style lang="scss" scoped>
.login-page {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  background: #ddd;
  .login-title {
    font-size: 1.5rem;
    margin: 30px 0;
    color: rgb(224, 93, 53);
    text-align: center;
  }
  form {
    margin: 0 30px;
    padding: 1rem;
    border-radius: 6px;
    background: rgba(255, 255, 255, .5);
    button {
      margin-top: 2rem;
      background: rgb(224, 93, 53);
      color: #fff;
    }
  }
  .login-footer {
    position: absolute;
    bottom: 0;
    width: 100%;
    .register-link {
      float: right;
      margin-right: 10px;
      margin-bottom: 10px;
      color: rgb(224, 93, 53);
    }
  }
}
</style>
