# Pandas 读取数据

## 1 csv文件读取			.read_csv('文件名.csv')

## 2 excel文件读取	 		.read_excel('文件名.xlsx')

## 3 txt读取				.read_table('文件.txt')

## 4 SQL读取

## 5 json





## Pandas CSV 文件

CSV（Comma-Separated Values，逗号分隔值，有时也称为字符分隔值，因为分隔字符也可以不是逗号），其文件以纯文本形式存储表格数据（数字和文本）。

CSV 是一种通用的、相对简单的文件格式，被用户、商业和科学广泛应用。

Pandas 可以很方便的处理 CSV 文件

### .read_csv('xxx.csv')

eg：

```
import pandas as pd

df = pd.read_csv('nba.csv')
print(df.to_string())
```

**to_string()** 用于返回 DataFrame 类型的数据，如果不使用该函数，则输出结果为数据的前面 5 行和末尾 5 行，中间部分以 **...** 代替。

```
import pandas as pd

df = pd.read_csv('nba.csv')
print(df)
```

输出：

```
              Name            Team  Number Position   Age Height  Weight            College     Salary
0    		  Java  Boston Celtics     0.0       PG  25.0    6-2   180.0              Texas  7730337.0
1      		     C  Boston Celtics    99.0       SF  25.0    6-6   235.0          Marquette  6796117.0
2     		  Hello  Boston Celtics    30.0       SG  27.0    6-5   205.0  Boston University        NaN
3      		  Name  Boston Celtics    28.0       SG  22.0    6-5   185.0      Georgia State  1148640.0
4    		         Jonas Celtics     8.0       PF  29.0   6-10   231.0                NaN  5000000.0
..             ...             ...     ...      ...   ...    ...     ...                ...        ...
453   			         Utah Jazz     8.0       PG  26.0    6-3   203.0             Butler  2433333.0
454      Raul Neto       Utah Jazz    25.0       PG  24.0    6-1   179.0                NaN   900000.0
455   Tibor Pleiss       Utah Jazz    21.0        C  26.0    7-3   256.0                NaN  2900000.0
456    Jeff Withey       Utah Jazz    24.0        C  26.0    7-0   231.0             Kansas   947276.0
457            NaN             NaN     NaN      NaN   NaN    NaN     NaN                NaN        NaN

```





### to_csv()

我们也可以使用 **to_csv()** 方法将 DataFrame 存储为 csv 文件：

```
import pandas as pd 
   
# 三个字段 name, site, age
nme = ["百度", "腾讯", "网易", "酷狗"]
st = ["www.baidu.com", "www.tenxun.com", "www.wangyi.com", "www.kugou.org"]
ag = [90, 40, 80, 98]
   
# 字典
dict = {'name': nme, 'site': st, 'age': ag} 
     
df = pd.DataFrame(dict)
  
# 保存 dataframe
df.to_csv('site.csv')
```





## 数据处理

### head()

**head( n )** 方法用于读取前面的 n 行，如果不填参数 n ，默认返回 5 行。

#### 实例 - 读取前面 5 行

```
import pandas as pd

df = pd.read_csv('nba.csv')

print(df.head())
```

输出：

```
            Name            Team  Number Position   Age Height  Weight            College     Salary
0  Avery Bradley  Boston Celtics     0.0       PG  25.0    6-2   180.0              Texas  7730337.0
1    Jae Crowder  Boston Celtics    99.0       SF  25.0    6-6   235.0          Marquette  6796117.0
2   John Holland  Boston Celtics    30.0       SG  27.0    6-5   205.0  Boston University        NaN
3    R.J. Hunter  Boston Celtics    28.0       SG  22.0    6-5   185.0      Georgia State  1148640.0
4  Jonas Jerebko  Boston Celtics     8.0       PF  29.0   6-10   231.0                NaN  5000000.0
```

#### 实例 - 读取前面 10 行

```
import pandas as pd

df = pd.read_csv('nba.csv')

print(df.head(10))
```

输出：

