# 06Numpy 数组操作——

Numpy 中包含了一些函数用于处理数组，大概可分为以下几类：

## 修改数组形状

| 函数      | 描述                                               |
| :-------- | :------------------------------------------------- |
| `reshape` | 不改变数据的条件下修改形状                         |
| `flat`    | 数组元素迭代器                                     |
| `flatten` | 返回一份数组拷贝，对拷贝所做的修改不会影响原始数组 |
| `ravel`   | 返回展开数组                                       |

### numpy.reshape

numpy.reshape 函数可以在不改变数据的条件下修改形状，格式如下：

```
numpy.reshape(arr)
```

arr ：要修改形状的数组

**实例**

```
import numpy as np
 
a = np.arange(8)
print ('原始数组：')
print (a)
print ('\n')
 
b = a.reshape(4,2)
print ('修改后的数组：')
print (b)
```

输出：

```
原始数组：
[0 1 2 3 4 5 6 7]

修改后的数组：
[[0 1]
 [2 3]
 [4 5]
 [6 7]]
```



### numpy.ndarray.flat

numpy.ndarray.flat 是一个数组元素迭代器，实例如下:

**实例 **

```
import numpy as np

a = np.arange(9).reshape(3, 3)
print("原始数据：")
for row in a:
    print(row)

print("迭代后的数据:")
for row in a.flat:  # 迭代flat属性
    print(row,end=" ")
print("\n")
for row in np.nditer(a):
    print(row,end=" ")
print("\n")
for row in a.flatten():
    print(row,end=" ")

```

输出：

```
原始数据：
[0 1 2]
[3 4 5]
[6 7 8]
迭代后的数据:
0 1 2 3 4 5 6 7 8 

0 1 2 3 4 5 6 7 8 

0 1 2 3 4 5 6 7 8
```



### numpy.ndarray.flatten

numpy.ndarray.flatten 是一个数组展开属性，如下：

```
ndarray.flatten(order='C')
```

order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。

**实例**

```
import numpy as np

a = np.arange(9).reshape(3, 3)
print("原始数据：")
print(a)

print("使用flatten函数后的数据:")
b = a.flatten()
print(b)

print('以F风格顺序展开的数组:')
print(a.flatten('F'))
```

输出：

```
原始数据：
[[0 1 2]
 [3 4 5]
 [6 7 8]]
使用flatten函数后的数据:
[0 1 2 3 4 5 6 7 8]
以F风格顺序展开的数组:
[0 3 6 1 4 7 2 5 8]
```





## 翻转数组

| 函数        | 描述                       |
| :---------- | :------------------------- |
| `transpose` | 对换数组的维度             |
| `ndarray.T` | 和 `self.transpose()` 相同 |

### numpy.transpose

numpy.transpose 函数用于对换数组的维度，格式如下：

```
numpy.transpose(arr, axes)
```

参数:

**arr**：要操作的数组

**axes**：整数列表，原维度，其排列为改后维度

**实例**

```
import numpy as np
 
a = np.arange(12).reshape(3,4)
print ('原数组：')
print (a )
print ('对换数组：')
print (np.transpose(a))


b = np.arange(24).reshape(2,3,4)
print(np.transpose(b))					# 默认：维度完全反转 => (4,3,2)
print(np.transpose(b, axes=(1,0,2)))	# 自定义：维度顺序 (1,0,2) => (3,2,4)
```

输出：

```
原数组：
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
对换数组：
[[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]

[[[ 0 12]
  [ 4 16]
  [ 8 20]]
 [[ 1 13]
  [ 5 17]
  [ 9 21]]
 [[ 2 14]
  [ 6 18]
  [10 22]]
 [[ 3 15]
  [ 7 19]
  [11 23]]]

[[[ 0  1  2  3]
  [12 13 14 15]]
 [[ 4  5  6  7]
  [16 17 18 19]]
 [[ 8  9 10 11]
  [20 21 22 23]]]

```



注：numpy.ndarray.T 类似 numpy.transpose

```
import numpy as np
 
a = np.arange(12).reshape(3,4)
 
print ('原数组：')
print (a)
print ('\n')
 
print ('转置数组：')
print (a.T)
```

输出：

```
原数组：
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]


转置数组：
[[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]
```





