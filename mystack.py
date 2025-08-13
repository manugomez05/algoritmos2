from algo1 import *

def pop(L):
    if L.head==None:
        return None
    headvalue=L.head.value
    L.head=L.head.nextNode
    return headvalue