```
            Name            Team  Number Position   Age Height  Weight            College      Salary
0  Avery Bradley  Boston Celtics     0.0       PG  25.0    6-2   180.0              Texas   7730337.0
1    Jae Crowder  Boston Celtics    99.0       SF  25.0    6-6   235.0          Marquette   6796117.0
2   John Holland  Boston Celtics    30.0       SG  27.0    6-5   205.0  Boston University         NaN
3    R.J. Hunter  Boston Celtics    28.0       SG  22.0    6-5   185.0      Georgia State   1148640.0
4  Jonas Jerebko  Boston Celtics     8.0       PF  29.0   6-10   231.0                NaN   5000000.0
5   Amir Johnson  Boston Celtics    90.0       PF  29.0    6-9   240.0                NaN  12000000.0
6  Jordan Mickey  Boston Celtics    55.0       PF  21.0    6-8   235.0                LSU   1170960.0
7   Kelly Olynyk  Boston Celtics    41.0        C  25.0    7-0   238.0            Gonzaga   2165160.0
8   Terry Rozier  Boston Celtics    12.0       PG  22.0    6-2   190.0         Louisville   1824360.0
9   Marcus Smart  Boston Celtics    36.0       PG  22.0    6-4   220.0     Oklahoma State   3431040.0
```

### tail()

**tail( n )** 方法用于读取尾部的 n 行，如果不填参数 n ，默认返回 5 行，空行各个字段的值返回 **NaN**。

#### 实例 - 读取末尾 5 行

```
import pandas as pd

df = pd.read_csv('nba.csv')

print(df.tail())
```

输出：

```
             Name       Team  Number Position   Age Height  Weight College     Salary
453  Shelvin Mack  Utah Jazz     8.0       PG  26.0    6-3   203.0  Butler  2433333.0
454     Raul Neto  Utah Jazz    25.0       PG  24.0    6-1   179.0     NaN   900000.0
455  Tibor Pleiss  Utah Jazz    21.0        C  26.0    7-3   256.0     NaN  2900000.0
456   Jeff Withey  Utah Jazz    24.0        C  26.0    7-0   231.0  Kansas   947276.0
457           NaN        NaN     NaN      NaN   NaN    NaN     NaN     NaN        NaN
```

#### 实例 - 读取末尾 10 行

```
import pandas as pd

df = pd.read_csv('nba.csv')

print(df.tail(10))
```

输出：

```
               Name       Team  Number Position   Age Height  Weight   College      Salary
448  Gordon Hayward  Utah Jazz    20.0       SF  26.0    6-8   226.0    Butler  15409570.0
449     Rodney Hood  Utah Jazz     5.0       SG  23.0    6-8   206.0      Duke   1348440.0
450      Joe Ingles  Utah Jazz     2.0       SF  28.0    6-8   226.0       NaN   2050000.0
451   Chris Johnson  Utah Jazz    23.0       SF  26.0    6-6   206.0    Dayton    981348.0
452      Trey Lyles  Utah Jazz    41.0       PF  20.0   6-10   234.0  Kentucky   2239800.0
453    Shelvin Mack  Utah Jazz     8.0       PG  26.0    6-3   203.0    Butler   2433333.0
454       Raul Neto  Utah Jazz    25.0       PG  24.0    6-1   179.0       NaN    900000.0
455    Tibor Pleiss  Utah Jazz    21.0        C  26.0    7-3   256.0       NaN   2900000.0
456     Jeff Withey  Utah Jazz    24.0        C  26.0    7-0   231.0    Kansas    947276.0
457             NaN        NaN     NaN      NaN   NaN    NaN     NaN       NaN         NaN
```

### info()展示

info() 方法返回表格的一些基本信息：

#### 实例

```
import pandas as pd
df = pd.read_csv('nba.csv')
print(df.info())
```

输出：

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 458 entries, 0 to 457          # 行数，458 行，第一行编号为 0
Data columns (total 9 columns):            # 列数，9列
 #   Column    Non-Null Count  Dtype       # 各列的数据类型
