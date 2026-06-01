# pyecharts 简介

**pyecharts官网地址：[简介 - pyecharts - A Python Echarts Plotting Library built with love.](https://pyecharts.org/#/zh-cn/intro)**

pyecharts是基于Echart图表的一个类库，而Echart是百度开源的一个可视化JavaScript库

pyecharts主要基于web浏览器进行显示，绘制的图形比较多，包括折线图，柱状图、饼图、漏斗图、地图、极坐标图等，代码量很少，而且很灵活，绘制出来的图形很美观

使用pyecharts时，需要安装相应的库，安装命令为：    pip install pyecharts

图形绘制过程，基本上所有的图表类型都是这样绘制的

pyecharts是百度开源的数据可视化工具，交互性良好，图表设计精巧，非常适合用于数据处理。

1. 支持30+常见图表  
2. 支持notebook环境（jupyter）
3. 集成Flask、Django等主流框架
4. 400+地图文件
5. ……

## 安装

#### 1.1pip安装

```
!pip install pyecharts
```

#### 1.2 源码安装

```
cd pyecharts
pip install -r requirements.txt
python setup.py install# 或者执行 python install.py
```



#### 柱状图

```python
from pyecharts.charts import Bar

bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render()
bar.render_notebook()
```

![image-20260122144429098](D:\博客\python\数据分析\pyecharts模块\辅助图片等\13图片\image-20260122144429098.png)

#### 1.2 链式调用

```
from pyecharts.charts import Bar

bar = (
    Bar()
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
)
bar.render()

```

![image-20260122144536937](D:\博客\python\数据分析\pyecharts模块\辅助图片等\13图片\image-20260122144536937.png)

## 创建折线图

3.1 创建.py文件

```python
from pyecharts.charts import Line
#得到折线图对象
line = Line()
#添加x轴数据
line.add_xaxis(["衬衫","羊毛衫","雪纺衫"])
#添加y轴数据
line.add_yaxis("商家A",[5,20,36])
#生成图表
line.render()
```

3.2 在.py文件中右键运行

3.3 在项目根目录中会生成一个render.html文件

![image-20241018135317245](D:\博客\python\数据分析\pyecharts模块\辅助图片等\13图片\image-20241018135317245.png)

3.4 浏览器中打开此页面，就能得到对应的折线图

![image-20241018135422346](D:\博客\python\数据分析\pyecharts模块\辅助图片等\13图片\image-20241018135422346.png)

### 1.常用配置项

pyecharts配置项分为：全局配置选项和系列配置选项

全局配置选项

​	基本介绍：针对整个图像进行设置，比如图像的标题，图像的图例，工具箱

​	设置方法：使用set_global_opts方法进行设置，具体有那些配置项可以去[官网](https://pyecharts.org/#/zh-cn/global_options)查看

```
from pyecharts.charts import Line
from pyecharts import options as opts
#得到折线图对象
line = Line()
#添加x轴数据
line.add_xaxis(["衬衫","羊毛衫","雪纺衫"])
#添加y轴数据
line.add_yaxis("商家A",[5,20,36])
#设置全局配置项
line.set_global_opts(
    #设置标题，设置居中展示，设置距离底部0%的距离
    title_opts=opts.TitleOpts(title="这是主标题", subtitle="这是副标题",pos_left="center",pos_bottom="0%"),
    #控制图例，图例是默认显示的
    legend_opts=opts.LegendOpts(is_show=True),
    #设置工具箱
    toolbox_opts=opts.ToolboxOpts(is_show=True),
    #设置视觉映射
    visualmap_opts=opts.VisualMapOpts(is_show=True)
)
#生成图表
line.render()
```

![image-20241018135808508](D:\博客\python\数据分析\pyecharts模块\辅助图片等\13图片\image-20241018135808508.png)

### 2.系列配置选项

​		基本介绍：针对具体的轴数据进行配置，比如y轴的某个数据

​		设置方法：在设置y轴数据时，后面添加各种配置项

```
from pyecharts.charts import Line
from pyecharts import options as opts
#得到折线图对象
line = Line()
#添加x轴数据
line.add_xaxis(["衬衫","羊毛衫","雪纺衫"])
#添加y轴数据，配置不显示y轴每个具体数据值的展示
line.add_yaxis("商家A",[5,20,36], label_opts=opts.LabelOpts(is_show=False))
#生成图表
line.render()
```

![image-20241018140012601](D:\博客\python\数据分析\pyecharts模块\辅助图片等\13图片\image-20241018140012601.png)

## 创建柱状图

### 1.创建基本柱状图

在创建柱状图前，需要了解第二步中的基础入门介绍，以便更好理解代码内容和执行流程

```
from pyecharts.charts import Bar
from pyecharts import options as opts
#得到柱状图对象
bar = Bar()
#添加x轴数据
bar.add_xaxis(["衬衫","羊毛衫","雪纺衫"])
#添加y轴数据
bar.add_yaxis("商家A",[5,20,36], label_opts=opts.LabelOpts(is_show=False))
#生成图表
bar.render()
```

![image-20241018140339140](D:\博客\python\数据分析\pyecharts模块\辅助图片等\13图片\image-20241018140339140.png)

### 2.创建反转柱状图

基本柱状图是以x轴为底座，y轴为数据展示，想要将x轴和y轴的功能反转可以如下操作

```
from pyecharts.charts import Bar
from pyecharts import options as opts
#得到折线图对象
bar = Bar()
#添加x轴数据
bar.add_xaxis(["衬衫","羊毛衫","雪纺衫"])
#添加y轴数据，并设置系列配置选项（数字默认是在柱状图中间显示的，这是设置数字居右显示）
bar.add_yaxis("商家A",[5,20,36],label_opts=opts.LabelOpts(position="right"))
#反转x轴和y轴
bar.reversal_axis()
#生成图表
bar.render()
```

![image-20241018140605641](D:\博客\python\数据分析\pyecharts模块\辅助图片等\13图片\image-20241018140605641.png)

### 3.创建含有时间线的柱状图

想要创建一个根据不同的时间动态显示柱状图，从而能动态查看到柱状图不同类别的数据变化，其原理就是创建一个时间线对象，再创建多个柱状图，将柱状图分别添加到时间线对象中，设置时间线对象的自动播放

```
from pyecharts.charts import Bar, Timeline
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# 第一步：创建柱状图对象
bar1 = Bar()
bar1.add_xaxis(["衬衫", "羊毛衫", "雪纺衫"])
bar1.add_yaxis("商家A", [5, 20, 30], label_opts=opts.LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["衬衫", "羊毛衫", "雪纺衫"])
bar2.add_yaxis("商家A", [10, 15, 25], label_opts=opts.LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["羊毛衫","衬衫", "雪纺衫"])			#这里想要在图表中将数据大的放上面，则需要按从小到大的顺序排序
bar3.add_yaxis("商家A", [10, 15, 20], label_opts=opts.LabelOpts(position="right"))
bar3.reversal_axis()

# 第二步：创建时间线对象
#timeline = Timeline()          #此为创建空的时间线对象
timeline = Timeline({           #创建带主题的时间线对象
    "theme": ThemeType.LIGHT,  #设置主题
})
# 第三步：在时间线内添加柱状图对象
timeline.add(bar1, "点1")
timeline.add(bar2, "点2")
timeline.add(bar3, "点3")

# 第四步：设置自动播放
timeline.add_schema(
    play_interval=1000,     # 自动播放的时间间隔，单位毫秒
    is_timeline_show=True,  # 在自动播放时，是否显示时间线
    is_auto_play=True,      # 是否自动播放
    is_loop_play=True,      # 是否循环播放
)
# 第五步：生成图表，这里是用时间线对象生成图标，而不是柱状图对象
timeline.render()

```

![image-20241018141702011](D:\博客\python\数据分析\pyecharts模块\辅助图片等\13图片\image-20241018141702011.png)

### 4.pyecharts绘制饼图

```
# 导入模块
from pyecharts import options as opts
from pyecharts.charts import Pie
#准备数据
label=['Mac口红','Tom Ford口红','圣罗兰','纪梵希','花西子','迪奥','阿玛尼','香奈儿']  
values = [300,300,300,300,44,300,300,300]
# 自定义函数
def pie_base():
    c = (
        Pie()
        .add("",[list(z) for z in zip(label,values)])
        .set_global_opts(title_opts = opts.TitleOpts(title="口红品牌分析"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c} {d}%"))   # 值得一提的是，{d}%为百分比
    )
    return c
# 调用自定义函数生成render.html
pie_base().render()

```

![image-20241018183430768](D:\博客\python\数据分析\pyecharts模块\辅助图片等\13图片\image-20241018183430768.png)





**官方地址：**

https://gallery.pyecharts.org/#/Boxplot/boxplot_light_velocity

https://pyecharts.org/#/zh-cn/intro





## Faker

用于**测试、数据库填充、原型开发、数据脱敏**等场景。

应用

```
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values(), stack="stack1")
    .add_yaxis("商家B", Faker.values(), stack="stack1")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-堆叠数据（全部）"))
    .render("bar_stack0.html")
)
```

