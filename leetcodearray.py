from algo1 import *

def twoSum(ArraySum, target):
        ArrayNuevo=Array(2,0)
        for i in range(0,len(ArraySum)):
            for j in range(0,len(ArraySum)):
                if ArraySum[i]+ArraySum[j]==target:
                    ArrayNuevo[0]=i
                    ArrayNuevo[1]=j
                    return ArrayNuevo
                
        return ArrayNuevo

ArraySum=Array(9,0)
ArraySum[0]=1
ArraySum[1]=8
ArraySum[2]=6
ArraySum[3]=2
ArraySum[4]=5
ArraySum[5]=4
ArraySum[6]=8
ArraySum[7]=3
ArraySum[8]=9
target=8



def removeDuplicates(ArrayR):
    ArrayNuevo=Array(len(ArrayR),0)
    for i in range(0,len(ArrayR)):
        repe=True
        for j in range(i+1,len(ArrayR)):
            if ArrayR[i]==ArrayR[j]:
                repe=False
        if repe:
             ArrayNuevo[i]=ArrayR[i]
    return ArrayNuevo





def waterArea(ArrayA):
     varAux=0
     for i in range(0,len(ArrayA)):
          AreaAct=ArrayA[i]*(len(ArrayA)-(i+1))
          if AreaAct>varAux:
               varAux=AreaAct
     return varAux



def removeElements(ArrayA,num):
     total=len(ArrayA)
     for i in range(0,len(ArrayA)):
          if num==ArrayA[i]:
               ArrayA[i]=None
               total-=1
     print(ArrayA)
     return total



def plusOne(ArrayA):
     if ArrayA[len(ArrayA)-1]==9:
          ArrayNuevo=Array(len(ArrayA)+1,0)
          ArrayNuevo[0]=1
          for i in range(1,len(ArrayNuevo)):
               ArrayNuevo[i]=0
          return ArrayNuevo
     else:
          ArrayA[len(ArrayA)-1]+=1
          return ArrayA