## 广播拓展

| 维度           | 描述               |
| :------------- | :----------------- |
| `broadcast`    | 产生模仿广播的对象 |
| `broadcast_to` | 将数组广播到新形状 |

### numpy.broadcast

numpy.broadcast 用于模仿广播的对象，它返回一个对象，该对象封装了将一个数组广播到另一个数组的结果。该函数使用两个数组作为输入参数

**实例**

```
# 5 numpy.broadcast()函数
import numpy as np
 
x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])  
 
# 对 y 广播 x
b = np.broadcast(x,y)  	  # 它拥有 iterator 属性,它内部会把 x、y 各自变成迭代器，然后一起遍历
 
print ('对 y 广播 x：')
r,c = b.iters
 
print (next(r), next(c))
print (next(r), next(c))
print (next(r), next(c))
print (next(r), next(c))
print ('\n')
# shape 属性返回广播对象的形状
 
print ('广播对象的形状：')
print (b.shape)
print ('\n')
```

输出：

```
对 y 广播 x：
1 4
1 5
1 6
2 4


广播对象的形状：
(3, 3)
```



### numpy.broadcast_to

numpy.broadcast_to 函数将数组广播到新形状。它在原始数组上返回只读视图。 它通常不连续。 如果新形状不符合 NumPy 的广播规则，该函数可能会抛出ValueError。

它能把一个数组按照指定形状直接广播并生成新数组，而不是返回一个广播对象

```
numpy.broadcast_to(array, shape, subok)
```

**实例**

```
import numpy as np
 
a = np.arange(4).reshape(1,4)
 
print ('原数组：')
print (a)
print ('\n')
 
print ('调用 broadcast_to 函数之后：')
print (np.broadcast_to(a,(4,4)))

print ('调用 np.tile 函数之后：')
print (np.tile(a,(4,1)))
```

输出：

```
原数组：
[[0 1 2 3]]


调用 broadcast_to 函数之后：
[[0 1 2 3]
 [0 1 2 3]
 [0 1 2 3]
 [0 1 2 3]]
调用 np.tile 函数之后：
[[0 1 2 3]
 [0 1 2 3]
 [0 1 2 3]
 [0 1 2 3]]
```

#### 注

np.broadcast_to 返回的是**视图**（和原数组共享内存），所以修改原数组会影响广播后的数组：

```
import numpy as np
x = np.array([1, 2, 3])
x_broadcast = np.broadcast_to(x, (2, 3))		# 把 x 广播成 (2, 3) 的形状

print("原始数组：")
print(x)

print("\n广播后的数组：")
print(x_broadcast)

x[0] = 100 		# 修改原数组的第一个元素,广播后的数组也会同步变化
print("\n",x_broadcast)
```

输出：

```
原始数组：
[1 2 3]
广播后的数组：
[[1 2 3]
 [1 2 3]]
 
 [[100   2   3]
 [100   2   3]]
 
```

如果需要独立的数组（不共享内存），可以加 .copy()：

```
x_broadcast_copy = np.broadcast_to(x, (2, 3)).copy()
x[0] = 1  # 再修改原数组
print(x_broadcast_copy)  # 不受影响
```





## 连接数组

| 函数          | 描述                           |
| :------------ | :----------------------------- |
| `concatenate` | 连接沿现有轴的数组序列         |
| `stack`       | 沿着新的轴加入一系列数组。     |
| `hstack`      | 水平堆叠序列中的数组（列方向） |
| `vstack`      | 竖直堆叠序列中的数组（行方向） |

### numpy.concatenate

numpy.concatenate 函数用于沿指定轴连接相同形状的两个或多个数组，格式如下：

```
numpy.concatenate((a1, a2, ...), axis)
```

参数说明：

**a1, a2, ...**：相同类型的数组

**axis**：沿着它连接数组的轴，默认为 0

实例

```
import numpy as np
 
a = np.array([[1,2],[3,4]])
 
print ('第一个数组：')
print (a)
print ('\n')
b = np.array([[5,6],[7,8]])
 
print ('第二个数组：')
print (b)
print ('\n')
# 两个数组的维度相同
 
print ('沿轴 0 连接两个数组：')
print (np.concatenate((a,b)))
print ('\n')
 
print ('沿轴 1 连接两个数组：')
print (np.concatenate((a,b),axis = 1))
```

