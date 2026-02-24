import execjs
import requests
import time
import jsonpath

headers = {
    'accept': '*/*',

    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0',
}

params = {
    'csrf_token': 'bb07c89dfe08d62239e35a1a1e9e74ac',
}
cursor = "-1"
for page in range(1, 8):
    with open("wyyjb.js", "r", encoding="utf-8") as f:
        # 编译读取到的 js 代码，获取 js 对象
        js_obj = execjs.compile(f.read())
        # 调用 js 函数，第一个参数是函数名称，后面的参数是函数的参数
        res = js_obj.call("getpwd", page, cursor)

    # print(res)

    response = requests.post(
        'https://music.163.com/weapi/comment/resource/comments/get',
        params=params,
        headers=headers,
        data=res,
    )

    time.sleep(1)
    cursor = jsonpath.jsonpath(response.json(), '$..cursor')
    # print(cursor)
    # print(response.text)
    a = jsonpath.jsonpath(response.json(), '$..content')
    b = jsonpath.jsonpath(response.json(), '$..nickname')
    c = len(a)

    print("————————————————", "第", page, "页", "————————————————")
    x = 0
    while (x < c):
        print(b[x], ':', a[x], end="\n")
        x += 1
