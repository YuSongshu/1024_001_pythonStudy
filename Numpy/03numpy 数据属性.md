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
