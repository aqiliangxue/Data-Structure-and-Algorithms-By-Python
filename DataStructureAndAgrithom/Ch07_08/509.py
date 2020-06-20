# -*- encoding=utf-8 -*-
import hashlib

# print(hashlib.md5("hello world".encode("utf-8")).hexdigest())
# print(hashlib.sha1("hello world".encode("utf-8")).hexdigest())

m=hashlib.md5()
m.update("hello world".encode("utf-8"))
m.update("this is part #2".encode("utf-8"))
m.update("this is part #3".encode("utf-8"))
print(m.hexdigest())


