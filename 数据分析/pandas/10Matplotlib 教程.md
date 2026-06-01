# 初识Matplotlib 

Matplotlib 是 Python 的绘图库，它能让使用者很轻松地将数据图形化，并且提供多样化的输出格式。

Matplotlib 可以用来绘制各种静态，动态，交互式的图表。

Matplotlib 是一个非常强大的 Python 画图工具，我们可以使用该工具将很多数据通过图表的形式更直观的呈现出来。

Matplotlib 可以绘制折线图、散点图、等高线图、条形图、柱状图、3D 图形、甚至是图形动画等等。

## Matplotlib 应用

Matplotlib 通常与 NumPy 和 pandas一起使用， 这种组合广泛用于替代 MatLab，是一个强大的科学计算环境，有助于我们通过 Python 学习数据科学或者机器学习。

## Matplotlib 安装

Matplotlib 是一个强大的 Python 绘图库，用于创建各种类型的静态、动态和交互式图表。

本章节，我们使用 pip 工具来安装 Matplotlib 库，如果还未安装该工具，可以参考 [Python pip 安装与使用])。

升级 pip：

```
python3 -m pip install -U pip
```

安装 matplotlib 库：

```
python3 -m pip install -U matplotlib
```

```
pip install matplotlib
```



安装完成后，我们就可以通过 import 来导入 matplotlib 库：

```
import matplotlib
```

以下实例，我们通过导入 matplotlib 库，然后查看 matplotlib 库的版本号：

### 查看 matplotlib 库的版本号

```
import matplotlib

print(matplotlib.__version__)
```

输出结果如下：

```
3.4.2
```

### 中文字体显示

```
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'WenQuanYi Micro Hei']
plt.rcParams['axes.unicode_minus'] = False
```



## Matplotlib Pyplot

Pyplot 是 Matplotlib 的子库，提供了和 MATLAB 类似的绘图 API。

Pyplot 是常用的绘图模块，能很方便让用户绘制 2D 图表。

Pyplot 包含一系列绘图函数的相关函数，每个函数会对当前的图像进行一些修改，例如：给图像加上标记，生新的图像，在图像中产生新的绘图区域等等。

使用的时候，我们可以使用 import 导入 pyplot 库，并设置一个别名 **plt**：

```
import matplotlib.pyplot as plt
```

这样我们就可以使用 **plt** 来引用 Pyplot 包的方法。

以下是一些常用的 pyplot 函数：

* `show()`:相当于 “绘图的最后一步”—— 如果不写 `plt.show()`，代码执行后只会在内存中生成图表，不会在屏幕上显示。

- `plot()`：用于绘制折线图
- `scatter()`：用于绘制散点图
- `bar()`：用于绘制垂直条形图和水平条形图
- `hist()`：用于绘制柱状图
- `pie()`：用于绘制饼图
- `imshow()`：用于绘制图像
- `subplots()`：用于创建子图

除了这些基本的函数，pyplot 还提供了很多其他的函数，例如用于设置图表属性的函数、用于添加文本和注释的函数、用于保存图表到文件的函数等等。



### 绘制一条线

```
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 6])
y = np.array([0, 100])

plt.plot(x, y)
plt.show()
```

输出：

![image-20260121220250550](D:\tool\数据分析\10：Matplotlib的2D图库\图片\image-20260121220250550.png)

### plot()

**plot()** 函数是绘制二维图形的最基本函数。

**plot()** 用于画图它可以绘制点和线，语法格式如下：

```
# 画单条线
plot([x], y, [fmt], *, data=None, **kwargs)
# 画多条线
plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)
```

参数说明：

- **x, y：**点或线的节点，x 为 x 轴数据，y 为 y 轴数据，数据可以列表或数组。
- **fmt：**可选，定义基本格式（如颜色、标记和线条样式）。
- ***\*kwargs：**可选，用在二维平面图上，设置指定属性，如标签，线的宽度等。

