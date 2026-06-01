# Matplotlib 网格线

我们可以使用 pyplot 中的 grid() 方法来设置图表中的网格线。

## 中文字体显示

```
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'WenQuanYi Micro Hei']
plt.rcParams['axes.unicode_minus'] = False
```

## grid()

grid() 方法语法格式如下：

```
matplotlib.pyplot.grid(b=None, which='major', axis='both', )
```

**参数说明：**

- **b**：默认为 true，可以设置布尔值，true 为显示网格线，false 为不显示
- **which**：可选，可选值有 'major'、'minor' 和 'both'，默认为 'major'，表示应用更改的网格线。
- **axis**：设置显示哪个方向的网格线，可以是取 'both'（默认），'x' 或 'y'，分别表示两个方向，x 轴方向或 y 轴方向。
- **kwargs**：设置网格样式，可以是 color='r', linestyle='-' 和 linewidth=2，分别表示网格线的颜色，样式和宽度。



### 一个简单的网格线

```
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'WenQuanYi Micro Hei']
plt.rcParams['axes.unicode_minus'] = False

x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])


plt.title("RUNOOB grid() Test")
plt.xlabel("x - label")
plt.ylabel("y - label")

plt.plot(x, y)

plt.grid()

plt.show()
```

显示结果如下：

![](D:\tool\数据分析\11：网格线图与柱形图\图片\pl_grid-1.png)

以下实例添加一个简单的网格线，axis 参数使用 x，设置 x 轴方向显示网格线：

#### axis 参数

```
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])


plt.title("RUNOOB grid() Test")
plt.xlabel("x - label")
plt.ylabel("y - label")

plt.plot(x, y)

plt.grid(axis='x') # 设置 y 就在轴方向显示网格线

plt.show()
```

显示结果如下：

![](D:\tool\数据分析\11：网格线图与柱形图\图片\pl_grid-2.png)



### 网格线的样式

```
grid(color = 'color', linestyle = 'linestyle', linewidth = number)
```

**参数说明：**

**color：**'b' 蓝色，'m' 洋红色，'g' 绿色，'y' 黄色，'r' 红色，'k' 黑色，'w' 白色，'c' 青绿色，'#008000' RGB 颜色符串。

**linestyle：**'‐' 实线，'‐‐' 破折线，'‐.' 点划线，':' 虚线。

**linewidth**：设置线的宽度，可以设置一个数字。

#### 实例

```
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])


plt.title("RUNOOB grid() Test")
plt.xlabel("x - label")
plt.ylabel("y - label")

plt.plot(x, y)

plt.grid(color = 'r', linestyle = '--', linewidth = 0.5)

plt.show()
```

显示结果如下：

![](D:\tool\数据分析\11：网格线图与柱形图\图片\pl_grid-3.png)



# Matplotlib 绘制多图

我们可以使用 pyplot 中的 **subplot()** 和 **subplots()** 方法来绘制多个子图。

**subplot()** 方法在绘图时需要指定位置，**subplots()** 方法可以一次生成多个，在调用时只需要调用生成对象的 ax 即可。

### subplot()

```
subplot(nrows, ncols, index, **kwargs)
subplot(pos, **kwargs)
subplot(**kwargs)
subplot(ax)
```

以上函数将整个绘图区域分成 nrows 行和 ncols 列，然后从左到右，从上到下的顺序对每个子区域进行编号 **1...N** ，左上的子区域的编号为 1、右下的区域编号为 N，编号可以通过参数 **index** 来设置。

`nrows=1`：子图网格**总行数**为 1

`ncols=2`：子图网格**总列数**为 2

`index=2`：选中**第 2 个**子图（子图编号从 **左到右、从上到下** 从 1 开始）

设置 numRows ＝ 1，numCols ＝ 2，就是将图表绘制成 1x2 的图片区域, 对应的坐标为：

```
(1, 1), (1, 2)
```

**plotNum ＝ 1**, 表示的坐标为(1, 1), 即第一行第一列的子图。

**plotNum ＝ 2**, 表示的坐标为(1, 2), 即第一行第二列的子图。

#### 实例

```
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
xpoints = np.array([0, 6])
ypoints = np.array([0, 100])

plt.subplot(1, 2, 1)
plt.plot(xpoints,ypoints)
plt.title("plot 1")

#plot 2:
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("plot 2")

plt.suptitle("RUNOOB subplot Test")
plt.show()
```

显示结果如下：

![](D:\tool\数据分析\11：网格线图与柱形图\图片\pl_subplot-1.png)



