<template>
	<view class="phoneLogin-box"></view>
</template>

<script>
	export default {
		data() {
			return {}
		},
		onLoad(option) {
			// 只要进来就要走登录
			// #ifdef MP-ALIPAY
			const that = this;
			this.option = option;
			dd.getAuthCode({
				success: function(res) {
					/*{
					    authCode: 'hYLK98jkf0m' //string authCode
					}*/
					if (res?.authCode) {
						uni.hideLoading();
						that.code = res.authCode;
						// 后续处理逻辑
						// that.mpFreeLogin(res.authCode, option);
					} else {
						uni.hideLoading();
						uni.showToast({
							title: '钉钉授权登录失败',
							icon: 'none'
						});
						this.msgTip = '钉钉授权登录失败'
						console.error('钉钉授权登录失败', res);
					}
				},
				fail: function(err) {
					uni.hideLoading();
					uni.showToast({
						title: '钉钉授权登录失败',
						icon: 'none'
					});
					console.error('钉钉授权登录失败', err);
				}
			});
			// #endif
		},
		methods: {}
	}
</script>

<style lang="scss" scoped></style>