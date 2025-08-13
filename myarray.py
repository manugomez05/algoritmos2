from algo1 import *


def search(Arreglo,element):
    pos=0
    for i in range(0,len(Arreglo)):
        if Arreglo[i]==element:
            return pos
        pos+=1
    return None


def insert(Array,element,position):
  if (position < len(Array) and position >= 0):
    for i in range(len(Array)-1, -1,-1):
      if (i != position):
        Array[i] = Array[i-1]
      else:
        Array[i] = element
        print(Array)
    return position
  else:
    return None



def delete(Arreglo,element):
  pos=search(Arreglo,element)
  if pos==len(Arreglo)-1:
     Arreglo[pos]=None
  elif pos is not None:
     for i in range(pos,len(Arreglo)-1):
        Arreglo[i]=Arreglo[i+1]
     Arreglo[len(Arreglo)-1]=None
     return pos
  return None

           
     

def length(Array):
   cont=0
   for i in range(0,len(Array)):
      if Array[i]!=None:
         cont+=1
   return cont
         
  