输出：

```
第一个数组：
[[1 2]
 [3 4]]


第二个数组：
[[5 6]
 [7 8]]


沿轴 0 连接两个数组：
[[1 2]
 [3 4]
 [5 6]
 [7 8]]


沿轴 1 连接两个数组：
[[1 2 5 6]
 [3 4 7 8]]
```

### numpy.stack

numpy.stack 函数用于沿新轴连接数组序列，格式如下：

```
numpy.stack(arrays, axis)
```

参数说明：

- `arrays`相同形状的数组序列
- `axis`：返回数组中的轴，输入数组沿着它来堆叠

实例

![image-20260116165741956](D:\博客\python\数据分析\Numpy\辅助图片等\06图片\image-20260116165741956.png)

```
import numpy as np
 
a = np.array([[1,2],[3,4]])
 
print ('第一个数组：')
print (a)
print ('\n')
b = np.array([[5,6],[7,8]])
 
print ('第二个数组：')
print (b)
print ('\n')
 
print ('沿轴 0 堆叠两个数组：')
print (np.stack((a,b),0))
print ('\n')
 
print ('沿轴 1 堆叠两个数组：')
print (np.stack((a,b),1))
```

输出：

```
第一个数组：
[[1 2]
 [3 4]]


第二个数组：
[[5 6]
 [7 8]]


沿轴 0 堆叠两个数组：
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]


沿轴 1 堆叠两个数组：
[[[1 2]
  [5 6]]

 [[3 4]
  [7 8]]]
```

### numpy.hstack

![image-20260116184212638](D:\博客\python\数据分析\Numpy\辅助图片等\06图片\image-20260116184212638.png)

numpy.hstack 是 numpy.stack 函数的变体，它通过水平堆叠来生成数组。

**实例**

```
import numpy as np
 
a = np.array([[1,2],[3,4]])
 
print ('第一个数组：')
print (a)
print ('\n')
b = np.array([[5,6],[7,8]])
 
print ('第二个数组：')
print (b)
print ('\n')
 
print ('水平堆叠：')
c = np.hstack((a,b))
print (c)
print ('\n')
```

输出：

```
第一个数组：
[[1 2]
 [3 4]]


第二个数组：
[[5 6]
 [7 8]]


水平堆叠：
[[1 2 5 6]
 [3 4 7 8]]
```

### numpy.vstack

numpy.vstack 是 numpy.stack 函数的变体，它通过垂直堆叠来生成数组。

![image-20260116184420976](D:\博客\python\数据分析\Numpy\辅助图片等\06图片\image-20260116184420976.png)

实例

```
import numpy as np
 
a = np.array([[1,2],[3,4]])
 
print ('第一个数组：')
print (a)
print ('\n')
b = np.array([[5,6],[7,8]])
 
print ('第二个数组：')
print (b)
print ('\n')
 
print ('竖直堆叠：')
c = np.vstack((a,b))
print (c)
```

输出：

```
第一个数组：
[[1 2]
 [3 4]]


第二个数组：
[[5 6]
 [7 8]]


竖直堆叠：
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
```

## 分割数组

| 函数     | 数组及操作                             |
| :------- | :------------------------------------- |
| `split`  | 将一个数组分割为多个子数组             |
| `hsplit` | 将一个数组水平分割为多个子数组（按列） |
| `vsplit` | 将一个数组垂直分割为多个子数组（按行） |

### numpy.split

numpy.split 函数沿特定的轴将数组分割为子数组，格式如下：

```
numpy.split(ary, indices_or_sections, axis)
```

参数说明：

- `ary`：被分割的数组
- `indices_or_sections`：如果是一个整数，就用该数平均切分，如果是一个数组，为沿轴切分的位置（左开右闭）
- `axis`：设置沿着哪个方向进行切分，默认为 0，横向切分，即水平方向。为 1 时，纵向切分，即竖直方向。

**实例**

```
import numpy as np

a = np.arange(1, 10)
print("原始数组:")
print(a)
print("\n")

print("将数组分为三个子数组:")
print(np.split(a,3))
print("\n")

print("将数组在数组中表明分割点:")
print(np.split(a,[2,5]))   # [2,5)
```

