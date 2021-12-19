<template>
  <div id="app">
    <!-- 需要被缓存的路由入口 -->
    <keep-alive>
      <router-view v-if="$route.meta.keepAlive"></router-view>
    </keep-alive>

    <!-- 不需要被缓存的路由入口 -->
    <router-view v-if="!$route.meta.keepAlive"></router-view>
<!--    <router-view/>-->
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>

</style>
