from binarytree import * 

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
      
