<template>

</template>

<script>
export default {
  name: "QQCallBack",
  data() {
    return {}
  },
  created() {
    // 接受QQ服务端的回调参数code和state参数
    // 查询字符串 query_string
    // 路由参数  router params
    // let code = this.$route.query.code
    // let state = this.$route.query.state
    // console.log(code, state)
    this.get_user_info();
  },
  methods: {
    get_user_info() {
      // 接受QQ服务端的回调参数code和state参数

      // 转发code提供给服务端 服务端通过Authorization Code 获取Access Token
      this.$axios.get(`${this.$settings.Host}/oauth/qq/user/`, {
        params: {
          code: this.$route.query.code,
          state: this.$route.query.state,
        }
      }).then(response => {
        //
        if (response.data.token) {
          // 接受服务端返回的jwt
          sessionStorage.user_token = response.data.token;
          sessionStorage.user_id = response.data.id;
          sessionStorage.user_name = response.data.username;
          sessionStorage.user_avatar = response.data.avatar;
          localStorage.removeItem("user_token");
          localStorage.removeItem("user_id");
          localStorage.removeItem("user_name");
          localStorage.removeItem("user_avatar");

          // 页面跳转
          this.$confirm('是否跳转到个人中心', '登录成功', {
            confirmButtonText: '个人中心',
            cancelButtonText: '返回首页',
            type: 'success'
          }).then(() => {
            // 前往个人中心
            this.$router.push("/users");
          }).catch(() => {
            // 返回站点首页
            this.$router.push("/");
          });
        }
      }).catch(error => {
        this.$message({
          type: "error",
          duration: 3000,
          message: "QQ登录失败!",
          onClose() {
            this.$router.push("/user/login");
          }
        });
      });
    }
  }
}
</script>

<style scoped>

</style>