输出：

```
原始数组:
[1 2 3 4 5 6 7 8 9]


将数组分为三个子数组:
[array([1, 2, 3]), array([4, 5, 6]), array([7, 8, 9])]


将数组在数组中表明分割点:
[array([1, 2]), array([3, 4, 5]), array([6, 7, 8, 9])]

```

axis 为 0 时在水平方向分割，axis 为 1 时在垂直方向分割：

**实例**

```
import numpy as np

a = np.arange(16).reshape(4, 4)
print('第一个数组：')
print(a)
print('\n')
print('默认分割（0轴）：')
b = np.split(a,2)
print(b)
print('\n')

print('沿水平方向分割：')
c = np.split(a,2,1)
print(c)
print('\n')

print('沿水平方向分割：')
d= np.hsplit(a,2)
print(d)

```

输出：

```
第一个数组：
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]


默认分割（0轴）：
[array([[0, 1, 2, 3],
       [4, 5, 6, 7]]), array([[ 8,  9, 10, 11],
       [12, 13, 14, 15]])]


沿水平方向分割：
[array([[ 0,  1],
       [ 4,  5],
       [ 8,  9],
       [12, 13]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11],
       [14, 15]])]


沿水平方向分割：
[array([[ 0,  1],
       [ 4,  5],
       [ 8,  9],
       [12, 13]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11],
       [14, 15]])]

```

### numpy.hsplit

numpy.hsplit 函数用于水平分割数组，通过指定要返回的相同形状的数组数量来拆分原数组。

1. np.floor()：向下取整
2. np.ceil()：向上取整
3. np.round()：四舍五入

**实例**

```
import numpy as np
 
harr = np.floor(10 * np.random.random((2, 6)))
print ('原array：')
print(harr)
 
print ('拆分后：')
print(np.hsplit(harr, 3))

```

输出：

```
原array：
[[4. 7. 6. 3. 2. 6.]
 [6. 3. 6. 7. 9. 7.]]
拆分后：
[array([[4., 7.],
       [6., 3.]]), array([[6., 3.],
       [6., 7.]]), array([[2., 6.],
       [9., 7.]])]

```

### numpy.vsplit

numpy.vsplit 沿着垂直轴分割，其分割方式与hsplit用法相同。

**实例**

```
import numpy as np
 
a = np.arange(16).reshape(4,4)
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('竖直分割：')
b = np.vsplit(a,2)
print (b)

```

输出：

```
第一个数组：
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]


竖直分割：
[array([[0, 1, 2, 3],
       [4, 5, 6, 7]]), array([[ 8,  9, 10, 11],
       [12, 13, 14, 15]])]

```

## 数组元素的添加与删除

| 函数     | 元素及描述                               |
| :------- | :--------------------------------------- |
| `resize` | 返回指定形状的新数组                     |
| `append` | 将值添加到数组末尾                       |
| `insert` | 沿指定轴将值插入到指定下标之前           |
| `delete` | 删掉某个轴的子数组，并返回删除后的新数组 |
| `unique` | 查找数组内的唯一元素                     |

### numpy.resize

numpy.resize 函数返回指定大小的新数组。

如果新数组大小大于原始大小，则包含原始数组中的元素的副本。

```
numpy.resize(arr, shape)

```

参数说明：

- `arr`：要修改大小的数组
- `shape`：返回数组的新形状

**实例**

```
import numpy as np
 
a = np.array([[1,2,3],[4,5,6]])
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('第一个数组的形状：')
print (a.shape)
print ('\n')
b = np.resize(a, (3,2))
c = a.reshape(3,2)
 
print ('第b个数组：')
print (b)
print ('\n')

print ('第c个数组：')
print (c)
print ('\n')
 
print ('第二个数组的形状：')
print (b.shape)
print ('\n')
# 要注意 a 的第一行在 b 中重复出现，因为尺寸变大了
 
print ('修改第二个数组的大小：')
b = np.resize(a,(3,3))
print (b)

```

输出：

```
第一个数组：
[[1 2 3]
 [4 5 6]]


第一个数组的形状：
(2, 3)


第二个数组：
[[1 2]
 [3 4]
 [5 6]]


第二个数组的形状：
(3, 2)


修改第二个数组的大小：
[[1 2 3]
 [4 5 6]
 [1 2 3]]

```

