#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#%% 1. Sin utilizar el comando abs, escribir un programa que calcule e imprima el valor absoluto de cualquier número (sea
#%% entero o decimal).

valor = float(input('ingrese un número: ')) #%%
decimales = valor % 1

if valor < 0 and not decimales:
    valor = int(valor)
    valor = valor*(-1)
    print('El valor absoluto es: ',valor)
    
elif valor > 0 and not decimales:
    valor = int(valor)
    print('El valor absoluto es: ',valor)
    
elif valor < 0 and decimal >= 0:
    valor = valor*(-1)
    print('El valor absoluto es: ',valor)
    
elif valor > 0 and decimales >=0:
    print('El valor absoluto es: ',valor)

elif valor < 0 and decimales == 0:
    valor = valor*(-1)
    print('El valor absoluto es: ',valor)


# In[ ]:


#%% 2. Leer un número entero y escribirlo en reversa. Por ejemplo, 461975 será 579164. No utilizar comandos de
#%%ordenamiento.


valor = int(input('Ingrese un número entero: '))

if valor < 0:
    signo = -1
else:
    signo = 1
    
valor = abs(valor)
inverso = 0

while valor/10 > 0:
    n = valor % 10
    valor = int(valor/10)
    inverso = (inverso*10) + n

inverso = inverso*signo
print('El inverso del valor es: ',inverso)  


# In[ ]:


#%% 3. Leer un número entero de 3 dígitos y determinar si contiene el dígito 8.

valor = int(input('Ingrese un número de tres cifras: '))

if valor > 99 and valor < 1000:
    a3 = valor % 10
    a2 = int((valor % 100)/10)
    a1 = int((valor % 1000)/100)
    if a1 == 8 or a2 == 8 or a3 == 8:
        print('El número contiene el dígito 8.')
    else:
        print('el número no contiene el dígito 8.')
elif valor < -99 and valor > -1000:
        b3 = -valor % 10
        b2 = int((-valor % 100)/10)
        b1 = int((-valor % 1000)/100)
        if b1 == 8 or b2== 8 or b3 == 8:
            print('El número contiene el dígito 8.')
        else:
            print('El número no contiene el dígito 8.')
else:
    print('El número no posee 3 dígitos.')


# In[ ]:


#%% 4. Leer un número entero positivo y determinar la suma de sus dígitos pares. Por ejemplo, en el número 124, los dígitos
#%% pares son el 2 y el 4 y su suma vale 6.

valor = int(input('Ingrese un número entero: '))

par=0

if valor < 0:
    print('El número no es un entero positivo')
else:
    while valor/10 > 0:
        n = valor % 10
        if n % 2 == 0:
            par = par + n
        valor = int(valor/10)   
    print('La suma de los pares del número ingresado es: ',par)   


# In[ ]:


#%% 5. Leer un número entero y determinar el número de cincos que están consecutivos en un número. Por ejemplo, en
#%%5512355551 hay 6 cincos consecutivos. Ahora, en 234555234512 solo hay 3 cincos consecutivos.

valor = int(input('Ingrese un número: '))

def count_consec(valor):
    count=1
    consec_list=[]
    for i in valor:
        if valor[i] == int(valor[i+1]+1):
            count+=1
        else:
            list.append(count)
    return consec_list

count_consec(valor)


# In[ ]:


#%% 6. Leer un número entero y determinar si la suma de sus dígitos es un número de Fibonacci.

def fib(n):                            
    fibonacci = []
    a,b = 1,1
    while a<=n:
        fibonacci.append(a)
        a,b = b,b+a
    return fibonacci

valor = int(input('Ingrese un número: '))
suma = 0

while valor/10 > 0:
    n = valor % 10
    valor = int(valor/10)
    suma = suma + n
    
if suma in fib(suma):
    print('La suma de los dígitos del número ingresado es un número de fibonacci.')
    
else:
    print('La suma del número ingresado no es un número de fibonnaci.')
    
    
    # In[ ]:


#%% 7. Leer un número entero positivo y determine si existen en el número dígitos repetidos. Reporte cuales son los dígitos
#%% repetidos.


    
    # In[ ]:
    
#%% 8. Iterar a través de los primeros cien enteros positivos, buscando los múltiplos de 3 e imprimiendo y almacenándolos en
#%% una lista hasta encontrar los primeros 15 de ellos. Una vez encontrados, continuar iterando en busca de los múltiplos
#%% de 4 y almacenarlos en otra lista.