设置 numRows ＝ 2，numCols ＝ 2，就是将图表绘制成 2x2 的图片区域, 对应的坐标为：

```
(1, 1), (1, 2)
(2, 1), (2, 2)
```

**plotNum ＝ 1**, 表示的坐标为(1, 1), 即第一行第一列的子图。

**plotNum ＝ 2**, 表示的坐标为(1, 2), 即第一行第二列的子图。

**plotNum ＝ 3**, 表示的坐标为(2, 1), 即第二行第一列的子图。

**plotNum ＝ 4**, 表示的坐标为(2, 2), 即第二行第二列的子图。

#### 实例

```
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 6])
y = np.array([0, 100])

plt.subplot(2, 2, 1)
plt.plot(x,y)
plt.title("plot 1")

#plot 2:
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])

plt.subplot(2, 2, 2)
plt.plot(x,y)
plt.title("plot 2")

#plot 3:
x = np.array([1, 2, 3, 4])
y = np.array([3, 5, 7, 9])

plt.subplot(2, 2, 3)
plt.plot(x,y)
plt.title("plot 3")

#plot 4:
x = np.array([1, 2, 3, 4])
y = np.array([4, 5, 6, 7])

plt.subplot(2, 2, 4)
plt.plot(x,y)
plt.title("plot 4")

plt.suptitle("RUNOOB subplot Test")
plt.show()
```

显示结果如下：

![](D:\tool\数据分析\11：网格线图与柱形图\图片\pl_subplot-2.png)





# Matplotlib 散点图

我们可以使用 pyplot 中的 scatter() 方法来绘制散点图。

scatter() 方法语法格式如下：

```
matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, *, edgecolors=None, plotnonfinite=False, data=None, **kwargs)
```

**参数说明：**

**x，y**：长度相同的数组，也就是我们即将绘制散点图的数据点，输入数据。

**s**：点的大小，默认 20，也可以是个数组，数组每个参数为对应点的大小。

**c**：点的颜色，默认蓝色 'b'，也可以是个 RGB 或 RGBA 二维行数组。

**marker**：点的样式，默认小圆圈 'o'。

**cmap**：Colormap，默认 None，标量或者是一个 colormap 的名字，只有 c 是一个浮点数数组的时才使用。如果没有申明就是 image.cmap。

**norm**：Normalize，默认 None，数据亮度在 0-1 之间，只有 c 是一个浮点数的数组的时才使用。

**vmin，vmax：**：亮度设置，在 norm 参数存在时会忽略。

**alpha：**：透明度设置，0-1 之间，默认 None，即不透明。

**linewidths：**：标记点的长度。

**edgecolors：**：颜色或颜色序列，默认为 'face'，可选值有 'face', 'none', None。

**plotnonfinite：**：布尔值，设置是否使用非限定的 c ( inf, -inf 或 nan) 绘制点。

***\*kwargs：**：其他参数。

以下实例 scatter() 函数接收长度相同的数组参数，一个用于 x 轴的值，另一个用于 y 轴上的值：

## 一个简单的散点图

```
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([1, 4, 9, 16, 7, 11, 23, 18])

plt.scatter(x, y)
plt.show()
```

显示结果如下：

![](D:\tool\数据分析\11：网格线图与柱形图\图片\pl_scatter-1.png)







## 设置图标大小

s

```
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([1, 4, 9, 16, 7, 11, 23, 18])
sizes = np.array([20,50,100,200,500,1000,60,90])
plt.scatter(x, y, s=sizes)
plt.show()
```

显示结果如下：

![](D:\tool\数据分析\11：网格线图与柱形图\图片\pl-scatter-5.png)





## 自定义点的颜色

```
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([1, 4, 9, 16, 7, 11, 23, 18])
colors = np.array(["red","green","black","orange","purple","beige","cyan","magenta"])

plt.scatter(x, y, c=colors)
plt.show()
```

显示结果如下：

![](D:\tool\数据分析\11：网格线图与柱形图\图片\pl-scatter-2.png)





## 设置两组散点图：

```
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')

plt.show()
```

显示结果如下：

![](D:\tool\数据分析\11：网格线图与柱形图\图片\img_matplotlib_scatter_color.png)





## 使用随机数来设置散点图：

```
import numpy as np
import matplotlib.pyplot as plt

# 随机数生成器的种子
np.random.seed(19680801)


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5) # 设置颜色及透明度

plt.title("RUNOOB Scatter Test") # 设置标题

plt.show()
```

显示结果如下：

