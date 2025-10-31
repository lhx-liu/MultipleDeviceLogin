# 钉钉计算签名脚本
import hashlib
import urllib.parse
from urllib.parse import urlparse
# 添加time模块用于获取当前时间戳
import time
# 添加requests模块用于发送HTTP请求
import requests

def byte_to_hex(buffer):
    """
    字节数组转化成十六进制字符串
    """
    return buffer.hex()

def decode_url(url_string):
    """
    因为ios端上传递的url是encode过的，android是原始的url。开发者使用的也是原始url,
    所以需要把参数进行一般urlDecode
    
    :param url_string: URL字符串
    :returns: 解码后的URL
    """
    try:
        parsed_url = urlparse(url_string)
        url_buffer = f"{parsed_url.scheme}:"
        if parsed_url.netloc:
            url_buffer += f"//{parsed_url.netloc}"
        if parsed_url.path:
            url_buffer += parsed_url.path
        if parsed_url.query:
            url_buffer += f"?{urllib.parse.unquote(parsed_url.query)}"
        return url_buffer
    except Exception as error:
        print(f"Error in decode_url function: {error}")
        raise error

def get_access_token(app_key, app_secret):
    """
    获取访问令牌
    
    :param app_key: 应用的appKey
    :param app_secret: 应用的appSecret
    :returns: accessToken
    """
    url = "https://api.dingtalk.com/v1.0/oauth2/accessToken"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "appKey": app_key,
        "appSecret": app_secret
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        # 检查HTTP状态码
        if response.status_code != 200:
            error_result = response.json()
            print(f"获取access_token失败: {error_result}")
            raise Exception(f"获取access_token失败: {error_result.get('message', '未知错误')}")
        
        result = response.json()
        # 检查返回结果是否包含accessToken
        if "accessToken" not in result:
            raise Exception("返回结果中未包含accessToken字段")
            
        return result["accessToken"]
    except requests.exceptions.RequestException as e:
        print(f"网络请求异常: {e}")
        raise Exception(f"网络请求异常: {e}")
    except ValueError as e:
        # JSON解析失败
        print(f"响应JSON解析失败: {e}")
        raise Exception(f"响应JSON解析失败: {e}")
    except Exception as e:
        print(f"获取access_token时发生未知错误: {e}")
        raise e

def get_jsapi_ticket(access_token):
    """
    获取JSAPI票据
    
    :param access_token: 访问令牌
    :returns: jsapiTicket
    """
    url = "https://api.dingtalk.com/v1.0/oauth2/jsapiTickets"
    headers = {
        "x-acs-dingtalk-access-token": access_token,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, headers=headers, json={})
        # 检查HTTP状态码
        if response.status_code != 200:
            error_result = response.json()
            print(f"获取jsapi_ticket失败: {error_result}")
            raise Exception(f"获取jsapi_ticket失败: {error_result.get('message', '未知错误')}")
        
        result = response.json()
        # 检查返回结果是否包含jsapiTicket
        if "jsapiTicket" not in result:
            raise Exception("返回结果中未包含jsapiTicket字段")
            
        return result["jsapiTicket"]
    except requests.exceptions.RequestException as e:
        print(f"网络请求异常: {e}")
        raise Exception(f"网络请求异常: {e}")
    except ValueError as e:
        # JSON解析失败
        print(f"响应JSON解析失败: {e}")
        raise Exception(f"响应JSON解析失败: {e}")
    except Exception as e:
        print(f"获取jsapi_ticket时发生未知错误: {e}")
        raise e

def sign(jsticket, nonce_str, time_stamp, url):
    """
    计算dd.config的签名参数 signature
    
    :param jsticket: 通过微应用appKey获取的jsticket
    :param nonce_str: 自定义固定字符串
    :param time_stamp: 当前时间戳
    :param url: 调用dd.config的当前页面URL
    :returns: 签名
    """
    try:
        plain = f"jsapi_ticket={jsticket}&noncestr={nonce_str}&timestamp={time_stamp}&url={decode_url(url)}"
        sha256 = hashlib.sha256()
        sha256.update(plain.encode('utf-8'))
        newJsticket = byte_to_hex(sha256.digest())
        print('生成票据时间戳=》' + time_stamp)
        print('生成sign=》' + newJsticket)
        print('生成签名成功，请将上述时间戳及签名放到前台dd.config中！')
        return byte_to_hex(sha256.digest())
    except Exception as error:
        print(f"Error in sign function: {error}")
        raise error
    
if __name__ == "__main__":
    # 应用凭证信息
    APP_KEY = "your_app_key_here"
    APP_SECRET = "your_app_secret_here"
    
    try:
        # 获取访问令牌
        access_token = get_access_token(APP_KEY, APP_SECRET)
        
        # 获取JSAPI票据
        jsticket = get_jsapi_ticket(access_token)
        
        _nonce_str = "123456"
        # 当前时间戳改为实时获取
        _time_stamp = str(int(time.time()))
        _url = "your_current_page_url_here"
        sign(jsticket, _nonce_str, _time_stamp, _url)
    except Exception as e:
        print(f"程序执行出错: {e}")