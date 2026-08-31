# 24fiddler

Fiddler （小提琴）是一个功能强大的网络调试工具，可以用于 HTTP/HTTPS 流量 的捕获、分析和调试

什么时候要用到它？

​	1.浏览器的开发者工具不好抓（反爬比较狠）

​	2.不使用浏览器的抓包

注：尽可能用浏览器的开发者工具，因为好看（个人），而且fiddler好多要手动解码



解码懒人方法：工具栏上的 **Decode** 按钮，把它按下（高亮），后续所有新抓的包，收到响应时自动解码



## 界面介绍

在http配置时，有以下配置选项

| 选项                            | 中文翻译           | 作用场景                                                     |
| ------------------------------- | :----------------- | ------------------------------------------------------------ |
| **from all processes...**       | 捕获全部进程       | 默认选项。电脑上浏览器、桌面软件、爬虫脚本，只要走 Fiddler 代理，全部抓下来。日常调试一般选这个。 |
| **from browsers only...**       | 仅浏览器进程       | 只捕获 Chrome、Edge 等浏览器发出的 http/https；桌面软件、APP、脚本流量直接忽略。只调试网页时用，减少杂乱包。 |
| **from non‑browsers only...**   | 仅非选项浏览器进程 | 不抓浏览器，只抓桌面客户端、Python 爬虫、Java 程序、Windows 系统后台服务等软件流量。适合抓软件、爬虫接口，屏蔽浏览器干扰。 |
| **from remote clients only...** | 仅远程客户端       | 不抓本机电脑流量，只抓别的设备过来的流量：比如手机、平板连电脑代理，手机上 APP 的请求。抓手机 APP 包时选这个，本机电脑的请求全部过滤掉，列表干净。 |



### 左侧大界面

#### 上方

\#：顺序号，按照抓包的顺序从 1 递增

**Result**：HTTP 状态码

Protocol：请求使用的协议，如 HTTP/HTTPS/FTP 等

HOST：请求地址的主机名或域名

**URL**：请求资源的位置

**Body**：该条请求产生的数据大小

Caching：请求的缓存过期时间或者缓存控制值

Content-Type：请求响应的类型

**Process**：发送此请求的进程 ID

Comments：备注

Custom：自定义值

#### 下方

Capturing 复选框：

​	打勾：**开启抓包**，Fiddler 作为系统代理，捕获本机网络 HTTP/HTTPS 流量。

​	取消勾选：**停止抓包**，不再捕获新请求，电脑恢复原本网络代理设置。



### 右侧 insepector

每个 Fiddler 抓取到的数据包都会在该列表中展示，点击具体的一条数据包可以在 右侧菜单点击 Insepector 查看详细内容。主要分为请求（即客户端发出的数据）和响 应（服务器返回的数据）两部分，上面是请求，下面是响应

Headers：请求头

TextView：显示请求或响应的数据

WebForms：请求部分以表单形式显示所有的请求参数和参数值；响应部分与TextView 内容是一样的
Auth：授权相关，如果显示如下两行，说明不需要授权，可以不用关注

```
No Proxy-Authorization Header is present.
No Authorization Headeris present.
```

Cookies：显示所有 cookies

Raw：查看一个完整请求的内容，Headers 和 Body 数据

JSON：若请求或响应数据是 json 格式，以 json 形式显示请求或响应内容

XML：若请求或响应数据是 xml 格式，以 xml 形式显示请求或响应内容



## 使用

### 快捷键

全局

| 快捷       | 功能说明                                                    |
| ---------- | ----------------------------------------------------------- |
| F12        | 开启 / 停止抓包（等价勾选左下角 Capturing）                 |
| Ctrl+Alt+F | 全局热键：直接把 Fiddler 窗口调到前台，就算窗口最小化也能用 |
| Alt+Q      | 光标跳到底部 QuickExec 命令输入框                           |
| Ctrl+F     | 查找会话，搜索 URL/Header 内容                              |
| Ctrl+R     | 打开 FiddlerScript 脚本编辑器                               |

会话列表操作 

| 快捷键           | 功能说明                             |
| ---------------- | ------------------------------------ |
| Ctrl+A           | 全选所有会话记录                     |
| ESC              | 取消全部选中                         |
| Ctrl+I           | 反向选择（选中没勾的，取消已选的）   |
| Delete           | 删除选中的会话                       |
| **Shift+Delete** | 删除所有未选中会话，只保留选中的记录 |
| **Ctrl+X**       | 清空全部会话列表（常用）             |
| R                | Replay 重放选中请求，发送 1 次       |
| Shift+R          | 重放，弹出框可设置循环重放次数       |
| M                | 给会话添加注释备注                   |

