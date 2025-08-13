from algo1 import*
from linkedlist import*
from mystack import*
import math
class BinaryTree:
    root=None

class BinaryTreeNode:
    key=None
    value=None
    leftnode=None
    rightnode=None
    parent=None

class LinkedList:
    head=None
class Node:
    value=None
    nextNode=None

B=BinaryTree()
nodoRaiz=BinaryTreeNode()
nodoRaiz.value=3
nodoRaiz.key=6
B.root=nodoRaiz
nodoIzq=BinaryTreeNode()
nodoIzq.value=8
nodoIzq.key=4
nodoRaiz.leftnode=nodoIzq
nodoDer=BinaryTreeNode()
nodoDer.value=10
nodoDer.key=8
nodoRaiz.rightnode=nodoDer

def searchR(node, element):

  if node == None:
    return None
  if node.value == element:
    return node.key
  searchleft = searchR(node.leftnode, element)
  if searchleft != None:
    return searchleft

  return searchR(node.rightnode, element)


def search(B, element):

  return searchR(B.root, element)
    
print(search(B,10))
def insert(B,element,key):
    current=B.root
    newNode=BinaryTreeNode()
    newNode.value=element
    newNode.key=key
    return insertR(current,newNode)

def insertR(current,newNode):
    if current.key<newNode.key:
        if current.rightnode==None:
            current.rightnode=newNode
            return newNode.key
        else:
            return insertR(current.rightnode,newNode)
    else:
        if current.leftnode==None:
            current.leftnode=newNode
            return newNode.key
        else:
            return insertR(current.leftnode,newNode)    

def mostrar_bst(tree):
    def _print_subtree(node, level=0, prefix="Root: "):
        if node is not None:
            print("    " * level + prefix + f"[{node.key} -> {node.value}]")
            if node.leftnode or node.rightnode:
                _print_subtree(node.leftnode, level + 1, "L--- ")
                _print_subtree(node.rightnode, level + 1, "R--- ")
        else:
            print("    " * level + prefix + "None")

    if tree.root is None:
        print("El árbol está vacío.")
    else:
        _print_subtree(tree.root)

mostrar_bst(B)
insert(B,5,7)
mostrar_bst(B)

def accessR(node, key):
  if node == None:
    return None
  else:
    if node.key == key:
      return node.value
    elif key < node.key:
      return accessR(node.leftnode, key)
    elif key > node.key:
      return accessR(node.rightnode, key)
    else:
      return None


def access(B, key):
  return accessR(B.root, key)
print(access(B,7))



def updateR(node,element,key):
    if node==None:
        return None
    else:
        if node.key==key:
            node.value=element
        elif node.key>key:
            return updateR(node.leftnode,element,key)
        elif node.key<key:
            return updateR(node.rightnode,element,key)
        else:
            return None

def update(B,element,key):
    return updateR(B.root,element,key)

mostrar_bst(B)
update(B,15,7)
mostrar_bst(B)


def traverseInOrder(B):
    Inorder=LinkedList()
    current=B.root
    traverseInOrderR(current,Inorder)
    return reverse(Inorder)

def traverseInOrderR(current,Inorder):
  if current!=None:
    traverseInOrder(current.leftnode)
    add(Inorder,current.value)
    traverseInOrder(current.rightnode)


def traverseInPostOrder(B):
   PostOrder=LinkedList()
   current=B.root
   traverseInPostOrderR(current,PostOrder)
   return reverse(PostOrder)

def traverseInPostOrderR(current,PostOrder):
   if current!=None:
      traverseInPostOrderR(current.leftnode,PostOrder)
      traverseInPostOrderR(current.rightnode,PostOrder)
      add(PostOrder,current.value)

def traverseInPreOrder(B):
   current=B.root
   PreOrder=LinkedList()
   traverseInPreOrderR(current,PreOrder)
   return reverse(PreOrder)

def traverseInPreOrderR(current,PreOrder):
   if current!=None:
      add(PreOrder,current.value)
      traverseInPreOrderR(current.leftnode,PreOrder)
      traverseInPreOrderR(current.rightnode,PreOrder)

def isBST(B):
   InOrder=LinkedList()
   InOrder=traverseInOrder(B)
   current=InOrder.head
   while current.nextNode!=None:
      if current.value>current.nextNode.value:
         return None
      current=current.nextNode
   return True

def isSubTree(B1,B2):
   lista1=traverseInOrder(B1)
   lista2=traverseInOrder(B2)
   return isSubTreeR(lista1,lista2)

def isSubTreeR(lista1,lista2):
   current1=lista1.head
   current2=lista2.head
   long=length(lista2)
   cont=0
   while current1.nextNode!=None:
      if current1.value==current2.value:
        cont=1
        current1Aux=current1.nextNode
        current2=current2.nextNode
        while current2.nextNode!=None and current1Aux.nextNode!=None:
           if current1Aux.value==current2.value:
              cont+=1
              current2=current2.nextNode
              current1Aux=current1Aux.nextNode
        if cont==long:
           return True
      current1=current1.nextNode
   return False

def getMaxSum(B):
   current=B.root
   total=0
   return getMaxSum(current,total)

def getMaxSumR(current,total):
   if current!=None:
      total=total+current.value
      getMaxSumR(current.leftnode,total)
      getMaxSumR(current.rightnode,total)
   return total

def searchFixedPoint(A):
  return searchFixedPointR(A,0,len(A)-1)

