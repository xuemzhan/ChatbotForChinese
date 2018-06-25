import jieba
a = "你好啊"
b = [w for w in jieba.cut(a)]
print (b)