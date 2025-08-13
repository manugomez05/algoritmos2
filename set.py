from algo1 import *



def Create_Set(ArrayS):
  ArrayAux=Array(len(ArrayS),0)
  cont=0
  contaux=0
  for i in range (0,len(ArrayS)):
    for j in range(0,len(ArrayS)):
      if ArrayAux[j]==ArrayS[i]:
        cont=cont+1
        print("repetido")
    if cont==0:
        print("cont=0")
        ArrayAux[contaux]=ArrayS[i]
        contaux=contaux+1
    else:
        print("Reiniciar")
        cont=0
  Set=Array(contaux,0)
  for i in range(0,contaux):
    Set[i]=ArrayAux[i]
    print(Set[i])
  return Set



def check_duplicates(arreglo):
  booleano=False
  for i in range(0,len(arreglo)):
    for j in range(0,len(arreglo)):
      if j!=i and arreglo[i]==arreglo[j]:
        booleano=True
  return booleano
     

def Union(ArrayS,ArrayT):
  nuevoArray=Array(len(ArrayS)+len(ArrayT),0)
  for i in range (0,len(ArrayS)):
    nuevoArray[i]=ArrayS[i]
  for i in range(len(ArrayS)+1,len(ArrayT)):
    nuevoArray[i]=ArrayT[i]
  
  arrayUnion=Create_Set(nuevoArray)
  return arrayUnion
            


def Intersection(ArrayS,ArrayT):
  contrepe=0
  cont=0
  for i in range(0,len(ArrayS)):
    for j in range(0,len(ArrayT)):
        if ArrayS[i]==ArrayT[j]:
            contrepe+=1
    arrayNuevo=Array(contrepe,0)
    for i in range(0,len(ArrayS)):
        for j in range(0,len(ArrayT)):
            if ArrayS[i]==ArrayT[j]:
                arrayNuevo[cont]=ArrayS[i]
                cont+=1
  arrayNuevo=Create_Set(arrayNuevo)
  return arrayNuevo

def Difference(ArrayS,ArrayT):
   contdif=0
   cont=0
   for i in range(0,len(ArrayS)):
      for j in range(0,len(ArrayT)):
         if ArrayS[i]!=ArrayT[j]:
            contdif+=1
   arrayNuevo=Array(contdif*2,0)
   for i in range(0,len(ArrayS)):
      for j in range(0,len(ArrayT)):
         if ArrayS[i]!=ArrayT[j]:
            arrayNuevo[cont]=ArrayS[i]
            arrayNuevo[cont+1]=ArrayT[j]
            cont+=2
   arrayNuevo=Create_Set(arrayNuevo)
   return arrayNuevo