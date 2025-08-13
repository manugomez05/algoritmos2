import binarytree

class AVLTree:
	root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None

def rotateLeft(Tree,avlnode):
      newRoot = avlnode.rightnode
      avlnode.rightnode = newRoot.leftnode

      if newRoot.leftnode!=None:
            newRoot.leftnode.parent=avlnode
      newRoot.parent=avlnode.parent

      if avlnode.parent==None:
            Tree.root = newRoot
      else:
            if avlnode.parent.leftnode==avlnode:
                avlnode.parent.leftnode = newRoot
            else:
                  avlnode.parent.rightnode=newRoot
      newRoot.leftnode=avlnode
      avlnode.parent=newRoot

def rotateRight(Tree,avlnode):
      newRoot = avlnode.leftnode
      avlnode.lefttnode = newRoot.righttnode

      if newRoot.rightnode!=None:
            newRoot.rightnode.parent=avlnode
      newRoot.parent=avlnode.parent

      if avlnode.parent==None:
            Tree.root = newRoot
      else:
            if avlnode.parent.rightnode==avlnode:
                avlnode.parent.rightnode = newRoot
            else:
                  avlnode.parent.leftnode=newRoot
      newRoot.rightnode=avlnode
      avlnode.parent=newRoot
      

def calculateBalance(AVLTree):
    def height(node):
        if node is None:
            return 0
        # altura = 1 + max(altura izquierda, altura derecha)
        return 1 + max(height(node.leftnode), height(node.rightnode))

    def update_bf(node):
        if node is None:
            return
        # calcular alturas de subárboles
        left_height = height(node.leftnode)
        right_height = height(node.rightnode)
        # asignar balance factor
        node.bf = left_height - right_height
        # seguir con los hijos
        update_bf(node.leftnode)
        update_bf(node.rightnode)

    update_bf(AVLTree.root)

def reBalance(AVLTree):
     current=AVLTree.root
     reBalanceR(current)


def reBalanceR(current):
     if current is None:
          return
     if current.bf==-2:
          rotateLeft(AVLTree,current)
     elif current.bf==2:
          rotateRight(AVLTree,current)
     reBalanceR(current.leftnode)
     reBalanceR(current.rightnode)

def insert(B,element,key):
     binarytree.insert(B,element,key)
     reBalance(B)

def delete(B,element):
     binarytree.delete(B,element)
     reBalance(B)