rango_inferior = 1
rango_superior = 101
Limite_3 = 16
Inicio_4 = Limite_3-5
multiples_3=[3]  #Lista de los multiplos de 3
multiples_4=[]  #Lista de los multiplos de 4

#%% Función

def multiple(valor, multiple):

#%% Contidición de la función
    
    residuo = valor % multiple
    if residuo == 0:
        return True
    else:
        return False

#%%Multiplos de 3

for i in range(rango_inferior,rango_superior):# bucle del 1 al 100
    if multiple(i,3):
        multiples_3.append(i)
print('Los primeros 15 multiplos de 3 son: ',multiples_3[rango_inferior:Limite_3])

#%%Multiplos de 4

for j in range(rango_inferior,rango_superior):
    if multiple(j,4):
        multiples_4.append(j)
print('De los restantes números, los multiplos de 4 son: ',multiples_4[Inicio_4:rango_superior])


# In[ ]:


#%% 9. Hacer un programa que lea las coordenadas (x1,y1,r1) y (x2,y2,r2) que corresponden al centro y al radio de dos círculos.
#%% Lea un punto de coordenadas (a,b). Determina si (a,b) está contenido: a) dentro del círculo 1; b) dentro del círculo 2;
#%% c) dentro de ambos círculos; d) fuera de ambos círculos. Recordemos que el círculo es el lugar geométrico de los puntos
#%% del plano cuya distancia a otro punto fijo, llamado centro, es menor o igual que una cantidad constante, llamada radio.

def distancia(x, y, a, b):
    
#teorema de pitágoras
    dist= (((x - a) ** 2)+((y - b) ** 2)) ** (1 / 2)
    return dist

# Ingresar los datos del círculo 1.
    
while True :
    try:
        coord_x_1= int(input('Ingresar la coordenada en X del círculo 1: '))
        break
    except ValueError :
        print ('\nEl valor ingresado no es correcto, intentelo de nuevo')

while True :
    try:
        coord_y_1= int(input('Ingresar la coordenada en Y del círculo 1: '))
        break
    except ValueError :
        print ('\nEl valor ingresado no es correcto, intentelo de nuevo')
        
while True :
    try:
        r_1= int(input('Ingrese el radio del círculo 1: '))
        if r_1 >= 0 : break
    except ValueError :
        print ('\nEl valor ingresado no es correcto, intente de nuevo')

#datos para el circulo 2.
    
while True :
    try:
        coord_x_2= int(input('Ingresar la coordenada en X del círculo 2: '))
        break
    except ValueError :
        print ('\nEl valor ingresado no es correcto, intente de nuevo')

while True :
    try:
        coord_y_2= int(input('Ingresar la coordenada en Y del círculo 2: '))
        break
    except ValueError :
        print ('\nEl valor ingresado no es correcto, intente de nuevo')
        
while True :
    try:
        r_2= int(input('Por favor ingrese el radio del círculo 2: '))
        if r_2 >= 0 : break
    except ValueError :
        print ('\nEl valor ingresado no es correcto, intente de nuevo')

# Ingresar las coordenadas del punto (a,b) a evaluar.
    
while True :
    try:
        a= int(input('Por favor ingrese la coordenada en X del punto: '))
        break
    except ValueError :
        print ('\nEl valor ingresado no es correcto, intente de nuevo')

while True :
    try:
        b= int(input('Por favor ingrese la coordenada en Y del punto: '))
        break
    except ValueError :
        print ('\nEl valor ingresado no es correcto, intente de nuevo')

# Ejecutar la función nombrada al inicio de código.
        
distancia_a_1= distancia(coord_x_1, coord_y_1, a, b)
distancia_a_2= distancia(coord_x_2, coord_y_2, a, b)

# Evaluar las condiciones de impresión.

if distancia_a_1 <= r_1 and distancia_a_2 <= r_2:
    print ('\nEl punto', a,',', b, 'se encuentra dentro de ambos círculos.')
    
elif distancia_a_1 > r_1 and distancia_a_2 <= r_2:
    print ('\nEl punto', a,',', b, 'se encuentra solo dentro del círculo 2.')
    
elif distancia_a_1 <= r_1 and distancia_a_2 > r_2:
    print ('\nEl punto', a,',', b, 'se encuentra solo dentro del círculo 1.')
    
