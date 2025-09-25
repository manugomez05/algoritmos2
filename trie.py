from linkedlist import *
class Trie:
    root=None

class TrieNode:
    parent=None
    children=None
    key=None
    isEndOfWord=False

def insert(T,element):
    insertR(T.root,element)

def insertR(trie_node,element):


    if len(element)==0:
        trie_node.isEndOfWord=True
        return
    caracter=element[0]
    while trie_node:
        

        if(trie_node).children==None:
            trie_node.children=linkedlist()
            new_node=TrieNode()
            new_node.parent=trie_node
            new_node.key=caracter
            linkedlist.add(trie_node.children,new_node)
            trie_node=new_node
        else:
            current=trie_node.children.head
            while current:
                if current.value.key==caracter:
                    trie_node=current.value
                    break
                current=current.nextNode
            if current==None:
                new_node=TrieNode()
                new_node.parent=trie_node
                new_node.key=caracter
                linkedlist.add(trie_node.children,new_node)
                trie_node=new_node
    
    element=element[1:]
    return insertR(trie_node,element)

def search(T,element):
    return searchR(T.root,element)

def searchR(trie_node,element):
    if trie_node.children==None:
        return False
    if len(element)==0:
        return True
    caracter=element[0]
    while trie_node:
        current=trie_node.children.head
        while current:
            if current.value.key==caracter:
                trie_node=current
                break        
            current=current.nextNode
        if current.nextNode==None:
            return False
    element=element[1:]               
    return searchR(trie_node,element)

def delete(T,element):
    if search(T,element):
        deleteR(T.root,element)

def deleteR(trie_node,element):
    if len(element)>0:
        caracter=element[0]
        while trie_node:
            current=trie_node.children.head
            while current:
                if current.value.key==caracter:
                    trie_node=current                      
                    break
                current=current.nextNode

        element=element[1:]
        deleteR(trie_node,element)
    else:
        current=trie_node
        while trie_node.parent:
            if current.nextNode==None:
                current=trie_node.parent
            else:
                 delete(trie_node.parent.children,trie_node)
                break


def mostrar_trie(node, nivel=0):
    if node is None:
        return

    indentacion = "  " * nivel
    fin = " (Fin)" if node.isEndOfWord else ""
    print(f"{indentacion}{node.key}{fin}")

    if node.children is not None:
        actual = node.children.head
        while actual is not None:
            mostrar_trie(actual.value, nivel + 1)
            actual = actual.nextNode
            
    
    
def insertR(trie_node, element):
  if len(element) == 0:
    trie_node.isEndOfWord = True
    return
  
  letra = element[0]

  if trie_node.children != None:
    current_node = trie_node.children.head

    while current_node != None:

      if current_node.value.key == letra:
        trie_node = current_node.value
        break
      current_node = current_node.nextNode

    if current_node == None:
      new_node = TrieNode()
      new_node.branch = False
      new_node.key = letra
      new_node.parent = trie_node

      add(trie_node.children, new_node)
      trie_node = new_node

  else:
    trie_node.children = LinkedList()
    new_node = TrieNode()
    new_node.branch = False
    new_node.key = letra
    new_node.parent = trie_node
    
    add(trie_node.children, new_node)
    trie_node = new_node

  element = element[1:]
  return insertR(trie_node, element)

def insert_trie(T, palabra):
  if T.root != None:
    insertR(T.root, palabra)
  else:
    root = TrieNode()
    root.key = None
    T.root = root
    return insert_trie(T, palabra)