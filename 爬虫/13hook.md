# 16_hook

## 初识

hook（钩子）：它允许开发者在不改变原始代码的情况下，插入自定义逻辑。——覆盖，注入

类似继承

```
function f1() {
    console.log(666);
}

f1 = function () {
    console.log(777);
}

f1();

// f1 = function () {
//     console.log(777);
// }
//出钩的时机很重要，早与晚都不行
```

原有流程不动，预埋 “钩子点位”，开发者插入自定义逻辑，拦截、扩展、修改原有行为，实现**无侵入扩展**

出钩的时机：对象生成之后，调用之前。



debugger: 调试。

 打断点：调试。

 debugger 等价于 手动打的断点（js）



### 为什么要调试

代码是按机器逻辑跑的，人脑很难预判每一步变量、执行顺序；

调试就是让机器慢放执行过程，直观看到每一步的数据，精准找到错误和不合理逻辑。



## hook 函数

通过参数里面的内容判断这个功能做的事情

应用

```
setInterval = function(a, b){
    console.log(a.toString());
    if (a.toString().indexOf("debugger") != -1){
        console.log("置空");
        return;
    }
    console.log("使用原来的函数");
};

```



### 主体步骤

备份原函数

替换新函数

自定义行为

调用原函数



## hook属性

```
它提供了对属性特性的精细控制

obj（必需）：
    这是要定义或修改属性的对象。

prop（必需）：
    这是要定义或修改的属性名称（可以是字符串或 Symbol）。

descriptor（必需）：
    这是一个对象，描述了要定义或修改的属性的特性。这个描述符对象可以包含以下属性：
 
```

defineProperty(对象, 属性名, 描述配置)	—— 内置静态方法

eg

```
var obj = {
    name: "alice",
    play: function(){
        console.log("play");
    }
}
var yname = obj.name;

Object.defineProperty(obj, "name", {
    // 获取：当读取属性时自动调用
    get: function () {
        return yname;
        // return "peter";
    },
    // 设置：当设置属性时自动调用
    set: function (newValue) {
        // console.log(666);
        yname = newValue;
    }
});
```



油猴插件安装【edge 浏览器版本】：

点击右上角【拼图】

点击最下面的【获取xx扩展】

右上角搜索【油猴】

点击右侧获取

点击右上角【拼图】

点击插件右侧的【图钉】

打开开发人员模式：

点击右上角【拼图】

点击倒数第二行【管理扩展】

点击左侧【开发人员模式】，使之打开



测试：

打开百度首页【https://www.baidu.com/】

点击右上角插件图标

点击添加新脚本，会弹出一个代码界面

编写脚本代码【hook】，并保存

回到百度首页

刷新，并打开开发者工具，如果右上角插件图标有红色标记，表示成功

如果不生效，重启浏览器



参数说明

```
// ==UserScript==
// @name         test01
// @namespace    http://tampermonkey.net/
// @version      2026-07-10
// @description  try to take over the world!
// @author       You
// @match        https://www.baidu.com/?tn=68018901_16_pg
// @icon         https://www.google.com/s2/favicons?sz=64&domain=baidu.com
// @grant        none
// ==/UserScript==

(function() {
    console.log(666);
})();
```

@name         脚本名称

@match       匹配的网站的匹配规则

@include      包含所有的网站【当前脚本对所有网站生效】

@run-at       在哪里跑【在什么时候运行这个脚本】



@run-at   有四个参数

document-start

时机：HTML 刚开始下载、DOM 还没解析，document.body = null

适用：拦截页面原生 JS、劫持XMLHttpRequest/fetch、重写原型、屏蔽广告脚本

注意：无法操作 DOM 元素，只能监听节点插入事件

document-body

时机：`<body>` 标签生成，但页面资源、图片还在加载

适用：提前修改页面样式、插入基础 DOM，比 document-end 更早

document-end

时机：触发`DOMContentLoaded`，DOM 树全部解析完毕，图片等资源还没加载完

适用：绝大多数 DOM 操作、按钮绑定、修改页面元素

document-idle

时机：DOM 加载完 + 所有图片 / 视频 / 异步资源加载完成，浏览器空闲

适用：不紧急功能、性能消耗大的操作、延迟美化页面

不写`@run-at`时，默认就是这个模式

 context-menu

```
快速选择建议
拦截接口、屏蔽网页 JS：document-start
想提前修改 DOM：document-body
普通改页面、绑定事件：document-end
等待图片加载完再处理：document-idle
需要手动右键触发：context-menu
```

