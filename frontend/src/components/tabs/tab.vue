<template>
  <div class="tab-item" v-show="isActive">
    <slot />
  </div>
</template>

<script>
export default {
  props: {
    selected: {
      type: Boolean,
      default: false
    },
    title: {
      type: String,
      required: true
    },
    hasNotication: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      isActive: false
    }
  },
  mounted () {
    this.isActive = this.selected
  }
}
</script>
