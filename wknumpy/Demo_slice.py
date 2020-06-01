# coding:utf-8
import numpy as np

# 对多维数组元素的切片存取内容

a = np.arange(1, 10, 1)
print(a)
# 切片获取全部
print(a[0:])

# 间隔两个获取
print(a[0::2])

# 从头获取到倒数第二个
print(a[:-1])

# 倒序获取
print(a[::-1])

print("--------------------------------------------------")
# 使用下标获取数组与原数组不共享地址空间
b = np.arange(1, 10, 1)
c = b[0:3]
b[1] = -10
print(a)
print(b)
print("------------------------------------------")
# 使用整数序列作为数组下标, 从而获取到的元素, 其结果不与源数组共享地址空间
d = np.arange(1, 10, 1)
e = d[[1, 2, 5]]
e[1] = -10
print(d)
print(e)
print('----------------------------------------')
# 使用布尔值 作为数据下标， 从而获取数组元素
f = np.arange(1, 10, 1)
g = f > 2
h = a[a > 2]
print(f)
print(g)
print(h)