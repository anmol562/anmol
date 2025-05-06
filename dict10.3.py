# 10c. dict3.py contains len3(d), add3(k,v), keys3(), values3()
d = {}

def len3():
    return len(d)

def add3(k, v):
    d[k] = v

def keys3():
    return list(d.keys())

def values3():
    return list(d.values())
