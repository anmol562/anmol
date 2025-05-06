# 10d. m4.py uses the code of list1.py, set2.py and dict3.py
import list1
import set2
import dict3

list1.append1(10)
list1.extend1([20, 30])
print(list1.pop())
list1.remove1(20)

set2.adds2(5)
print(set2.slen2())
set2.remove2(5)

dict3.add3('a', 1)
print(dict3.len3())
print(dict3.keys3())
print(dict3.values3())
