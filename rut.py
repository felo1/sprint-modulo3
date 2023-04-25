import random

def generar_rut():
    rut= random.randint(10000000, 27000000)
    rut_reves = rut.reverse()
    lista_para_multiplicar = zip(rut, rut_reves)
    for n in lista_para_multiplicar:
        n.append(lista_para_multiplicar[0]*lista_para_multiplicar[1])
        print lista_para_multiplicar
            
"""    
1) Se toman todos los números del RUT (sin el digito verificador).
27.962.409

2) Se da vuelta esa cifra, es decir, reordenamos los números comenzando de derecha a izquierda.
9 0 4 2 6 9 7 2

3) Ahora multiplicaremos cada uno de estos números por la siguiente serie: 2, 3, 4, 5, 6, 7 y si se acaba la serie, volvemos a empezar 2, 3, 4...

9 × 2 = 18
0 × 3 = 0
4 × 4 = 16
2 × 5 = 10
6 × 6 = 36
9 × 7 = 63
7 × 2 = 14
2 × 3 = 6

4) Una vez hecho esto, sumamos todos los resultados:
18 + 0 + 16 + 10 + 36 + 73 + 14 + 6 = 163

5) El resultado obtenido lo dividimos por 11, para luego obter el Resto de esa división.
163 / 11 = 14,81818181818182
Tomamos el resultado sin decimales y sin aproximación. En este caso quedaría 14 y lo multimplicamos por 11
14 x 11 = 154

6) Posteriormente, al resultado del paso 4 le restamos los 154 obtenidos anteriormente.
163 - 154 = 9 (valor absoluto, sin signo)

7) Y para finalizar, a 11 le restamos el resultado anterior:
11 - 9 = 2

Y así hemos calculado que 2 es el digito verificador de nuestro Rut, tal cual lo indicamos al comienzo de este ejercicio.

Ahora bien, si como resultado final del digito verficador nos da el número 11, el dígito verificador será 0 y si es 10 el dígito será la letra K.

11 => 0
10 => K
"""