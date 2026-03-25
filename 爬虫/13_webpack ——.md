# 13_webpack ——

webpack 是 JavaScript 应用程序的模块打包器，可以把开发中的所有资源都看成
模块，通过 loader（加载器）和 plugins （插件）对资源进行处理，打包成符合生
产环境部署的前端资源。

## 学习重点：

​    处理 webpack 类型的 js 代码。



## webpack 特点：

1.最外层一个自执行，实参是数组|对象，在自执行里面存在类似这样代码的调用
return e[t].call(a.exports, a, a.exports, s)
e[t]
**自执行形参[加载器形参].call（）**
[1]
{1}

2.批量存在类似结构的函数

3.window.webpackJsonp



## webpack 结构：

```
// 自执行函数，x 是自执行函数的实参（数组/对象）
!function (x) {
    // t 一般是缓存
    var t = {};
    
    // 加载器：这个y传入的可以是索引或对象的key，也就是要执行哪个函数，不能直接调用
    function xxx(y) {
        // 缓存中存在，直接使用缓存中的，一般不考虑这里
        if (t[y])
            return t[y].exports;

        var r = t[y] = {
            i: y,
            l: !1,
            exports: {}
        };
        /*
            执行函数模块：
                 x[y]：x 函数模块中的 y 那一个
                 .call：执行函数，并传递参数（空对象，r对象，空对象，加载器），后三个参数会传递给 x[y] 函数
         */
        return x[y].call(r.exports, r, r.exports, xxx), r.l = !0, r.exports;
    }
}(
    {
        // call 调用的，传递的就是实参（r对象，空对象，加载器）
        "0": function (a, b, c) {
            console.log("第一个")
            console.log("a:" + a);
            console.log("b:" + b);
            console.log("c:" + c);
            c(1)
        },
        "1": function (a, b, c) {
            console.log("a:" + a);
            console.log("b:" + b);
            console.log("c:" + c);
            console.log("第二个")
            c(2)
        },
        "2": function (a, b, c) {
            console.log("a:" + a);
            console.log("b:" + b);
            console.log("c:" + c);
            console.log("第三个")
        }
    }
);

```

js 代码可以局部调用全局，不能全局调用局部

现在要执行函数模块中的 0 函数，就需要先获取到加载器。



## 获取加载器

由于加载器存在于自执行函数内部，所以外部并不能直接调用，所以需要先将自执行函数导出才能使用。导出方式如下：

1. 创建全局变量在第一行编写

   ```js
   // 创建全局变量
   var jzq;
   ```

2. 局部将加载器赋值给全局变量

   ```js
   !function (x) {
       var t = {};
       function xxx(y) {
           // ...
       }
       // 局部将加载器赋值给全局变量
       jzq = xxx;
   }
   ```

3. 全局调用加载器，并调用函数

   ```js
   // 创建全局变量
   var jzq;
   !function (x) {
       var t = {};
       function xxx(y) {
           // ...
       }
       // 局部将加载器赋值给全局变量
       jzq = xxx;
   }({...});
   // 全局调用加载器，并调用函数
   jzq("0");
   ```





## 完整代码



```js
// 创建全局变量
var jzq;

// 自执行函数，x 是自执行函数的实参（数组/对象）
!function (x) {
    // t 一般是缓存
    var t = {};
    // 加载器：这个y传入的可以是索引或对象的key，也就是要执行哪个函数
    function xxx(y) {
        // 缓存中存在，直接使用缓存中的，一般不考虑这里
        if (t[y])
            return t[y].exports;

        var r = t[y] = {
            i: y,
            l: !1,
            exports: {}
        };
        /*
            执行函数模块：
                 x[y]：x 函数模块中的 y 那一个
                 .call：执行函数，并传递参数（空对象，r对象，空对象，加载器），后三个参数会传递给 x[y] 函数
         */
        return x[y].call(r.exports, r, r.exports, xxx), r.l = !0, r.exports;
    }
    // 局部将加载器赋值给全局变量
    jzq = xxx;
}(
    {
        // call 调用的，传递的就是实参（r对象，空对象，加载器）
        "0": function (a, b, c) {
            console.log("第一个")
            console.log("a:" + a);
            console.log("b:" + b);
            console.log("c:" + c);
            c(1)
        },
        "1": function (a, b, c) {
            console.log("a:" + a);
            console.log("b:" + b);
            console.log("c:" + c);
            console.log("第二个")
            c(2)
        },
        "2": function (a, b, c) {
            console.log("a:" + a);
            console.log("b:" + b);
            console.log("c:" + c);
            console.log("第三个")
        }
    }
);
// 全局调用加载器，并调用函数
jzq("0");
```





## 获取函数模块：

window.webpackJsonp  所有函数模块。

1.在加载器里面找类似上面的代码

2.页面执行完，在控制台打印上面代码

3.弹出的数组中，点开具体的某个数组，查看其中的 f，点击蓝色字体可以跳转到对应的函数模块。



但由于有些js文件的函数模块的函数很多所以要找具体函数

### 找具体函数：

1.找到加载器的位置并打断点

2.刷新网页在控制台打印 “自执行形参[自己所需要的函数模块名称]”，得到的就是对应的函数模块

