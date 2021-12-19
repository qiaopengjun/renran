import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home"
import Login from "../components/Login"

Vue.use(Router)

export default new Router({
  // 设置路由模式为‘history’，去掉默认的#
  mode: "history",
  routes: [
    {
      path: '/',
      name: "Home",
      component: Home,
    },
    {
      meta: {
        title: "荏苒项目-登录页面", //配置title
        keepAlive: true //是否缓存
      },
      name: "Login",
      path: "/login",
      component: Login,
    }
  ]
})
