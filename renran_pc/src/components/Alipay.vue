<template>

</template>

<script>
export default {
  name: "Alipay",
  data() {
    return {
      loading: "",
    }
  },
  mounted() {
    // 提示用户正在进行网络请求，请不要页面.
    this.loading = this.$loading({
      lock: true,
      text: '支付结果处理，请不要关闭当前页面.',
      spinner: 'el-icon-loading',
      background: 'rgba(0, 0, 0, 0.7)'
    });
    this.alipay_result();
  },
  methods: {
    alipay_result() {
      this.$axios.get(`${this.$settings.Host}/payments/alipay/result/` + location.search).then(response => {
        this.loading.close();
        this.$router.push(`/article/${response.data.article_id}`);
      }).catch(error => {
        this.$message.error(response.data.detail);
      });
    }
  }
}
</script>

<style scoped>

</style>
