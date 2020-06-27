# -*- encoding=utf-8 -*-
import hashlib
"""
散列Hashing：算法复杂度降到O（1），如果能事先知到要找的数据应该出现在什么位置，就可以直接到这个位置看看数据项是否存在，
散列表又称哈希表，是一种数据集，其中数据项的存储方式尤其有利于快速的查找定位，散列表的每一个存储位置称为槽，可以用来保存数据项，
每个槽有唯一名称。
散列函数：实现从数据项到存储槽名称转换的，称为散列函数。
常用散列方法：求余数


"""
# print(hashlib.md5("hello world".encode("utf-8")).hexdigest())
# print(hashlib.sha1("hello world".encode("utf-8")).hexdigest())

m=hashlib.md5()
m.update("hello world".encode("utf-8"))
m.update("this is part #2".encode("utf-8"))
m.update("this is part #3".encode("utf-8"))
print(m.hexdigest())


