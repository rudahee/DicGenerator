import itertools
import os
												
def dicGen():									# Imprime el mensaje de carga en consola
	print("""
··········································			
#  SU DICCIONARIO SE ESTA GENERANDO...   #
··········································""")
def dicFin():									# Imprime el mensaje de finalizacion en consola
	os.system("cls")
	print("""
#==============================#
# Su diccionario ha finalizado #
#==============================#""")			
def generacion(longitud, caracteres, nombre_txt='Diccionario.txt'):		# Generamos el diccionario y lo escribimos
	txt = open(nombre_txt, 'w')                                			# Creamos un archivo con permisos de escritura
	for t in itertools.product(list(caracteres), repeat=longitud):  	# Bucle que genera la lista
		if opcion == 4:
			txt.write('95573' + ''.join(str(x) for x in t) + '00\n')	# Escribe la lista generada con un prefijo y un sufijo
		else:
			txt.write(''.join(str(x) for x in t) + '\n')  				# Escribe la lista generada

os.system("cls")														# Imprime la consola el menu de bienvenida de bienvenida
opcion = int(input("""
	################################
	## GENERADOR DE DICCIONARIOS  ##
	################################
	#          Creado por          #
	#            ~Ruben~           #
	################################

	Seleccione una opcion:
	1) PIN/Passcode (4 digitos | 0-9)
	2) Contraseña Administracion Router Movistar (8 digitos | a-z & 0-9)
	3) Contraseña Router Movistar (20 digitos | A-F & 0-9)
	4) Numeros de telefono (4 digitos | 0-9) FORMATO 95573XXXX00
	5) Personalizado

OPCION > """))

os.system("cls")
if opcion == 1:																	# Opcion predefinida 1 - PIN/Passcode
	dicGen()
	generacion(4, '0123456789')
	dicFin()		
elif opcion == 2:																# Opcion predefinida 2 - Admin Router Movistar
	dicGen()
	generacion(8, 'abcdefghijklmnopqrstuvwxyz0123456789')
	dicFin()
elif opcion == 3:																# Opcion predefinida 3 - Router Movistar
	dicGen()
	generacion(20, 'ABCDEF0123456789')
	dicFin()
elif opcion == 4:																# Opcion predefinida 4 - Numeros de telefono
	dicGen()
	generacion(4, '0123456789')
	dicFin()
elif opcion == 5:																# Opcion Personalizada - Aqui el orden de llamada a las funciones es distinta
	l = int(input("Longitud de la clave \n> "))									# ya que primero debemos hacer las preguntas al usuario.
	c = input("\nCaracteres componen la clave \n> ")		
	n = input("\nNombre del fichero de salida (sin extension) \n> ") + ".txt"	# Agregamos el *.txt al nombre elegido por el usuario
	os.system("cls")
	dicGen()
	generacion(l, c, n)															# Pasamos 3 argumentos en vez de 2 por que hemos definido un nombre de archivo
	dicFin()																	# y no usaremos el nombre de "Diccionario.txt" que es el predefinido la en funcion

# Fin del codigo