### numpy.append

numpy.append 函数在数组的末尾添加值。 追加操作会分配整个数组，并把原来的数组复制到新数组中。 此外，输入数组的维度必须匹配否则将生成ValueError。

append 函数返回的始终是一个一维数组。

```
numpy.append(arr, values, axis=None)

```

参数说明：

- `arr`：输入数组
- `values`：要向`arr`添加的值，需要和`arr`形状相同（除了要添加的轴）
- `axis`：默认为 None。当axis无定义时，是横向加成，返回总是为一维数组！当axis有定义的时候，分别为0和1的时候。当axis有定义的时候，分别为0和1的时候（列数要相同）。当axis为1时，数组是加在右边（行数要相同）。

**实例**

```
import numpy as np
 
a = np.array([[1,2,3],[4,5,6]])
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('向数组添加元素：')
print (np.append(a, [7,8,9]))
print ('\n')
 
print ('沿轴 0 添加元素：')
print (np.append(a, [[7,8,9]],axis = 0))
print ('\n')
 
print ('沿轴 1 添加元素：')
print (np.append(a, [[5,5,5],[7,8,9]],axis = 1))

```

输出：

```
第一个数组：
[[1 2 3]
 [4 5 6]]


向数组添加元素：
[1 2 3 4 5 6 7 8 9]


沿轴 0 添加元素：
[[1 2 3]
 [4 5 6]
 [7 8 9]]


沿轴 1 添加元素：
[[1 2 3 5 5 5]
 [4 5 6 7 8 9]]

```

### numpy.insert

numpy.insert 函数在给定索引之前，沿给定轴在输入数组中插入值。

如果值的类型转换为要插入，则它与输入数组不同。 插入没有原地的，函数会返回一个新数组。 此外，如果未提供轴，则输入数组会被展开。

```
numpy.insert(arr, obj, values, axis)

```

参数说明：

- `arr`：输入数组
- `obj`：在其之前插入值的索引
- `values`：要插入的值
- `axis`：沿着它插入的轴，如果未提供，则输入数组会被展开

**实例**

```
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print("第一个数组:")
print(a)

b = np.insert(a, 1, 0, axis=0)
print("在行位置1插入0:")
print(b)

c = np.insert(a, 1, 0, axis=1)
print("在行位置1插入0:")
print(c)

d = np.insert(a, 0,1)    
print("在行位置0插入1:")  
print(d)

```

输出：

```
第一个数组:
[[1 2 3]
 [4 5 6]]
在行位置1插入0:
[[1 2 3]
 [0 0 0]
 [4 5 6]]
在行位置1插入0:
[[1 0 2 3]
 [4 0 5 6]]
在行位置0插入1:
[1 1 2 3 4 5 6]

```

### numpy.delete

numpy.delete 函数返回从输入数组中删除指定子数组的新数组。 与 insert() 函数的情况一样，如果未提供轴参数，则输入数组将展开。

```
Numpy.delete(arr, axis)

```

参数说明：

- `arr`：输入数组
- `axis`：沿着它删除给定子数组的轴，如果未提供，则输入数组会被展开

**实例**

```
import numpy as np
 
a = np.arange(12).reshape(3,4)
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('未传递 Axis 参数。 在插入之前输入数组会被展开。')
print (np.delete(a,5))
print ('\n')
 
print ('删除第二列：')
print (np.delete(a,1,axis = 1))
print ('\n')

```

输出：

```
第一个数组：
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]


未传递 Axis 参数。 在插入之前输入数组会被展开。
[ 0  1  2  3  4  6  7  8  9 10 11]


删除第二列：
[[ 0  2  3]
 [ 4  6  7]
 [ 8 10 11]]


```

### numpy.unique

numpy.unique 函数用于去除数组中的重复元素。

```
numpy.unique(arr)

```

**实例**

```
import numpy as np
 
a = np.array([5,2,6,2,7,5,6,8,2,9])
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('第一个数组的去重值：')
u = np.unique(a)
print (u)
print ('\n')

```

输出：

```
第一个数组：
[5 2 6 2 7 5 6 8 2 9]
```