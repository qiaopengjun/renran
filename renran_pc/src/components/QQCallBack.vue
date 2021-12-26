<template>
  <div>QQ登录的回调页面</div>
</template>

<script>
export default {
  name: "QQCallBack",
  data() {

  },
  created() {
    // 接受QQ服务端的回调参数code和state参数
    // 查询字符串 query_string
    // 路由参数  router params
    let code = this.$route.query.code
    let state = this.$route.query.state
    console.log(code, state)
    this.get_user_info();
  },
  methods: {
    get_user_info() {

      // 转发code提供给服务端 服务端通过Authorization Code 获取Access Token
      this.$axios.get(`${this.$settings.Host}/oauth/qq/info/` + location.search
      ).then(response => {
        //
        console.log("ok");
      }).catch(error => {
        this.$message.error("网络错误!无法使用QQ第三方登陆");
      });
    }
  }
}
</script>

<style scoped>

</style>
