# 1024_001_pythonStudy

学习

这是一个从零开始学 Java 的个人学习笔记，主要两块：**爬虫** 与 **数据分析**。



## 爬虫相关依赖

### Python 包

```bash
pip install requests
pip install fake-useragent
pip install jsonpath
pip install lxml
pip install pymongo
pip install redis
pip install aiohttp
pip install aiofiles
pip install openpyxl
pip install ffmpeg-python
pip install PyExecJS
pip install scrapy
pip install scrapy-redis
pip install fonttools
pip install Pillow
```

`ddddocr`（验证码识别）需要 **Python 3.12 及以下**：

```bash
pip install ddddocr
```

### Node.js 包（JS 逆向 / 环境）

```bash
npm install jsdom@19.0.0
```



## 加密相关

| 场景 | 安装 | 说明 |
|------|------|------|
| Python 侧 DES | `pip install pycryptodome` | DES 等对称加密 |
| JS 侧 crypto-js | `npm install crypto-js` | **必须在当前目录或其父目录**安装，供 JS 文件使用 |
| JS 侧 RSA | `npm install node-jsencrypt` | **必须在当前目录或其父目录**安装 |
| Python 侧 RSA | `pip install rsa` | 与 JS 的 `node-jsencrypt` 对应，要求不同 |

示例：

```python
# Python 哈希
import hashlib
```

```javascript
// JS 侧 crypto-js / node-jsencrypt 需在项目目录安装
// npm install crypto-js
// npm install node-jsencrypt
```

---

## 数据分析相关依赖

```bash
pip install numpy
pip install pandas
pip install matplotlib
pip install pyecharts
```



## 环境

环境是我学习时的环境，可以根据自己的需求变更

| 环境 | 用途 |
|------|------|
| Python 3.10 / 3.11 | 爬虫与数据分析（避开 ddddocr 版本限制） |
| Node.js 18+ | JS 逆向、jsdom、crypto-js |



## 一键安装脚本（可选）

pip install -r requirements.txt 



*笔记为个人学习记录，欢迎复习与补充。*

*新手小白，各路大神，请多关照，如有建议欢迎大家指点！*
