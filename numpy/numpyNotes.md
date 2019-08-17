# NumPy学习要点
NumPy的核心是**ndarray**对象，主要用于对多维数组执行计算，广泛用于需要进行矩阵计算的领域，如机器学习、图像处理、数学任务等。

## **基础知识**
### 1. 数组对象的关键属性
- **ndarray.ndim**：数组的轴（维度）的个数。在Python世界中，维度的数量被称为rank。
- **ndarray.shape**：数组的维度。这是一个整数的元组，表示每个维度中数组的大小。对于有n行和m列的矩阵，shape将是(n,m)。因此，shape元组的长度就是rank或维度的个数 ndim。
- **ndarray.size**：数组元素的总数。这等于shape的元素的乘积。
- **ndarray.dtype**：一个描述数组中元素类型的对象。可以使用标准的Python类型创建或指定dtype。另外NumPy提供它自己的类型。例如numpy.int32、numpy.int16和numpy.float64。
- **ndarray.itemsize**：数组中每个元素的字节大小。例如，元素为 float64 类型的数组的 itemsize 为8（=64/8），而 complex32 类型的数组的 itemsize 为4（=32/8）。它等于 ndarray.dtype.itemsize 。
- **ndarray.data**：该缓冲区包含数组的实际元素。通常，我们不需要使用此属性，因为我们将使用索引访问数组中的元素

### 2. 数组的创建
1. 从其他Python结构（例如，列表，元组）转换
```
>>> x = np.array(list, tuple etc.)
```
2. numpy原生数组的创建
```
>>> np.arange(1, 2, 0.1)    # 指定范围及步长
>>> np.zeros((2, 3)) # 用tuple指定形状
>>> np.ones((4, 4))
>>> np.linspace(1., 4., 6)   # 制定范围及元素数量
```
linspace()函数创建具有指定数量元素的数组，并在指定的开始值和结束值之间平均间隔

3. 从磁盘读取数组，无论是标准格式还是自定义格式 

这一方式最常见，如从.csv文件导入。

4. 通过使用字符串或缓冲区从原始字节创建数组

5. 使用特殊库函数（例如，random）