```
>>> plot(x, y)        # 创建 y 中数据与 x 中对应值的二维线图，使用默认样式
>>> plot(x, y, 'bo')  # 创建 y 中数据与 x 中对应值的二维线图，使用蓝色实心圈绘制
>>> plot(y)           # x 的值为 0..N-1
>>> plot(y, 'r+')     # 使用红色 + 号
```



**颜色字符：**'b' 蓝色，'m' 洋红色，'g' 绿色，'y' 黄色，'r' 红色，'k' 黑色，'w' 白色，'c' 青绿色，'#008000' RGB 颜色符串。多条曲线不指定颜色时，会自动选择不同颜色。



**线型参数：**'‐' 实线，':' 虚线，'--'破折线，'-.'点划线，'.'仅数据点



**标记字符：**'.' 点标记，',' 像素标记(极小点)，'o' 实心圈标记，'v' 倒三角标记，'^' 上三角标记，'>' 右三角标记，'<' 左三角标记...等等。

#### 实例

```
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,6])
y = np.array([0,100])

plt.plot(x,y,':',color='green')
plt.show()
```

输出：

![image-20260120134141885](D:\tool\数据分析\10：Matplotlib的2D图库\图片\image-20260120134141885.png)



如果我们只想绘制两个坐标点，而不是一条线，可以使用 **o** 参数，表示一个实心圈的标记：

#### 绘制坐标 (1, 3) 和 (8, 10) 的两个点

```
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()
```

输出结果为：

![image-20260121220316682](D:\tool\数据分析\10：Matplotlib的2D图库\图片\image-20260121220316682.png)



#### 任意数量的点

需确保两个轴上的点数相同

```
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()
```

输出：

![image-20260121220337275](D:\tool\数据分析\10：Matplotlib的2D图库\图片\image-20260121220337275.png)




#### 如果不指定 x 轴上的点，则 x 会根据 y 的值来设置为 *0, 1, 2, 3..N-1*



```
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()
```

输出：

![image-20260121220405069](D:\tool\数据分析\10：Matplotlib的2D图库\图片\image-20260121220405069.png)

从上图可以看出 **x** 的值默认设置为 **[0, 1, 2, 3, 4, 5]**。



### 正弦和余弦图

以下实例我们绘制一个正弦和余弦图，在 plt.plot() 参数中包含两对 **x,y** 值，第一对是 **x,y**，这对应于正弦函数，第二对是 **x,z**，这对应于余弦函数。



```
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,4*np.pi,0.1)   # start,stop,step
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,x,z)
plt.show()
```

输出：

![image-20260121220413968](D:\tool\数据分析\10：Matplotlib的2D图库\图片\image-20260121220413968.png)

## Matplotlib 绘图标记

绘图过程如果我们想要给坐标自定义一些不一样的标记，就可以使用 **plot()** 方法的 **marker** 参数来定义。

### 实心圆标记：

```
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([1,3,4,5,8,9,6,1,3,4,5,2,4])

plt.plot(ypoints, marker = 'o')
plt.show()
```

显示结果如下：

![image-20260121220426152](D:\tool\数据分析\10：Matplotlib的2D图库\图片\image-20260121220426152.png)

### **marker** 可以定义的符号如下：

