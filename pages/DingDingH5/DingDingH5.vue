<template>
	<view>
		code为：{{code}}
	</view>
</template>

<script>
	import * as dd from 'dingtalk-jsapi'; // 此方式为整体加载，也可按需进行加载 
	export default {
		data() {
			return {
				code: ''
			}
		},
		onLoad() {
			// 判断是否在钉钉平台
			if (dd.env.platform === "notInDingTalk") {
				uni.showToast({
					icon: 'none',
					title: '请在钉钉应用中打开'
				});
				return;
			}
			this._autoLogin();
		},
		methods: {
			_autoLogin() {
				const that = this;
				// 钉钉h5平台
				dd.requestAuthCode({
					corpId: 'dinge7f2890a997ec0c5f2c783f7214b6d69',
					clientId: 'dingqisx24r48bmgmb3t',
					onSuccess: function(result) {
						/*{
						    code: 'hYLK98jkf0m' //string authCode
						}*/
						// 比如成功获取code后这里可以进行dd.config
						// 如果前台涉及到鉴权的接口 这个方法必须执行
						that.ddconfig();
						that.code = result.code;
						// 正常这里开始进行后续业务逻辑
						// ...do something
					},
					onFail: function(err) {
						that.code = JSON.stringify(err);
					},
				});
			},
			/**
			 * 钉钉H5微应用JSAPI鉴权示例
			 * 针对当前单页面应用 只需鉴权一次即可
			 */
			ddconfig() {
				uni.showToast({
					icon: 'none',
					title: '开始配置dd.config'
				})
				dd.config({
					agentId: '4045610093', // 企业内部应用，该值为企业内部应用的agentId。
					corpId: 'dinge7f2890a997ec0c5f2c783f7214b6d69', //必填，企业ID
					timeStamp: '1761804057', // 必填，生成签名的时间戳
					nonceStr: '123456', // 必填，自定义固定字符串。
					signature: '789320d45372deec14640492cb9c99701d31763a5680a674dc09222c0193d7c6', // 必填，签名
					type: 0, //选填。0表示微应用的jsapi,1表示服务窗的jsapi；不填默认为0。该参数从dingtalk.js的0.8.3版本开始支持
					jsApiList: [
						'device.geolocation.get',
						'chooseChat',
						'biz.contact.choose'
					] // 必填，需要使用的jsapi列表，注意：不要带dd。
				});
				//该方法必须带上，用来捕获鉴权出现的异常信息，否则不方便排查出现的问题
				dd.error(function(err) {
					alert('dd error: ' + JSON.stringify(err));

				})
				// 调用示例
				this.jsApiTest();
			},
			// 钉钉jsapi调用示例
			jsApiTest() {
				const that = this;
				// 钉钉获取当前位置示例 PC端不支持
				dd.getLocation({
					type: 1,
					useCache: true,
					coordinate: '1',
					cacheTimeout: 20,
					withReGeocode: true,
					targetAccuracy: '200',
					success: (res) => {
						const {
							city,
							address,
							accuracy,
							latitude,
							province,
							longitude
						} = res;
						console.log('res', res)
					},
					fail: (e) => {
						console.log('获取位置失败', e)
					},
					complete: () => {},
				});
				// 调用钉钉会话示例
				dd.chooseChat({
					corpId: `dinge7f2890a997ec0c5f2c783f7214b6d69`,
					isAllowCreateGroup: true,
					filterNotOwnerGroup: true,
					success: (res) => {
						const {
							title,
							chatId,
							openConversationId
						} = res;
						console.log('res', res);
					},
					fail: (e) => {
						console.error('e', e);
					},
					complete: () => {},
				});
			}
		}
	}
</script>

<style>

</style>