![](D:\tool\数据分析\11：网格线图与柱形图\图片\pl-scatter-3.png)



## 颜色条 Colormap

Matplotlib 模块提供了很多可用的颜色条。

颜色条就像一个颜色列表，其中每种颜色都有一个范围从 0 到 100 的值。

下面是一个颜色条的例子：

![](D:\tool\数据分析\11：网格线图与柱形图\图片\img_colorbar.png)



设置颜色条需要使用 cmap 参数，默认值为 'viridis'，之后颜色值设置为 0 到 100 的数组。

### 实例

```
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.show()
```

显示结果如下：

![](D:\tool\数据分析\11：网格线图与柱形图\图片\img_matplotlib_scatter_colormap1.png)



如果要显示颜色条，需要使用 **plt.colorbar()** 方法：

## plt.colorbar()

```
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()

plt.show()
```

显示结果如下：

![](D:\tool\数据分析\11：网格线图与柱形图\图片\img_matplotlib_scatter_colormap2.png)



换个颜色条参数， cmap 设置为 **afmhot_r**：

### 实例

```
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='afmhot_r')
plt.colorbar()
plt.show()
```

显示结果如下：

![](D:\tool\数据分析\11：网格线图与柱形图\图片\xssss-pl-scatter.png)



颜色条参数值可以是以下值：

| 颜色名称         |      | 保留关键字         |
| :--------------- | :--- | :----------------- |
| Accent           |      | Accent_r           |
| Blues            |      | Blues_r            |
| BrBG             |      | BrBG_r             |
| BuGn             |      | BuGn_r             |
| BuPu             |      | BuPu_r             |
| CMRmap           |      | CMRmap_r           |
| Dark2            |      | Dark2_r            |
| GnBu             |      | GnBu_r             |
| Greens           |      | Greens_r           |
| Greys            |      | Greys_r            |
| OrRd             |      | OrRd_r             |
| Oranges          |      | Oranges_r          |
| PRGn             |      | PRGn_r             |
| Paired           |      | Paired_r           |
| Pastel1          |      | Pastel1_r          |
| Pastel2          |      | Pastel2_r          |
| PiYG             |      | PiYG_r             |
| PuBu             |      | PuBu_r             |
| PuBuGn           |      | PuBuGn_r           |
| PuOr             |      | PuOr_r             |
| PuRd             |      | PuRd_r             |
| Purples          |      | Purples_r          |
| RdBu             |      | RdBu_r             |
| RdGy             |      | RdGy_r             |
| RdPu             |      | RdPu_r             |
| RdYlBu           |      | RdYlBu_r           |
| RdYlGn           |      | RdYlGn_r           |
| Reds             |      | Reds_r             |
| Set1             |      | Set1_r             |
| Set2             |      | Set2_r             |
| Set3             |      | Set3_r             |
| Spectral         |      | Spectral_r         |
| Wistia           |      | Wistia_r           |
| YlGn             |      | YlGn_r             |
| YlGnBu           |      | YlGnBu_r           |
| YlOrBr           |      | YlOrBr_r           |
| YlOrRd           |      | YlOrRd_r           |
| afmhot           |      | afmhot_r           |
| autumn           |      | autumn_r           |
| binary           |      | binary_r           |
| bone             |      | bone_r             |
| brg              |      | brg_r              |
| bwr              |      | bwr_r              |
| cividis          |      | cividis_r          |
| cool             |      | cool_r             |
| coolwarm         |      | coolwarm_r         |
| copper           |      | copper_r           |
| cubehelix        |      | cubehelix_r        |
| flag             |      | flag_r             |
| gist_earth       |      | gist_earth_r       |
| gist_gray        |      | gist_gray_r        |
| gist_heat        |      | gist_heat_r        |
| gist_ncar        |      | gist_ncar_r        |
| gist_rainbow     |      | gist_rainbow_r     |
| gist_stern       |      | gist_stern_r       |
| gist_yarg        |      | gist_yarg_r        |
| gnuplot          |      | gnuplot_r          |
| gnuplot2         |      | gnuplot2_r         |
| gray             |      | gray_r             |
| hot              |      | hot_r              |
| hsv              |      | hsv_r              |
| inferno          |      | inferno_r          |
| jet              |      | jet_r              |
| magma            |      | magma_r            |
| nipy_spectral    |      | nipy_spectral_r    |
| ocean            |      | ocean_r            |
| pink             |      | pink_r             |
| plasma           |      | plasma_r           |
| prism            |      | prism_r            |
| rainbow          |      | rainbow_r          |
| seismic          |      | seismic_r          |
| spring           |      | spring_r           |
| summer           |      | summer_r           |
| tab10            |      | tab10_r            |
| tab20            |      | tab20_r            |
| tab20b           |      | tab20b_r           |
| tab20c           |      | tab20c_r           |
| terrain          |      | terrain_r          |
| twilight         |      | twilight_r         |
| twilight_shifted |      | twilight_shifted_r |
| viridis          |      | viridis_r          |
| winter           |      | winter_r           |

