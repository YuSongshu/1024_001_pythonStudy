# 17playwright进阶

## with管理

离开代码块（正常结束 / 抛出异常）：**自动执行资源回收**，避免进程残留、内存泄漏。（不用写close）

```
# 如果用 with 管理，不要加上 .start() 方法
with sync_playwright() as pw:
    # pw = sync_playwright().start()

    browser = pw.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.baidu.com')
```





## 等待机制

为什么要等待？

脚本与浏览器存在**时序差**



指定时间等待： page.wait_for_timeout(毫秒) 

等待加载完成： page.wait_for_load_state('load') 

等待元素状态： page.wait_for_selector(元素, state=状态)

​		visible：等待某个元素可见

​		hidden：等待某个元素隐

```
Literal["domcontentloaded", "load", "networkidle"]
```

domcontentloaded：html 文本，html文本加载【管不管文本中的资源加载了没有】

load：包含资源，资源加载完成

networkidle：不再需要网络了

page.wait_for_load_state("networkidle")





## iframe

网页文本中有的，响应文本中可能没有，故网页中复制的xpath可能无效

iframe：内联框架

作用：在当前页面嵌入另一个独立 HTML 页面

相当于页面中的页面

因为不是同一个html，故要切换html（创建新的对象）

```
frame = page.frame("iframe名称")
```



```
import time
from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://qzone.qq.com/')

    # 切换 html =》 iframe
    login_frame = page.frame('login_frame')

    # 点击密码登录 =》 iframe
    password_login = login_frame.locator('//*[@id="switcher_plogin"]')
    if password_login.count() != 0:
        password_login.click()
        print("点击成功")
    else:
        print("密码登录不存在")

    page.wait_for_timeout(1000)

    # 输入用户名
    user_ele = login_frame.locator('//*[@id="u"]')
    user_ele.fill("13800@qq.com")

    page.wait_for_timeout(1000)

    # 输入密码
    password_ele = login_frame.locator('//*[@id="p"]')
    password_ele.fill("123456")

    time.sleep(3)
```



## 翻页

### 点击翻页

通过点击“下一页”的xpath实现

```
next_ele = page.locator('//*[@id="content"]/div/div[1]/div[2]/span[3]/a')
next_ele.click()
```

滚动到元素可见：元素对象.scroll_into_view_if_needed()

```
next_ele = page.locator('//*[@id="content"]/div/div[1]/div[2]/span[3]/a')
next_ele.scroll_into_view_if_needed()
page.wait_for_timeout(1000)
next_ele.click()
```



## 通过 js 代码滚动

有些网页下滑才加载内容，这时可以通过 js 代码滚动

```
js = "window.scrollTo(0, document.body.scrollHeight)"
page.evaluate(js代码)
```

示例

```
js_code = "window.scrollTo(0, 500)"
page.evaluate(js_code)
page.wait_for_timeout(1000)
```

注

document.body.scrollHeight 在网页的控制台可以查看网页上下长度

翻页可以加入循环



## 滚动鼠标

```
page.mouse.wheel(delta_x, delta_y)
```

示例

```
js_code = "document.body.scrollHeight"
height = page.evaluate(js_code)
page.mouse.wheel(0, height)
page.wait_for_timeout(1000)
```





## 下载图片

playwright 如何下载图片呢？ 

### 响应监听

监听要放在访问之前

```
page.on('response', 回调函数)
```

demo

```
import time
from playwright.sync_api import sync_playwright

def download_print(response):
	print(f"响应的url：{response.url}")
with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # 监听事件：响应
    page.on('response', download_print)

    page.goto('https://www.baidu.com')

    time.sleep(3)
```



通过判断过滤掉自己不需要的响应【响应对象】，url ，headers

若要下载图片可以通过 Content_type的image/jpeg类型来筛选，下载通过 open 写入响应体作为图片

```
content_type = response.headers.get('content-type')
if content_type and 'image' in content_type:    #有些响应没有content_type会报错，故加它判定content_type是否存在
	with open("a.png", "wb") as f:
		# 响应体
		f.write(response.body())
```

批量获取图片名称

```
filename = response.url.split('/')[-1]
```

注

```
with open("images/" + filename, "wb") as f:
```

表示图片存在当前目录的images文件夹里（images要提前创建好）

