# Pandas 教程

## 初识pandas

Pandas 是 Python 语言的一个扩展程序库，用于数据分析。

Pandas 名字衍生自术语 "panel data"（面板数据）和 "**Python data analysis**"（Python 数据分析）。

Pandas 是一个开放源码、BSD 许可的库，提供高性能、易于使用的数据结构和数据分析工具。

Pandas 一个强大的分析结构化数据的工具集，基础是 [Numpy](https://www.runoob.com/numpy/numpy-tutorial.html)（提供高性能的矩阵运算）。

***Pandas 可以从各种文件格式比如 CSV、JSON、SQL、Microsoft Excel 导入数据。***

Pandas 可以对各种数据进行运算操作，比如归并、再成形、选择，还有***数据清洗和数据加工特征***。

### Pandas 应用

Pandas 的主要数据结构是 Series （一维数据）与 ***DataFrame（二维数据***）。

Pandas 广泛应用在学术、金融、统计学等各个数据分析领域。

### 数据结构

**[Series](https://www.runoob.com/pandas/pandas-series.html)** 是一种类似于一维数组的对象，它由一组数据（各种 Numpy 数据类型）以及一组与之相关的数据标签（即索引）组成。

**DataFrame** 是一个***表格型***的数据结构，它含有一组有序的列，***每列可以是不同的值类型（数值、字符串、布尔型值）***。DataFrame 既有行索引也有列索引，它可以被看做由 Series 组成的字典（共同用一个索引）。



### Pandas 简介

Pandas 是一个开源的数据分析和数据处理库，它是基于 Python 编程语言的。

Pandas 提供了易于使用的数据结构和数据分析工具，特别适用于处理结构化数据，如***表格型数据（类似于Excel表格）***。

Pandas 是数据科学和分析领域中常用的工具之一，它使得用户能够轻松地从各种数据源中导入数据，并对数据进行高效的操作和分析。

Pandas 主要引入了两种新的数据结构：**DataFrame** 和 **Series**。

- **Series**： 类似于一维数组或列表，是由一组数据以及与之相关的数据标签（索引）构成。Series 可以看作是 DataFrame 中的一列，也可以是单独存在的一维数据结构。



- **DataFrame**： 类似于一个二维表格，它是 Pandas 中最重要的数据结构。DataFrame 可以看作是由多个 Series 按列排列构成的表格，它既有行索引也有列索引，因此可以方便地进行行列选择、过滤、合并等操作。



**DataFrame 可视为由多个 Series 组成的数据结构：**

![pandas-DataStructure](D:\tool\数据分析\7：Pandas简介与使用\图片\pandas-DataStructure.png)

Pandas 提供了丰富的功能，包括：

- 数据清洗：处理缺失数据、重复数据等。
- 数据转换：改变数据的形状、结构或格式。
- 数据分析：进行统计分析、聚合、分组等。
- 数据可视化：通过整合 Matplotlib 和 Seaborn 等库，可以进行数据可视化。



### Pandas 应用

Pandas 在数据科学和数据分析领域中具有广泛的应用，其主要优势在于能够处理和分析结构化数据。

以下是 Pandas 的一些主要应用领域：

- **数据清洗和预处理：** Pandas被广泛用于清理和预处理数据，包括处理缺失值、异常值、重复值等。它提供了各种方法来使数据更适合进行进一步的分析。
- **数据分析和统计：** Pandas使数据分析变得更加简单，通过DataFrame和Series的灵活操作，用户可以轻松地进行统计分析、汇总、聚合等操作。从均值、中位数到标准差和相关性分析，Pandas都提供了丰富的功能。
- **数据可视化：** 将Pandas与Matplotlib、Seaborn等数据可视化库结合使用，可以创建各种图表和图形，从而更直观地理解数据分布和趋势。这对于数据科学家、分析师和决策者来说都是关键的。
- **时间序列分析：** Pandas在处理时间序列数据方面表现出色，支持对日期和时间进行高效操作。这对于金融领域、生产领域以及其他需要处理时间序列的行业尤为重要。
- **机器学习和数据建模：** 在机器学习中，数据预处理是非常关键的一步，而Pandas提供了强大的功能来处理和准备数据。它可以帮助用户将数据整理成适用于机器学习算法的格式。
- **数据库操作：** Pandas可以轻松地与数据库进行交互，从数据库中导入数据到DataFrame中，进行分析和处理，然后将结果导回数据库。这在数据库管理和分析中非常有用。
- **实时数据分析：** 对于需要实时监控和分析数据的应用，Pandas的高效性能使其成为一个强大的工具。结合其他实时数据处理工具，可以构建实时分析系统。

Pandas 在许多领域中都是一种强大而灵活的工具，为数据科学家、分析师和工程师提供了处理和分析数据的便捷方式。

### Pandas 安装

安装 pandas 需要基础环境是 Python，Pandas 是一个基于 Python 的库，因此你需要先安装 Python，然后再通过 Python 的包管理工具 **pip** 安装 Pandas。

使用 pip 安装 pandas:

```
!pip install pandas
```

安装成功后，我们就可以导入 pandas 包使用：

```
import pandas
```

## 查看 pandas 版本

```
>>> import pandas
>>> pandas.__version__  # 查看版本
'1.1.5'
```

导入 pandas 一般使用别名 **pd** 来代替：

```
import pandas as pd
```



## 查看 pandas 版本

```
>>> import pandas as pd
>>> pd.__version__  # 查看版本
'1.1.5'
```



## 一个简单的 pandas 实例：

```
import pandas as pd

mydataset = {
  'sites': ["Google", "Runoob", "Wiki"],
  'number': [1, 2, 3]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
```

执行以上代码，输出结果为：

```
    sites  number
0  Google       1
1  Runoob       2
2    Wiki       3
```



## Pandas 数据结构 - Series

Pandas Series 类似表格中的一个列（column），类似于一维数组，可以保存任何数据类型。

### Series 特点：

- **索引：** 每个 `Series` 都有一个索引，它可以是整数、字符串、日期等类型。如果没有显式指定索引，Pandas 会自动创建一个默认的整数索引。
- **数据类型：** `Series` 可以容纳不同数据类型的元素，包括整数、浮点数、字符串等。



Series 是 Pandas 中的一种基本数据结构，类似于一维数组或列表，但具有标签（索引），使得数据在处理和分析时更具灵活性。

以下是关于 Pandas 中的 Series 的详细介绍： 创建 Series： 可以使用 pd.Series() 构造函数创建一个 Series 对象，传递一个数据数组（可以是列表、NumPy 数组等）和一个可选的索引数组。

```
pandas.Series( data, index, dtype, name, copy)
```

参数说明：

- **data**：一组数据(ndarray 类型)。
- **index**：数据索引标签，如果不指定，默认从 0 开始。
- **dtype**：数据类型，默认会自己判断。
- **name**：设置名称。
- **copy**：拷贝数据，默认为 False。



### 创建一个简单的 Series 实例：

```
import pandas as pd

a = [1, 2, 3]

myvar = pd.Series(a)

print(myvar)
```

输出：

```
0    1
1    2
2    3
dtype: int64
```



#### 从上例可知，如果没有指定索引，索引值就从 0 开始，我们可以根据索引值读取数据：

```
import pandas as pd

a = [1, 2, 3]

myvar = pd.Series(a)

print(myvar[1])
```

输出：

```
2
```

#### 我们可以指定索引值：

```
import pandas as pd

a = ["Google", "Runoob", "Wiki"]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
```

输出：

```
x    Google
y    Runoob
z      Wiki
dtype: str
```



#### 根据索引值读取数据:

```
import pandas as pd

a = ["Google", "Runoob", "Wiki"]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar["y"])
```

输出：

```
Runoob
```



### 使用 key/value 对象，类似字典来创建 Series：

```
import pandas as pd

sites = {1: "Google", 2: "Runoob", 3: "Wiki"}

myvar = pd.Series(sites)

print(myvar)
```

输出：

```
1    Google
2    Runoob
3      Wiki
dtype: str
```



#### 从上例可知，字典的 key 变成了索引值。如果我们只需要字典中的一部分数据，只需要指定需要数据的索引即可：

```
import pandas as pd

sites = {1: "Google", 2: "Runoob", 3: "Wiki"}

myvar = pd.Series(sites, index = [1，1, 2])

print(myvar)
```

输出：

```
1    Google
1    Google
2    Runoob
dtype: str
```



#### 设置 Series 名称参数：

```
import pandas as pd

sites = {1: "Google", 2: "Runoob", 3: "Wiki"}

myvar = pd.Series(sites, index = [1, 2], name="RUNOOB-Series-TEST" )

print(myvar)
```

输出：

```
1    Google
2    Runoob
Name: RUNOOB-Series-TEST, dtype: str
```



### 更多 Series 说明

**基本操作：**

```
# 获取值
value = series[2]  # 获取索引为2的值

# 获取多个值
subset = series[1:4]  # 获取索引为1到3的值

# 索引和值的对应关系
0
```

**基本运算：**

```
# 算术运算
result = series * 2  # 所有元素乘以2

# 过滤
filtered_series = series[series > 2]  # 选择大于2的元素
```

**属性和方法：**

```
# 获取索引
index = series_with_index.index

# 获取值数组
values = series_with_index.values

# 获取描述统计信息
stats = series_with_index.describe()

# 获取最大值和最小值的索引
max_index = series_with_index.idxmax()
min_index = series_with_index.idxmin()
```

**注意事项：**

- `Series` 中的数据是有序的。
- 可以将 `Series` 视为带有索引的一维数组。
- 索引可以是唯一的，但不是必须的。   # 废话
- 数据可以是标量、列表、NumPy 数组等。 

## Pandas 数据结构 - DataFrame

DataFrame 是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型值）。DataFrame 既有行索引也有列索引，它可以被看做由 Series 组成的字典（共同用一个索引）。

**DataFrame 特点：**

- **列和行：** `DataFrame` 由多个列组成，每一列都有一个名称，可以看作是一个 `Series`。同时，`DataFrame` 有一个行索引，用于标识每一行。
- **二维结构：** `DataFrame` 是一个二维表格，具有行和列。可以将其视为多个 `Series` 对象组成的字典。
- **列的数据类型：** 不同的列可以包含不同的数据类型，例如整数、浮点数、字符串等。



DataFrame 构造方法如下：

```
pandas.DataFrame( data, index, columns, dtype, copy)
```

参数说明：

- **data**：一组数据(ndarray、series, map, lists, dict 等类型)。
- **index**：索引值，或者可以称为行标签。
- **columns**：列标签，默认为 RangeIndex (0, 1, 2, …, n) 。
- **dtype**：数据类型。
- **copy**：拷贝数据，默认为 False。

Pandas DataFrame 是一个二维的数组结构，类似二维数组。



### 使用列表创建

```
import pandas as pd

data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]

# 创建DataFrame
df = pd.DataFrame(data, columns=['Site', 'Age'])

# 使用astype方法设置每列的数据类型
df['Site'] = df['Site'].astype(str)
df['Age'] = df['Age'].astype(float)

print(df)
print('\n')
print(df.dtypes)
```

输出：

```
     Site   Age
0  Google  10.0
1  Runoob  12.0
2    Wiki  13.0


Site        str
Age     float64
dtype: object
```





ndarrays 可以参考：[NumPy Ndarray 对象](https://www.runoob.com/numpy/numpy-ndarray-object.html)

### 使用 ndarrays 创建

使用 ndarrays 创建，ndarray 的长度必须相同， 如果传递了 index，则索引的长度应等于数组的长度。如果没有传递索引，则默认情况下，索引将是range(n)，其中n是数组长度。

```
import numpy as np
import pandas as pd

# 创建一个包含网站和年龄的二维ndarray
ndarray_data = np.array([
    ['Google', 10],
    ['Runoob', 12],
    ['Wiki', 13]
])

# 使用DataFrame构造函数创建数据帧
df = pd.DataFrame(ndarray_data, columns=['Site', 'Age'])

# 打印数据帧
print(df)
```

输出：

```
     Site Age
0  Google  10
1  Runoob  12
2    Wiki  13
```



### 使用字典创建

字典的 key 为列名

```
import pandas as pd

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

df = pd.DataFrame(data)

print (df)
```

输出结果为：

```
   a   b     c
0  1   2   NaN
1  5  10  20.0
```

**注：**

没有对应的部分数据为 **NaN**。



###  **loc** 属性

Pandas 可以使用 **loc** 属性返回指定行的数据，如果没有设置索引，第一行索引为 **0**，第二行索引为 **1**，以此类推：

#### 实例

```
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)

# 返回第一行
print(df.loc[0])
# 返回第二行
print(df.loc[1])
```

输出：

```
calories    420
duration     50
Name: 0, dtype: int64
calories    380
duration     40
Name: 1, dtype: int64

```

**注：**

返回结果其实就是一个 Pandas Series 数据。

也可以返回多行数据，使用 **[[ ... ]]** 格式，**...** 为各行的索引，以逗号隔开：

```
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)

# 返回第一行和第二行
print(df.loc[[0, 1]])

```

输出结果为：

```
   calories  duration
0       420        50
1       380        40

```

**注：**

返回结果其实就是一个 Pandas DataFrame 数据。



#### 指定索引值：

##### 实例

```
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)

```

输出结果为：

```
      calories  duration
day1       420        50
day2       380        40
day3       390        45

```



#### Pandas 可以使用 **loc** 属性返回指定索引对应到某一行：

##### 实例

```
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

# 指定索引
print(df.loc["day2"])

```

输出结果为：

```
calories    380
duration     40
Name: day2, dtype: int64

```





### 更多 DataFrame 说明

#### 基本操作：

```
# 获取列
name_column = df['Name']

# 获取行
first_row = df.loc[0]

# 选择多列
subset = df[['Name', 'Age']]

# 过滤行
filtered_rows = df[df['Age'] > 30]

```



#### 属性和方法：

```
# 获取列名
columns = df.columns

# 获取形状（行数和列数）
shape = df.shape

# 获取索引
index = df.index			# 注意：series和DataFrame的索引获取，结果显示不一样

# 获取描述统计信息
stats = df.describe()
```

#### 数据操作：

```
# 添加新列
df['Salary'] = [50000, 60000, 70000]

# 删除列
df.drop('City', axis=1, inplace=True)

# 排序
df.sort_values(by='Age', ascending=False, inplace=True)

# 重命名列
df.rename(columns={'Name': 'Full Name'}, inplace=True)
```



#### 从外部数据源创建 DataFrame：

```
# 从CSV文件创建 DataFrame
df_csv = pd.read_csv('example.csv')

# 从Excel文件创建 DataFrame
df_excel = pd.read_excel('example.xlsx')

# 从字典列表创建 DataFrame
import pandas as pd
data_list = [{'Name': 'Alice', 'Age': 25}, {'Name': 'Bob', 'Age': 30}]
df_from_list = pd.DataFrame(data_list)
print(df_from_list)

```

**注：**

- `DataFrame` 是一种灵活的数据结构，可以容纳不同数据类型的列。
- 列名和行索引可以是字符串、整数等。
- `DataFrame` 可以通过多种方式进行数据选择、过滤、修改和分析。
- 通过对 `DataFrame` 的操作，可以进行数据清洗、转换、分析和可视化等工作。