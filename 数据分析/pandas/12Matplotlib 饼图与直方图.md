# Matplotlib 饼图

饼图（Pie Chart）是一种常用的数据可视化图形，用来展示各类别在总体中所占的比例。

![img](https://help.fanruan.com/finebi5.1/uploads/20211109/1636441075909072.png)

## 中文显示

```
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'WenQuanYi Micro Hei']
plt.rcParams['axes.unicode_minus'] = False
```

## pie()

使用 pyplot 中的 **pie()** 方法来绘制饼图。

pie() 方法语法格式如下：

```
matplotlib.pyplot.pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=0, radius=1, counterclock=True, wedgeprops=None, textprops=None, center=0, 0, frame=False, rotatelabels=False, *, normalize=None, data=None)[source]
```

### 参数说明

- **x**：浮点型数组或列表，用于绘制饼图的数据，表示每个扇形的面积。
- **explode**：数组，表示各个扇形之间的间隔，默认值为0。
- **labels**：列表，各个扇形的标签，默认值为 None。
- **colors**：数组，表示各个扇形的颜色，默认值为 None。
- **autopct**：设置饼图内各个扇形百分比显示格式，**%d%%** 整数百分比，**%0.1f** 一位小数， **%0.1f%%** 一位小数百分比， **%0.2f%%** 两位小数百分比。
- **labeldistance**：标签标记的绘制位置，相对于半径的比例，默认值为 1.1，如 **<1**则绘制在饼图内侧。
- **pctdistance：**类似于 labeldistance，指定 autopct 的位置刻度，默认值为 0.6。
- **shadow：**布尔值 True 或 False，设置饼图的阴影，默认为 False，不设置阴影。
- **radius：**设置饼图的半径，默认为 1。
- **startangle：**用于指定饼图的起始角度，默认为从 x 轴正方向逆时针画起，如设定 =90 则从 y 轴正方向画起。
- **counterclock**：布尔值，用于指定是否逆时针绘制扇形，默认为 True，即逆时针绘制，False 为顺时针。
- **wedgeprops**：字典类型，默认值 None。用于指定扇形的属性，比如边框线颜色、边框线宽度等。例如：wedgeprops={'linewidth':5} 设置 wedge 线宽为5。
- **textprops** ：字典类型，用于指定文本标签的属性，比如字体大小、字体颜色等，默认值为 None。
- **center**：浮点类型的列表，用于指定饼图的中心位置，默认值：(0,0)。
- **frame**：布尔类型，用于指定是否绘制饼图的边框，默认值：False。如果是 True，绘制带有表的轴框架。
- **rotatelabels**：布尔类型，用于指定是否旋转文本标签，默认为 False。如果为 True，旋转每个 label 到指定的角度。
- **data**：用于指定数据。如果设置了 data 参数，则可以直接使用数据框中的列作为 x、labels 等参数的值，无需再次传递。

除此之外，pie() 函数还可以返回三个参数：

- `wedges`：一个包含扇形对象的列表。
- `texts`：一个包含文本标签对象的列表。
- `autotexts`：一个包含自动生成的文本标签对象的列表。

以下实例我们简单实用 pie() 来创建一个饼图:

## 第一个简单的饼图

```
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()
```

显示结果如下：

![](D:\tool\数据分析\12.饼图与直方图\图片\img_matplotlib_pie1.png)



## 设置各个扇形的标签与颜色：

```
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y,
        labels=['A','B','C','D'], # 设置饼图标签
        colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"], # 设置饼图颜色
       )
plt.title("RUNOOB Pie Test") # 设置标题
plt.show()
```

显示结果如下：

![](D:\tool\数据分析\12.饼图与直方图\图片\pl-pie-2.png)



## 突出显示

```
import matplotlib.pyplot as plt

# 数据
sizes = [15, 30, 45, 10]

# 饼图的标签
labels = ['A', 'B', 'C', 'D']

# 饼图的颜色
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

# 突出显示第二个扇形，值越大，距离中心越远
explode = (0, 0.1, 0, 0)

# 绘制饼图
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
     

# 标题
plt.title("RUNOOB Pie Test")

# 显示图形
plt.show()
```



```
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y,
        labels=['A','B','C','D'], # 设置饼图标签
        colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"], # 设置饼图颜色
        explode=(0, 0.2, 0, 0), # 第二部分突出显示，值越大，距离中心越远
        autopct='%.2f%%', # 格式化输出百分比
       )
plt.title("RUNOOB Pie Test")
plt.show()
```

显示结果如下：

![](D:\tool\数据分析\12.饼图与直方图\图片\pl_pie-3.png)

# Matplotlib 直方图

我们可以使用 pyplot 中的 hist() 方法来绘制直方图。

![image-20260122141829382](D:\tool\数据分析\12.饼图与直方图\图片\image-20260122141829382.png)

## 应用

1. 正态分布：成年人身高分布

- **分布类型**：正态分布（钟形曲线）
- **现实场景**：成年人的身高数据
- **特点**：以170cm为中心对称，大部分人在160-180cm之间，极端值较少
- **理论曲线**：红色曲线显示了理想的正态分布形态

2. 右偏分布：个人月收入分布

- **分布类型**：右偏分布（正偏态）
- **现实场景**：个人月收入情况
- **特点**：多数人收入集中在较低水平（5000元以下），少数高收入者拉长右侧尾部
- **社会现象**：反映了收入不平等现象

3. 均匀分布：紧急事件发生时间分布

- **分布类型**：均匀分布
- **现实场景**：紧急事件在一天中的发生时间
- **特点**：各时间段发生的概率基本相等，没有明显高峰时段
- **应用**：应急资源调度、值班安排参考

4. 指数分布：公交车等待时间

- **分布类型**：指数分布
- **现实场景**：乘客等待公交车的时间
- **特点**：短等待时间概率高，长等待时间概率低，呈快速衰减趋势
- **理论曲线**：红色曲线显示了指数分布的典型形状



## hist() 

hist() 方法是 Matplotlib 库中的 pyplot 子库中的一种用于绘制直方图的函数。

hist() 方法可以用于可视化数据的分布情况，例如观察数据的中心趋势、偏态和异常值等。

hist() 方法语法格式如下：

```
matplotlib.pyplot.hist(x, bins=None, range=None, density=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, **kwargs)
```

### 参数说明

| 参数       | 含义                                             | 填写         | 默认                                                         |
| ---------- | ------------------------------------------------ | ------------ | ------------------------------------------------------------ |
| x          | 表示要绘制直方图的数据，可以是一个一维数组或列表 | 数组或列表   |                                                              |
| bins       | 表示直方图的箱数                                 | int          | 10                                                           |
| range      | 表示直方图的值域范围                             | 二元组或列表 | None（即使用数据中的最小值和最大值）                         |
| density    | 表示是否将直方图归一化                           | boolean      | False（即直方图的高度为每个箱子内的样本数，而不是频率或概率密度） |
| weights    | 表示每个数据点的权重                             | 数组         | None                                                         |
| cumulative | 表示是否绘制累积分布图                           | boolean      | False（不累积，普通直方图）                                  |
| bottom     | 表示直方图的起始高度                             | 数值数据     | None（等价于 `0`，从 x 轴开始画）                            |
| log        | 表示是否在y轴上使用对数刻度                      | boolean      | False                                                        |

| 参数        | 含义                     | 填写                                                 | 默认       |
| ----------- | ------------------------ | ---------------------------------------------------- | ---------- |
| histtype    | 表示直方图的类型         | 'bar'、'barstacked'、'step'、'stepfilled'等          | 'bar'      |
| align       | 表示直方图箱子的对齐方式 | 'left'（柱子左边缘对齐刻度）、'mid'、'right'（同理） | 'mid'      |
| orientation | 表示直方图的方向         | 'vertical'、'horizontal'（横着）                     | 'vertical' |
| rwidth      | 表示每个箱子的宽度       | **0 ~ 1** 之间的小数                                 | None（0）  |
| color       | 表示直方图的颜色         | 详见查询ai                                           |            |
| label       | 表示直方图的标签         | 自己填写                                             |            |
| stacked     | 表示是否堆叠不同的直方图 | bboolean                                             | False      |
| **kwargs    | 表示其他绘图参数         |                                                      |            |



#### 详细说明

##### range

```
只统计 0 ~ 100 范围内的数据
plt.hist(data, range=(0, 100))

等价写法
plt.hist(data, range=[0, 100])
```

##### density

```
density=False（默认）
直方图高度 = 每个箱子里的样本数量（计数）
纵轴含义：个数 / 频次
用途：看每个区间有多少个数据

density=True
直方图高度 = 概率密度
所有柱子面积之和 = 1
纵轴含义：密度 / 频率
用途：	看分布、拟合曲线、对比不同样本量的数据
```

##### weights

```
长度必须一致：weights 数组长度 = 数据长度
可以是小数：比如 0.5、2.3、100
和 density 兼容：有权重时，总面积依然可以 = 1
用途：统计加权频次、采样权重、归一化统计

data = [1, 2, 2, 3]
# 权重：第1个算1，第2个算5，第3个算1，第4个算1
weights = [1, 5, 1, 1]
plt.hist(data, bins=3, weights=weights, edgecolor='black')
# 数值 2 的柱子高度 = 5+1 = 6
```

##### cumulative

```
#cumulative=False：只显示当前区间的数量（普通直方图，有高有低）
#cumulative=True：从左到右不断累加（直方图只会一直上升，最后等于总数）


```

##### bottom

```
作用：让柱子不从 0 开始，而是从你指定的高度开始

常用于堆叠直方图

plt.hist(data1, bins=5, label='第一层')
# 第二层：bottom=第一层的高度 → 堆叠
plt.hist(data2, bins=5, bottom=np.histogram(data1, bins=5)[0], label='第二层')
plt.legend()		#必须配合 label 参数一起用，图表右上角会出现一个小方框显示图例
plt.show()
```

注：plt.tight_layout()     	 自动排版，让图表不拥挤、不重叠

1.画多个子图的时候

2.坐标轴标签、标题**重叠、挤在一起**的时候

3.图表边缘内容被切掉的时候



##### histtype

```
plt.hist(data, histtype='bar')        # 普通柱状（默认）
plt.hist(data, histtype='barstacked') # 堆叠柱状
plt.hist(data, histtype='step')       # 只有台阶线
plt.hist(data, histtype='stepfilled') # 填充台阶
```



##### log

```
log=False（默认）：普通刻度（数值差距大时，小的看不见）
log=True：对数刻度（能同时看清很大和很小的数据）把大数字 “压缩”，小数字 “放大” 
```



##### stacked

```
stacked=True 是自动堆叠直方图，无需手动计算底层高度；
bottom 需手动指定起始高度，属于手动堆叠方式
```



## 第一个简单的直方图

```
import matplotlib.pyplot as plt
import numpy as np

# 生成一组随机数据，语法：np.random.normal( 均值, 标准差, 数量 )
data = np.random.randn(1000)

# 绘制直方图
plt.hist(data, bins=30, color='skyblue', alpha=0.8)

# 设置图表属性
plt.title('RUNOOB hist() Test')
plt.xlabel('Value')
plt.ylabel('Frequency')

# 显示图表
plt.show()
```

显示结果如下：

![](D:\tool\数据分析\12.饼图与直方图\图片\runoob-test-hist.png)



## 多个数据组的直方图

以下实例演示了如何使用 hist() 函数绘制多个数据组的直方图，并进行比较：

```
import matplotlib.pyplot as plt
import numpy as np

# 生成三组随机数据
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(2, 1, 1000)
data3 = np.random.normal(-2, 1, 1000)

# 绘制直方图
plt.hist(data1, bins=30, alpha=0.5, label='Data 1')
plt.hist(data2, bins=30, alpha=0.5, label='Data 2')
plt.hist(data3, bins=30, alpha=0.5, label='Data 3')

# 设置图表属性
plt.title('RUNOOB hist() TEST')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

# 显示图表
plt.show()
```

以上实例中我们生成了三组不同的随机数据，并使用 hist() 函数绘制了它们的直方图。通过设置不同的均值和标准差，我们可以生成具有不同分布特征的随机数据。

我们设置了 bins 参数为 30，这意味着将数据范围分成 30 个等宽的区间，然后统计每个区间内数据的频数。

我们设置了 alpha 参数为 0.5，这意味着每个直方图的颜色透明度为 50%。

我们使用 label 参数设置了每个直方图的标签，以便在图例中显示。

然后使用 legend() 函数显示图例。最后，我们使用 title()、xlabel() 和 ylabel() 函数设置了图表的标题和坐标轴标签。

显示结果如下：

![](D:\tool\数据分析\12.饼图与直方图\图片\runoob-test-hist-2.png)

从上图中我们可以清晰地看出这三组数据的分布情况，其中 data1 和 data2 分布接近正态分布，而 data3 分布偏态。

这种比较直方图的方式可以帮助我们分析和比较不同数据组的分布情况。

## 结合 Pandas

以下实例我们结合 Pandas 来绘制直方图：

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
# 使用 NumPy 生成随机数
random_data = np.random.normal(0, 1, 1000)
 
# 将数据转换为 Pandas DataFrame
dataframe = pd.DataFrame(random_data)
 
# 使用 Pandas hist() 方法绘制直方图
dataframe.hist()


# 设置图表属性
plt.title('RUNOOB hist() Test')
plt.xlabel('X-Value')
plt.ylabel('Y-Value')

# 显示图表
plt.show()
```

显示结果如下：

![](D:\tool\数据分析\12.饼图与直方图\图片\hist-pandas.png)



除了数据框之外，您还可以使用 Pandas 中的 Series 对象绘制直方图。只需将数据框中的列替换为 Series 对象即可。

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 生成随机数据
data = pd.Series(np.random.normal(size=100))

# 绘制直方图
# bins 参数指定了直方图中的柱子数量
plt.hist(data, bins=10)

# 设置图形标题和坐标轴标签
plt.title('RUNOOB hist() Tes')
plt.xlabel('X-Values')
plt.ylabel('Y-Values')

# 显示图形
plt.show()
```

![](D:\tool\数据分析\12.饼图与直方图\图片\af3ddff7580ee52a9ee24d7368ab1dbc.png)

