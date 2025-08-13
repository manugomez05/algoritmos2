from algo1 import*
class LinkedList:
    head=None
class Node:
    value=None
    nextNode=None

L=LinkedList()

def add(L,element):
    current = L.head
    newNode=Node()
    newNode.value=element
    if current==None:
        L.head=newNode
    else:
        newNode.nextNode=current
        L.head=newNode
    return
add(L,8)
add(L,9)
add(L,10)

def reverse(L):
    current=L.head
    reverseList=LinkedList()
    while current!=None:
        add(reverseList,current.value)
        current=current.nextNode
    return reverseList


def search(L,element):
    current = L.head
    pos=0
    while current!=None:
        if current.value==element:
            return pos
        else:
            pos+=1
            current=current.nextNode
    return None
    

def insert(L,element,position):
    current=L.head
    newNode=Node()
    newNode.value=element
    pos=0
    while current!=None:
        if pos==position:
            current.nextNode=current
            current=newNode
            return position
        else:
            pos+=1
    return None

def delete(L,element):
    pos=search(L,element)
    if pos:
        current=L.head
        for i in range(0,pos-1):
            current=current.nextNode
        current.nextNode=current.nextNode.nextNode
        return pos
    return None

def length(L):
    current=L.head
    pos=0
    while current!=None:
        pos+=1
        current=current.nextNode
    return pos

def access(L,position):
    current=L.head
    if position==0:
        return current.value
    else:
        for i in range(0,position):
            current.nextNode=current 
        if current!=None:
            return current.value 
    return None


def update(L,element,position):
    current=L.head
    for i in range(0,position):
        current=current.nextNode
    if current!=None:
        current.value=element
        return position
    return None


def imprimir_lista(lista: LinkedList):
    actual = lista.head
    while actual is not None:
        print(actual.value, end=" → " if actual.nextNode else "")
        actual = actual.nextNode
    print()  # Salto de línea al final      


imprimir_lista(L)
L=reverse(L)
imprimir_lista(L)  