<template>
	<view class="phoneLogin-box">
		<view class="text">
			手机快捷登录弹窗示例
		</view>
		<view class="btn" @click="openLogin">
			打开弹窗
		</view>
		<phone-login
			:show="show"
			privacyUrl="/pages/login/privacy"
			userAgreementUrl="/pages/login/userAgreement"
			@maskClick="maskClick"
			@loginSuccessFun="loginSuccessFun">
		</phone-login>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				show: false
			}
		},
		methods: {
			openLogin() {
				this.show = true;
			},
			maskClick() {
				this.show = false;
			},
			loginSuccessFun(code) {
				this.show = false;
				uni.showToast({
					icon: 'none',
					duration: 10000,
					title:'获取手机code==>' + code
				});
			}
		}
	}
</script>

<style lang="scss" scoped>
	.phoneLogin-box {
		height: 100vh;
		position: relative;
		width: 100%;
		display: flex;
		flex-flow: column;
		align-items: center;
		justify-content: center;
		
		.text {
			font-family: HarmonyOS_Sans_SC;
			font-size: 40rpx;
		}
		
		.btn {
			height: 60rpx;
			width: 100px;
			box-sizing: border-box;
			border-radius: 36rpx;
			font-family: HarmonyOS_Sans_SC;
			font-size: 28rpx;
			color: rgba(0, 0, 0, 0.60);
			display: flex;
			align-items: center;
			justify-content: center;
			border: 2rpx solid #CCCCCC;
			margin-top: 30rpx;
			
			background: #0066FF;
			color: #FFFFFF;
			border: 2rpx solid #0066FF;
		}
	}
</style>