elif distancia_a_1 > r_1 and distancia_a_2 > r_2:
    print ('\nEl punto', a,',', b, 'no se encuentra dentro de ningún círculo.')


# In[ ]:


#%% 10. Sin utilizar el método .upper() para cadenas, escribir un programa que lea una cadena de texto y la imprima en
#%% mayúscula. Tenga en cuenta que el programa debe aceptar las letras con tilde, la ñ y la ü.

def imprimir_en_mayuscula(long):
    
    for n in range (long + 1) :
        if n == long :
            break
        else: 
            code = ord (cad[n])
            if 224 <= code <= 252 or 97 <= code <= 122:
                code -= 32
                caracter= chr((code))
                print (caracter, end='')
            else:
                caracter= chr((code))
                print (caracter, end='')
    return caracter

while True :
    try:
        cad= input('Por favor ingrese una cadena de texto: ')
        break
    except ValueError :
        print ('\nEl valor ingresado no es correcto, intente de nuevo')
        
 
long = len(cad)

print ('\nLa cadena de texto escrita en mayusculas es:')

cadena_en_mayuscula= imprimir_en_mayuscula(long)

    
# In[ ]:


#%% 12. Hacer un programa que lea dos palabras (podrían estar en mayúscula o minúscula) y determine cual está primero en
#%% el diccionario. El programa debe soportar letras con tilde, la ü y la ñ.

word1 = (input('Ingrese un palabra: '))
word2 = (input('Ingrese otra palabra: '))

x = word1
y = word2
word1 = word1.lower()
word2 = word2.lower() 

if word1 < word2:
    print('va primero en el diccionario',x)

else:
    print('va primero en el diccionario',y)


# In[ ]:


#%% 13. Escribir un programa que lea una cadena de texto y la imprima como un triángulo. Por ejemplo, si la cadena entrada
#%% es: "Es una locura odiar a todas las rosas porque una te pinchó: renunciar a todos tus sueños porque uno de ellos no
#%% se realizó - El Principito", el programa debe imprimir:

piramid = (input('Ingrese palabra o texto: '))
tamaño1 = [piramid]
tamaño = len(tamaño1)
m = (2 * tamaño) - 2
for i in range(0, tamaño):
    for j in range(0, m):
        print(end=" ")
    m = m - 1 
    for j in range(0, i + 1):
       
        print(F"{piramid}", end=' ')
    print(" ")

   
# In[ ]:


#%% 14. Leer una cadena de texto y organice alfabéticamente cada una de las letras que la componen, repitiendo cada una
#%% tantas veces como se encuentra. Por ejemplo, la cadena ‘tarea importante’ será ‘aaaeeimnoprrttt’. (Note que no se
#%% incluyen los espacios).

cadena = (input('Ingrese un oracion: '))
cadena1 = cadena.replace(" ", "")
cadena1 = sorted(cadena1)
cadena1 = ''.join(cadena1)
print('El orden alfabetico de la palabra es: ',cadena1) 


# In[ ]:


#%% 15. Leer una lista de números enteros y enumerar cuantos elementos se repiten exactamente dos veces. Utilizar para tal
#%% fin el método count() de listas.

lista = list(input('Ingrese una lista de números ordenados ascendentemente: '))

lista1 = lista[:] 
lista1.sort() 
if (lista1 == lista):
    print('La lista está correctamente ordenada.')
else:
    print('La lista no está ordenada correctamente.')
    
valor = list(input('Ingrese un número: '))

lista2= lista+valor
lista2.sort()
print('La nueva lista es: ',lista2)


# In[ ]:


#%% 16. Leer una lista de números ya ordenados de forma ascendente y verificar que dicha lista está ordenada. Luego, leer un
#%% número e insertarlo en la lista en la posición que le corresponde a dicho número.

defina = int(input('Ingrese la cantidad de numeros que ingresara: '))
lista1 = list(range(defina))


contador = defina
contador2 = 0
while contador >=0 and contador2 <= defina:
   numero = int(input('Ingrese los numeros  enteros: '))
   lista1[0+contador2] = numero
   
   contador = defina-1
   contador2 = contador2+1
   

b = lista1


contador3 = defina
while contador3 >=0:
    b1 = b.pop(contador3-1)
    contador3 = defina-1

