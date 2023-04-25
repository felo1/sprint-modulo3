import random
silabario = ['ba', 'be', 'bi', 'bo', 'bu', 'da', 'de', 'di', 'do', 'du', 'ga', 'ge', 'gi', 'go', 'gu',
             'ka', 'ke', 'ki', 'ko', 'ku', 'la', 'le', 'li', 'lo', 'lu', 'ma', 'me', 'mi', 'mo', 'mu',
             'na', 'ne', 'ni', 'no', 'nu', 'pa', 'pe', 'pi', 'po', 'pu', 'ra', 're', 'ri', 'ro', 'ru',
             'sa', 'se', 'si', 'so', 'su', 'ta', 'te', 'ti', 'to', 'tu', 'va', 've', 'vi', 'vo', 'vu',
             'za', 'ze', 'zi', 'zo', 'zu']
simbolos = "!#$%&/()=?" #puros iconos accesibles con el teclado LATAM pasando el dedo + shift
    #exigencias:
    #crear 10 usuarios iterativamente
    #asignar contraseñas
    #cada cuenta en una nueva -variable- (diccionario nuevo), con su contraseña
    #por cada cuenta, al momento de crear, pedir un teléfono (input tb en la iteracion)
    #justamente piden que el programa no cierre hasta q se indiquen los 10 fonos
    #cada input debe verificarse de tener 8 digitos y solo digitos
    #se guarda como string
    #la contraseña debe generarse y tener los criterios de mayus, mius y numeros random

usuarios = []
#Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.
def crear_usuario():
    
    for  i in range(10): #10 loops fijos
        #generador de nombres rudimentario que randomiza SILABAS preinstruidas (definidas más arriba abajo de los import)
        #con una cantidad entre 3 y 6
        n_silabas = random.randint(3, 6) #elige un numero entre 3 y 6 para fabricar un nombre en base a las silabas incluídas en hardcode.
        nombre_usuario = ''.join(random.sample(silabario, n_silabas)).capitalize() 
        #se realiza un join sin espacios de silabas elegidas al azar del silabario, mediante el metodo random.sample() 
        apellido_usuario = ''.join(random.sample(silabario, n_silabas)).capitalize()
        username = nombre_usuario[0] + apellido_usuario + "@adalid.cl" #arma un username con la inicial del nombre de usuario, apellido y dominio
        #rut_usuario = generador_rut()
        nombre_completo = nombre_usuario + " " + apellido_usuario 
        #La contraseña debe ser creada con random y 
        # debe cumplir con los siguientes criterios: mayúsculas, minúsculas y números.
        #password compuesto por una concatenacion de 3 cositas:
        password_1_3 = str(nombre_usuario)[0:3] #las 3 primeras letras, la primera siempre capitalizada y otras dos minus
        password_4_7 = str(random.randint(1000,9999)) #para minimo 5 dígitos
        simbolo_random = random.randint(0, len(simbolos) - 1) #un numero al azar entre 0 y el largo del arreglo-1, para no salirse del index.
        password_8 = simbolos[simbolo_random] #un simbolo random de la seleccion, al final
        password = str(password_1_3 + password_4_7 + password_8) #concatena
        #por cada cuenta, al momento de crear, pedir un teléfono (input tb en la iteracion)
        
        #cada input debe verificarse de tener 8 digitos y solo digitos
        while True: #loop chequeo telefono, recordar que while true es un loop infinito por diseño, necesita un break
            telefono = str(input(f"Ingrese el teléfono móvil para el usuario {nombre_completo}: \n"))
            if telefono.isdigit() == True and len(telefono) == 8:  #verifica tener solo digitos y largo exacto 8
                break
                #si entramos acá exitosamente podemos salir del while
            else:
                #repite si alguna de las dos condiciones falla.
                print("teléfono inválido, ingrese un número de 8 carácteres:\n")
                continue
        telefono = "+569" + telefono #agrega el prefijo de pais, +569
        usuario_nuevo = {"nombre_usuario":nombre_completo, "password":password, "telefono":telefono, "username":username.lower()}
        usuarios.append(usuario_nuevo)
        print("Usuario creado exitosamente")
    print("Creación de usuarios terminada")

crear_usuario()
#Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios de tu
#aplicación (pueden ser personas, pacientes, organizaciones sociales o instituciones públicas).
#este print cumple con la función de recorrer la lista
for user in usuarios: print(user)