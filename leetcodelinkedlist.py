from algo1 import*
from linkedlist import*
import math
class LinkedList:
    head=None
class Node:
    value=None
    nextNode=None

l1= LinkedList()
l2=LinkedList()
add(l1,1)
add(l1,1)
add(l1,1)

def mergeTwoSortedLists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    dummy = Node()         # Nodo auxiliar para simplificar el manejo del head
    tail = dummy           # Puntero para ir construyendo la lista fusionada

    # Punteros para recorrer ambas listas
    p1 = list1.head
    p2 = list2.head

    while p1 is not None and p2 is not None:
        if p1.value <= p2.value:
            tail.nextNode = p1
            p1 = p1.nextNode
        else:
            tail.nextNode = p2
            p2 = p2.nextNode
        tail = tail.nextNode  # Avanza el puntero del resultado

    # Si queda algún nodo en alguna lista, lo enlazamos al final
    if p1 is not None:
        tail.nextNode = p1
    elif p2 is not None:
        tail.nextNode = p2

    # Crear la lista resultado
    mergedList = LinkedList()
    mergedList.head = dummy.nextNode  # Ignora el nodo dummy

    return mergedList


def deleteDuplicates(A):
    current=A.head
    while current.nextNode is not None:
        if current.nextNode.value==current.value:
            current.nextNode=current.nextNode.nextNode
        current=current.nextNode
    return current


def checkCycles(A):
    pasosimple=A.head
    pasodoble=A.head.nextNode
    while pasodoble.nextNode.nextNode!=None:
        if pasodoble==pasosimple:
            return True
        pasosimple=pasosimple.nextNode
        pasodoble=pasodoble.nextNode.nextNode
    return False

def intersectionLists(A,B):
    currentA=A.head
    currentB=B.head
    posA=1
    posB=1
    while currentA is not None:
        while currentB is not None:
            if currentA.value ==currentB.value:
                print("La intersección es ",currentA.value,", en la posición de A: ",posA," y en la posición de B: ",posB)
                return
            currentB=currentB.nextNode
            posB+=1
        currentA=currentA.nextNode
        posA+=1


def reverseList(A):
    current=A.head
    B=LinkedList()
    while current!=None:
        add(B,current.value)
        current=current.nextNode
    return B
imprimir_lista(l1)
imprimir_lista(reverseList(l1))

def palindrome(A):
    long=length(A)
    ArrayA=Array(long,0)
    current=A.head
    cont=long-1
    for i in range(0,long):
        ArrayA[i]=current.value
        current=current.nextNode  
    if long%2==0:
        for i in range(0,long/2):
            if ArrayA[i]!=ArrayA[cont]:
                return False
            cont-=1
    else:
        cont=long-1
        for i in range(0,math.trunc(long/2)):
            if ArrayA[i]!=ArrayA[cont]:
                return False
            cont-=1
    return True
print(palindrome(l1))

def convertBinary(A):
    long=length(A)-1
    current=A.head
    total=0
    while current!=None:
        total=total+current.value*(2**long)
        long-=1
        current=current.nextNode
    return total

print(convertBinary(l1))