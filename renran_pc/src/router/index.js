import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home"
import Login from "../components/Login"
import Register from "../components/Register"
import FindPassword from "../components/FindPassword";
import ResetPassword from "../components/ResetPassword";
import QQCallBack from "../components/QQCallBack"
import Writer from "../components/Writer";

Vue.use(Router)

export default new Router({
  // 设置路由模式为‘history’，去掉默认的#
  mode: "history",
  routes: [
    {
      meta: {
        title: "荏苒项目-首页", //配置title
        keepAlive: true //是否缓存
      },
      path: '/',
      name: "Home",
      component: Home,
    },
     {
       name:"Home",
       path:"/home",
       component:Home,
     },
    {
      meta: {
        title: "荏苒项目-登录页面", //配置title
        keepAlive: true //是否缓存
      },
      name: "Login",
      path: "/user/login",
      component: Login,
    },
    {
      meta: {
        title: "荏苒项目-注册页面", //配置title
        keepAlive: true //是否缓存
      },
      name: "Register",
      path: "/user/register",
      component: Register,
    },
    {
      meta: {
        title: "荏苒项目-找回密码页面", //配置title
        keepAlive: true //是否缓存
      },
      path: "/find_password",
      name: "FindPassword",
      component: FindPassword,
    },
     {
      meta: {
        title: "荏苒项目-重置密码页面", //配置title
        keepAlive: true //是否缓存
      },
      path: "/reset_password",
      name: "ResetPassword",
      component: ResetPassword,
    },
    {
      meta: {
        title: "荏苒项目-QQ登录的回调页面", //配置title
        keepAlive: true //是否缓存
      },
      path: '/oauth_callback.html',
      name: "QQCallBack",
      component: QQCallBack,
    },
    {
      meta: {
        title: "荏苒项目-写文章页面", //配置title
        keepAlive: true //是否缓存
      },
       name:"Writer",
       path:"/writer",
       component: Writer,
     },
  ]
})
