def fibonacci(n):
    if (n<0): return
    elif(n==0): return 0
    elif(n==1): return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    

def sum_enteros(n):
    if n<0: return
    elif(n==0): return 0
    else:
        return n+sum_enteros(n-1)


def suma_pares(n):
    if n%2!=0: print("error")
    elif (n==2): return 2
    else:
        return n+suma_pares(n-2) 