![](D:\tool\数据分析\11：网格线图与柱形图\图片\sphx_glr_colormaps_001.webp)



![](D:\tool\数据分析\11：网格线图与柱形图\图片\sphx_glr_colormaps_002.webp)



![](D:\tool\数据分析\11：网格线图与柱形图\图片\sphx_glr_colormaps_003.webp)



![](D:\tool\数据分析\11：网格线图与柱形图\图片\sphx_glr_colormaps_004.webp)



![](D:\tool\数据分析\11：网格线图与柱形图\图片\sphx_glr_colormaps_005.webp)



![](D:\tool\数据分析\11：网格线图与柱形图\图片\sphx_glr_colormaps_006.webp)



![](D:\tool\数据分析\11：网格线图与柱形图\图片\sphx_glr_colormaps_007.webp)



# Matplotlib 柱形图

使用 pyplot 中的 bar() 方法来绘制柱形图。

bar() 方法语法格式如下：

```
matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
```

**参数说明：**

**x**：浮点型数组，柱形图的 x 轴数据。

**height**：浮点型数组，柱形图的高度。

**width**：浮点型数组，柱形图的宽度。

**bottom**：浮点型数组，底座的 y 坐标，默认 0。

**align**：柱形图与 x 坐标的对齐方式，'center' 以 x 位置为中心，这是默认值。 'edge'：将柱形图的左边缘与 x 位置对齐。要对齐右边缘的条形，可以传递负数的宽度值及 align='edge'。

***\*kwargs：**：其他参数。



plot() 折线图 、scatter() 散点图、bar() 柱状图

## 一个简单的柱形图

```
# 13 创建一个名为 "Runoob" 的柱状图
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'WenQuanYi Micro Hei']
plt.rcParams['axes.unicode_minus'] = False

x = np.array(["唐僧", "沙僧", "孙悟空", "猪八戒"])
y = np.array([50, 10, 30, 20])

plt.bar(x,y)
plt.show()
```

显示结果如下：

![image-20260306144418773](D:\tool\数据分析\11：网格线图与柱形图\图片\image-20260306144418773.png)





## 垂直方向的柱形图 barh()

注：

横 => barh()

竖 => bar()

```
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["曹操", "刘备", "孙权"])
y = np.array([50, 48, 39])

plt.barh(x,y)
plt.show()
```

显示结果如下：

![image-20260306144605243](D:\tool\数据分析\11：网格线图与柱形图\图片\image-20260306144605243.png)





## 设置柱形图颜色：

```
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
y = np.array([12, 22, 6, 18])

plt.bar(x, y, color = "#4CAF50")
plt.show()
```

显示结果如下：

![](D:\tool\数据分析\11：网格线图与柱形图\图片\pl-bar-3.png)

注：

color可以简写为c



## 自定义各个柱形的颜色：

```
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
y = np.array([12, 22, 6, 18])

plt.bar(x, y,  color = ["#4CAF50","red","hotpink","#556B2F"])
plt.show()
```

显示结果如下：

![](D:\tool\数据分析\11：网格线图与柱形图\图片\pl-bar-6.png)

注：

`color = ["#4CAF50","red","hotpink","#556B2F"]`是遍历的数组，即x轴若有五个数据则第五个数据颜色为`#4CAF50`





## 设置柱形图宽度

**bar()** 方法使用 **width** 设置，**barh()** 方法使用 **height** 设置 **height**

```
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
y = np.array([12, 22, 6, 18])

plt.bar(x, y, width = 0.1)
plt.show()
```

显示结果如下：

![](D:\tool\数据分析\11：网格线图与柱形图\图片\pl-bar-4.png)





```
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
y = np.array([12, 22, 6, 18])

plt.barh(x, y, height = 0.1)
plt.show()
```

显示结果如下：

![](D:\tool\数据分析\11：网格线图与柱形图\图片\pl-bar-5.png)





# 注：

- **类别文字短** → 用 `plt.bar()`（竖着）
- **类别文字长** → 用 `plt.barh()`（横着，不挤）