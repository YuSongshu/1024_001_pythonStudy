# 饼图

```
#绘制饼图
from pyecharts.charts import Pie
from pyecharts import options as opts

#创建饼图对象(注意：如果在做数据分析图的时候不知道怎么做可以照搬官网模板在自己修改)
pie = (
    Pie().add("果园",[("苹果",30),("梨子",20),("香蕉",50)])
    .set_colors(["red", "green", "yellow"])
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .set_global_opts(title_opts = opts.TitleOpts(title = "果园比例分析图"))
)

pie.render_notebook()
```

# 雷达图

```
#雷达图
from pyecharts import options as opts
from pyecharts.charts import Radar

data1 = [[10,7,8,8,9,7]]  # 自由属性点
data2 = [[9,5,7,8,6,7]]   # 初始属性点

c = (
    Radar()
    .add_schema(
        schema=[
            opts.RadarIndicatorItem(name="攻击", max_=10),
            opts.RadarIndicatorItem(name="法攻", max_=10),
            opts.RadarIndicatorItem(name="防御", max_=10),
            opts.RadarIndicatorItem(name="体力", max_=10),
            opts.RadarIndicatorItem(name="速度", max_=10),
            opts.RadarIndicatorItem(name="血量", max_=10),
        ]
    )
    .add("自由属性点", data1)
    .add("初始属性点", data2)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="游戏角色属性分配"))
)
# c.render("DataName666.html")  # 将 render 单独调用
c.render_notebook()
```

# 箱型图

使用场景： 查看异常值的时候，比较有用,发现异常过大 或者 多小的数据

数据：[1, 3, 5, 7, 9, 11, 13, 15]

​	数据个数 n = 8

​	已排序 

**中位数（Q2）位置：**

​	在第 4 和第 5 个数之间：(7 + 9) / 2 = 8



**使用百分位法求取：**

Q1 位置 = (8+1) × 0.25 = 9 × 0.25 = 2.25

​	在第 2 和第 3 个数之间，距离第 2 个数 0.25 的位置

​	Q1 = 3 + 0.25 × (5 - 3) = 3 + 0.5 = **3.5**

Q3 位置 = (8+1) × 0.75 = 9 × 0.75 = 6.75

​	在第 6 和第 7 个数之间，距离第 6 个数 0.75 的位置

​	Q3 = 11 + 0.75 × (13 - 11) = 11 + 1.5 = **12.5**

**总结：** 根据常用的两种计算方法：

​	**分割法：Q1 = 4, Q3 = 12**

​	**百分位法：Q1 = 3.5, Q3 = 12.5**

​	**四分位数定义：**

Q0（最小值）= 1       # min 最小值

Q1（第 25 百分位） = 3.5

Q2（中位数，第 50 百分位） = 8    # median 中位数

Q3（第 75 百分位）= 12.5

Q4（最大值）= 15      # max  最大值

```
# 箱型图

from pyecharts import options as opts
from pyecharts.charts import Boxplot

v1 = [  
    [1, 3, 5, 7, 9, 11, 13, 15]
]

c = Boxplot()  
c.add_xaxis(["数据1"])     
c.add_yaxis("", c.prepare_data(v1))
c.set_global_opts(title_opts=opts.TitleOpts(title="箱型图的演练"))

c.render_notebook()
```



# 数据可视化拓展知识点

## 1. 饼图（Pie Chart）进阶应用

### 1.1 南丁格尔玫瑰图
南丁格尔玫瑰图也叫极坐标堆叠图，通过弧度和面积来表现数据的大小。

```python
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(['香蕉','橘子','玫瑰'],[10, 20, 30])],
        radius=["40%", "75%"],  # 内外半径
        rosetype="area"  # 设置为南丁格尔玫瑰图
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="南丁格尔玫瑰图"),
        legend_opts=opts.LegendOpts(
            orient="vertical", pos_top="15%", pos_left="2%"
        ),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    
)

c.render_notebook()
```

### 
## 2. 雷达图（Radar Chart）进阶应用

### 2.1 多维度对比雷达图
```python
from pyecharts import options as opts
from pyecharts.charts import Radar

v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]

c = (
    Radar()
    .add_schema(
        schema=[
            opts.RadarIndicatorItem(name="销售", max_=6500),
            opts.RadarIndicatorItem(name="管理", max_=16000),
            opts.RadarIndicatorItem(name="信息技术", max_=30000),
            opts.RadarIndicatorItem(name="客服", max_=38000),
            opts.RadarIndicatorItem(name="研发", max_=52000),
            opts.RadarIndicatorItem(name="市场", max_=25000),
        ]
    )
    .add("预算", v1, color="#f97054")
    .add("实际", v2, color="#009800")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="企业各部门能力对比"),
        legend_opts=opts.LegendOpts(selected_mode="single")
    )
    .render_notebook()
)
```




## 3. 实际生活应用场景

### 3.1 学生成绩分析
```python
from pyecharts import options as opts
from pyecharts.charts import Radar, Boxplot

# 学生能力雷达图
student_scores = [[85, 78, 92, 88, 80, 90]]
subjects = ["语文", "数学", "英语", "物理", "化学", "生物"]

radar = (
    Radar()
    .add_schema(
        schema=[
            opts.RadarIndicatorItem(name="语文", max_=100),
            opts.RadarIndicatorItem(name="数学", max_=100),
            opts.RadarIndicatorItem(name="英语", max_=100),
            opts.RadarIndicatorItem(name="物理", max_=100),
            opts.RadarIndicatorItem(name="化学", max_=100),
            opts.RadarIndicatorItem(name="生物", max_=100),
        ]
    )
    .add("张同学", student_scores)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="学生综合能力分析"),
        legend_opts=opts.LegendOpts(selected_mode="single")
    )
)

radar.render_notebook()
```

```
# 班级成绩分布箱型图
class_a = [75, 78, 80, 82, 85, 88, 90, 92, 95, 98]
class_b = [70, 72, 75, 78, 80, 82, 85, 88, 90, 92]
class_c = [65, 68, 70, 72, 75, 78, 80, 82, 85, 88]

boxplot = Boxplot()
classes = ["A班", "B班", "C班"]
scores = [class_a, class_b, class_c]

box_plot = (
    Boxplot()
    .add_xaxis(xaxis_data=classes)
    .add_yaxis(series_name="", y_axis=boxplot.prepare_data(scores))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="各班级成绩分布对比"),
        tooltip_opts=opts.TooltipOpts(trigger="item", axis_pointer_type="shadow"),
    )
)

box_plot.render_notebook()
```