### 会话列表选中操作

单选：鼠标左键点一行，选中 1 条请求。

连续多选：点第一条，按住`Shift`点最后一条，中间全部选中。

零散跳选：按住`Ctrl`，鼠标点一条条，可间隔选中多条。

取消某一条：按住`Ctrl`，点击已经选中的行，取消该行。

​		注：按住`Ctrl`时无法滚动



## 案例

### 百度

#### 定位请求

方法

​	1.Ctrl+F查找

​	2.Filters 过滤器：右侧 Filters → Use Filters，Hosts 填目标域名，Run Filterset now，只显示目标域名流量

过滤host的选项

| 选项                          | 是否隐藏其他请求       | 使用场景                             |
| ----------------------------- | ---------------------- | ------------------------------------ |
| No Host Filter                | 不隐藏                 | 全部流量，调试初期                   |
| Hide the following Hosts      | 隐藏填写的域名         | 屏蔽广告、无关站点                   |
| Show only the following Hosts | 隐藏全部，只留填写域名 | 定位目标接口，高频                   |
| Flag the following Hosts      | 不隐藏，仅标记颜色     | 需要同时看全部流量，重点标出目标域名 |

​	3.根据数据大小估测(经验方法)



#### 处理请求头

找到后全选复制

```
GET https://www.baidu.com/ HTTP/1.1
Host: www.baidu.com
Connection: keep-alive
Cache-Control: max-age=0
sec-ch-ua: "Not=A?Brand";v="99", "Microsoft Edge";v="151", "Chromium";v="151"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
DNT: 1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36 Edg/151.0.0.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cookie: BDUSS=C1wcDNvRXZMaU9XVFNVLS0tcjJjQmhtbjlNcXVpUnduMmIwTk9FYlA0bU0zSjVwRVFBQUFBJCQAAAAAAQAAAAEAAAD3OsUS6KTkwcrxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIxPd2mMT3dpc; BDUSS_BFESS=C1wcDNvRXZMaU9XVFNVLS0tcjJjQmhtbjlNcXVpUnduMmIwTk9FYlA0bU0zSjVwRVFBQUFBJCQAAAAAAQAAAAEAAAD3OsUS6KTkwcrxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIxPd2mMT3dpc; PSTM=1771045585; BIDUPSID=475DC635C028635EAC223AB6F4AB974D; PAD_BROWSER=1; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1771265603; COOKIE_SESSION=4488_0_9_9_4_73_1_0_8_7_12_13_1973707_0_14_0_1773239186_0_1773239172%7C9%23634991_24_1765372316%7C5; ZFY=yF3FARuEExdbh8214:BY9KaMgEGbZ8L7VEkfg6Oi3oJo:C; BAIDUID=83C5F2AEC00F6F98EB242F6CEEE7303B:FG=1; BAIDUID_BFESS=83C5F2AEC00F6F98EB242F6CEEE7303B:FG=1; SMARTINPUT=%5Bobject%20Object%5D; BAIDUID_REF=83C5F2AEC00F6F98EB242F6CEEE7303B:FG=1; BDPASSGATE=IlPT2AEptyoA_yiU4SO43lIN8eDEUsCD34OtVnti3ECGh67BmhGv4dx0F6zLN7_tB5Ll-YyfmqxPpjrFV6xjg0N_gRsLhkd6dCzaubmls10vL0tesKMeIKbcYiY4trzIfRhL-3MEF3VEVFoKhAP2pvwQehTT7xBIhR4I7FKyh1rs2CCD17n_xHyQ19tKLHvfKtiFwvrXnHlKXyafA4HiSC8yhCIiCHcrzcyOatMlDA_DuX5XGurSRvAa3GjQHWl3EQy61eaQkL8TCkocwpdYSkUtdEiV5tD6Mk960Bz7j_haQqjhMKb4OIe3_1o2nNnbLQdWKQ3zmtkGDV9Y95ssJo2rRa0FIWzGKpwKLMigiBjZCXwVqlOEIwDLvIA5RrXoFOIXZApDSVBaiyefnNWmpSr2HwPgi0FvM0wGCXOYyZl46pN3Gm4K6Hqzc7Jv-p_dT9OKG6zd3cHlT7VFquKyJaXaVKr82VEbqimagCXNek8MDwzdFdB7kzgCwnV7TWiB9QeHNTCqX4vt5MF9srXqvszDu9SUqzaZwEipLc374wB5YUI1jR6rCmjJzGy_eXx_O4Gduo4wWD0fm5FDstyIjyZnlPA01NJKO0L4BR-b7cSIkWwV0yYto_Sz3wNf1-zkjuBUIcT4T9af2l0VZnxmgrtA2V4vIJTzvtLgQDVmEj_VYzzaC_RxwF-2eHIWORf1OCy-odUQXi4tosQKOcaip7diFOEjEi25vXzj4mf2CRnv70JGkl58th1nOHGsZvTU6Y55iLgqUyCuyrbWCwf5gzE25nrebNB4ALaMWF858FKyIBEq-nnzEFyXxK; delPer=0; PSINO=7; H_WISE_SIDS_BFESS=110085_667682_691780_694235_702753_645234_707515_708077_708854_706863_710571_711399_711496_711497_711500_711502_711503_711701_711822_711807_711873_712192_711920_712624_712620_712646_713045_713346_713059_713740_713822_713817_713811_713848_713707_713743_714092_713830_714222_714210_714285_714324_713351_714519_714564_712397_714975_714803_714363_715066_715195_715199_715301_715279_715316_715326_715273_715108_715514_715532_716019_714986_715985_716085_716070_716075_716077_714848_716101_716104_716215_716224_716220_716250_716246_715860_716390_716436_712917_709173_716641_716667_716671_716692_716535_716676_716829_716814_716846_716839_716849_714786_716759_716883_716868_716873_716866_716972_716683_717126_717147_717157_717145_717134_717194_717190_717198_716906_713066_716893_717251_717296_717362_717369_717339_717350_717357_717523_717542_717526_717563_717713_717710_717796_717813_717742_717752_717583_717566_8000054_8000126_8000137_8000149_8000162_8000166_8000168_8000177_8000176_8000185_8000189_8000204_8000210; SE_LAUNCH=5%3A1788084853; BDORZ=AE84CDB3A529C0F8A2B9DCDD1D18B695; BA_HECTOR=ah0h212g05000h0h802ga5a0000h241l980jo29; rsv_i=1bcbp5GoU55mI1Pd4fdnWCmupC+9/rEuGEYzmPGHekgRU30ag+MpCpt8up+N5JVe8lZnmTElP6LfLs0Tjhf6877uRWyU88o; H_PS_PSSID=63141_67862_71501_72028_72661_72694_72762_72950_73001_73011_73039_73028_73052_73117_73109_73219_73231_73234_73263_73160_73212_73309_73286_73399_73386_73357_73364_73414_73447_73449_73451_73559_73540_73594_73599_73046_73662_73705_73712_73714_73731_73723_73726_73756_73742_73699_73649_73651_73747_73721_73740_73782_73784_73787_73779_73785_73796_73793_73790_73828_73831_73843_73865_73886_73896_73908_73920_73922_73939_73950_73952; BD_UPN=12314753; H_WISE_SIDS=63141_67862_71501_72028_72661_72694_72762_72950_73001_73011_73039_73028_73052_73117_73109_73219_73231_73234_73263_73160_73212_73309_73286_73399_73386_73357_73364_73414_73447_73449_73451_73559_73540_73594_73599_73046_73662_73705_73712_73714_73723_73726_73756_73742_73699_73649_73651_73747_73721_73740_73782_73784_73787_73779_73785_73796_73793_73790_73828_73831_73843_73865_73886_73896_73908_73920_73922_73939_73950_73952


```