---  ------    --------------  -----  
 0   Name      457 non-null    object 
 1   Team      457 non-null    object 
 2   Number    457 non-null    float64
 3   Position  457 non-null    object 
 4   Age       457 non-null    float64
 5   Height    457 non-null    object 
 6   Weight    457 non-null    float64
 7   College   373 non-null    object         # non-null，意思为非空的数据    
 8   Salary    446 non-null    float64
dtypes: float64(4), object(5)                 # 类型
```

non-null 为非空数据，我们可以看到上面的信息中，总共 458 行，College 字段的空值最多。

### describe()展示

快速生成**数值型数据**统计摘要的核心方法

```
import pandas as pd
df = pd.read_csv('nba.csv')
print(df.describe())
```

输出：

```
           Number         Age      Weight        Salary
count  457.000000  457.000000  457.000000  4.460000e+02
mean    17.678337   26.938731  221.522976  4.842684e+06
std     15.966090    4.404016   26.368343  5.229238e+06
min      0.000000   19.000000  161.000000  3.088800e+04
25%      5.000000   24.000000  200.000000  1.044792e+06
50%     13.000000   26.000000  220.000000  2.839073e+06
75%     25.000000   30.000000  240.000000  6.500000e+06
max     99.000000   40.000000  307.000000  2.500000e+07
```

注：

`e`（或 `E`）：代表 “乘以 10 的 n 次方”，是科学计数法的通用符号；

`+02`：代表指数为**正 2**，即乘以 `10²`；如果是 `e-02`，则是乘以 `10⁻²`（0.01）。





### 缺失值处理	dropna()

作用：删除包含缺失值（NaN/None）的行或列，返回一个删除了缺失值的新对象（默认不修改原数据）。

```
print(df.dropna())
```

拓展

DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

| 参数    | 作用                                                         | 默认值 |
| ------- | ------------------------------------------------------------ | ------ |
| axis    | ``指定删除维度：`0`（删除行）/ `1`（删除列）                 | 0      |
| how     | 删除条件：`any`（只要有一个 NaN 就删）/ `all`（全部为 NaN 才删） | 'any'  |
| thresh  | 保留至少有 `thresh` 个非 NaN 值的行 / 列（比如 thresh=2：至少 2 个有效值） | None   |
| subset  | 指定检查缺失值的列 / 行（仅检查这些列 / 行的 NaN）           | None   |
| inplace | 是否直接修改原数据：`True`（修改原数据）/ `False`（返回新数据） | False  |

`subset`

```
import pandas as pd
import numpy as np

# 创建包含缺失值的DataFrame
df = pd.DataFrame({
    '姓名': ['张三', '李四', np.nan, '王五', '赵六'],
    '年龄': [20, np.nan, 22, np.nan, 25],
    '成绩': [85, 90, np.nan, 95, np.nan]
})
df_drop3 = df.dropna(subset=['姓名'])
print("\n仅删除姓名为NaN的行：")
print(df_drop3)
```



### 异常值处理  

销售额 (0<销售额<1000) 或  年龄(0<年龄<120)  的行进行处理，将正确数据筛选出来。

```
 print(df[(df['销售额']>0) & (df['销售额'] < 1000)])
print(df[(df['年龄']>0) & (df['年龄']<120)])
print(df[(df['销售额']>0) & (df['销售额'] < 1000) & (df['年龄']>0) & (df['年龄']<120)])
```

注：

缺失值Nun，也算异常值，在处理时内部也是返回flase



### 统计汇总

计算 `销售额列` 的均值、总额、最小值与最大值

```
print(round(df['销售额'].mean(),2)) 	  		#平均值
print(round(df['销售额'].sum(),2))				#求和
print(df['销售额'].min())						#取最小值
print(df['销售额'].max())						#取最大值
```

排序

```

