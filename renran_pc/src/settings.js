export default {
  Host: "http://api.renran.cn:8000", // ajax请求服务器的地址
  TC_captcha: {
    // 这里的app_id必须和Django中配置里面的app_id一致，否则报错
    app_id: "2060272005",
  },
  check_user_login(vm) {
    let token = localStorage.user_token || sessionStorage.user_token;
    if (!token) {
      vm.$confirm('您尚未登录,是否登录后继续操作', '荏苒提示', {
        confirmButtonText: '去登录',
        cancelButtonText: '回首页',
        type: 'info'
      }).then(() => {
        // 前往登录页面
        vm.$router.push("/user/login");
      }).catch(() => {
        // 返回站点首页
        vm.$router.push("/");
      });
    } else {
      vm.is_show_page = true;
      return token;
    }
  },
}