观察可得其由两部分组成：GET https://www.baidu.com/ HTTP/1.1(请求方式，请求路径，协议版本)与 headers



改造（正则）headers 备用

`(.*?):(.*)  ->  '$1':'$2'`

```
GET https://www.baidu.com/ HTTP/1.1

'Host':' www.baidu.com'
'Connection':' keep-alive'
'Cache-Control':' max-age=0'
'sec-ch-ua':' "Not=A?Brand";v="99", "Microsoft Edge";v="151", "Chromium";v="151"'
'sec-ch-ua-mobile':' ?0'
'sec-ch-ua-platform':' "Windows"'
'DNT':' 1'
'Upgrade-Insecure-Requests':' 1'
'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36 Edg/151.0.0.0'
'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
'Sec-Fetch-Site':' none'
'Sec-Fetch-Mode':' navigate'
'Sec-Fetch-User':' ?1'
'Sec-Fetch-Dest':' document'
'Accept-Encoding':' gzip, deflate, br, zstd'
'Accept-Language':' zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
'Cookie':' BDUSS=C1wcDNvRXZMaU9XVFNVLS0tcjJjQmhtbjlNcXVpUnduMmIwTk9FYlA0bU0zSjVwRVFBQUFBJCQAAAAAAQAAAAEAAAD3OsUS6KTkwcrxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIxPd2mMT3dpc; BDUSS_BFESS=C1wcDNvRXZMaU9XVFNVLS0tcjJjQmhtbjlNcXVpUnduMmIwTk9FYlA0bU0zSjVwRVFBQUFBJCQAAAAAAQAAAAEAAAD3OsUS6KTkwcrxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIxPd2mMT3dpc; PSTM=1771045585; BIDUPSID=475DC635C028635EAC223AB6F4AB974D; PAD_BROWSER=1; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1771265603; COOKIE_SESSION=4488_0_9_9_4_73_1_0_8_7_12_13_1973707_0_14_0_1773239186_0_1773239172%7C9%23634991_24_1765372316%7C5; ZFY=yF3FARuEExdbh8214:BY9KaMgEGbZ8L7VEkfg6Oi3oJo:C; BAIDUID=83C5F2AEC00F6F98EB242F6CEEE7303B:FG=1; BAIDUID_BFESS=83C5F2AEC00F6F98EB242F6CEEE7303B:FG=1; SMARTINPUT=%5Bobject%20Object%5D; BAIDUID_REF=83C5F2AEC00F6F98EB242F6CEEE7303B:FG=1; BDPASSGATE=IlPT2AEptyoA_yiU4SO43lIN8eDEUsCD34OtVnti3ECGh67BmhGv4dx0F6zLN7_tB5Ll-YyfmqxPpjrFV6xjg0N_gRsLhkd6dCzaubmls10vL0tesKMeIKbcYiY4trzIfRhL-3MEF3VEVFoKhAP2pvwQehTT7xBIhR4I7FKyh1rs2CCD17n_xHyQ19tKLHvfKtiFwvrXnHlKXyafA4HiSC8yhCIiCHcrzcyOatMlDA_DuX5XGurSRvAa3GjQHWl3EQy61eaQkL8TCkocwpdYSkUtdEiV5tD6Mk960Bz7j_haQqjhMKb4OIe3_1o2nNnbLQdWKQ3zmtkGDV9Y95ssJo2rRa0FIWzGKpwKLMigiBjZCXwVqlOEIwDLvIA5RrXoFOIXZApDSVBaiyefnNWmpSr2HwPgi0FvM0wGCXOYyZl46pN3Gm4K6Hqzc7Jv-p_dT9OKG6zd3cHlT7VFquKyJaXaVKr82VEbqimagCXNek8MDwzdFdB7kzgCwnV7TWiB9QeHNTCqX4vt5MF9srXqvszDu9SUqzaZwEipLc374wB5YUI1jR6rCmjJzGy_eXx_O4Gduo4wWD0fm5FDstyIjyZnlPA01NJKO0L4BR-b7cSIkWwV0yYto_Sz3wNf1-zkjuBUIcT4T9af2l0VZnxmgrtA2V4vIJTzvtLgQDVmEj_VYzzaC_RxwF-2eHIWORf1OCy-odUQXi4tosQKOcaip7diFOEjEi25vXzj4mf2CRnv70JGkl58th1nOHGsZvTU6Y55iLgqUyCuyrbWCwf5gzE25nrebNB4ALaMWF858FKyIBEq-nnzEFyXxK; delPer=0; PSINO=7; H_WISE_SIDS_BFESS=110085_667682_691780_694235_702753_645234_707515_708077_708854_706863_710571_711399_711496_711497_711500_711502_711503_711701_711822_711807_711873_712192_711920_712624_712620_712646_713045_713346_713059_713740_713822_713817_713811_713848_713707_713743_714092_713830_714222_714210_714285_714324_713351_714519_714564_712397_714975_714803_714363_715066_715195_715199_715301_715279_715316_715326_715273_715108_715514_715532_716019_714986_715985_716085_716070_716075_716077_714848_716101_716104_716215_716224_716220_716250_716246_715860_716390_716436_712917_709173_716641_716667_716671_716692_716535_716676_716829_716814_716846_716839_716849_714786_716759_716883_716868_716873_716866_716972_716683_717126_717147_717157_717145_717134_717194_717190_717198_716906_713066_716893_717251_717296_717362_717369_717339_717350_717357_717523_717542_717526_717563_717713_717710_717796_717813_717742_717752_717583_717566_8000054_8000126_8000137_8000149_8000162_8000166_8000168_8000177_8000176_8000185_8000189_8000204_8000210; SE_LAUNCH=5%3A1788084853; BDORZ=AE84CDB3A529C0F8A2B9DCDD1D18B695; BA_HECTOR=ah0h212g05000h0h802ga5a0000h241l980jo29; rsv_i=1bcbp5GoU55mI1Pd4fdnWCmupC+9/rEuGEYzmPGHekgRU30ag+MpCpt8up+N5JVe8lZnmTElP6LfLs0Tjhf6877uRWyU88o; H_PS_PSSID=63141_67862_71501_72028_72661_72694_72762_72950_73001_73011_73039_73028_73052_73117_73109_73219_73231_73234_73263_73160_73212_73309_73286_73399_73386_73357_73364_73414_73447_73449_73451_73559_73540_73594_73599_73046_73662_73705_73712_73714_73731_73723_73726_73756_73742_73699_73649_73651_73747_73721_73740_73782_73784_73787_73779_73785_73796_73793_73790_73828_73831_73843_73865_73886_73896_73908_73920_73922_73939_73950_73952; BD_UPN=12314753; H_WISE_SIDS=63141_67862_71501_72028_72661_72694_72762_72950_73001_73011_73039_73028_73052_73117_73109_73219_73231_73234_73263_73160_73212_73309_73286_73399_73386_73357_73364_73414_73447_73449_73451_73559_73540_73594_73599_73046_73662_73705_73712_73714_73723_73726_73756_73742_73699_73649_73651_73747_73721_73740_73782_73784_73787_73779_73785_73796_73793_73790_73828_73831_73843_73865_73886_73896_73908_73920_73922_73939_73950_73952'
```

