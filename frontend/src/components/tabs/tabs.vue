<template>
  <div class="tabs">
    <div class="tabs-header">
      <div 
        v-for="(tab, i) in tabs"
        :key="i"
        :class="{'active': currentIndex == i}"
        class="tab-header"
        @click="changeTab(i)">
        {{ tab.title }}
        <span class="notication" v-if="tab.hasNotication"></span>
      </div>
    </div>
    <div class="tabs-content">
      <slot />
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      tabs: [],
      currentIndex: 0
    }
  },
  created () {
    this.tabs = this.$children
  },
  methods: {
    changeTab (i) {
      this.currentIndex = i
      this.tabs.forEach((tab, index) => {
        tab.isActive = (index == i)
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.tabs {
  .tabs-header {
    display: flex;
    align-items: center;
    .tab-header {
      position: relative;
      flex: 1;
      line-height: 30px;
      margin-right: 2px;
      text-align: center;
      background: #eee;
      &:last-child {
        margin-right: 0;
      }
      &.active {
        background: #fff;
      }
      .notication {
        right: 3px;
        top: 2px;
      }
    }
  }
  .tabs-content {
    padding: 10px;
  }
}
</style>
