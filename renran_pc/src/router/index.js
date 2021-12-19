import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home"

Vue.use(Router)

export default new Router({
   // 设置路由模式为‘history’，去掉默认的#
  mode: "history",
  routes: [
    {
      path: '/',
      name:"Home",
      component:Home,
    }
  ]
})