def searchFixedPointR(A,inicio,fin):
  medio=math.trunc(len(A)/2)
  if A[medio]<medio:
    return searchFixedPointR(A,medio+1,fin)
  elif A[medio]>medio:
    return searchFixedPointR(A,inicio,medio-1)
  else:
    return medio




def height(current):
  if current==None:
    return 0
  return 1+ max(heightR(current.leftnode),heightR(current.rightnode))

def width(B):
  w=LinkedList()
  return widthR(B.root,w,0)

def widthR(current,w,level):
  if current==None:
    return w
  if level>=length(w):
    insert(w,0,level)
  currentwidth=search(w,level)
  update(w,currentwidth+1,level)
  widthR(current.leftnode,w,level+1)
  widthR(current.rightnode,w,level+1)
  return w

def pathWithSum(B,X):
   p=LinkedList()
   path=LinkedList()
   return pathWithSumR(B.root,X,path,p)

def pathWithSumR(current,X,path,p):
   if current==None:
      return path
   add(p,current.key)
   subx=X-current.key
   if subx==0 and current.leftnode is None and current.rightnode is None:
      newp=reverse(p)
      add(path,newp)
   pathWithSumR(current.leftnode,subx,path,p)
   pathWithSumR(current.rightnode,subx,path,p)
   pop(p)
   return path
      
def mirror(B):
   B.root=mirrorR(B.root)
   return B.root

def mirrorR(current):
   if current is None:
      return None
   left_mirror=mirrorR(current.leftnode)
   right_mirror=mirrorR(current.rightnode)
   current.rightnode=left_mirror
   current.leftnode=right_mirror
   return current


def isSymetric(B):
   if B.root==None:
      return None
   w=LinkedList()
   left_width=widthR(B.root.leftnode,w,0)
   right_width=widthR(B.root.rightnode,w,0)
   pass


def isBalanced(B):
   if B.root==None:
      return None
   left_height=height(B.root.leftnode)
   right_height=height(B.root.rightnode)
   return abs(left_height,right_height)<=1


def minimalTree(A):
   B=BinaryTree()
   B.root=minimalTreeR(A,0,len(A)-1)

def minimalTreeR(A,inicio,fin):
   medio=math.trunc(len(A)/2)
   current=BinaryTreeNode()
   current.key=A[medio]
   current.value=A[medio]
   current.leftnode=minimalTreeR(A,inicio,medio-1)
   current.rightnode=minimalTreeR(A,medio+1,fin)
   return current

def contains(B1,B2):
   return containsR(B1.root,B2.root)

def containsR(current1,current2):
   if current1==None and current2==None:
      return False
   if current2==None:
      return True
   if current1.key==current2.key:
      return containsR(current1.leftnode,current2.leftnode) and containsR(current1.rightnode,current2.rightnode)
   else:
      return containsR(current1.leftnode,current2) or containsR(current1.rightnode,current2)

def searchFixedPointA(A):
   return searchFixedPointRA(A,0,len(A)-1)

def searchFixedPointRA(A,inicio,fin):
   if inicio>fin:
      return -1
   medio=math.trunc(len(A))

   if A[medio]>medio:
      return searchFixedPointRA(A,inicio,medio-1)
   elif A[medio]<medio:
      return searchFixedPointRA(A,medio+1,fin)
   else:
      return medio

def heightA(current):
   current
   if current==None:
      return 0
   return 1+max(heightA(current.leftnode),heightA(current.rightnode))


def widthsA(B):
   w=LinkedList()
   return widthsRA(B.root,w,0)

def widthsRA(current,w,level):
   if length(w)>level:
      insert(w,0,level)
   current_widht=access(w,level)
   update(w,current_widht+1,level)
   widthsRA(current.leftnode,w,level+1)
   widthsRA(current.rightnode,w,level+1)
   return w

def pathWithSumA(B,X):
   p=LinkedList()
   paths=LinkedList()
   pathWithSumRA(B.root,X,paths,p)
   return paths
def pathWithSumRA(current,X,paths,p):
   if current==None:
      return paths
   add(p,current.key)
   xParcial=X-current.key
   if xParcial==0 and current.leftnode is None and current.rightnode is None:
      newp=reverse(p)
      add(paths,newp)
   pathWithSumRA(current.leftnode,xParcial,paths,p)
   pathWithSumRA(current.rightnode,xParcial,paths,p)
   pop(p)
   return paths

def mirrorA(B):
   B.root=mirrorRA(B.root)
   return B.root

def mirrorRA(current):
   if current is None:
      return None
   left_mirror=mirrorRA(current.leftnode)
   right_mirror=mirrorRA(current.rightnode)
   current.leftnode=right_mirror
   current.rightnode=left_mirror
   return current 

def isBalanced(B):
   if B.root==None:
      return None
   left_height=height(B.root.leftnode)
   right_height=height(B.root.rightnode)
   return abs(left_height,right_height)<=1

def isSymetricA(B):
   if B.root==None:
      return True
   w=LinkedList()
   left_widths=widthsRA(B.root.leftnode,w,0)
   right_widths=widthsRA(B.root.rightnode,w,0)
   pass

def extract_keys_with_condition(B):
   if B.root==None:
      return None
   w=LinkedList()
   return extract_keys_with_conditionR(B.root,w,0)

def extract_keys_with_conditionR(current,w,sum):
   if current.leftnode==None and current.rightnode==None:
      return None
   sum=sum+current.key
   left_sum=extract_keys_with_conditionR(current.leftnode,w,sum)
   right_sum=extract_keys_with_conditionR(current.rightnode,w,sum)
   if left_sum<right_sum:
      add(w,current.key)
   return sum