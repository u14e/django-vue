<template>
  <div class="user-page">
    <div class="user-header">
      <span class="identify">家长身份</span>
      <div class="user-header-content shadow">
        <div class="avatar"></div>
        <div class="user-name">教师姓名</div>
        <div class="text-secondary">自从学习了文言文，感谢上帝给我掀开了整个宇宙</div>
        <div class="user-header-bottom">
          <div class="bottom-item">三年级1班</div>
          <div class="bottom-item">语文</div>
          <div class="bottom-item">班主任</div>
        </div>
      </div>
    </div>
    <div class="user-card">
      <div class="card-line" v-for="(item, i) in [1, 2]" :key="i">
        <div class="card-item shadow">
          <div class="item-icon"></div>
          <div class="item-title">账户管理</div>
        </div>
        <div class="card-item shadow">
          <div class="item-icon"></div>
          <div class="item-title">账户管理</div>
        </div>
        <div class="card-item shadow">
          <div class="item-icon"></div>
          <div class="item-title">账户管理</div>
        </div>
      </div>
      
    </div>
    <div class="user-footer">
      <button @click="logout" class="btn btn-block btn-quit">退出登录</button>      
    </div>
  </div>
</template>

<script>
import store from 'store'

export default {
  methods: {
    logout () {
      store.remove('user')
      this.$router.push({ name: 'login' })
    }
  }
}
</script>

<style lang="scss" scoped>
.user-page {
  position: relative;
  height: calc(100vh - 60px);
  padding: 20px;
  background: #efefef;
  .user-header {
    position: relative;
    padding-top: 40px;
    .identify {
      position: absolute;
      right: 0;
      top: 0;
      background: #f90;
      color: #fff;
      padding: 6px;
      border-radius: 6px;
      font-size: 14px;
    }
    .user-header-content {
      position: relative;
      padding-top: 30px;
      background-color: #fff;
      border-radius: 6px;
      text-align: center;
      .avatar {
        width: 48px;
        height: 48px;
        border-radius: 6px;
        position: absolute;
        top: 0;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: #f40;
      }
      .user-name + div {
        margin: 10px;
        font-size: 14px;
      }
    }
    .user-header-bottom {
      display: flex;
      align-items: center;
      margin: 0 10px;
      border-top: 1px solid #aaa;
    }
    .bottom-item {
      flex: 1;
      line-height: 40px;
    }
  }
  .user-card {
    margin-top: 20px;
    .card-line {
      display: flex;
    }
    .card-item {
      flex: 1;
      margin: 0 10px 10px 0;
      padding: 20px 0;
      border-radius: 6px;
      text-align: center;
      background-color: #fff;
      &:last-child {
        margin-right: 0;
      }
      .item-icon {
        display: inline-block;
        width: 24px;
        height: 24px;
        background-color: #f40;
      }
      .item-title {
        margin-top: 5px;
        font-size: 14px;
      }
    }
  } 
  .user-footer {
    position: absolute;
    width: calc(100% - 40px);
    bottom: 20px;
    .btn-quit {
      background-color: #f40;
      color: #fff;
    }
  }
  
}
</style>