| 标记 | 符号                                          | 描述          |
| :--- | :-------------------------------------------- | :------------ |
| "."  | ![m00](https://www.runoob.com/images/m00.png) | 点            |
| ","  | ![m01](https://www.runoob.com/images/m01.png) | 像素点        |
| "o"  | ![m02](https://www.runoob.com/images/m02.png) | 实心圆        |
| "v"  | ![m03](https://www.runoob.com/images/m03.png) | 下三角        |
| "^"  | ![m04](https://www.runoob.com/images/m04.png) | 上三角        |
| "<"  | ![m05](https://www.runoob.com/images/m05.png) | 左三角        |
| ">"  | ![m06](https://www.runoob.com/images/m06.png) | 右三角        |
| "1"  | ![m07](https://www.runoob.com/images/m07.png) | 下三叉        |
| "2"  | ![m08](https://www.runoob.com/images/m08.png) | 上三叉        |
| "3"  | ![m09](https://www.runoob.com/images/m09.png) | 左三叉        |
| "4"  | ![m10](https://www.runoob.com/images/m10.png) | 右三叉        |
| "8"  | ![m11](https://www.runoob.com/images/m11.png) | 八角形        |
| "s"  | ![m12](https://www.runoob.com/images/m12.png) | 正方形        |
| "p"  | ![m13](https://www.runoob.com/images/m13.png) | 五边形        |
| "P"  | ![m23](https://www.runoob.com/images/m23.png) | 加号（填充）  |
| "*"  | ![m14](https://www.runoob.com/images/m14.png) | 星号          |
| "h"  | ![m15](https://www.runoob.com/images/m15.png) | 六边形 1      |
| "H"  | ![m16](https://www.runoob.com/images/m16.png) | 六边形 2      |
| "+"  | ![m17](https://www.runoob.com/images/m17.png) | 加号          |
| "x"  | ![m18](https://www.runoob.com/images/m18.png) | 乘号 x        |
| "X"  | ![m24](https://www.runoob.com/images/m24.png) | 乘号 x (填充) |
| "D"  | ![m19](https://www.runoob.com/images/m19.png) | 菱形          |
| "d"  | ![m20](https://www.runoob.com/images/m20.png) | 瘦菱形        |
| "\|" | ![m21](https://www.runoob.com/images/m21.png) | 竖线          |
| "_"  | ![m22](https://www.runoob.com/images/m22.png) | 横线          |



### fmt 参数

fmt 参数定义了基本格式，如标记、线条样式和颜色。

```
fmt = '[marker][line][color]'
```

例如 **o:r**，**o** 表示实心圆标记，**:** 表示虚线，**r** 表示颜色为红色。

参数顺序可无序

#### 实例

```
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, 'o:r')
plt.show()
```

显示结果如下：

![image-20260121220513410](D:\tool\数据分析\10：Matplotlib的2D图库\图片\image-20260121220513410.png)



线类型：

| 线类型标记             | 描述   |
| :--------------------- | :----- |
| '-'（注意：是横岗线）  | 实线   |
| ':'                    | 虚线   |
| '--'（注意：是横岗线） | 破折线 |
| '-.'                   | 点划线 |

颜色类型：

| 颜色标记 | 描述 |
| :------- | :--- |
| 'r'      | 红色 |
| 'g'      | 绿色 |
| 'b'      | 蓝色 |
| 'c'      | 青色 |
| 'm'      | 品红 |
| 'y'      | 黄色 |
| 'k'      | 黑色 |
| 'w'      | 白色 |

### 标记大小与颜色

我们可以自定义标记的大小与颜色，使用的参数分别是：

- markersize，简写为 **ms**：定义标记的大小。
- **m**arker**f**ace**c**olor，简写为 **mfc**：定义标记**内部**的颜色。
- **m**arker**e**dge**c**olor，简写为 **mec**：定义标记**边框**的颜色。

设置标记大小：

```
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()
```

显示结果如下：

![image-20260121220538906](D:\tool\数据分析\10：Matplotlib的2D图库\图片\image-20260121220538906.png)

#### 设置标记外边框颜色：

```
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()
```

显示结果如下：

![image-20260121220548303](D:\tool\数据分析\10：Matplotlib的2D图库\图片\image-20260121220548303.png)

#### 设置标记内部颜色：

```
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()
```

显示结果如下：

![image-20260121220557629](D:\tool\数据分析\10：Matplotlib的2D图库\图片\image-20260121220557629.png)



#### 自定义标记内部与边框的颜色：

```
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
plt.show()
```

显示结果如下：

![image-20260121220612914](D:\tool\数据分析\10：Matplotlib的2D图库\图片\image-20260121220612914.png)

## Matplotlib 绘图线

绘图过程如果我们自定义线的样式，包括线的类型、颜色和大小等。

### 线的类型

线的类型可以使用 **linestyle** 参数来定义，简写为 **ls**。

| 类型           | 简写      | 说明   |
| :------------- | :-------- | :----- |
| 'solid' (默认) | '-'       | 实线   |
| 'dotted'       | ':'       | 点虚线 |
| 'dashed'       | '--'      | 破折线 |
| 'dashdot'      | '-.'      | 点划线 |
| 'None'         | '' 或 ' ' | 不画线 |

#### 实例

```
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()
```

显示结果如下：

![image-20260121220732815](D:\tool\数据分析\10：Matplotlib的2D图库\图片\image-20260121220732815.png)



#### ls=linestyle	(简写)

```
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, ls = '-.')
plt.show()
```

显示结果如下：

![image-20260121220744058](D:\tool\数据分析\10：Matplotlib的2D图库\图片\image-20260121220744058.png)

### 线的颜色

线的颜色可以使用 **color** 参数来定义，简写为 **c**。

颜色类型：

| 颜色标记 | 描述 |
| :------- | :--- |
| 'r'      | 红色 |
| 'g'      | 绿色 |
| 'b'      | 蓝色 |
| 'c'      | 青色 |
| 'm'      | 品红 |
| 'y'      | 黄色 |
| 'k'      | 黑色 |
| 'w'      | 白色 |

当然也可以自定义颜色类型，例如：**SeaGreen、#8FBC8F** 等，完整样式可以参考 [HTML 颜色值])。

#### 自定义颜色类型

```
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, color = 'r')
plt.show()
```

显示结果如下：

![image-20260121220802594](D:\tool\数据分析\10：Matplotlib的2D图库\图片\image-20260121220802594.png)

#### c=color	(简写)

```
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, c = '#8FBC8F')
plt.show()
```

显示结果如下：

![image-20260121220813105](D:\tool\数据分析\10：Matplotlib的2D图库\图片\image-20260121220813105.png)



### 线的宽度

线的宽度可以使用 **linewidth** 参数来定义，简写为 **lw**，值可以是浮点数，如：**1**、**2.0**、**5.67** 等。

```
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, linewidth = '12.5')
plt.show()
```

显示结果如下：

![image-20260121220921854](D:\tool\数据分析\10：Matplotlib的2D图库\图片\image-20260121220921854.png)

### 多条线

plot() 方法中可以包含多对 x,y 值来绘制多条线。

```
import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 7, 5, 9])
y2 = np.array([6, 2, 13, 10])

plt.plot(y1)
plt.plot(y2)

plt.show()
```

从上图可以看出 **x** 的值默认设置为 **[0, 1, 2, 3]**。

显示结果如下：

![image-20260121220938957](D:\tool\数据分析\10：Matplotlib的2D图库\图片\image-20260121220938957.png)



自己设置 x 坐标等值

```
import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 7, 5, 9])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 13, 10])

plt.plot(x1, y1, x2, y2)
plt.show()
```

显示结果如下：

![image-20260121220948059](D:\tool\数据分析\10：Matplotlib的2D图库\图片\image-20260121220948059.png)



## Matplotlib 轴标签和标题

我们可以使用 **xlabel()** 和 **ylabel()** 方法来设置 x 轴和 y 轴的标签。

### 轴标签

```
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])
plt.plot(x, y)

plt.xlabel("x - label")
plt.ylabel("y - label")

plt.show()
```

显示结果如下：

![image-20260121220957657](D:\tool\数据分析\10：Matplotlib的2D图库\图片\image-20260121220957657.png)

### 标题

我们可以使用 **title()** 方法来设置标题。

```
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])
plt.plot(x, y)

plt.title("RUNOOB TEST TITLE")
plt.xlabel("x - label")
plt.ylabel("y - label")

plt.show()
```

显示结果如下：

![image-20260121221008397](D:\tool\数据分析\10：Matplotlib的2D图库\图片\image-20260121221008397.png)





### 注：

中文默认无法识别

若要显示中文字体，要添加如下代码

```
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'WenQuanYi Micro Hei']
plt.rcParams['axes.unicode_minus'] = False
```

eg：

```
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'WenQuanYi Micro Hei']
plt.rcParams['axes.unicode_minus'] = False

x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])
plt.plot(x, y)

plt.xlabel("X轴")
plt.ylabel("Y轴")

plt.show()
```

