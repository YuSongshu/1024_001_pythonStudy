# 16自动化（Playwright 初识）

Playwright 是一个开源的自动化库，由 Microsoft 开发，用于基于 Chromium,  Firefox, 和 WebKit 的**浏览器自动化**。它支持多种语言，包括 Python，并能在  Windows, Linux, 和 macOS 上运行。

官方文档：https://playwright.dev/python/docs/api/class-elementhandle



测试工程师：测试项目是否存在 bug

为什么用 Playwright

1.天然支持三大浏览器内核，一套代码多端运行

2.自动等待，极大减少

3.不用逆向

4.反爬手段少



## 安装

python -m playwright install

安装在这个目录：C:\Users\你自己电脑名称\AppData\Local\ms-playwright

注·：安装之后不要移动位置。



## 使用

基础

```
# 导包
from playwright.sync_api import sync_playwright

# 创建playwright对象  =》 需要通过 python 操作浏览器， 所以需要拿到这个工具【playwright 对象】
pw = sync_playwright().start()

# 启动浏览器
browser = pw.chromium.launch(headless=False)

# 创建上下文管理器（管理所管理的页面，关闭管理器，所以页面关闭）
context = browser.new_context()

# 打开一个页面）（相当于+号，重新打开一个页面）
page = context.new_page()

# 访问网站
page.goto('https://www.baidu.com')

# page.wait_for_timeout(1000)
# page.locator('//*[@id="chat-textarea"]').fill("hello world")

# 等待时长 =》让浏览器等待一会再关闭（不加就闪退，因为这是一个程序，会结束）
page.wait_for_timeout(10000)

#关闭资源
page.close()
browser.close()
context.close()
```

```
from playwright.sync_api import sync_playwright

pw = sync_playwright().start()
browser = pw.chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()
page.goto('网址')
```

### page对象

获取页面源码： page.content() =>html

获取页面标题： page.title() 

获取页面 url： page.url



locator = page.locator(selector)

元素定位器

selector 支持三种主流写法：

1.CSS 选择器（优先推荐，速度最快）

2.XPath

3.Playwright 内置语义选择器（`text=`、`role=` 等，稳定性极强）



推荐 XPath （复制简单）

```
from playwright.sync_api import sync_playwright
pw = sync_playwright().start()
browser = pw.chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()
page.goto('https://www.baidu.com')
page.wait_for_timeout(1000)
page.locator('//*[@id="chat-textarea"]').fill("hello world")

page.wait_for_timeout(10000)
```

表示百度搜索框输入 hello world 





## 元素操作

获取所有元素： 元素对象.all() 

获取文本：   元素对象.inner_text() 

获取所有文本： 元素对象.all_inner_texts() 

获取元素属性：   元素对象.get_attribute() 

输入：元素对象.fill(文本内容) 

点击：元素对象.click()



应用

1.在百度搜索框里面输入 “熊猫”，然后点击搜索

```
from playwright.sync_api import sync_playwright

pw = sync_playwright().start()
browser = pw.chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()
page.goto('https://www.baidu.com')

page.wait_for_timeout(1000)

# xpath 定位
baidu_input = page.locator('//*[@id="chat-textarea"]')
button = page.locator('//*[@id="chat-submit-button"]')
if baidu_input.count() != 0:
    print("输入文本")
    baidu_input.fill("熊猫")
else:
    print("元素不存在")
    
page.wait_for_timeout(500)
button.click()
```

playwright 在使用给定的 xpath 定位不到元素的时候，不会报错，但是拿这个没有定位到元素的对象去做操作则会报错

最好是先判断是否存在这个元素

```
if baidu_input.count() != 0:
    print("输入文本")
    baidu_input.fill("熊猫")
else:
    print("元素不存在")
```







2..在百度获取文本

```
from playwright.sync_api import sync_playwright

pw = sync_playwright().start()
browser = pw.chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()
page.goto('https://www.baidu.com')

page.wait_for_timeout(1000)

# xpath 定位
baidu_input = page.locator('//*[@id="chat-textarea"]')
button = page.locator('//*[@id="chat-submit-button"]')
li_list = page.locator('//*[@id="hotsearch-content-wrapper"]/li').all()
print(li_list)
print(type(li_list))

for li in li_list:
    # 如果路径语法是以 // 开头的，默认表示是 xpath 语法，如果不是就要加xpath=
    title = li.locator('xpath=./a/span[2]').inner_text()
    print(title)
button.click()
```



## 鼠标操作

演示测试网址

```
https://www.helloweba.net/demo/2017/unlock/
```

### 移动鼠标

 page.mouse.down()：按下鼠标 

page.mouse.move(x, y)：移动鼠标 

page.mouse.up()：释放鼠标 

### 获取元素坐标 

元素对象.bounding_box()



注：坐标是以左上角为圆心，向下为y轴正方向与向左为x轴正方向



示例

```
from playwright.sync_api import sync_playwright

pw = sync_playwright().start()
browser = pw.chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()
page.goto('https://www.helloweba.net/demo/2017/unlock/#google_vignette')

page.wait_for_timeout(1000)
hk = page.locator('xpath=/html/body/div[1]/div[1]/div/div[1]/div[1]/div[3]')

hk_location = hk.bounding_box()
print(hk_location) # {'x': 68, 'y': 190.7916717529297, 'width': 37, 'height': 38}
page.mouse.move(hk_location['x']+hk_location['width']/2, hk_location['y']+hk_location['height']/2)
page.wait_for_timeout(1000)

page.mouse.down()

box = page.locator('//html/body/div/div/div/div[1]/div[1]/div[1]')
box_location = box.bounding_box()
print(box_location) # {'x': 68, 'y': 190.7916717529297, 'width': 298, 'height': 38}
page.mouse.move(hk_location['x'] + box_location['width'], hk_location['y'])
page.wait_for_timeout(1000)

page.mouse.up()

page.wait_for_timeout(3000)
```

page.mouse.move(hk_location['x']+hk_location['width']/2, hk_location['y']+hk_location['height']/2)原因

滑块左上角是它的坐标，可能点不到，故xy轴加一点



## 复杂的验证

 图文、滑块、点选     可以用ai
ai有免费和收费。免费的处理，可能会出错
不想花钱
手动处理（自动化是可以手动加入操作的。）

```

print("请手动处理验证码")
page.wait_for_timeout(5000)

print("通过验证，做其他事情")
page.wait_for_timeout(3000)
```

应用

```
from playwright.sync_api import sync_playwright

pw = sync_playwright().start()
browser = pw.chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()
page.goto('https://www.baidu.com')

page.wait_for_timeout(1000)

# xpath 定位
baidu_input = page.locator('//*[@id="chat-textarea"]')
button = page.locator('//*[@id="chat-submit-button"]')


if baidu_input.count() != 0:
    print("输入文本")
    baidu_input.fill("熊猫")
    button.click()\

else:
    print("元素不存在")
    
print("手动处理验证码")
page.wait_for_timeout(15000)

page.wait_for_timeout(333000)
```

