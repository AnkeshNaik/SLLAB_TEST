import sys
from functools import reduce
from collections import Counter


f = open(sys.argv[1])


contents=f.read().split()

print("file contents")
print(*contents,sep=' ')


count_dict=Counter(contents)
print("\n",count_dict)

print("decreasing order")
s= sorted(count_dict.items(),key=lambda x:x[1],reverse=True)
print(s[:10])

wl=[len(i) for i,j in s[:10]]
print("length",wl)

avg=(reduce(lambda x,y:x+y,wl)/len(wl))
print("average",avg)

sq_o=[i*i for i in wl if i%2!=0]
print("sq of odd numbers",sq_o)