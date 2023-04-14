import sqlite3

def crear_tabla_estudiante():
	try:
		conn = sqlite3.connect('test.db')
		c = conn.cursor()
		c.execute(
			'''CREATE TABLE ESTUDIANTE(
				primer_nombre TEXT  NOT NULL, 
				segundo_nombre TEXT , 
				primer_apellido TEXT  NOT NULL, 
				segundo_apellido TEXT ,
				tipo_documento TEXT  NOT NULL,
				numero_documento INTEGER PRIMARY KEY,
				nombre_padre TEXT ,
				nombre_madre TEXT ,
				telefono INTEGER,
				eps TEXT ,
				puntaje_sisben REAL,
				correo VARCHAR(255) ,
				direccion TEXT,
				clave TEXT 
				)'''
				)
		conn.commit()
		conn.close()
	except:
  		print("La base de datos ya existe")
def crear_tabla_notas():
	try:
		conn = sqlite3.connect('test.db')
		c = conn.cursor()
		c.execute(
			'''CREATE TABLE NOTAS(
				id_nota INTEGER PRIMARY KEY AUTOINCREMENT,
				documento_estudiante INTEGER  NOT NULL, 
				id_asignatura TEXT,
				nombre_asignatura TEXT,
				saber REAL,
				saber_hacer REAL,
				ser REAL
				)'''
				)
		conn.commit()
		conn.close()
	except:
  		print("La base de datos ya existe")

def insertar_nota():
	documento_estudiante = int(input("Numero de documento del estudiante:\n"))
	id_asignatura = input("ID de la asignatura:\n")
	nombre_asignatura = input("Nombre de la asignatura:\n")
	saber = float(input("Nota del saber:\n"))
	saber_hacer   = float(input("Nota del saber hacer:\n"))
	ser  = float(input("Nota del ser:\n"))

	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	sql = "INSERT INTO NOTAS (documento_estudiante,id_asignatura,nombre_asignatura,saber,saber_hacer,ser) VALUES ({},'{}','{}',{},{},{})".format(
		documento_estudiante,id_asignatura,nombre_asignatura,saber,saber_hacer,ser)
	c.execute(sql)
	conn.commit()
	conn.close()

def insertar_estudiante():
	primer_nombre = input("Primer nombre:\n")
	segundo_nombre = input("Segundo nombre:\n")
	primer_apellido = input("Primer apellido:\n")
	segundo_apellido = input("Segundo apellido:\n")
	tipo_documento   = input("Tipo de documento:\n")
	numero_documento  = int(input("numero documento:\n"))
	nombre_padre  = input("Nombre del padre:\n")
	nombre_madre =  input("Nombre de la madre:\n")
	telefono =  int(input("Telefono:\n"))
	eps =  input("Eps:\n")
	puntaje_sisben =  float(input("Puntaje de sisben:\n"))
	correo =  input("Correo:\n")
	direccion =  input("Direccion:\n")
	clave = input("Clave:\n")

	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	sql = "INSERT INTO ESTUDIANTE VALUES ('{}','{}','{}','{}','{}',{},'{}','{}',{},'{}',{},'{}','{}','{}')".format(
		primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,tipo_documento,
		numero_documento,nombre_padre,nombre_madre,telefono,eps,puntaje_sisben,correo,direccion,clave)
	c.execute(sql)
	conn.commit()
	conn.close()

def consulta_estudiante():
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('SELECT * FROM ESTUDIANTE')
	table = c.fetchall()

	for row in table:
		print(row)
	conn.close()

def consulta_notas():
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	c.execute('SELECT * FROM NOTAS')
	table = c.fetchall()
	for row in table:
		print(row)
	conn.close()
def main():
	#crear_tabla_estudiante()
	#crear_tabla_notas()

	#insertar_estudiante()
	#insertar_estudiante()
	consulta_notas()
	insertar_nota()
	insertar_nota()
	#insertar_nota()
	
	#consulta_estudiante()
	consulta_notas()

main()
