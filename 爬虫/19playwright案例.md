# 19playwright案例

## 豆瓣数据采集

```
import time
from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://movie.douban.com/top250')
    lst = page.locator('//*[@id="content"]/div/div[1]/ol/li').all()

    while True:
        time.sleep(1)

        for li in lst:
            id = li.locator('xpath=./div/div[1]/em').inner_text()
            title = li.locator('xpath=./div/div[2]/div[1]/a/span[1]').inner_text()
            score = li.locator('xpath=./div/div[2]/div[2]/div/span[2]').inner_text()
            print(f'排名:{id}, 名称：{title}, 评分：{score}')
        next_page = page.locator('//*[@id="content"]/div/div[1]/div[2]/span[3]/a')
        if next_page.count() != 0:
            next_page.scroll_into_view_if_needed()
            time.sleep(1)
            next_page.click()
        else:
            print("结束")
            break




    time.sleep(3)
```

## 彼岸图网

```
import os
import time
import random
from playwright.sync_api import sync_playwright

os.makedirs("images", exist_ok=True)


def download_img(response):
    try:
        content_type = response.headers.get('content-type', '')
        filename = response.url.split('/')[-1]
        if content_type and 'image' in content_type and '-' in filename:
            save_path = os.path.join("images", filename)
            if os.path.exists(save_path):
                return
            with open(save_path, "wb") as f:
                f.write(response.body())
            print(f"下载完成：{filename}")
    except Exception:
        return


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.on('response', download_img)

    with open("stealth.min.js", 'r', encoding="utf-8") as f:
        page.add_init_script(f.read())

    page.goto('https://pic.netbian.com/4kdongman/')
    print("请手动处理验证码，等待10秒")
    page.wait_for_timeout(10000)

    while True:
        page.wait_for_load_state("networkidle")
        time.sleep(random.uniform(3, 4))

        next_page = page.locator('//*[@id="main"]/div[4]/a[9]')
        if next_page.count() != 0:
            next_page.scroll_into_view_if_needed()
            next_page.click()
            time.sleep(random.uniform(3, 4))
        else:
            print("无了")
            break

    time.sleep(30)
    browser.close()
```

补充

`scroll_into_view_if_needed()`：元素不在可视区域则自动滚动到视野内



## 网易云

```
import time
from playwright.sync_api import sync_playwright
import subprocess


class DataCollector(object):

    # 启动浏览器
    def launch_browser(self):
        path = r'C:\Users\AppData\Local\ms-playwright\chromium-1228\chrome-win64\chrome.exe'
        params = "--remote-debugging-port=7899"
        cmd = f'"{path}" {params}'
        subprocess.Popen(cmd)

    def parse(self, page):
        content_frame = page.frame('contentFrame')
        time.sleep(2)
        num_page = 1

        for i in range(7):
            time.sleep(2)
            print(f"========================第{num_page}页==============================")
            div = content_frame.locator('//*[@class="cmmts j-flag"]/div')
            next_page = content_frame.locator('//a[text()="下一页"]')
            if div.count() != 0:
                for div in div.all():
                    content = div.locator('xpath=./div[2]/div[1]/div').inner_text()
                    print(content)

            else:
                print('错误：无信息')

            if next_page.is_visible():
                next_page.scroll_into_view_if_needed()
                next_page.click()
                time.sleep(1)
                num_page += 1

            else:
                print("不存在下一页了，退出程序")
                break

    def main(self):
        self.launch_browser()
        time.sleep(1)

        with sync_playwright() as pw:
            browser = pw.chromium.connect_over_cdp(f"http://127.0.0.1:7899")
            context = browser.contexts[0]
            page = context.pages[0]
            page.goto('https://music.163.com/#/song?id=204072')
            self.parse(page)

if __name__ == '__main__':
    dc = DataCollector()
    dc.main()


```

补充：

xpath不存在可能是要等待资源加载

while不是所以都适用，上例中无法判定”下一页“是否存在

于是用for循环，次数自定义，通过网页显示的最后一页













