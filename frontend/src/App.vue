<template>
  <div id="app">
    <tabbar></tabbar>
    <keep-alive>
      <router-view/>
    </keep-alive>
  </div>
</template>

<script>
import Tabbar from '@/views/tabbar'

export default {
  name: 'App',
  components: {
    Tabbar
  }
}
</script>

<style lang="scss">
@import '~@/common/scss/index';
</style>