再加上url就可以发请求了

```
import requests

url = 'https://www.baidu.com/'
headers = {
    'Host': 'www.baidu.com',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Microsoft Edge";v="146"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cookie': 'BIDUPSID=0D487EFDA1CD47B345722635F50A749A; PSTM=1769601690; BAIDUID=0D487EFDA1CD47B35D826ECEF6365265:FG=1; BD_UPN=12314753; BAIDUID_BFESS=0D487EFDA1CD47B35D826ECEF6365265:FG=1; H_WISE_SIDS_BFESS=60272_63145_67084_67496_67600_67722_67754_67834_67862_67884_67888_67894_67947_67952_67953_67956_67965_67979_68009_68050_68087_67986_68004_68127_68130_68142_68145_68139_68184; __bid_n=19cae87fd101152a6a53c9; H_WISE_SIDS=60272_63145_67722_67862_67888_68050_67986_68004_68130_68142_68145_68139_68192_68228_68262_68267_68297_68308_68335_68423_68433_68455_68513_68542_68537_68547_68552_68580_68503_68518_68623_68611_68605_68681_68677_68697_68545_68729_68789; v=A7AwBwFhrXjThXF8lnSqwszPgXUH-ZRDtt3oR6oBfIveZV6rUglk0wbtuNb5; BAIDU_WISE_UID=wapp_1775133935999_669; COOKIE_SESSION=176171_0_5_5_1_5_1_0_5_5_3_0_0_0_0_0_1775737900_0_1775914068%7C5%230_0_1775914068%7C1; ZFY=Yavu166cI67DMR1e3:BWbYeGu5hYSPPyB7TO:Am:ANfRto:C; baikeVisitId=804cbfca-1173-4c32-9dd2-5552e3eea516; PAD_BROWSER=1; RT="z=1&dm=baidu.com&si=59707659-1feb-4a27-995f-5883b79ed287&ss=moh6y60z&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=36m&ul=17zr0&hd=17zrg"; H_PS_PSSID=60272_63145_67722_67862_68297_68423_68455_68542_68580_68697_68789_69014_69039_69081_69185_69169_69202_69226_69245_69239_69230_69234_69292_69294_68779_69317_69251_69252_69254_69257_69258_68907_69354_69359_69398_69400_69396_69420_69416_69413_69446_69449_69437_69343_69339_69346_69345_69348_69350_69341_69493_69501_69504_69559_69554_69574_69594_69607; BD_HOME=1; BA_HECTOR=200g01200h8l2g2k818k8ha0ag2ha71kv199427',
}
response = requests.get(url, headers=headers)
print(response.text)
```





补充：

`()`抓内容，替换用`$1`拿出来

`*`尽量多，`*?`尽量少

`^`开头`$`结尾

元字符要匹配字面，记得加反斜杠`\`

