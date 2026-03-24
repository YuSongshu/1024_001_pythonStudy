# 01NumPy是什么——

NumPy 的全称是“ Numeric [Python]”，它是 Python 的第三方扩展包，主要用来计算、处理一维或多维数组。

在数组算术计算方面， NumPy 提供了大量的数学函数。NumPy 的底层主要用 C语言编写，因此它能够高速地执行数值计算。NumPy 还提供了多种[数据结构]，这些数据结构能够非常契合的应用在数组和矩阵的运算上。

NumPy 的前身是 Numeric 程序包，该包由 Jim Hugunin 开发，在这之后，他还开发了另一个类似的的程序包 Numarray，相比前者而言 Numarray 具有更加全面的功能 。在 2005 年，Travis Oliphant 通过整合 Numarray 与 Numeric 软件包的功能，从而集成了 NumPy。NumPy 的最新版本 1.19.2 已于 2020 年 9 月10 日发布。

> NumPy 作为一个开源项目，它由许多协作者共同开发维护，这也是 NumPy 的优势之一。



## NumPy使用需求

随着数据科学（Data Science，简称 DS，包括大数据分析与处理、大数据存储、数据抓取等分支）的蓬勃发展，像 NumPy、SciPy（Python科学计算库）、Pandas（基于NumPy的数据处理库） 等数据分析库都有了大量的增长，它们都具有较简单的语法格式。

在矩阵乘法与数组形状处理上，NumPy 有着非常不错的性能，再加上 NumPy 的计算速度很快，这些都是 NumPy 成为一款数据分析工具的重要原因。

> 数组形状可以理解为数组的维度，比如一维数组、二维数组、三维数组等；以二维数组为例，改变数组形状就是交换数组的行和列，也即将数组旋转 90 度。

NumPy 可以很便捷高效地处理大量数据，那么使用 NumPy 做数据处理有哪些优点呢？总结如下：

- NumPy 是 Python 科学计算基础库；
- NumPy 可以对数组进行高效的数学运算；
- NumPy 的 ndarray 对象可以用来构建多维数组；
- NumPy 能够执行傅立叶变换与重塑多维数组形状；
- NumPy 提供了线性代数，以及随机数生成的内置函数。





## NumPy应用场景

NumPy 通常与 SciPy（Python科学计算库）和 Matplotlib（Python绘图库）等软件包组合使用，这种组合方式被用来广泛地代替 MatLab 的使用。

MatLab 是一款强大的数学计算软件，广泛应用在数据分析、电子通信、深度学习、图像处理、机器视觉、量化金融等领域，但近些年随着 Python 语言的迅猛发展，Python 被看作是一种更适合代替  MatLab 的编程语言。您可以使用 NumPy、SciPy 与 Matplotlib 等 Python 工具包搭建科学计算环境，比如 Anaconda 就是是一个开源的 Python 发行版本，它包含了 Python 、NumPy 等 180 多个科学包及其依赖项。

