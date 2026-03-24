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

| 序号 | 参数   | 描述说明           |
| ---- | ------ | ------------------ |
| 1    | object | 表示一个数组序列。 |

| 2    | dtype  | 可选参数，通过它可以更改数组的数据类型。                     

| 3   | ndim   | 用于指定数组的维度。                                         

| 4   | reshape   | 用于改变行数和列数

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
​```xxxxxxxxxx 原数组 [[1 2][3 4][5 6]]新数组 [[1 2 3][4 5 6]]
```