```



### 保存

to_csv

to_excel

to_json

```
将该两种创建好的pandas，导出成txt、excel、csv、json等文件
df.to_csv(r'我保存的第一个CSV文件.csv')
df.to_excel(r'我保存的第一个EXCEL文件.xlsx')
df.to_csv(r'我保存的第一个TXT文件.txt')  # txt的文件的存储
df.to_json(r'我保存的第一个JSON文件.json') 
```

注：

`r` 是 Python 里的**原始字符串（Raw String）** 标识，核心作用是**取消反斜杠 \ 的转义功能**，避免路径字符串因转义字符报错，是处理文件路径时的必备技巧





## Pandas JSON

JSON（JavaScript Object Notation，JavaScript 对象表示法），是存储和交换文本信息的语法，类似 XML。JSON 比 XML 更小、更快，更易解析，更多 JSON 内容可以参考 JSON 教程。

Pandas 可以很方便的处理 JSON 数据，本文以 sites.json 为例，内容如下：

实例

```
[
   {
   "id": "A001",
   "name": "百度",
   "url": "www.baidu.com",
   "likes": 61
   },
   {
   "id": "A002",
   "name": "Google",
   "url": "www.google.com",
   "likes": 124
   },
   {
   "id": "A003",
   "name": "淘宝",
   "url": "www.taobao.com",
   "likes": 45
   }
]
```

### 实例

```
import pandas as pd

df = pd.read_json('西游冰淇凌公司.json')
   
print(df.to_string())
```

**to_string()** 用于返回 DataFrame 类型的数据，我们也可以直接处理 JSON 字符串。

### 实例

```
import pandas as pd

data1 =[
    {
      "id": "A001",
      "name": "百度",
      "url": "www.baidu.com",
      "likes": 61
    },
    {
      "id": "A002",
      "name": "腾讯",
      "url": "www.tenxun.com",
      "likes": 124
    },
    {
      "id": "A003",
      "name": "淘宝",
      "url": "www.taobao.com",
      "likes": 45
    }
]

data2 = [{"id": "A001","name": "百度","url": "www.baidu.com","likes": 61},{"id": "A002","name": "腾讯","url": "www.tenxun.com","likes": 124},{"id": "A003","name": "淘宝","url": "www.taobao.com","likes": 45}]

df = pd.DataFrame(data)

print(df)
```

以上实例输出：

```
     id    name      url          likes
0  A001    百度  www.baidu.com     61
1  A002    腾讯  www.google.com    124
2  A003    淘宝  www.taobao.com    45
```

JSON 对象与 Python 字典具有相同的格式，所以我们可以直接将 Python 字典转化为 DataFrame 数据：

### 实例

```
import pandas as pd


# 字典格式的 JSON                                                                                              
s = {
    "col1":{"row1":1,"row2":2,"row3":3},
    "col2":{"row1":"x","row2":"y","row3":"z"}
}

# 读取 JSON 转为 DataFrame                                                                                           
df = pd.DataFrame(s)
print(df)
```

以上实例输出：

```
      col1 col2
row1     1    x
row2     2    y
row3     3    z
```

## 数据库连接

***python有自带可以连接数据库的库，只要我们将IP地址、端口号、账号和密码告诉它，就可以读取相关数据库里面的数据：***

```
import pymysql
import pandas as pd

# 数据库连接参数
host = '47.115.169.78'        
port = 3306                   
user = 'haoxuexingcheng'      
password = 'Hxxc@123'         
database = 'stu_python'           

# 建立数据库连接
connection = pymysql.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

try:
    # 创建游标对象
    cursor = connection.cursor()
    
    # 查询世界幸福报告2015表的数据
    query = "SELECT * FROM `人物信息表`"
    
    # 执行查询
    cursor.execute(query)
    
    # 获取列名
    columns = [desc[0] for desc in cursor.description]
    
    # 获取查询结果
    results = cursor.fetchall()
    
    # 将结果转换为DataFrame（可选，便于数据处理）
    df = pd.DataFrame(results, columns=columns)
    
    print("数据读取成功！")
    print(f"共读取 {len(results)} 行数据")
    print("\n前5行数据：")
    print(df.to_string())
    
except Exception as e:
    print(f"读取数据时发生错误: {e}")
    
finally:
    # 关闭游标和连接
    cursor.close()
    connection.close()
    print("数据库连接已关闭")
```


