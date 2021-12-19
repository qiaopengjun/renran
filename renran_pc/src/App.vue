<template>
  <div id="app">
<!--    &lt;!&ndash; 需要被缓存的路由入口 &ndash;&gt;-->
<!--    <keep-alive>-->
<!--      <router-view v-if="$route.meta.keepAlive"></router-view>-->
<!--    </keep-alive>-->

<!--    &lt;!&ndash; 不需要被缓存的路由入口 &ndash;&gt;-->
<!--    <router-view v-if="!$route.meta.keepAlive"></router-view>-->
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>

</style>
