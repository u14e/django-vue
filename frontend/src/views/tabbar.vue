<template>
  <div class="tabbar">
    <router-link tag="div" class="tabbar-item" to="/home">
      <div class="tabbar-icon"></div>
      <div class="tabbar-title">主页</div>
    </router-link>
    <router-link tag="div" class="tabbar-item" to="/contacts">
      <div class="tabbar-icon"></div>
      <div class="tabbar-title">通讯录</div>
    </router-link>
    <router-link tag="div" class="tabbar-item" to="/explore">
      <div class="tabbar-icon"></div>
      <div class="tabbar-title">发现</div>
    </router-link>
    <router-link tag="div" class="tabbar-item" to="/user">
      <div class="tabbar-icon"></div>
      <div class="tabbar-title">我</div>
    </router-link>
  </div>
</template>

<style lang="scss" scoped>
.tabbar {
  display: flex;
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 60px;
  box-shadow: 0 -1px rgba($color: #000000, $alpha: .25);
  .tabbar-item {
    flex: 1;
    text-align: center;
    .tabbar-icon {
      display: inline-block;
      margin-top: 8px;
      width: 22px;
      height: 22px;
      background: #000;
    }
    .tabbar-title {
      margin-top: 5px;
      color: #000;
    }
    &.router-link-active {
      .tabbar-icon {
        background-color: orangered;
      }
      .tabbar-title {
        color: orangered;
      }
    }
  }
}
</style>