因为 NumPy 是 Python 的扩展程序包，所以您在学习 NumPy 之前应该具备一些 Python 基础知识，这对本教程的学习将大有裨益。如果您想了解关于 NumPy 更多的知识可浏览 NumPy 官网：[NumPy -](https://numpy.org/)







## NumPy下载与安装

NumPy 是 [Python] 的第三方扩展包，但它并没有包含在 Python 标准库中，因此您需要单独安装它。本节介绍如何在不同的操作系统上安装 NumPy。

### Windows系统安装

在 Windows 系统下安装 NumPy 有两种常用方式，下面分别对其进行介绍。

使用 Python 包管理器`pip`来安装 NumPy，是一种最简单、最轻量级的方法。只需执行以下命令即可：

```
!pip install numpy
```

在实际项目中， NumPy 通常与 SciPy 程序包一起使用，SciPy 可以看做对 NumPy 库的扩展，它在 NumPy 的基础上又增加了许多工程计算函数。因此将它们同时安装是一个不错的选择。但如果你只想针对 NumPy 进行学习，可以不用考虑这种安装方法。

注意：在 Windows 下直接使用 pip 安装 SciPy 会发生报错，需要我们解决 SciPy 的依赖项问题，所以不推荐使用`pip`安装 SciPy 程序包。下面介绍如何使用 SciPy 栈安装。

首先我们要知道什么是 SciPy 栈？其实它是一个科学计算软件包的集成平台，这类平台囊括了常用的数值计算与机器学习库，比如 NumPy、Matplotlib、SciPy 库、IPython 等，并且它可以自动解决包之间的依赖问题。通过安装一个集成平台就可以实现上述所有软件包的安装，何乐而不为呢

下面介绍几种常用的 SciPy 栈，主要有以下几种：

Anaconda（官网下载：https://www.anaconda.com/）是一个开源的 Python 发行版，它包含了 NumPy、SciPy 等180多个科学包及其依赖项。除了支持 Windows 外，也支持 Linux 和 Mac 系统。Anaconda 就目前应用较为广泛，因此建议安装。

> Anaconda 的下载文件约 500 MB 左右，你可以选择安装 Miniconda，它是 Anaconda 的轻巧版，只需 40 余兆。

Python(x,y)（下载地址：https://python-xy.github.io/）是一款基于 Python、[Qt](https://c.biancheng.net/qt/) （图形用户界面）和 Spyder （交互式开发环境）开发的软件，主要用于数值计算、数据分析和数据可视化等工程项目，目前只支持 Python 2 版本。

Pyzo（下载地址：https://pyzo.org/）是一个跨平台 Python IDE，基于 Python 3 编写，非常适合科学计算，它设计的宗旨就是为了简化和提供效率。

WinPython（下载地址：https://sourceforge.net/projects/winpython/files/）免费的 Python 发行版，包含了常用的科学计算包与 Spyder IDE 开发环境，但仅支持 Windows 系统。





### MacOSX系统安装

Mac 系统虽然自带包管理器`Homebrew`，但是它不能下载 NumPy 等科学计算包，所以需要使用下列方式安装：

```
$ pip3 install numpy scipy matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
```

注意：-i 参数后指的是国内下载源，加快下载的速度。





### Linux系统安装

在 Linux 系统中，您可以选择只单独安装 NumPy 一个软件包，也可以同时安装多个软件包。下面介绍了不同的 Linux 发行版具体的安装命令，如下所示：

#### 1) Ubuntu/Debian

对于 Ubuntu/Debian 系统，可以在终端上执行以下命令：

```
$ sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose 
```



#### 2) Redhat/CentOS

在 Redhat/CentOS 系统上执行以下命令来安装 NumPy 与其它科学计算包：

```
$ sudo yum install numpy scipy python-matplotlib ipython python-pandas sympy python-nose
```

注意：不同的软件包之间必须使用“一个空格”隔开。

最后验证是否安装成功，如下所示：

打开 Python 交互解释器 ，并导入 NumPy 模块，如下图 2 所示如果未出现错误提示，则表示已安装成功。

```
注意：这里是以 Windows 系统为例进行验证的，Linux 验证方式与其相同。
```







## NumPy ndarray对象

NumPy 定义了一个 n 维数组对象，简称 ndarray 对象，它是一个一系列相同类型元素组成的数组集合。数组中的每个元素都占有大小相同的内存块，您可以使用索引或切片的方式获取数组中的每个元素。

> ndarray 对象有一个 dtype 属性，该属性用来描述元素的数据类型，

ndarray 对象采用了数组的索引机制，将数组中的每个元素映射到内存块上，并且按照一定的布局对内存块进行排列，常用的布局方式有两种，即按行或者按列。

### 创建 ndarray 对象

通过 NumPy 的内置函数 array() 可以创建 ndarray 对象，其语法格式如下：

```
numpy.array(object,ndmin = 0)
```

下面表格对其参数做了说明：

| 序号 | 参数    | 描述说明                                 |
| ---- | ------- | ---------------------------------------- |
| 1    | object  | 表示一个数组序列。                       |
| 2    | dtype   | 可选参数，通过它可以更改数组的数据类型。 |
| 3    | ndim    | 用于指定数组的维度。                     |
| 4    | reshape | 用于改变行数和列数                       |

创建一维数组：

```
a=numpy.array([1,2,3])
```

示例代码：

```
import numpy
a=numpy.array([1,2,3])#使用列表构建一维数组
print(a)
[1 2 3]
print(type(a))
#ndarray数组类型
<class 'numpy.ndarray'>
```

创建多维数组：

```
b=numpy.array([[1,2,3],[4,5,6]])
```

示例代码：

```
b=numpy.array([[1,2,3],[4,5,6]])
print(b)
[[1 2 3]
[4 5 6]]
```

如果要改变数组元素的数据类型，可以使用通过设置 dtype，如下所示：

```
c=numpy.array([2,4,6,8],dtype="数据类型名称")
```

array() 是创建 ndarray 对象的基本方法，在后续内容中还会介绍其他方法。



### ndim查看数组维数

通过 ndim 可以查看数组的维度：

```
import numpy as np 
arr = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [9, 10, 11, 23]]) 
print(arr.ndim) 
2
```

您也可以使用 ndim 参数创建不同维度的数组：

```
#输出一个二维数组
import numpy as np
a = np.array([1, 2, 3,4,5], ndimn = 2)
print(a)
```

输出结果如下：

```
[[1 2 3 4 5]]
```



### reshape数组变维

数组的形状指的是多维数组的行数和列数。Numpy 模块提供 reshape() 函数可以改变多维数组行数和列数，从而达到数组变维的目的。因此数组变维即对数组形状的重塑：

reshape() 函数可以接受一个元组作为参数，用于指定了新数组的行数和列数，示例如下：

```
import numpy as np 
e = np.array([[1,2],[3,4],[5,6]]) 
print("原数组",e) 
e=e.reshape(2,3) 
print("新数组",e)  
```

输出如下：

```
原数组 [[1 2]
[3 4]
[5 6]]
新数组 [[1 2 3]
[4 5 6]]
```







# 02类型——

## 1. NumPy 数据类型

numpy 支持的数据类型比 Python 内置的类型要多很多，基本上可以和 C 语言的数据类型对应上，其中部分类型对应为 Python 内置的类型。下表列举了常用 NumPy 基本类型。

| 名称        | 描述                                                         |
| :---------- | :----------------------------------------------------------- |
| **bool_**   | 布尔型数据类型（True 或者 False）                            |
| int_        | 默认的整数类型（类似于 C 语言中的 long，int32 或 int64）     |
| intc        | 与 C 的 int 类型一样，一般是 int32 或 int 64                 |
| intp        | 用于索引的整数类型（类似于 C 的 ssize_t，一般情况下仍然是 int32 或 int64） |
| **int8**    | **字节（范围-128 to 127）（代表与1字节相同的8位整数）**      |
| **int16**   | **整数（范围-32768 to 32767）（代表 2 字节（16位）的整数）** |
| **int32**   | **整数（-范围2147483648 to 2147483647）（代表 4 字节（32位）整数）** |
| **int64**   | **整数（范围-9223372036854775808 to 9223372036854775807）（表示 8 字节（64位）整数）** |
| uint8       | 无符号整数（0 to 255）                                       |
| uint16      | 无符号整数（0 to 65535）                                     |
| uint32      | 无符号整数（0 to 4294967295）                                |
| uint64      | 无符号整数（0 to 18446744073709551615）                      |
| **float16** | **半精度浮点数，包括：1 个符号位，5 个指数位，10 个尾数位**  |
| **float32** | **单精度浮点数，包括：1 个符号位，8 个指数位，23 个尾数位**  |
| **float_**  | **float64 类型的简写**                                       |
| **float64** | **双精度浮点数，包括：1 个符号位，11 个指数位，52 个尾数位** |
| complex_    | complex128 类型的简写，即 128 位复数                         |
| complex64   | 复数，表示双 32 位浮点数（实数部分和虚数部分）               |
| complex128  | 复数，表示双 64 位浮点数（实数部分和虚数部分）               |
| **str_**    | **表示字符串类型**                                           |
| **string_** | **表示字节串类型**                                           |

numpy 的数值类型实际上是 dtype 对象的实例，并对应唯一的字符，包括 np.bool_，np.int32，np.float32，等等。

### 数据类型标识码

NumPy 中每种数据类型都有一个唯一标识的字符码，如下所示：

数据类型标识码：

| 字符 | 对应类型                 |
| ---- | ------------------------ |
| b    | 代表布尔型               |
| i    | 带符号整型               |
| u    | 无符号整型               |
| f    | 浮点型                   |
| c    | 复数浮点型               |
| m    | 时间间隔（timedelta）    |
| M    | datatime（日期时间）     |
| O    | Python对象               |
| S,a  | 字节串（S）与字符串（a） |
| U    | Unicode                  |
| V    | 原始数据（void）         |

### 数据类型对象 (dtype)

数据类型对象（numpy.dtype 类的实例）用来描述与数组对应的内存区域是如何使用，它描述了数据的以下几个方面：：

- 数据的类型（整数，浮点数或者 Python 对象）
- 数据的大小（例如， 整数使用多少个字节存储）
- 数据的字节顺序（小端法或大端法）
- 在结构化类型的情况下，字段的名称、每个字段的数据类型和每个字段所取的内存块的部分
- 如果数据类型是子数组，那么它的形状和数据类型是什么。

字节顺序是通过对数据类型预先设定 **<** 或 **>** 来决定的。 **<** 意味着小端法(最小值存储在最小的地址，即低位组放在最前面)。**>** 意味着大端法(最重要的字节存储在最小的地址，即高位组放在最前面)。

dtype 对象是使用以下语法构造的：

```
numpy.dtype(object, align, copy)
```

- object - 要转换为的数据类型对象
- align - 如果为 true，填充字段使其类似 C 的结构体。
- copy - 复制 dtype 对象 ，如果为 false，则是对内置数据类型对象的引用

#### 实例

通过实例来理解

**实例 1**

```
import numpy as np
# 使用标量类型
dt = np.dtype(np.int32)
print(dt)
```

输出：

```
int32
```



**实例 2**

```
import numpy as np
# int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
dt = np.dtype('i4')
print(dt)
```

输出：

```
int32
```



**实例 3**

```
import numpy as np
# 字节顺序标注
dt = np.dtype('<i4')
print(dt)
```

输出：

```
int32
```



**实例 4**

下面实例展示结构化数据类型的使用，类型字段和对应的实际类型将被创建

```
# 首先创建结构化数据类型
import numpy as np
dt = np.dtype([('age',np.int8)]) 
print(dt)
```

输出：

```
[('age', 'i1')]
​``````
```



**实例 5**

下面的示例定义一个结构化数据类型 student，包含字符串字段 name，整数字段 age，及浮点字段 marks，并将这个 dtype 应用到 ndarray 对象。

```
import numpy as np
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)
```

输出：

```
[('name', 'S20'), ('age', 'i1'), ('marks', 'f4')]
```



**实例 8**

```
import numpy as np
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
a = np.array([('name1', 21, 50),('xyz', 18, 75)], dtype = student) 
print(a)
```

输出：

```
[('name1', 21, 50.0), ('xyz', 18, 75.0)]
```



## 2. NumPy 数组属性

NumPy 的数组中比较重要 ndarray 对象属性有：

| 属性               | 说明                                                         |
| :----------------- | :----------------------------------------------------------- |
| `ndarray.ndim`     | 数组的秩（rank），即数组的维度数量或轴的数量。               |
| `ndarray.shape`    | 数组的维度，表示数组在每个轴上的大小。对于二维数组（矩阵），表示其行数和列数。 |
| `ndarray.size`     | 数组中元素的总个数，等于 `ndarray.shape` 中各个轴上大小的乘积。 |
| `ndarray.dtype`    | 数组中元素的数据类型。                                       |
| `ndarray.itemsize` | 数组中每个元素的大小，以字节为单位。                         |



### ndarray.shape

shape 属性的返回值一个由数组维度构成的元组，比如 2 行 3 列的二维数组可以表示为`(2,3)`，该属性可以用来调整数组维度的大小。

```
import numpy as np
a = np.array([[2,4,6],[3,5,7]])
print(a.shape)
```

输出：

```
(2,3)
```



通过 shape 属性修改数组的形状大小： 

```
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
a.shape = (3,2)
print(a)
```

输出：

```
[[1, 2][3, 4][5, 6]]
```



### ndarray.reshape() 

作用：调整数组形状

```python
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(3,2)
print(b)
```

输出：

```python
[[1, 2][3, 4]
[5, 6]]
```



### ndarray.ndim

该属性返回的是数组的维数：

```
import numpy as np   #随机生成一个一维数组
c = np.arange(24)
print(c)
print(c.ndim)    #对数组进行变维操作
e = c.reshape(2,4,3)   *
print(e) 
print(e.ndim)
```

输出：

```
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
1
[[[ 0  1  2][ 3 4 5]
  [ 6  7  8][ 9 10 11]]

[[12 13 14][15 16 17]
  [18 19 20][21 22 23]]]
3

```



### ndarray.itemsize

返回数组中每个元素的大小（以字节为单位）：

数据类型为int8，代表1字节=8 bit

```
import numpy as np
x = np.array([1,2,3,4,5], dtype = np.int8)
print (x.itemsize)
```

输出：

```
1
```



数据类型为int64，代表8字节

```
import numpy as np
x = np.array([1,2,3,4,5], dtype = np.int64)
print (x.itemsize)
```

输出：

```
8
```







# 03数组——

## NumPy 数组属性

NumPy 的数组中比较重要 ndarray 对象属性有：

| 属性               | 说明                                                         |
| :----------------- | :----------------------------------------------------------- |
| `ndarray.ndim`     | 数组的秩（rank），即数组的维度数量或轴的数量。               |
| `ndarray.shape`    | 数组的维度，表示数组在每个轴上的大小。对于二维数组（矩阵），表示其行数和列数。 |
| `ndarray.size`     | 数组中元素的总个数，等于 `ndarray.shape` 中各个轴上大小的乘积。 |
| `ndarray.dtype`    | 数组中元素的数据类型。                                       |
| `ndarray.itemsize` | 数组中每个元素的大小，以字节为单位。                         |

## NumPy 创建数组

ndarray 数组除了可以使用底层 ndarray 构造器来创建外，也可以通过以下几种方式来创建

### numpy.empty

numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组：

```
numpy.empty(shape, dtype = float, order = 'C')
```

参数：

| 参数  | 描述                                                         |
| :---- | :----------------------------------------------------------- |
| shape | 数组形状                                                     |
| dtype | 数据类型，可选                                               |
| order | 有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。 |

**实例**

```
#创建数组
#empty表示：方法用来创建一个指定形状数组
a = np.empty([3,2],dtype = np.int64)
print(a)
```

输出：

```
[[25895968444448860 23925768161198147]
 [32370111954616435 31525648370892892]
 [18296268630786147 27303364806049904]]
```



注:  数组元素为随机值，因为它们未初始化



### numpy.zeros

创建指定大小的数组，数组元素以 0 来填充：

```
numpy.zeros(shape, dtype = float)
```

参数：

| 参数  | 描述           |
| :---- | :------------- |
| shape | 数组形状       |
| dtype | 数据类型，可选 |

**实例**

```
#创建指定大小的数组，数组元素以 0 来填充：
# 默认为浮点类型
a = np.zeros(5)
print(a)

#设置数据类型
y = np.zeros(5,dtype = int)
print(y)
```

输出：

```
[0. 0. 0. 0. 0.]
[0 0 0 0 0]
```



### numpy.ones

创建指定形状的数组，数组元素以 1 来填充：

```
numpy.ones(shape, dtype = None)
```

参数：

| 参数  | 描述           |
| :---- | :------------- |
| shape | 数组形状       |
| dtype | 数据类型，可选 |

**实例**

```
#创建指定形状的数组，数组元素以 1 来填充
# 默认为浮点类型
a = np.ones(5)
print(a)

#设置数据类型
y = np.ones(5,dtype=np.int32)
print(y)
```

输出：

```
[1. 1. 1. 1. 1.]
[1 1 1 1 1]
```



### numpy.zeros_like

numpy.zeros_like 用于创建一个与给定数组具有相同形状的数组，数组元素以 0 来填充

numpy.zeros 和 numpy.zeros_like 都是用于创建一个指定形状的数组，其中所有元素都是 0

它们之间的区别在于：numpy.zeros 可以直接指定要创建的数组的形状，而 numpy.zeros_like 则是创建一个与给定数组具有相同形状的数组

```
numpy.zeros_like(a, dtype=None, order='K')
```

参数：

| 参数  | 描述                                                         |
| :---- | :----------------------------------------------------------- |
| a     | 给定要创建相同形状的数组                                     |
| dtype | 创建的数组的数据类型                                         |
| order | 数组在内存中的存储顺序，可选值为 'C'（按行优先）或 'F'（按列优先），默认为 'K'（保留输入数组的存储顺序） |
| shape | 创建的数组的形状，如果不指定，则默认为 a 数组的形状。        |



**实例**

**创建一个与 arr 形状相同的，所有元素都为 0 的数组：**

```
#用于创建一个与给定数组具有相同形状的数组，数组元素以 0 来填充。
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

#调用zeros_like函数来进行操作
x = np.zeros_like(a)
print(x)
```

输出：

```
[[1 2 3]
 [4 5 6]
 [7 8 9]]
[[0 0 0]
 [0 0 0]
 [0 0 0]]
```



### numpy.ones_like

numpy.ones_like 用于创建一个与给定数组具有相同形状的数组，数组元素以 1 来填充

numpy.ones 和 numpy.ones_like 都是用于创建一个指定形状的数组，其中所有元素都是 1

它们之间的区别在于：numpy.ones 可以直接指定要创建的数组的形状，而 numpy.ones_like 则是创建一个与给定数组具有相同形状的数组

```
numpy.ones_like(a, dtype=None, order='K')
```

参数：

| 参数  | 描述                                                         |
| :---- | :----------------------------------------------------------- |
| a     | 给定要创建相同形状的数组                                     |
| dtype | 创建的数组的数据类型                                         |
| order | 数组在内存中的存储顺序，可选值为 'C'（按行优先）或 'F'（按列优先），默认为 'K'（保留输入数组的存储顺序） |



**实例**

**创建一个与 arr 形状相同的，所有元素都为 1 的数组：**

```
#用于创建一个与给定数组具有相同形状的数组，数组元素以 1 来填充。
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

#调用ones_like函数来进行操作
x = np.ones_like(a)
print(x)
```

输出：

```
[[1 2 3]
 [4 5 6]
 [7 8 9]]
[[1 1 1]
 [1 1 1]
 [1 1 1]]
```







## NumPy 从已有的数组创建数组

### numpy.asarray

numpy.asarray 类似 numpy.array，但 numpy.asarray 参数只有三个，比 numpy.array 少两个

```
# array和asarray的区别

import numpy as np
x = np.arange(3)
y = np.asarray(x)
z = np.array(x)
print(y is x)  # True，通常不拷贝
print(z is x)  # False，默认会拷贝
```

```
numpy.asarray(a, dtype = None, order = None)
```

参数：

| 参数  | 描述                                                         |
| :---- | :----------------------------------------------------------- |
| a     | 任意形式的输入参数，可以是，列表, 列表的元组, 元组, 元组的元组, 元组的列表，多维数组 |
| dtype | 数据类型，可选                                               |
| order | 可选，有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。 |

**实例**

将列表转换为 ndarray:

```
#从已有的数组创建数组
x = [1,2,3,4,5,6]
#将列表转换为 ndarray对象
a = np.asarray(x)
print(a)
```

输出：

```
[1 2 3 4 5 6]
```



**将元组转换为 ndarray: **

```
#将元组转换为 ndarray对象
x = (1,2,3,4,5,6)
a = np.asarray(x)
print(a)
```

输出：

```
[1 2 3 4 5 6]
```



**将元组列表转换为 ndarray: **

```
#将元组列表转换为 ndarray对象
x = [(1,2,3),(4,5,6)]
a = np.asarray(x,dtype = float)
print(a)
```

输出：

```
[[1. 2. 3.]
 [4. 5. 6.]]
```



**设置 dtype 参数：**

```
import numpy as np 
 
x =  [1,2,3] 
a = np.asarray(x, dtype =  float)  
print (a)
```

输出：

```
[ 1.  2.  3.]
```



### numpy.frombuffer

numpy.frombuffer 用于实现动态数组

numpy.frombuffer 接受 buffer 输入参数，以流的形式读入转化成 ndarray 对象

```
numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
```

> **注意：**buffer 是字符串的时候，Python3 默认 str 是 Unicode 类型，所以要转成 bytestring 在原 str 前加上 b

参数：

| 参数   | 描述                               |
| :----- | :--------------------------------- |
| buffer | 可以是任意对象，会以流的形式读入。 |
| dtype  | 返回数组的数据类型，可选           |

```python
import numpy as np 
 
s =  b'Hello World' 
a = np.frombuffer(s, dtype =  'S1')  
print (a)
```

输出：

```
[b'H' b'e' b'l' b'l' b'o' b' ' b'W' b'o' b'r' b'l' b'd']
```



### numpy.fromiter

**numpy.fromiter 方法从可迭代对象中建立 ndarray 对象，返回一维数组**

```
numpy.fromiter(iterable, dtype)
```

| 参数     | 描述               |
| :------- | :----------------- |
| iterable | 可迭代对象         |
| dtype    | 返回数组的数据类型 |

**实例**

```
# 9 np.fromiter()函数
import numpy as np
lis = range(0,10)
arr = np.fromiter(i,dtype = np.float64)
print(arr)
```

输出：

```
[0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]

```





## NumPy 从数值范围创建数组

### numpy.arange

numpy 包中的使用 arange 函数创建数值范围并返回 ndarray 对象，函数格式如下：

```
numpy.arange(start, stop, step, dtype)

```

根据 start 与 stop 指定的范围以及 step 设定的步长，生成一个 ndarray

参数：

| 参数    | 描述                                                         |
| :------ | :----------------------------------------------------------- |
| `start` | 起始值，默认为`0`                                            |
| `stop`  | 终止值（不包含）                                             |
| `step`  | 步长，默认为`1`                                              |
| `dtype` | 返回`ndarray`的数据类型，如果没有提供，则会使用输入数据的类型。 |

**实例**

**生成 0 到 4 长度为 5 的数组: **

```
import numpy as np
 
x = np.arange(5)  
print (x)

```

输出：

```
[0  1  2  3  4]

```



**设置返回类型位 float:**

```
import numpy as np
 
# 设置 dtype
x = np.arange(5, dtype =  float)  
print (x)

```

输出结果如下：

```
[0.  1.  2.  3.  4.]

```



**设置起始值、终止值及步长：**

```
import numpy as np
x = np.arange(10,20,2)  
print (x)

```

输出：

```
[10  12  14  16  18]

```



### numpy.linspace

numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的，格式如下：

```
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)

```

参数：

| 参数       | 描述                                                         |
| :--------- | :----------------------------------------------------------- |
| `start`    | 序列的起始值                                                 |
| `stop`     | 序列的终止值，如果`endpoint`为`true`，该值包含于数列中       |
| `num`      | 要生成的等步长的样本数量，默认为`50`                         |
| `endpoint` | 该值为 `true` 时，数列中包含`stop`值，反之不包含，默认是True。 |
| `retstep`  | 如果为 True 时，生成的数组中会显示间距，反之不显示。         |
| `dtype`    | `ndarray` 的数据类型                                         |

**实例**

**以下实例用到三个参数，设置起始点为 1 ，终止点为 10，数列个数为 10**

```
import numpy as np
a = np.linspace(1,10,10)
print(a)

```

输出：

```
[ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]

```



**设置元素全部是1的等差数列：**

```
import numpy as np
a = np.linspace(1,1,10)
print(a)

```

输出：

```
[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

```



**将 endpoint 设为 false，不包含终止:** 

```
import numpy as np
 
a = np.linspace(10, 20,  5, endpoint =  False)  
print(a)

```

输出：

```
[10. 12. 14. 16. 18.]

```

如果将 endpoint 设为 true，则会包含 20



**设置间距**

```
import numpy as np
a =np.linspace(1,10,10,retstep= True)
 
print(a)
# 拓展例子
b =np.linspace(0,10,10).reshape(2,5)  # 重塑为2行5列的数组
print(b)

```

输出：

```
(array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.]), 1.0)
[[ 1.  2.  3.  4.  5.]
 [ 6.  7.  8.  9. 10.]]

```







# 04切片和索引——

ndarray对象的内容可以通过索引或切片来访问和修改，与 Python 中 list 的切片操作一样。

## 1.实例

**ndarray 数组可以基于 0 - n 的下标进行索引，切片对象可以通过内置的 slice 函数，并设置 start, stop 及 step 参数进行，从原数组中切割出一个新数组。**

```python
import numpy as np
 
a = np.arange(10)
s = slice(2,7,2)   # 从索引 2 开始到索引 7 停止，间隔为2
print (a[s])
```

输出：

```
[2  4  6]
```



## 2.实例

**通过 arange() 函数创建 ndarray 对象。 然后，分别设置起始，终止和步长的参数为 2，7 和 2。也可以通过冒号分隔切片参数 start:stop:step 来进行切片操作：**

```
import numpy as np
 
a = np.arange(10)  
b = a[2:7:2]   # 从索引 2 开始到索引 7 停止，间隔为 2
print(b)
```

输出：

```
[2  4  6]
```



## 3.实例

**冒号 :的解释：如果只放置一个参数，如 **[2]**，将返回与该索引相对应的单个元素。如果为 **[2:]**，表示从该索引开始以后的所有项都将被提取。如果使用了两个参数，如 **[2:7]**，那么则提取两个索引(不包括停止索引)之间的项。**

```
import numpy as np
 
a = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]
b = a[5] 
print(b)
```

输出：

```
5
```



```
import numpy as np
 
a = np.arange(10)
print(a[2:])
```

输出：

```
[2  3  4  5  6  7  8  9]
```





```
import numpy as np
 
a = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]
print(a[2:5])
```

输出：

```
[2  3  4]
```



## 4.实例

**多维数组同样适用上述索引提取方法： **

```
import numpy as np
 
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a)
# 从某个索引处开始切割
print('从数组索引 a[1:] 处开始切割')
print(a[1:])
```

输出：

```
[[1 2 3]
 [3 4 5]
 [4 5 6]]
从数组索引 a[1:] 处开始切割
[[3 4 5]
 [4 5 6]]
```



## 5.实例

**切片还可以包括省略号 …，来使选择元组的长度与数组的维度相同。 如果在行位置使用省略号，它将返回包含行中元素的 ndarray。**

```
import numpy as np
 
a = np.array([[1,2,3],[3,4,5],[4,5,6]])  
print (a[...,1])   # 第2列元素
print (a[1,...])   # 第2行元素
print (a[...,1:])  # 第2列及剩下的所有元素
```

输出：

```
[2 4 5]
[3 4 5]
[[2 3]
 [4 5]
 [5 6]]
```







## NumPy 高级索引

NumPy 比一般的 Python 序列提供更多的索引方式。

除了之前看到的用整数和切片的索引外，数组可以由整数数组索引、布尔索引及花式索引。

NumPy 中的高级索引指的是使用整数数组、布尔数组或者其他序列来访问数组的元素。相比于基本索引，高级索引可以访问到数组中的任意元素，并且可以用来对数组进行复杂的操作和修改。

### 1. 整数数组索引

整数数组索引是指使用一个数组来访问另一个数组的元素。这个数组中的每个元素都是目标数组中某个维度上的索引值。

以下实例

#### 实例

**获取数组中 (0,0)，(1,1) 和 (2,0)位置处的元素。**

```
import numpy as np 
 
x = np.array([[1,  2],  [3,  4],  [5,  6]]) 
y = x[[0,1,2],  [0,1,0]]  
print (y)
```

输出：

```
[1  4  5]
```



**以下实例获取了 4X3 数组中的四个角的元素。 行索引是 [0,0] 和 [3,3]，而列索引是 [0,2] 和 [0,2]。**

```
import numpy as np 
 
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])  
print ('我们的数组是：' )
print (x)
print ('\n')
rows = np.array([[0,0],[3,3]]) 
cols = np.array([[0,2],[0,2]]) 
y = x[rows,cols]  
print  ('这个数组的四个角元素是：')
print (y)
```

输出：

```
我们的数组是：
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]


这个数组的四个角元素是：
[[ 0  2]
 [ 9 11]]
```

返回的结果是包含每个角元素的 ndarray 对象。



### 2. 布尔索引

可以通过一个布尔数组来索引目标数组。

布尔索引通过布尔运算（如：比较运算符）来获取符合指定条件的元素的数组。

#### 实例

**获取大于 5 的元素： **

```
import numpy as np 
 
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])  
print ('我们的数组是：')
print (x)
print ('\n')
# 现在我们会打印出大于 5 的元素  
print  ('大于 5 的元素是：')
print (x[x >  5])
```

输出：

```
我们的数组是：
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]


大于 5 的元素是：
[ 6  7  8  9 10 11]
```



### 3. 花式索引

花式索引指的是利用整数数组进行索引。

**花式索引根据索引数组的值作为目标数组的某个轴的下标来取值。**

对于使用一维整型数组作为索引，如果目标是一维数组，那么索引的结果就是对应位置的元素，如果目标是二维数组，那么就是对应下标的行。

花式索引跟切片不一样，它总是将数据复制到新数组中。

#### 一维数组

##### 实例

**一维数组只有一个轴 axis = 0，所以一维数组就在 axis = 0 这个轴上取值：**

```
import numpy as np

x = np.arange(9)
print(x)
# 一维数组读取指定下标对应的元素
print("-------读取下标对应的元素-------")
x2 = x[[0, 6]] # 使用花式索引
print(x2) 

print(x2[0])
print(x2[1])
```

输出：

```
[0 1 2 3 4 5 6 7 8]
-------读取下标对应的元素-------
[0 6]
0
6
```



#### 二维数组

传入顺序索引数组

##### 实例

```
import numpy as np 
 
x = np.arange(32).reshape(8, 4)
print(x)
# 二维数组读取指定下标对应的行
print("-------读取下标对应的行-------")
print (x[[4,2,1,7]])
```

输出：

```
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]
 [24 25 26 27]
 [28 29 30 31]]
-------读取下标对应的行-------
[[16 17 18 19]
 [ 8  9 10 11]
 [ 4  5  6  7]
 [28 29 30 31]]
```







# 05广播及迭代——	

## 广播(Broadcast)

广播(Broadcast)是 numpy 对不同形状(shape)的数组进行数值计算的方式， 对数组的算术运算通常在相应的元素上进行。

### 实例

**1. 如果两个数组 a 和 b 形状相同，即满足 a.shape == b.shape，那么 a*b 的结果就是 a 与 b 数组对应位相乘。这要求维数相同，且各维度的长度相同。**

```
import numpy as np 
 
a = np.array([1,2,3,4]) 
b = np.array([10,20,30,40]) 
c = a * b 
print (c)
```

输出：

```
[ 10  40  90 160]
```



**2. 当运算中的 2 个数组的形状不同时，numpy 将自动触发广播机制。**

```
import numpy as np 
 
a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([0,1,2])
print(a + b)
```

输出：

```
[[ 0  1  2]
 [10 11 12]
 [20 21 22]
 [30 31 32]]
```



**4x3 的二维数组与长为 3 的一维数组相加，等效于把数组 b 在二维上重复 4 次再运算： **

```
import numpy as np 
 
a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([1,2,3])
bb = np.tile(b, (4, 1))  # 重复 b 的各个维度
print(a + bb)
```

输出：

```
[[ 1  2  3]
 [11 12 13]
 [21 22 23]
 [31 32 33]]
```





## NumPy 迭代数组

NumPy 迭代器对象 numpy.nditer 提供了一种灵活访问一个或者多个数组元素的方式。

迭代器最基本的任务的可以完成对数组元素的访问。

### 实例

```
import numpy as np
 
a = np.arange(6).reshape(2,3)
print ('原始数组是：')
print (a)
print ('\n')
print ('迭代输出元素：')
for x in np.nditer(a):
    print (x, end=", " )
print('\b')      # \b  \t  \n   
```

输出：

```
原始数组是：
[[0 1 2]
 [3 4 5]]


迭代输出元素：
0, 1, 2, 3, 4, 5, 
```



### 控制遍历顺序

**for x in np.nditer(a, order='F'):**Fortran order，即是列序优先；

**for x in np.nditer(a.T, order='C'): **Corder，即是行序优先；

```
import numpy as np 
 
a = np.arange(0,60,5) 
a = a.reshape(3,4)  
print ('原始数组是：')
print (a)
print ('\n')
print ('以 C 风格顺序排序：')
for x in np.nditer(a, order =  'C'):  
    print (x, end=", " )
print ('\n')
print ('以 F 风格顺序排序：')
for x in np.nditer(a, order =  'F'):  
    print (x, end=", " )
```

输出：

```
原始数组是：
[[ 0  5 10 15]
 [20 25 30 35]
 [40 45 50 55]]


以 C 风格顺序排序：
0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 

以 F 风格顺序排序：
0, 20, 40, 5, 25, 45, 10, 30, 50, 15, 35, 55,
```



### 广播迭代

如果两个数组是可广播的，nditer 组合对象能够同时迭代它们。 假设数组 a 的维度为 3X4，数组 b 的维度为 1X4 ，则使用以下迭代器（数组 b 被广播到 a 的大小）。

#### 实例

```
import numpy as np

a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print("第一个数组为:")
print(a)
print('\n')
print("第二个数组为:")
b = np.array([1, 2, 3, 4],dtype=int)
print(b)
print('\n')
print("修改后的数组为:")
for x,y in np.nditer([a, b]):
    print(x,y)
```

输出：

```
第一个数组为:
[[ 0  5 10 15]
 [20 25 30 35]
 [40 45 50 55]]


第二个数组为:
[1 2 3 4]


修改后的数组为:
0 1
5 2
10 3
15 4
20 1
25 2
30 3
35 4
40 1
45 2
50 3
55 4
```





