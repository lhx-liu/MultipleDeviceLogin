<template>
	<view class="phoneLogin-box">
		<view class="btn" @click="wxlogin">
			微信授权登录示例
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {}
		},
		onLoad(opt) {
			const { code, ...otherparams} = opt;
			// 如果有code代表微信授权登录的回调
			if(code) {
				// 获取code后，路径里是不携带otherparams
				// 从缓存中获取
				const params = uni.getStorageSync('opt');
				this._login(code, params);
			} else {
				// 如果涉及到微信业务的模版推送 这里的otherparams需要暂时存起来
				// 方便后面使用
				uni.setStorageSync('opt', otherparams);
				// 如果不需要手动点击登录, 就把wxlogin放在这里自动触发
				// this.wxlogin();
				// 这里各自业务处理其他逻辑		
				
			}
		},
		methods: {
			// 微信授权登录
			wxlogin() {
				try {
					// 其他业务逻辑
					// 比如加载loading
					// 比如判断隐私协议勾选等等
					
					
					// snsapi_base：用来获取进入页面的用户的openid的，并且是静默授权并自动跳转到回调页的。（不会弹出信息确认框,仅能获取用户 openid 等信息，无法获取昵称头像）
					// snsapi_userinfo：用来获取用户的基本信息的。但这种授权需要用户手动同意。（由于用户同意过，所以无须依赖用户关注服务号，就可在授权后获取该用户的基本信息）
					const snsapiBase = 'snsapi_base';
					// 微信服务号的appid 后台获取或者从配置文件获取
					const appId = 'xxxxxxxx';
					// 微信授权之后的回调地址页面 默认为当前工程首页，请根据自己业务需要自行修改url
					let url = `${location.origin}/h5`
					// 参数redirect_uri
					const redirect_uri = encodeURIComponent(url);
					console.log('url', url);
					console.log('redirect_uri', redirect_uri);
					// 参数state
					const state = '';
					const OAuthUrl =
						`https://open.weixin.qq.com/connect/oauth2/authorize?appid=${appId}&redirect_uri=${redirect_uri}&response_type=code&scope=${snsapiBase}&state=${state}#wechat_redirect`
					// 跳到微信授权页面
					location.href = OAuthUrl;
				} catch (error) {
					console.error('微信授权登录', error);
				}
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