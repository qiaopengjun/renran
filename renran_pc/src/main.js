// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

Vue.config.productionTip = false
// 加载项目的全局变量和全局方法
import settings from "./settings"
Vue.prototype.$settings = settings;

// elementUI 导入
import ElementUI from 'element-ui';
import "element-ui/lib/theme-chalk/index.css";
// 调用插件
Vue.use(ElementUI);

// 引入初始化样式
import "../static/css/reset.css";

// iconfont字体
import "../static/css/iconfont.css";
import "../static/css/iconfont.eot";

// 初始化axios
import axios from 'axios'; // 从node_modules目录中导入包

// 允许ajax发送请求时附带cookie，设置为不允许
axios.defaults.withCredentials = false;

Vue.prototype.$axios = axios; // 把对象挂载vue中

// 导入防水墙验证码的核心js文件
import "../static/js/TCaptcha"

router.beforeEach((to,from,next)=>{
    if(to.meta.title){
        document.title=to.meta.title
    }
    next()
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
