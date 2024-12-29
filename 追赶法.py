#chase.py
import numpy as np
def chase(a,b,c,d):
    n1,n2=np.shape(b)
    n=n1
    u=np.empty((n,1))
    l=np.empty((n,1))
    y=np.empty((n,1))
    x=np.empty((n,1))
    u[[0]]=b[[0]]
    for i in range(1,n):
        l[[i]]=a[[i]]/u[[i-1]]
        u[[i]]=b[[i]]-l[[i]]*c[[i-1]]
    print("l is {}".format(l))
    print("u is {}".format(u))
    y[[0]]=d[[0]]
    for i in range(1,n):
        y[[i]]=d[[i]]-l[[i]]*y[[i-1]]
    print("y is {}".format(y))
    x[[n-1]]=y[[n-1]]/u[[n-1]]
    for i in range(n-2,-1,-1):
        x[[i]]=(y[[i]]-c[[i]]*x[[i+1]])/u[[i]]
    print("x is {}".format(x))
    return x

import numpy as np
a=np.array([[0],[1],[1],[1],[1],[1],[1],[1],[1],[1]])
b=np.array([[-2],[-2],[-2],[-2],[-2],[-2],[-2],[-2],[-2],[-2]])
c=np.array([[1],[0],[1],[0],[1],[0],[1],[0],[1],[0]])
d=np.array([[1],[1],[0],[-1],[1],[0],[-1],[1],[0],[-1]])
chase(a,b,c,d)