#  requests发送请求

requests是 Python 爬虫开发中最常使用到的库，它提供了简单易用的API，使得
在 Python 中发送 HTTP 请求变得非常容易

库是什么？
​    如果你们只学习 Python 基础，让你去开发游戏，用什么知识点？
​    pygame：封装，类里面实现了游戏开发的功能。
​        把别人封装好的这个工具，拿过来使用。
​    让你们去对百度首页发请求，你怎么做？
​        Python基础没有办法实现的东西，别人有没有制作好工具，直接使用。
​            requests

pip是什么？
​    专门用来管理这些工具。
​    去百度搜 =》别人实现的代码段。
​    你要用的这个工具叫什么名字。
​    pip 库管理工具【帮你拿功能库（pygame）的工具】
如何使用？
​    pip install 库名称    =》使用 pip 工具 安装 库
​    安装 requests 库：pip install requests
​         already 表示已经安装过。
​         黄色表示警告：不用管
​         红色表示报错：表示没下载成功

            1. 网络问题
                为什么会存在网络问题？
                ​    工具存放在哪里？
                ​        国外【进口】
                ​        能不能用国内的？
                ​            可以

                -i
                pip install requests -i 镜像原地址
                ​    -i 指定镜像原地址：表示工具从哪个地方拿
                ​    其他国内镜像源
                ​        清华大学TUNA镜像源： https://pypi.tuna.tsinghua.edu.cn/simple
                ​        阿里云镜像源： http://mirrors.aliyun.com/pypi/simple/
                ​        中国科学技术大学镜像源： https://mirrors.ustc.edu.cn/pypi/simple/
                ​        华为云镜像源： https://repo.huaweicloud.com/repository/pypi/simple/
                ​        腾讯云镜像源：https://mirrors.cloud.tencent.com/pypi/simple/
                ​    pip install requests -i http://mirrors.aliyun.com/pypi/simple/
                ​    pip install pygame -i http://mirrors.aliyun.com/pypi/simple/

                            2. 名称问题【版本】



## requests 使用：

     import requests
    response = requests.get(url,headers=headers,params,timeout)
    

参数说明：
​    • url：要抓取的 url 地址；【必须传递】
​    【下面的都是可选】
​    • headers：用于包装请求头信息；
​    • params：请求时携带的查询字符串参数；
​    • timeout：超时时间，超过时间会抛出异常；
返回值：
​    • response：返回页面响应对象；
​        响应对象可以调用的一些属性和方法

url 参数在真正发送请求的时候，并不是直接复制地址栏的网址。
​    发送请求本质是模拟浏览器的行为 =》需要看浏览器做了什么。

## 开发者工具 - 网络：

监控【请求/抓包】：
​        监视浏览器做了什么事情。



响应
​    网站给我们的东西叫响应。
​    响应对象里面的东西。
​    报纸文章 =》报文
​    搜索快捷键：
​        ctrl+f

响应里面的属性和方法：
响应内容：
​    • text： 以字符串形式输出【获取响应文本】
​        针对文本数据
​    • content： 以字节流形式输出，若要保存下载图片需使用该属性
​        针对媒体数据
​    • json()： 获取json数据【暂时忽略】
响应属性：
​    • encoding： 查看或者指定响应字符编码
​    • status_code： 返回 HTTP 响应码
​    • url： 查看请求的 url 地址
​    • cookies： 查看 cookies

浏览器中使用：
​    在浏览器里面直接搜索响应内容：
​        1. 点击响应内容里面
​        2. ctrl+f
​    定位请求 - 搜索：
​        1. 点击任意一个请求
​        2. ctrl+f


