#input
n=int(input("Digite el valor de n:"))

#Proseccing
i = 1 
suma = 0 
while (i<=n):
    suma=suma+i
    i=i+1

#output
    print("La suma de los " + str(n) + " primeros numeros: " + str(suma))