<template>
  <div class="register-page">
    <h2 class="register-title">八斗教育</h2>
    <form>
      <div class="form-group">
        <input type="text" v-model="phone" class="form-control" placeholder="请输入您的手机号">
      </div>
      <div class="form-group">
        <div class="input-group">
          <input type="text" v-model="code" class="form-control"  placeholder="请输入您的验证码">
          <div class="input-group-append" @click="get_code">
            <span class="input-group-text">{{ timer ? timerText : '验证码' }}</span>
          </div>
        </div>
      </div>
      <div class="form-group">
        <input type="password" v-model="password" class="form-control" placeholder="请输入您的密码">
      </div>
      <div class="form-group">
        <input type="password" v-model="password1" class="form-control" placeholder="请再次输入您的密码">
      </div>
      <button @click.prevent="handle_register" class="btn btn-block">确定</button>
      <div class="text-danger mt-3 text-center" v-if="error">{{ error }}</div>
    </form>
  </div>
</template>

<script>
import { fetch_code, register } from '@/api/user'
export default {
  data () {
    return {
      phone: '',
      code: '',
      password: '',
      password1: '',
      error: '',
      timer: null,
      timerText: ''
    }
  },
  methods: {
    get_code () {
      if (this.timer) {
        console.log('距离上次发送未超过60s')
      } else {
        fetch_code(this.phone).then(data => {
          this.disable_get_code()
        }).catch(error => {
          this.error = error
          console.log(error)
        })
      }
      
    },
    handle_register (e) {
      if (this.password != this.password1) {
        this.error = '密码不一致'
        return
      }
      const form = {
        phone: this.phone,
        code: this.code,
        password: this.password
      }
      register(form).then(data => {
        this.$router.push({ name: 'login' })
      }).catch(error => {
        console.error(error)
      })
    },
    disable_get_code () {
      clearInterval(this.timer)
      let num = 60
      this.timer = setInterval(() => {
        this.timerText = `${num}s后再发送`
        num -= 1
        if (num == 0) {
          clearInterval(this.timer)
          this.timer = null
        }
      }, 1000)
    }
  },
  beforeDestroy () {
    clearInterval(this.timer)
  }
}
</script>

<style lang="scss" scoped>
.register-page {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  z-index: 100;
  background: #fff;
  .register-title {
    margin: 20px 0 30px;
    color: rgb(224, 93, 53);;
    text-align: center;
  }
  form {
    margin: 0 20px;
    .input-group-text {
      background: rgb(224, 93, 53);
      color: #fff;
    }
    button {
      background: rgb(224, 93, 53);
      color: #fff;
    }
  }
}
</style>
