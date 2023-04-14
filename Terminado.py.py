from tkinter import *
from tkinter import messagebox
import sqlite3
import time
from tkinter import ttk
import tkinter

ruloz = sqlite3.connect("matriculas.db")
cursor = ruloz.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS ESTUDIANTES_1 (nombre TEXT, nombre2 TEXT, apellido TEXT, apellido2 TEXT
,doc_id TEXT , identidad NUMERIC,genero TEXT,fecha_nacimiento TEXT,edad TEXT,rh TEXT, ciudad TEXT,direccion TEXT,salud TEXT
,entidad TEXT,correo TEXT,telefono TEXT,acudiente TEXT, nombre2a TEXT, apellidoa TEXT,apellido2a TEXT
,parentesco TEXT,ocupacion TEXT, ciudad2 TEXT, direccion2 TEXT,correo2 TEXT, telefono2 TEXT,doc_id2 TEXT,identidad2 TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS ESTUDIANTES_2 (nombre TEXT, nombre2 TEXT, apellido TEXT, apellido2 TEXT
,doc_id TEXT , identidad NUMERIC,genero TEXT,fecha_nacimiento TEXT,edad TEXT,rh TEXT, ciudad TEXT,direccion TEXT,salud TEXT
,entidad TEXT,correo TEXT,telefono TEXT,acudiente TEXT, nombre2a TEXT, apellidoa TEXT,apellido2a TEXT
,parentesco TEXT,ocupacion TEXT, ciudad2 TEXT, direccion2 TEXT,correo2 TEXT, telefono2 TEXT,doc_id2 TEXT,identidad2 TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS ESTUDIANTES_3 (nombre TEXT, nombre2 TEXT, apellido TEXT, apellido2 TEXT
,doc_id TEXT , identidad NUMERIC,genero TEXT,fecha_nacimiento TEXT,edad TEXT,rh TEXT, ciudad TEXT,direccion TEXT,salud TEXT
,entidad TEXT,correo TEXT,telefono TEXT,acudiente TEXT, nombre2a TEXT, apellidoa TEXT,apellido2a TEXT
,parentesco TEXT,ocupacion TEXT, ciudad2 TEXT, direccion2 TEXT,correo2 TEXT, telefono2 TEXT,doc_id2 TEXT,identidad2 TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS ESTUDIANTES_4 (nombre TEXT, nombre2 TEXT, apellido TEXT, apellido2 TEXT
,doc_id TEXT , identidad NUMERIC,genero TEXT,fecha_nacimiento TEXT,edad TEXT,rh TEXT, ciudad TEXT,direccion TEXT,salud TEXT
,entidad TEXT,correo TEXT,telefono TEXT,acudiente TEXT, nombre2a TEXT, apellidoa TEXT,apellido2a TEXT
,parentesco TEXT,ocupacion TEXT, ciudad2 TEXT, direccion2 TEXT,correo2 TEXT, telefono2 TEXT,doc_id2 TEXT,identidad2 TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS ESTUDIANTES_5 (nombre TEXT, nombre2 TEXT, apellido TEXT, apellido2 TEXT
,doc_id TEXT , identidad NUMERIC,genero TEXT,fecha_nacimiento TEXT,edad TEXT,rh TEXT, ciudad TEXT,direccion TEXT,salud TEXT
,entidad TEXT,correo TEXT,telefono TEXT,acudiente TEXT, nombre2a TEXT, apellidoa TEXT,apellido2a TEXT
,parentesco TEXT,ocupacion TEXT, ciudad2 TEXT, direccion2 TEXT,correo2 TEXT, telefono2 TEXT,doc_id2 TEXT,identidad2 TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS ESTUDIANTES_6 (nombre TEXT, nombre2 TEXT, apellido TEXT, apellido2 TEXT
,doc_id TEXT , identidad NUMERIC,genero TEXT,fecha_nacimiento TEXT,edad TEXT,rh TEXT, ciudad TEXT,direccion TEXT,salud TEXT
,entidad TEXT,correo TEXT,telefono TEXT,acudiente TEXT, nombre2a TEXT, apellidoa TEXT,apellido2a TEXT
,parentesco TEXT,ocupacion TEXT, ciudad2 TEXT, direccion2 TEXT,correo2 TEXT, telefono2 TEXT,doc_id2 TEXT,identidad2 TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS ESTUDIANTES_7 (nombre TEXT, nombre2 TEXT, apellido TEXT, apellido2 TEXT
,doc_id TEXT , identidad NUMERIC,genero TEXT,fecha_nacimiento TEXT,edad TEXT,rh TEXT, ciudad TEXT,direccion TEXT,salud TEXT
,entidad TEXT,correo TEXT,telefono TEXT,acudiente TEXT, nombre2a TEXT, apellidoa TEXT,apellido2a TEXT
,parentesco TEXT,ocupacion TEXT, ciudad2 TEXT, direccion2 TEXT,correo2 TEXT, telefono2 TEXT,doc_id2 TEXT,identidad2 TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS ESTUDIANTES_8 (nombre TEXT, nombre2 TEXT, apellido TEXT, apellido2 TEXT
,doc_id TEXT , identidad NUMERIC,genero TEXT,fecha_nacimiento TEXT,edad TEXT,rh TEXT, ciudad TEXT,direccion TEXT,salud TEXT
,entidad TEXT,correo TEXT,telefono TEXT,acudiente TEXT, nombre2a TEXT, apellidoa TEXT,apellido2a TEXT
,parentesco TEXT,ocupacion TEXT, ciudad2 TEXT, direccion2 TEXT,correo2 TEXT, telefono2 TEXT,doc_id2 TEXT,identidad2 TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS ESTUDIANTES_9 (nombre TEXT, nombre2 TEXT, apellido TEXT, apellido2 TEXT
,doc_id TEXT , identidad NUMERIC,genero TEXT,fecha_nacimiento TEXT,edad TEXT,rh TEXT, ciudad TEXT,direccion TEXT,salud TEXT
,entidad TEXT,correo TEXT,telefono TEXT,acudiente TEXT, nombre2a TEXT, apellidoa TEXT,apellido2a TEXT
,parentesco TEXT,ocupacion TEXT, ciudad2 TEXT, direccion2 TEXT,correo2 TEXT, telefono2 TEXT,doc_id2 TEXT,identidad2 TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS ESTUDIANTES_10 (nombre TEXT, nombre2 TEXT, apellido TEXT, apellido2 TEXT
,doc_id TEXT , identidad NUMERIC,genero TEXT,fecha_nacimiento TEXT,edad TEXT,rh TEXT, ciudad TEXT,direccion TEXT,salud TEXT
,entidad TEXT,correo TEXT,telefono TEXT,acudiente TEXT, nombre2a TEXT, apellidoa TEXT,apellido2a TEXT
,parentesco TEXT,ocupacion TEXT, ciudad2 TEXT, direccion2 TEXT,correo2 TEXT, telefono2 TEXT,doc_id2 TEXT,identidad2 TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS ESTUDIANTES_11 (nombre TEXT, nombre2 TEXT, apellido TEXT, apellido2 TEXT
,doc_id TEXT , identidad NUMERIC,genero TEXT,fecha_nacimiento TEXT,edad TEXT,rh TEXT, ciudad TEXT,direccion TEXT,salud TEXT
,entidad TEXT,correo TEXT,telefono TEXT,acudiente TEXT, nombre2a TEXT, apellidoa TEXT,apellido2a TEXT
,parentesco TEXT,ocupacion TEXT, ciudad2 TEXT, direccion2 TEXT,correo2 TEXT, telefono2 TEXT,doc_id2 TEXT,identidad2 TEXT)""")
cursor.close()

#Crear base de datos
conexion = sqlite3.connect('Base_total')
cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS ADMINISTRATIVO (ID INTEGER PRIMARY KEY AUTOINCREMENT, USUARIO VARCHAR, CONTRASEÑA VARCHAR)")
cursor.execute("SELECT * FROM ADMINISTRATIVO")
lista_admi = cursor.fetchall()
cursor.close()
conexion.close()



#Verificar admi
def verificar():
	conexion=sqlite3.connect('Base_total')
	cursor=conexion.cursor()
	cursor.execute("SELECT * FROM ADMINISTRATIVO")
	lista_admi = cursor.fetchall()
	cursor.close()
	conexion.close()
	for i in lista_admi:
		opcion=False
		if usuario.get()==i[1] and contrasena.get()==i[2]:
			administrativo()

			opcion = True
			break
	if opcion==False:
		opcion=messagebox.askretrycancel('Error', 'Usuario o contraseña incorrecta')
		if opcion:
			Acceder()
#ventana para acceder admi
def Acceder():

	vAcceder=Tk()
	vAcceder.title('Acceder')
	vAcceder.iconbitmap('UISIcono.ico')
	global usuario
	global contrasena
	usuario=StringVar('')
	contrasena=StringVar('')

	textUsuario=Label(vAcceder, text='Usuario')
	textUsuario.grid(row=0,column=0, sticky='w',padx=5,pady=5)
	cuadroUsuario=Entry(vAcceder,textvariable=usuario)
	cuadroUsuario.grid(row=0,column=1)

	textContrasena=Label(vAcceder,text='Contraseña')
	textContrasena.grid(row=1,column=0, sticky='w',padx=5,pady=5)
	cuadroContrasena=Entry(vAcceder,textvariable=contrasena)
	cuadroContrasena.grid(row=1,column=1)
	cuadroContrasena.config(show='*')


	boton1=Button(vAcceder,text='Entrar',command=lambda:[vAcceder.destroy(), verificar()])
	boton1.grid(row=3,column=1)
	Button(vAcceder, text='Volver',command=lambda:(vAcceder.destroy(),inicioP())).grid(row=3, column=0)

	vAcceder.mainloop()

#ventana ya ingresado y verificado el admi
def administrativo():
	def profesor():
		def crearProfesor():
			def verificar():
				if materia.get()==1:
					MateriaAsignada.set("Calculo 1")
					materiaPass=True
				elif materia.get()==2:
					MateriaAsignada.set('Algebra Lineal 1')
					materiaPass=True
				elif materia.get()==3:
					MateriaAsignada.set('Quimica Basica')
					materiaPass=True
				elif materia.get()==4:
					MateriaAsignada.set('Quimica 1')
					materiaPass=True
				elif materia.get()==5:
					MateriaAsignada.set('Ingles 1')
					materiaPass=True
				else:
					materiaPass=False
				if len(nombre.get())>0 and materiaPass:
					if len(apellido.get())>0:
							crear()
					else:
						messagebox.showinfo('Error', 'Por favor llene las casillas.')
				else:
					messagebox.showinfo('Error', 'Por favor llene las casillas.')

			def crear():
				nombreTotal=nombre.get()+' '+apellido.get()
				conexion = sqlite3.connect('Base_total')
				cursor = conexion.cursor()
				cursor.execute("INSERT INTO PROFESORES VALUES (NULL,?,?,?,0)",(nombreTotal , MateriaAsignada.get(), contraseña.get()))
				conexion.commit()
				cursor.close()
				conexion.close()
				messagebox.showinfo('Crear profesor', 'Profesor creado correctamente')
				vcrearprofesor.destroy()
				profesor()

			
			vcrearprofesor=Tk()
			vcrearprofesor.config(bg='AliceBlue')
			vcrearprofesor.title('Crear profesor')
			nombre=StringVar('')
			contraseña=StringVar('')
			apellido=StringVar('')
			materia=IntVar(0)
			MateriaAsignada=StringVar()

			Label(vcrearprofesor, text='Nombre', bg='AliceBlue').grid(row=1, column=0)
			Entry(vcrearprofesor,width=20,textvariable=nombre).grid(row=1, column=1)
			Label(vcrearprofesor, text='Apellido',bg='AliceBlue').grid(row=2, column = 0)
			Entry(vcrearprofesor,width=20,textvariable=apellido).grid(row=2, column=1)
			Label(vcrearprofesor, text= 'Contraseña', bg='AliceBlue').grid(row=3, column=0)
			Entry(vcrearprofesor, width=20, textvariable=contraseña).grid(row=3,column=1)
			Label(vcrearprofesor, text='Seleccione la materia a dictar:',bg='AliceBlue').grid(row=1,column=3)
			Radiobutton(vcrearprofesor,text='Calculo I',variable=materia,value=1).grid(row=2,column=3)
			Radiobutton(vcrearprofesor,text='Algebra I',variable=materia,value=2).grid(row=3,column=3)
			Radiobutton(vcrearprofesor,text='Quimica Basica',variable=materia,value=3).grid(row=4,column=3)
			Radiobutton(vcrearprofesor,text='Quimica I',variable=materia,value=4).grid(row=5,column=3)
			Radiobutton(vcrearprofesor,text='Ingles I',variable=materia,value=5).grid(row=6,column=3)
			Button(vcrearprofesor, text='Crear', command=lambda:(verificar())).grid(row=7, column=0,columnspan=2)
			Button(vcrearprofesor, text= 'Volver',command=lambda:(vcrearprofesor.destroy(),profesor())).grid(row=7, column=2, columnspan=2)
			vcrearprofesor.mainloop()

		def cargar():
			Id.config(state='normal')
			n.config(state='normal')
			m.config(state='normal')
			c.config(state='normal')

			conexion = sqlite3.connect('Base_total')
			cursor = conexion.cursor()
			cursor.execute("SELECT * FROM PROFESORES")
			lista_profesores=cursor.fetchall()
			cursor.close()
			conexion.close()

			for i in lista_profesores:
				Id.insert(INSERT, i[0])
				Id.insert(INSERT, '\n')
				n.insert(INSERT, i[1]+'\n' )
				m.insert(INSERT, i[2]+'\n')
				c.insert(INSERT, i[3]+'\n')

			Id.config(state='disabled')
			n.config(state='disabled')
			m.config(state='disabled')
			c.config(state='disabled')

		def editarProfesor():
			def verificar():
				global encontrar
				conexion = sqlite3.connect('Base_total')
				cursor = conexion.cursor()
				cursor.execute("SELECT * FROM PROFESORES")
				lista_profesores= cursor.fetchall()
				cursor.close()
				conexion.close()
				encontrar=False
				if Id.get().isdigit():
					for i in range(len(lista_profesores)):
						if int(Id.get())==lista_profesores[i][0]:
							encontra_profesor=lista_profesores[i]
							encontrar=True
				if encontrar:
					nombre.set(encontra_profesor[1])
					contraseña.set(encontra_profesor[3])
					materia.set(encontra_profesor[2])	
				else:
					if messagebox.askretrycancel('ID incorrecta','Por favor verifique que la ID exista'):
						pass
					else:
						vEditarProfesor.destroy()
						profesor()

			def guardar():
				if encontrar:
					if materia.get()==1:
						MateriaAsignada.set("Calculo 1")
						materiaPass=True
					elif materia.get()==2:
						MateriaAsignada.set('Algebra Lineal 1')
						materiaPass=True
					elif materia.get()==3:
						MateriaAsignada.set('Quimica Basica')
						materiaPass=True
					elif materia.get()==4:
						MateriaAsignada.set('Quimica 1')
						materiaPass=True
					elif materia.get()==5:
						MateriaAsignada.set('Ingles 1')
						materiaPass=True
					conexion = sqlite3.connect('Base_total')
					cursor = conexion.cursor()
					cursor.execute("UPDATE PROFESORES SET NOMBRE='%s', MATERIAS='%s', CONTRASEÑA='%s' WHERE CODIGO='%s'"%(nombre.get(),MateriaAsignada.get(),contraseña.get(),int(Id.get())))
					conexion.commit()
					cursor.close()
					conexion.close()
					messagebox.showinfo('Editado correctamente', 'Profesor editado correctamente')
					vEditarProfesor.destroy()
					profesor()

			vEditarProfesor=Tk()
			vEditarProfesor.title('Editar profesor')
			vEditarProfesor.config(bg='AliceBlue')
		
			Id=StringVar()
			nombre=StringVar()
			contraseña=StringVar()
			materia=IntVar(0)
			global encontrar
			encontrar=False
			Label(vEditarProfesor, text=' ',bg='AliceBlue').grid(row=0,column=0)
			Label(vEditarProfesor, text='Ingrese la ID del profesor a editar:',bg='AliceBlue').grid(row=1,column=0)
			Entry(vEditarProfesor, textvariable=Id, width=20, ).grid(row=1, column=1)
			Button(vEditarProfesor, text='Cargar',command=lambda:verificar()).grid(row=1, column=2)

			Label(vEditarProfesor, text='Nombre:',bg='AliceBlue').grid(row=2,column=0)
			Entry(vEditarProfesor, textvariable=nombre).grid(row=2, column=1)

			Label(vEditarProfesor, text='Contraseña',bg='AliceBlue').grid(row=3,column=0)
			Entry(vEditarProfesor, textvariable=contraseña).grid(row=3,column=1)

			Label(vEditarProfesor, text='Seleccione la materia a dictar:',bg='AliceBlue').grid(row=2,column=2)
			Radiobutton(vEditarProfesor,text='Calculo I',variable=materia,value=1).grid(row=3,column=2)
			Radiobutton(vEditarProfesor,text='Algebra I',variable=materia,value=2).grid(row=4,column=2)
			Radiobutton(vEditarProfesor,text='Quimica Basica',variable=materia,value=3).grid(row=5,column=2)
			Radiobutton(vEditarProfesor,text='Quimica I',variable=materia,value=4).grid(row=6,column=2)
			Radiobutton(vEditarProfesor,text='Ingles I',variable=materia,value=5).grid(row=7,column=2)
			Button(vEditarProfesor, text='Guardar', command=lambda:(guardar())).grid(row=8, column=2,columnspan=2)
			Button(vEditarProfesor, text='volver', command=lambda:(vEditarProfesor.destroy(), profesor())).grid(row=8, column=0,columnspan=2)

		vprofesor = Tk()
		vprofesor.title('Profesores')
		vprofesor.config(bg='AliceBlue')

		conexion = sqlite3.connect('Base_total')
		cursor = conexion.cursor()
		cursor.execute("""CREATE TABLE IF NOT EXISTS PROFESORES (CODIGO INTEGER PRIMARY KEY AUTOINCREMENT,
							NOMBRE VARCHAR,
							MATERIAS VARCHAR,
							CONTRASEÑA VARCHAR)""")
		cursor.close()
		conexion.close()

		Id=Text(vprofesor,width=10, height=15, state='disabled')
		n=Text(vprofesor,width=20, height=15, state='disabled')
		m=Text(vprofesor,width=20, height=15, state='disabled')
		c=Text(vprofesor,width=10, height=15, state='disabled')

		Label(vprofesor, text='ID', bg='AliceBlue').grid(row=0,column=0)
		Label(vprofesor, text='Nombre', bg='AliceBlue').grid(row=0,column=1)
		Label(vprofesor, text='Materia', bg='AliceBlue').grid(row=0,column=2)
		Label(vprofesor, text='Contraseña', bg='AliceBlue').grid(row=0,column=4)

		Id.grid(row=1,column=0)
		n.grid(row=1,column=1)
		m.grid(row=1,column=2)
		c.grid(row=1,column=4)
			
		Button(vprofesor, text='Crear profesor', command=lambda:(vprofesor.destroy(),crearProfesor())).grid(row=2, column=0)
		Button(vprofesor, text='Editar profesor', command= lambda:(vprofesor.destroy(),editarProfesor())).grid(row=2,column=1)
		
		Button(vprofesor, text='volver',command=lambda:(vprofesor.destroy(),administrativo())).grid(row=2, column=4)
		cargar()
		vprofesor.mainloop()

	def estudiantes():
		def cargar():
			Id.config(state='normal')
			n.config(state='normal')
			ca.config(state='normal')
			c.config(state='normal')
			
			conexion = sqlite3.connect('Base_total')
			cursor = conexion.cursor()
			cursor.execute("SELECT * FROM ESTUDIANTES")
			lista_estudiantes=cursor.fetchall()
			cursor.close()
			conexion.close()

			for i in lista_estudiantes:
				Id.insert(INSERT, i[0])
				Id.insert(INSERT, '\n')
				ca.insert(INSERT, i[2]+'\n')
				n.insert(INSERT, i[1]+'\n' )
				c.insert(INSERT, i[3]+'\n')

			Id.config(state='disabled')
			n.config(state='disabled')
			ca.config(state='disabled')
			c.config(state='disabled')

		def crearEstudiante():
			def verificar():
				if carrera.get()==1:
					carreraPass=True
					eleccion.set('Ingeneria Electronica')
					materias.set('Calculo 1&Quimica Basica&Algebra Lineal 1&Ingles 1')
				elif carrera.get()==2:
					carreraPass=True
					eleccion.set('Ingeneria Electrica')
					materias.set('Calculo 1&Quimica Basica&Algebra Lineal 1&Ingles 1')
				elif carrera.get()==3:
					carreraPass=True
					eleccion.set('Ingeneria Quimica')
					materias.set('Calculo 1&Quimica 1&Algebra Lineal 1&Ingles 1')
				elif carrera.get()==4:
					carreraPass=True
					eleccion.set('Ingeneria Civil')
					materias.set('Calculo 1&Quimica Basica&Algebra Lineal 1&Procesos de Lectura')
				elif carrera.get()==5:
					carreraPass=True
					eleccion.set('Ingeneria Industrial')
					materias.set('Calculo 1&Quimica Basica&Algebra Lineal 1&Cultura fisica')
				else:
					carreraPass=False

				if len(nombre.get())>0 and carreraPass:
					if len(apellido.get())>0:
						if len(contraseña.get())>0:
							crear()
						else:
							messagebox.showinfo('Error', 'Por favor llene las casillas.')
					else:
						messagebox.showinfo('Error', 'Por favor llene las casillas.')
				else:
					messagebox.showinfo('Error', 'Por favor llene las casillas.')


			def crear():
				nombreTotal= nombre.get()+' '+apellido.get()
				conexion = sqlite3.connect('Base_total')
				cursor = conexion.cursor()
				cursor.execute("INSERT INTO ESTUDIANTES VALUES (NULL,?,?,?,0,?,0)",(nombreTotal , eleccion.get(), contraseña.get(), materias.get()))
				conexion.commit()
				cursor.close()
				conexion.close()
				messagebox.showinfo('Creado correctamente', 'El estudiante fue creado correctamente')
				vCrearEstudiante.destroy()
				estudiantes()

			vCrearEstudiante=Tk()
			vCrearEstudiante.title('Crear Estudiante')
			vCrearEstudiante.config(bg='AliceBlue')
			nombre=StringVar()

			apellido=StringVar()
			contraseña=StringVar()
			carrera=IntVar()
			eleccion =StringVar()
			materias = StringVar()

			Label(vCrearEstudiante, text='Nombre', bg='AliceBlue').grid(row=1, column=0)
			Entry(vCrearEstudiante,width=20,textvariable=nombre).grid(row=1, column=1)
			Label(vCrearEstudiante, text='Apellido',bg='AliceBlue').grid(row=2, column = 0)
			Entry(vCrearEstudiante,width=20,textvariable=apellido).grid(row=2, column=1)
			Label(vCrearEstudiante, text= 'Contraseña', bg='AliceBlue').grid(row=3, column=0)
			Entry(vCrearEstudiante, width=20, textvariable=contraseña).grid(row=3,column=1)
			Label(vCrearEstudiante, text='Seleccione la carrera del estudiante',bg='AliceBlue').grid(row=1,column=3)
			Radiobutton(vCrearEstudiante,text='Ingeneria Electronica',variable=carrera,value=1, bg='AliceBlue').grid(row=2,column=3)
			Radiobutton(vCrearEstudiante,text='Ingeneria Electrica',variable=carrera,value=2, bg='AliceBlue').grid(row=3,column=3)
			Radiobutton(vCrearEstudiante,text='Ingeneria Quimica',variable=carrera,value=3, bg='AliceBlue').grid(row=4,column=3)
			Radiobutton(vCrearEstudiante,text='Ingeneria Civil',variable=carrera,value=4, bg='AliceBlue').grid(row=5,column=3)
			Radiobutton(vCrearEstudiante,text='Ingeneria Industrial',variable=carrera,value=5, bg='AliceBlue').grid(row=6,column=3)
			Button(vCrearEstudiante, text='Crear', command=lambda:(verificar())).grid(row=7, column=2,columnspan=2)
			Button(vCrearEstudiante, text='volver', command=lambda:(vCrearEstudiante.destroy(),estudiantes())).grid(row=7, column=0,columnspan=2)
			vCrearEstudiante.mainloop()

		def editarEstudiante():
			def verificar():
				global encontrar
				conexion = sqlite3.connect('Base_total')
				cursor = conexion.cursor()
				cursor.execute("SELECT * FROM ESTUDIANTES")
				lista_estudiantes= cursor.fetchall()
				cursor.close()
				conexion.close()
				encontrar=False
				if Id.get().isdigit():
					for i in range(len(lista_estudiantes)):
						if int(Id.get())==lista_estudiantes[i][0]:
							encontra_estudiante=lista_estudiantes[i]
							encontrar=True
				if encontrar:
					if encontra_estudiante[2]=='Ingeneria Electronica':
						carrera.set(1)
					elif encontra_estudiante[2]=='Ingeneria Electrica':
						carrera.set(2)
					elif encontra_estudiante[2]=='Ingeneria Quimica':
						carrera.set(3)
					elif encontra_estudiante[2]=='Ingeneria Civil':
						carrera.set(4)
					elif encontra_estudiante[2]=='Ingeneria Industrial':
						carrera.set(5)

					nombre.set(encontra_estudiante[1])
					contraseña.set(encontra_estudiante[3])
					
				else:
					if messagebox.askretrycancel('ID incorrecta','Por favor verifique que la ID exista'):
						pass
					else:
						vEditarEstudiante.destroy()
						profesor()

			def guardar():
				if encontrar:
					if carrera.get()==1:
						eleccion.set('Ingeneria Electronica')
						materias.set('Calculo 1$Quimica Basica&Algrabra Lineal 1&Ingles 1')
					elif carrera.get()==2:
						eleccion.set('Ingeneria Electrica')
						materias.set('Calculo 1$Quimica Basica&Algrabra Lineal 1&Ingles 1')
					elif carrera.get()==3:
						eleccion.set('Ingeneria Quimica')
						materias.set('Calculo 1$Quimica 1&Algrabra Lineal 1&Ingles 1')
					elif carrera.get()==4:
						eleccion.set('Ingeneria Civil')
						materias.set('Calculo 1$Quimica Basica&Algrabra Lineal 1&Procesos de Lectura')
					elif carrera.get()==5:
						eleccion.set('Ingeneria Industrial')
						materias.set('Calculo 1$Quimica Basica&Algrabra Lineal 1&Cultura fisica')

					conexion = sqlite3.connect('Base_total')
					cursor = conexion.cursor()
					cursor.execute("UPDATE ESTUDIANTES SET NOMBRE='%s', CARRERA='%s', CONTRASEÑA='%s', MATERIAS='%s' WHERE CODIGO='%s'"%(nombre.get(),eleccion.get(),contraseña.get(),materias.get(),int(Id.get())))
					conexion.commit()
					cursor.close()
					conexion.close()
					messagebox.showinfo('Editado correctamente', 'Profesor editado correctamente')
					vEditarEstudiante.destroy()
					estudiantes()
				else:
					messagebox.askretrycancel('ID incorrecta','Por favor verifique que la ID exista')

			vEditarEstudiante = Tk()
			vEditarEstudiante.title('Editar Estudiante')
			vEditarEstudiante.config(bg='AliceBlue')
			nombre = StringVar()
			apellido = StringVar()
			contraseña = StringVar()
			carrera = IntVar()
			eleccion =StringVar()
			materias = StringVar()
			Id=StringVar()
			global encontrar
			encontrar=False

			Label(vEditarEstudiante, text=' ', bg='AliceBlue').grid(row=0, column=0)
			Label(vEditarEstudiante, text='Ingrese la ID que desea editar', bg='AliceBlue').grid(row=1, column=0)
			Entry(vEditarEstudiante, width=20, textvariable=Id).grid(row=1,column=1)
			Button(vEditarEstudiante, text='Cargar', command=lambda:verificar()).grid(row=1,column=3)
			Label(vEditarEstudiante, text='Nombre', bg='AliceBlue').grid(row=2, column=0)
			Entry(vEditarEstudiante,width=20,textvariable=nombre).grid(row=2, column=1)
			Label(vEditarEstudiante, text= 'Contraseña', bg='AliceBlue').grid(row=3, column=0)
			Entry(vEditarEstudiante, width=20, textvariable=contraseña).grid(row=3,column=1)
			Label(vEditarEstudiante, text='Seleccione la carrera del estudiante',bg='AliceBlue').grid(row=2,column=3)
			Radiobutton(vEditarEstudiante,text='Ingeneria Electronica',variable=carrera,value=1, bg='AliceBlue').grid(row=3,column=3)
			Radiobutton(vEditarEstudiante,text='Ingeneria Electrica',variable=carrera,value=2, bg='AliceBlue').grid(row=4,column=3)
			Radiobutton(vEditarEstudiante,text='Ingeneria Quimica',variable=carrera,value=3, bg='AliceBlue').grid(row=5,column=3)
			Radiobutton(vEditarEstudiante,text='Ingeneria Civil',variable=carrera,value=4, bg='AliceBlue').grid(row=6,column=3)
			Radiobutton(vEditarEstudiante,text='Ingeneria Industrial',variable=carrera,value=5, bg='AliceBlue').grid(row=7,column=3)
			Button(vEditarEstudiante, text='Guardar', command=lambda:(guardar())).grid(row=8, column=2,columnspan=2)
			Button(vEditarEstudiante, text='Volver', command=lambda:(vEditarEstudiante.destroy(), estudiantes())).grid(row=8, column=0,columnspan=2)

			vEditarEstudiante.mainloop()


		vEstudiante=Tk()
		vEstudiante.title('Estudiantes')
		vEstudiante.config(bg='AliceBlue')

		conexion = sqlite3.connect('Base_total')
		cursor = conexion.cursor()
		cursor.execute("""CREATE TABLE IF NOT EXISTS ESTUDIANTES (CODIGO INTEGER PRIMARY KEY AUTOINCREMENT,
						NOMBRE VARCHAR,
						CARRERA VARCHAR,
						CONTRASEÑA VARCHAR,
						VOTO INTEGER,
						MATERIAS VARCHAR,
						MATERIASINGRESADA INTEGER)""")
		cursor.close()
		conexion.close()

		Id=Text(vEstudiante,width=10, height=15, state='disabled')
		n=Text(vEstudiante,width=20, height=15, state='disabled')
		ca=Text(vEstudiante,width=25, height=15, state='disabled')
		c=Text(vEstudiante,width=10, height=15, state='disabled')

		Label(vEstudiante, text='ID', bg='AliceBlue').grid(row=0,column=0)
		Label(vEstudiante, text='Nombre', bg='AliceBlue').grid(row=0,column=1)
		Label(vEstudiante, text='Carrera', bg='AliceBlue').grid(row=0,column=2)
		Label(vEstudiante, text='Contraseña', bg='AliceBlue').grid(row=0,column=4)

		Id.grid(row=1,column=0)
		n.grid(row=1,column=1)
		ca.grid(row=1,column=2)
		c.grid(row=1,column=4)

		Button(vEstudiante, text='Crear estudiante', command=lambda:(vEstudiante.destroy(),crearEstudiante())).grid(row=2, column=0)
		Button(vEstudiante, text='Editar estudiante', command= lambda:(vEstudiante.destroy(),editarEstudiante())).grid(row=2,column=1)
		Button(vEstudiante, text='volver',command=lambda:( vEstudiante.destroy(), administrativo())).grid(row=2, column=4)
		cargar()
		vEstudiante.mainloop()

	def cargarAdmi():
		conexion = sqlite3.connect('Base_total')
		cursor = conexion.cursor()
		cursor.execute("SELECT * FROM PROFESORES")
		lista_profesores=(len(cursor.fetchall()))
		cursor.execute("SELECT * FROM ESTUDIANTES")
		lista_estudiantes=(len(cursor.fetchall()))
		cursor.execute("SELECT * FROM ADMINISTRATIVO")
		lista_administrativo=(len(cursor.fetchall()))
		cursor.close()
		conexion.close()
		Label(vadministrativo, text=lista_profesores, bg='AliceBlue').grid(row=2, column=3)
		Label(vadministrativo, text=lista_estudiantes, bg='AliceBlue').grid(row=3, column=3)
		Label(vadministrativo, text=lista_administrativo, bg='AliceBlue').grid(row=4, column=3)

	def administradores():
		def cargar():
			conexion=sqlite3.connect('Base_total')
			cursor=conexion.cursor()
			cursor.execute("SELECT * FROM ADMINISTRATIVO")
			lista_administrativo=cursor.fetchall()
			cursor.close()
			conexion.close()
			ID.config(state='normal')
			s.config(state='normal')
			c.config(state='normal')

			for i in lista_administrativo:
				ID.insert(INSERT, i[0])
				ID.insert(INSERT, '\n')
				s.insert(INSERT, i[1]+'\n')
				c.insert(INSERT, i[2]+'\n')

			ID.config(state='disabled')
			s.config(state='disabled')
			c.config(state='disabled')

		def crearAdministrador():
			def verificarA():
				if len(usuario.get())>0 and len(contraseña.get())>0:
					guardar()
				else:
					messagebox.showinfo('Error', 'Por favor llene las casillas')
					crearAdmi.destroy()
					crearAdministrador()

			def guardar():
				conexion=sqlite3.connect('Base_total')
				cursor=conexion.cursor()
				cursor.execute("INSERT INTO ADMINISTRATIVO VALUES(NULL,?,?)",(usuario.get(), contraseña.get()))
				conexion.commit()
				cursor.close()
				conexion.close()
				messagebox.showinfo('Administrador', 'Administrador creado correctamete.')
				crearAdmi.destroy()
				administradores()

			crearAdmi=Tk()
			crearAdmi.title('Crear Administrador')
			crearAdmi.config(bg='AliceBlue')
			usuario=StringVar()
			contraseña=StringVar()

			Label(crearAdmi, text='Por favor ingrese los datos para crear el administrador',bg='AliceBlue').grid(row=1,column=0, columnspan=3,padx=5,pady=5)
			Label(crearAdmi, text="Usuario:",bg='AliceBlue').grid(row=2,column=0,padx=5,pady=5)
			Entry(crearAdmi, textvariable=usuario).grid(row=2, column=1,padx=5,pady=5)
			Label(crearAdmi, text="Contraseña: ",bg='AliceBlue').grid(row=3, column=0,padx=5,pady=5)
			Entry(crearAdmi, textvariable=contraseña).grid(row=3, column=1)
			Button(crearAdmi, text='Guardar', command=lambda:verificarA()).grid(row=4, column=2, columnspan=2,padx=5,pady=5)
			Button(crearAdmi, text='Volver', command=lambda:(crearAdmi.destroy(), administradores())).grid(row=4, column=0, columnspan=2,padx=5,pady=5)

			crearAdmi.mainloop()

		def editarAdmi():
			def cargar():
				pass
			
			def verificarA():
				pass

			editarAdministrador=Tk()
			editarAdministrador.title('Crear Administrador')
			editarAdministrador.config(bg='AliceBlue')
			ID=StringVar()
			usuario=StringVar()
			contraseña=StringVar()

			Label(editarAdministrador, text='Ingrese la ID del administrador a editar:').grid(row=0, column=0)
			Entry(editarAdministrador, textvariable=ID).grid(row=0, column=1)
			Button(editarAdministrador, text='Cargar', command=lambda:cargar()).grid(row=0, column=2)
			Label(editarAdministrador, text='Por favor ingrese los datos una vez ingresada la ID administrador',bg='AliceBlue').grid(row=1,column=0, columnspan=3,padx=5,pady=5)
			Label(editarAdministrador, text="Usuario:",bg='AliceBlue').grid(row=2,column=0,padx=5,pady=5)
			Entry(editarAdministrador, textvariable=usuario).grid(row=2, column=1,padx=5,pady=5)
			Label(editarAdministrador, text="Contraseña: ",bg='AliceBlue').grid(row=3, column=0,padx=5,pady=5)
			Entry(editarAdministrador, textvariable=contraseña).grid(row=3, column=1)
			Button(editarAdministrador, text='Guardar', command=lambda:verificarA()).grid(row=4, column=2, columnspan=3,padx=5,pady=5)
			Button(editarAdministrador, text='Volver', command=lambda:(editarAdministrador.destroy(), administradores())).grid(row=4, column=0,padx=5,pady=5)

			editarAdministrador.mainloop()


		vAdministradores=Tk()
		vAdministradores.title('Administradores')
		vAdministradores.config(bg='AliceBlue')

		ID=Text(vAdministradores, width=15, height=15, state='disabled')
		s=Text(vAdministradores,width=15, height=15, state='disabled')
		c=Text(vAdministradores,width=15, height=15, state='disabled')

		Label(vAdministradores, text='ID', bg='AliceBlue').grid(row=0,column=1)
		Label(vAdministradores, text='Usuario', bg='AliceBlue').grid(row=0,column=1)
		Label(vAdministradores, text='Contraseña', bg='AliceBlue').grid(row=0,column=2)

		ID.grid(row=1, column=0)
		s.grid(row=1,column=1)
		c.grid(row=1,column=2)

		Button(vAdministradores, text='Crear administrador', command=lambda:(vAdministradores.destroy(),crearAdministrador())).grid(row=2, column=0)
		Button(vAdministradores, text='Editar administrador', command= lambda:(vAdministradores.destroy(),editarAdmi())).grid(row=2,column=1)
		Button(vAdministradores, text='volver',command=lambda:( vAdministradores.destroy(),administrativo())).grid(row=2, column=4)

		cargar()
		vAdministradores.mainloop()

	def CargarMaterias():
		conexion = sqlite3.connect('Base_total')
		cursor = conexion.cursor()
		cursor.execute("""CREATE TABLE IF NOT EXISTS ESTUDIANTES (CODIGO INTEGER PRIMARY KEY AUTOINCREMENT,
					NOMBRE VARCHAR,
					CARRERA VARCHAR,
					CONTRASEÑA VARCHAR,
					VOTO INTEGER,
					MATERIAS VARCHAR,
					MATERIASINGRESADA INTEGER)""")
		cursor.close()
		conexion.close()

		conexion = sqlite3.connect('Base_total')
		cursor = conexion.cursor()
		cursor.execute("SELECT * FROM ESTUDIANTES WHERE MATERIASINGRESADA=0")
		IngresarMaterias=cursor.fetchall()
		cursor.close()
		conexion.close()

		conexion = sqlite3.connect('Base_total')
		cursor = conexion.cursor()
		cursor.execute("""CREATE TABLE IF NOT EXISTS NOTAS (CODIGON INTEGER ,
					NOMBRE VARCHAR,
					CARRERA VARCHAR,
					SABER VARCHAR,
					SABERHACER INTEGER,
					SER VARCHAR,
					MATERIAQ)""")
		cursor.close()
		conexion.close()

		for i in IngresarMaterias:
			print(i)
			if i[6]==0:
				#calculo 1&ingles&quimica =materiaselct=['caluclo 1', 'quimica', ingles']
				MateriaSelect=i[5].split("&")

				for k in range(len(MateriaSelect)):	
					conexion = sqlite3.connect('Base_total')
					cursor = conexion.cursor()
					cursor.execute("INSERT INTO NOTAS VALUES(?,?,?,0,0,0,?)",(i[0],i[1],i[2],MateriaSelect[k]))
					conexion.commit()
					cursor.close()
					conexion.close()

				conexion = sqlite3.connect('Base_total')
				cursor = conexion.cursor()
				cursor.execute("UPDATE ESTUDIANTES SET MATERIASINGRESADA=1 WHERE CODIGO='%s'"%(i[0]))
				conexion.commit()
				cursor.close()
				conexion.close()

	def matricula():
		def fmenu():
			ventana=tkinter.Tk()
			ventana.geometry("920x698+0+0")
			ventana.title("Menu de matricula")
			fondo=PhotoImage(file="menus.PNG")
			Label(ventana,image=fondo).place(x=0,y=0)
			#main_title=Label(text="BIENVENIDO", font=(20),bg='#56cd63',width="250",fg='white',height='2')
			#Botones GUARDAR, EDITAR, SALIR, NUEVO,
			bedita=Button(ventana, text='EDITAR',command=lambda:feditar(),font=('Agency FB',28),width="30",bg='ivory3').place(x=350, y=312)
			bnuevoo=Button(ventana, text='NUEVO',command=lambda: fnuevo(),font=('Agency FB',28),width="30",bg='ivory3').place(x=350, y=145)
			bsalirr=Button(ventana, text='SALIR',command=lambda:(ventana.destroy(), administrativo()),font=('Agency FB',28),width="30",bg='ivory3').place(x=350, y=486)
			ventana.mainloop()

		def fnuevo():
			vnuevo=Toplevel()
			vnuevo.geometry("1350x690+0+0")
			vnuevo.title("Menu de matricula")
			vnuevo.configure(bg='light gray')
			Label(vnuevo, text='',bg='light gray').grid(row=1, column=0 )
			Label(vnuevo, text='',bg='light gray').grid(row=2, column=0 )
			Label(vnuevo, text='',bg='light gray').grid(row=3, column=0 )
			Label(vnuevo, text='',bg='light gray').grid(row=4, column=0 )
			Label(vnuevo, text='',bg='light gray').grid(row=5, column=0 )
			Label(vnuevo, text='              ',bg='light gray').grid(row=6, column=1 )
			Label(vnuevo, text='              ',bg='light gray').grid(row=7, column=1 )
			Label(vnuevo, text='              ',bg='light gray').grid(row=8, column=1)
			Label(vnuevo, text='',bg='light gray').grid(row=10, column=0 )
			Label(vnuevo, text='',bg='light gray').grid(row=11, column=0 )
			Label(vnuevo, text='',bg='light gray').grid(row=12, column=0 )
			Label(vnuevo, text='',bg='light gray').grid(row=13, column=1 )
			Label(vnuevo, text='',bg='light gray').grid(row=14, column=1 )
			Label(vnuevo, text='',bg='light gray').grid(row=15, column=1 )
			Label(vnuevo, text='',bg='light gray').grid(row=16, column=1 )
			Label(vnuevo, text='',bg='light gray').grid(row=17, column=1 )
			Label(vnuevo, text='',bg='light gray').grid(row=18, column=1 )
			Label(vnuevo, text='',bg='light gray').grid(row=19, column=1)
			Label(vnuevo, text=' DATOS  ',font=('Vineta BT',15),bg='light gray',fg='dodger blue').grid(row=4, column=4 )
			Label(vnuevo, text='DE   EST', font=('Vineta BT', 15),bg='light gray',fg='dodger blue').grid(row=4, column=5)
			Label(vnuevo, text='UDIANTE', font=('Vineta BT', 15),bg='light gray',fg='dodger blue').grid(row=4, column=6)
			Label(vnuevo, text='Grado entrante: ',font=(15),bg='light gray',fg='dodger blue').grid(row=6, column= 2)
			grado=Entry(vnuevo)
			grado.focus()
			grado.grid(row=6, column=3)
			Label(vnuevo, text='Primer nombre: ',font=(15),bg='light gray',fg='dodger blue').grid(row=7, column= 2)
			nombre = Entry(vnuevo)
			nombre.focus()
			nombre.grid(row=7, column=3)
			#Entrada nomre2
			Label(vnuevo, text='Segundo nombre: ',font=(15),bg='light gray',fg='dodger blue').grid(row=7, column=4 )
			nombre1 = Entry(vnuevo)
			nombre1.grid(row=7, column=5)
			#Entrada de apellido1
			Label(vnuevo, text= 'Primer apellido: ',font=(15),bg='light gray',fg='dodger blue').grid(row=7, column=6)
			apellido=Entry(vnuevo)
			apellido.grid(row=7, column=7)
			#Entrada de apellido2
			Label(vnuevo, text= 'Segundo apellido: ',font=(15),bg='light gray',fg='dodger blue').grid(row=7, column=8)
			apellido1=Entry(vnuevo)
			apellido1.grid(row=7, column=9)
			#Entrada de identidad
			Label(vnuevo, text='Doc. id: ',font=(15),bg='light gray',fg='dodger blue').grid(row=8,column=2)
			did=StringVar()
			combo=ttk.Combobox(vnuevo,textvariable=did)
			combo.grid(row=8,column=3)
			#combo.current(1)
			combo['values']=['R.C','T.I','C.C','C.E']
			Label(vnuevo, text='Numero de identidad: ',font=(15),bg='light gray',fg='dodger blue').grid(row=8,column=4)
			identidad=Entry(vnuevo)
			identidad.grid(row=8,column=5)
			Label(vnuevo, text='Genero: ',font=(15),bg='light gray',fg='dodger blue').grid(row=8,column=6)
			genero=Entry(vnuevo)
			genero.grid(row=8,column=7)
			Label(vnuevo, text='RH : ', font=(15),bg='light gray',fg='dodger blue').grid(row=8, column=8)
			rh = Entry(vnuevo)
			rh.grid(row=8, column=9)
			#Entradad fecha de nacimiento
			Label(vnuevo, text='Fecha de nacimiento: ',font=(15),bg='light gray',fg='dodger blue').grid(row=9,column=2)
			fecha=Entry(vnuevo)
			fecha.grid(row=9,column=3)
			Label(vnuevo, text='Edad : ',font=(15),bg='light gray',fg='dodger blue').grid(row=9, column=4)
			edad=Entry(vnuevo)
			edad.grid(row=9,column=5)
			Label(vnuevo, text='Salud : ', font=(15),bg='light gray',fg='dodger blue').grid(row=9, column=6)
			salud = StringVar()
			combo2 = ttk.Combobox(vnuevo, textvariable=salud)
			combo2.grid(row=9, column=7)
			combo2['values'] = ('EPS', 'SISBEN', 'ARL')
			# combo2.current(0)
			tsalud = Entry(vnuevo)
			tsalud.grid(row=9, column=8)
			#Entrada de ciudad
			Label(vnuevo, text='Ciudad: ',font=(15),bg='light gray',fg='dodger blue').grid(row=10,column=2)
			ciudad=Entry(vnuevo)
			ciudad.grid(row=10,column=3)
			Label(vnuevo, text='Direccion: ',font=(15),bg='light gray',fg='dodger blue').grid(row=10,column=4)
			direccion=Entry(vnuevo)
			direccion.grid(row=10,column=5)
			Label(vnuevo, text='Correo electronico: ',font=(15),bg='light gray',fg='dodger blue').grid(row=11,column=2)
			correo1=Entry(vnuevo)
			correo1.grid(row=11,column=3)
			Label(vnuevo, text='Telefono: ',font=(15),bg='light gray',fg='dodger blue').grid(row=11,column=4)
			telefono1=Entry(vnuevo)
			telefono1.grid(row=11,column=5)
			#Datos acudiente
			#Entada nombre1
			Label(vnuevo, text='  DATOS ', font=('Vineta BT', 15),bg='light gray',fg='dodger blue').grid(row=16, column=4)
			Label(vnuevo, text='  DE    AC', font=('Vineta BT', 15),bg='light gray',fg='dodger blue').grid(row=16, column=5)
			Label(vnuevo, text='UDIENTE', font=('Vineta BT', 15),bg='light gray',fg='dodger blue').grid(row=16, column=6)
			Label(vnuevo, text='Primer nombre: ',font=(15),bg='light gray',fg='dodger blue').grid(row=19, column= 2)
			nombrea = Entry(vnuevo)
			nombrea.focus()
			nombrea.grid(row=19, column=3)
     		#Entrada nomre2
			Label(vnuevo, text='Segundo nombre: ',font=(15),bg='light gray',fg='dodger blue').grid(row=19, column=4 )
			nombre1a = Entry(vnuevo)
			nombre1a.grid(row=19, column=5)
			#Entrada de apellido1
			Label(vnuevo, text= 'Primer apellido: ',font=(15),bg='light gray',fg='dodger blue').grid(row=19, column=6)
			apellidoa=Entry(vnuevo)
			apellidoa.grid(row=19, column=7)
			#Entrada de apellido2
			Label(vnuevo, text= 'Segundo apellido: ',font=(15),bg='light gray',fg='dodger blue').grid(row=19, column=8)
			apellido1a=Entry(vnuevo)
			apellido1a.grid(row=19, column=9)
			Label(vnuevo, text= 'Parentesco: ',font=(15),bg='light gray',fg='dodger blue').grid(row=20, column=2)
			parentesco=Entry(vnuevo)
			parentesco.grid(row=20, column=3)
			Label(vnuevo, text= 'Ocupacion: ',font=(15),bg='light gray',fg='dodger blue').grid(row=20, column=4)
			ocupacion=Entry(vnuevo)
			ocupacion.grid(row=20, column=5)
			Label(vnuevo, text='Ciudad: ',font=(15),bg='light gray',fg='dodger blue').grid(row=20,column=6)
			ciudad2=Entry(vnuevo)
			ciudad2.grid(row=20,column=7)
			Label(vnuevo, text='Direccion: ',font=(15),bg='light gray',fg='dodger blue').grid(row=20,column=8)
			direccion2=Entry(vnuevo)
			direccion2.grid(row=20,column=9)
			Label(vnuevo, text='Correo electronico: ',font=(15),bg='light gray',fg='dodger blue').grid(row=21,column=2)
			correo2=Entry(vnuevo)
			correo2.grid(row=21,column=3)
			Label(vnuevo, text='Telefono: ',font=(15),bg='light gray',fg='dodger blue').grid(row=21,column=4)
			telefono2=Entry(vnuevo)
			telefono2.grid(row=21,column=5)
			did2 = StringVar()
			Label(vnuevo, text='Doc. id: ', font=(15),bg='light gray',fg='dodger blue').grid(row=21, column=6)
			combo3 = ttk.Combobox(vnuevo, textvariable=did2)
			combo3.grid(row=21, column=7)
			# combo.current(1)
			combo3['values'] = [ 'C.C', 'C.E']
			Label(vnuevo, text='Numero de identidad: ', font=(15),bg='light gray',fg='dodger blue').grid(row=21, column=8)
			identidad2 = Entry(vnuevo)
			identidad2.grid(row=21, column=9)
			#Boton guardar
			#ttk.Button(ventana1,text='Guardar').grid(row=7,column=4, sticky = W+E)
			guardar=Button(vnuevo, text='GUARDAR',command=lambda:fguardar(vnuevo,grado,nombre,apellido,nombre1,apellido1,did.get(),identidad,genero,fecha,edad,rh,ciudad,direccion,salud.get(),tsalud,correo1,telefono1,nombrea,apellidoa,nombre1a,apellido1a,parentesco,ocupacion,ciudad2,direccion2,correo2,telefono2,did2.get(),identidad2),font=(15),bg='dodger blue',width="30",fg='white',height='2').place(x=500, y=600)

		def feditar():
			ventedit=Tk()
			ventedit.geometry("1350x250+0+0")
			ventedit.title("Editar informacion")
			Label(ventedit, text=' EDITAR DATOS DE ESTUDIANTE ', font=('Vineta BT', 15)).grid(row=0, column=0)
			#fonnuevo=tk.PhotoImage(file="editar.PNG")
			#f=Label(ventedit,image=fonnuevo)
			#f.place(x=0,y=0)
			Label(ventedit, text='Ingrese grado: ',font=(60)).grid(row=3, column=2,ipadx=5,ipady=5)
			busgrado = Entry(ventedit,width=30)
			busgrado.focus()
			busgrado.grid(row=3, column=3,padx=10, pady=10,ipadx=3,ipady=3)
			Label(ventedit, text='Ingrese documento de identidad: ', font=(60)).grid(row=4, column=2, ipadx=3, ipady=3)
			buscar = Entry(ventedit, width=30)
			buscar.grid(row=4, column=3, padx=10, pady=10, ipadx=3, ipady=3)
			bbuscar=Button(ventedit, text='Buscar',command=lambda:fmostrar(ventedit,buscar,busgrado),font=(30),bg='#56cd63',width="25",fg='white',height='1')
			bbuscar.grid(row=5, column=2,ipadx=3,ipady=3)

		def feliminar(borrar,buscgrado,busqueda):
			#egrado=buscgrado.get
   			 #elim=busqueda.get
			ruloz = sqlite3.connect("matriculas.db")
			cursor = ruloz.cursor()
			if buscgrado == '1':
				mb=messagebox.askyesno('CONFIRMAR', message='¿ESTA SEGURO DE ELIMINAR ESTE CONTACTO?')
				if mb==True:
					cursor.execute("DELETE FROM ESTUDIANTES_1  WHERE identidad='%s'" % (busqueda))
					borrar.destroy
			elif buscgrado=='2':
				mb = messagebox.askyesno('CONFIRMAR', message='¿ESTA SEGURO DE ELIMINAR ESTE CONTACTO?')
				if mb == True:
					cursor.execute("DELETE FROM ESTUDIANTES_2  WHERE identidad='%s'" % (busqueda))
					borrar.destroy
			elif buscgrado=='3':
				mb = messagebox.askyesno('CONFIRMAR', message='¿ESTA SEGURO DE ELIMINAR ESTE CONTACTO?')
				if mb == True:
					cursor.execute("DELETE FROM ESTUDIANTES_3  WHERE identidad='%s'" % (busqueda))
					borrar.destroy
			elif buscgrado=='4':
				mb = messagebox.askyesno('CONFIRMAR', message='¿ESTA SEGURO DE ELIMINAR ESTE CONTACTO?')
				if mb == True:
					cursor.execute("DELETE FROM ESTUDIANTES_4  WHERE identidad='%s'" % (busqueda))
					borrar.destroy
			elif buscgrado=='5':
				mb = messagebox.askyesno('CONFIRMAR', message='¿ESTA SEGURO DE ELIMINAR ESTE CONTACTO?')
				if mb == True:
					cursor.execute("DELETE FROM ESTUDIANTES_5  WHERE identidad='%s'" % (busqueda))
					borrar.destroy
			elif buscgrado=='6':
				mb = messagebox.askyesno('CONFIRMAR', message='¿ESTA SEGURO DE ELIMINAR ESTE CONTACTO?')
				if mb == True:
					cursor.execute("DELETE FROM ESTUDIANTES_6  WHERE identidad='%s'" % (busqueda))
					borrar.destroy
			elif buscgrado=='7':
				mb = messagebox.askyesno('CONFIRMAR', message='¿ESTA SEGURO DE ELIMINAR ESTE CONTACTO?')
				if mb == True:
					cursor.execute("DELETE FROM ESTUDIANTES_7  WHERE identidad='%s'" % (busqueda))
					borrar.destroy
			elif buscgrado=='8':
				mb = messagebox.askyesno('CONFIRMAR', message='¿ESTA SEGURO DE ELIMINAR ESTE CONTACTO?')
				if mb == True:
					cursor.execute("DELETE FROM ESTUDIANTES_8  WHERE identidad='%s'" % (busqueda))
					borrar.destroy
			elif buscgrado=='9':
				mb = messagebox.askyesno('CONFIRMAR', message='¿ESTA SEGURO DE ELIMINAR ESTE CONTACTO?')
				if mb == True:
					cursor.execute("DELETE FROM ESTUDIANTES_9  WHERE identidad='%s'" % (busqueda))
					borrar.destroy
			elif buscgrado=='10':
				mb = messagebox.askyesno('CONFIRMAR', message='¿ESTA SEGURO DE ELIMINAR ESTE CONTACTO?')
				if mb == True:
					cursor.execute("DELETE FROM ESTUDIANTES_10  WHERE identidad='%s'" % (busqueda))
					borrar.destroy
			elif buscgrado=='11':
				mb = messagebox.askyesno('CONFIRMAR', message='¿ESTA SEGURO DE ELIMINAR ESTE CONTACTO?')
				if mb == True:
					cursor.execute("DELETE FROM ESTUDIANTES_11  WHERE identidad='%s'" % (busqueda))
					borrar.destroy
			ruloz.commit()
			cursor.close()

		def fguardar(vcerrar,grado,nombre,apellido,nombre1,apellido1,did,identidad,genero,fecha,edad,rh,ciudad,direccion,salud,tsalud,correo1,telefono1,nombrea,apellidoa,nombre1a,apellido1a,parentesco,ocupacion,ciudad2,direccion2,correo2,telefono2,did2,identidad2):
			gra=grado.get()
			n=nombre.get()
			n1=nombre1.get()
			a=apellido.get()
			a1=apellido1.get()
			iden=identidad.get()
			ge=genero.get()
			fe=fecha.get()
			ed=edad.get()
			rhh=rh.get()
			c=ciudad.get()
			direc=direccion.get()
			tsa=tsalud.get()
			co1=correo1.get()
			t1=telefono1.get()
			na=nombrea.get()
			apa=apellidoa.get()
			n1a=nombre1a.get()
			ap1a=apellido1a.get()
			paren=parentesco.get()
			ocup=ocupacion.get()
			c2=ciudad2.get()
			direc2=direccion2.get()
			co2=correo2.get()
			t2=telefono2.get()
			iden2=identidad2.get()
			if gra=='1':
				ruloz = sqlite3.connect("matriculas.db")
				cursor = ruloz.cursor()
				cursor.execute("SELECT identidad FROM ESTUDIANTES_1 WHERE identidad = '%s'" % (iden))
				y = cursor.fetchall()
				yy = 0
				for i in y:
					yy = i[0]
				if int(yy) != int(iden):
					valores = (n, a, n1, a1, did, iden, ge, fe, ed, rhh, c, direc, salud, tsa, co1, t1, na, n1a, apa, ap1a, paren, ocup,c2, direc2, co2, t2, did2, iden2)
					cursor.execute("INSERT INTO ESTUDIANTES_1 (nombre,nombre2,apellido,apellido2,doc_id,identidad,genero,fecha_nacimiento,edad,rh,ciudad,direccion,salud,entidad,correo,telefono,acudiente,nombre2a,apellidoa,apellido2a,parentesco,ocupacion,ciudad2,direccion2,correo2,telefono2,doc_id2,identidad2)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (valores))
					messagebox.showinfo('GUARDAR', message='DATOS GUARDADOS CON EXITO')
				else:
					messagebox.showerror('ERROR', message='  YA EXISTE ESE NUMERO DE IDENTIDAD ')
				ruloz.commit()
				cursor.close()
				vcerrar.destroy()
			elif gra=='2':
				ruloz = sqlite3.connect("matriculas.db")
				cursor = ruloz.cursor()
				cursor.execute("SELECT identidad FROM ESTUDIANTES_2 WHERE identidad = '%s'" % (iden))
				y = cursor.fetchall()
				yy = 0
				for i in y:
					yy = i[0]
				if int(yy) != int(iden):
					valores = (n, a, n1, a1, did, iden, ge, fe, ed, rhh, c, direc, salud, tsa, co1, t1, na, n1a, apa, ap1a, paren, ocup,c2, direc2, co2, t2, did2, iden2)
					cursor.execute("INSERT INTO ESTUDIANTES_2 (nombre,nombre2,apellido,apellido2,doc_id,identidad,genero,fecha_nacimiento,edad,rh,ciudad,direccion,salud,entidad,correo,telefono,acudiente,nombre2a,apellidoa,apellido2a,parentesco,ocupacion,ciudad2,direccion2,correo2,telefono2,doc_id2,identidad2)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (valores))
					messagebox.showinfo('GUARDAR', message='DATOS GUARDADOS CON EXITO')
				else:
					messagebox.showerror('ERROR', message='  YA EXISTE ESE NUMERO DE IDENTIDAD ')
				ruloz.commit()
				cursor.close()
				vcerrar.destroy()
			elif gra=='3':
				ruloz = sqlite3.connect("matriculas.db")
				cursor = ruloz.cursor()
				cursor.execute("SELECT identidad FROM ESTUDIANTES_3 WHERE identidad = '%s'" % (iden))
				y = cursor.fetchall()
				yy = 0
				for i in y:
					yy = i[0]
				if int(yy) != int(iden):
					valores = (n, a, n1, a1, did, iden, ge, fe, ed, rhh, c, direc, salud, tsa, co1, t1, na, n1a, apa, ap1a, paren, ocup,c2, direc2, co2, t2, did2, iden2)
					cursor.execute("INSERT INTO ESTUDIANTES_3 (nombre,nombre2,apellido,apellido2,doc_id,identidad,genero,fecha_nacimiento,edad,rh,ciudad,direccion,salud,entidad,correo,telefono,acudiente,nombre2a,apellidoa,apellido2a,parentesco,ocupacion,ciudad2,direccion2,correo2,telefono2,doc_id2,identidad2)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (valores))
					messagebox.showinfo('GUARDAR', message='DATOS GUARDADOS CON EXITO')
				else:
					messagebox.showerror('ERROR', message='  YA EXISTE ESE NUMERO DE IDENTIDAD ')
				ruloz.commit()
				cursor.close()
				vcerrar.destroy()
			elif gra=='4':
				ruloz = sqlite3.connect("matriculas.db")
				cursor = ruloz.cursor()
				cursor.execute("SELECT identidad FROM ESTUDIANTES_3 WHERE identidad = '%s'" % (iden))
				y = cursor.fetchall()
				yy = 0
				for i in y:
					yy = i[0]
				if int(yy) != int(iden):
					valores = (n, a, n1, a1, did, iden, ge, fe, ed, rhh, c, direc, salud, tsa, co1, t1, na, n1a, apa, ap1a, paren, ocup,c2, direc2, co2, t2, did2, iden2)
					cursor.execute("INSERT INTO ESTUDIANTES_3 (nombre,nombre2,apellido,apellido2,doc_id,identidad,genero,fecha_nacimiento,edad,rh,ciudad,direccion,salud,entidad,correo,telefono,acudiente,nombre2a,apellidoa,apellido2a,parentesco,ocupacion,ciudad2,direccion2,correo2,telefono2,doc_id2,identidad2)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (valores))
					messagebox.showinfo('GUARDAR', message='DATOS GUARDADOS CON EXITO')
				else:
					messagebox.showerror('ERROR', message='  YA EXISTE ESE NUMERO DE IDENTIDAD ')
				ruloz.commit()
				cursor.close()
				vcerrar.destroy()
			elif gra=='5':
				ruloz = sqlite3.connect("matriculas.db")
				cursor = ruloz.cursor()
				cursor.execute("SELECT identidad FROM ESTUDIANTES_3 WHERE identidad = '%s'" % (iden))
				y = cursor.fetchall()
				yy = 0
				for i in y:
					yy = i[0]
				if int(yy) != int(iden):
					valores = (n, a, n1, a1, did, iden, ge, fe, ed, rhh, c, direc, salud, tsa, co1, t1, na, n1a, apa, ap1a, paren, ocup,c2, direc2, co2, t2, did2, iden2)
					cursor.execute("INSERT INTO ESTUDIANTES_3 (nombre,nombre2,apellido,apellido2,doc_id,identidad,genero,fecha_nacimiento,edad,rh,ciudad,direccion,salud,entidad,correo,telefono,acudiente,nombre2a,apellidoa,apellido2a,parentesco,ocupacion,ciudad2,direccion2,correo2,telefono2,doc_id2,identidad2)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (valores))
					messagebox.showinfo('GUARDAR', message='DATOS GUARDADOS CON EXITO')
				else:
					messagebox.showerror('ERROR', message='  YA EXISTE ESE NUMERO DE IDENTIDAD ')
				ruloz.commit()
				cursor.close()
				vcerrar.destroy()
			elif gra=='6':
				ruloz = sqlite3.connect("matriculas.db")
				cursor = ruloz.cursor()
				cursor.execute("SELECT identidad FROM ESTUDIANTES_3 WHERE identidad = '%s'" % (iden))
				y = cursor.fetchall()
				yy = 0
				for i in y:
					yy = i[0]
				if int(yy) != int(iden):
					valores = (n, a, n1, a1, did, iden, ge, fe, ed, rhh, c, direc, salud, tsa, co1, t1, na, n1a, apa, ap1a, paren, ocup,c2, direc2, co2, t2, did2, iden2)
					cursor.execute("INSERT INTO ESTUDIANTES_3 (nombre,nombre2,apellido,apellido2,doc_id,identidad,genero,fecha_nacimiento,edad,rh,ciudad,direccion,salud,entidad,correo,telefono,acudiente,nombre2a,apellidoa,apellido2a,parentesco,ocupacion,ciudad2,direccion2,correo2,telefono2,doc_id2,identidad2)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (valores))
					messagebox.showinfo('GUARDAR', message='DATOS GUARDADOS CON EXITO')
				else:
					messagebox.showerror('ERROR', message='  YA EXISTE ESE NUMERO DE IDENTIDAD ')
				ruloz.commit()
				cursor.close()
				vcerrar.destroy()
			elif gra=='7':
				ruloz = sqlite3.connect("matriculas.db")
				cursor = ruloz.cursor()
				cursor.execute("SELECT identidad FROM ESTUDIANTES_3 WHERE identidad = '%s'" % (iden))
				y = cursor.fetchall()
				yy = 0
				for i in y:
					yy = i[0]
				if int(yy) != int(iden):
					valores = (n, a, n1, a1, did, iden, ge, fe, ed, rhh, c, direc, salud, tsa, co1, t1, na, n1a, apa, ap1a, paren, ocup,c2, direc2, co2, t2, did2, iden2)
					cursor.execute("INSERT INTO ESTUDIANTES_3 (nombre,nombre2,apellido,apellido2,doc_id,identidad,genero,fecha_nacimiento,edad,rh,ciudad,direccion,salud,entidad,correo,telefono,acudiente,nombre2a,apellidoa,apellido2a,parentesco,ocupacion,ciudad2,direccion2,correo2,telefono2,doc_id2,identidad2)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (valores))
					messagebox.showinfo('GUARDAR', message='DATOS GUARDADOS CON EXITO')
				else:
					messagebox.showerror('ERROR', message='  YA EXISTE ESE NUMERO DE IDENTIDAD ')
				ruloz.commit()
				cursor.close()
				vcerrar.destroy()
			elif gra=='8':
				ruloz = sqlite3.connect("matriculas.db")
				cursor = ruloz.cursor()
				cursor.execute("SELECT identidad FROM ESTUDIANTES_3 WHERE identidad = '%s'" % (iden))
				y = cursor.fetchall()
				yy = 0
				for i in y:
					yy = i[0]
				if int(yy) != int(iden):
					valores = (n, a, n1, a1, did, iden, ge, fe, ed, rhh, c, direc, salud, tsa, co1, t1, na, n1a, apa, ap1a, paren, ocup,c2, direc2, co2, t2, did2, iden2)
					cursor.execute("INSERT INTO ESTUDIANTES_3 (nombre,nombre2,apellido,apellido2,doc_id,identidad,genero,fecha_nacimiento,edad,rh,ciudad,direccion,salud,entidad,correo,telefono,acudiente,nombre2a,apellidoa,apellido2a,parentesco,ocupacion,ciudad2,direccion2,correo2,telefono2,doc_id2,identidad2)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (valores))
					messagebox.showinfo('GUARDAR', message='DATOS GUARDADOS CON EXITO')
				else:
					messagebox.showerror('ERROR', message='  YA EXISTE ESE NUMERO DE IDENTIDAD ')
				ruloz.commit()
				cursor.close()
				vcerrar.destroy()
			elif gra=='9':
				ruloz = sqlite3.connect("matriculas.db")
				cursor = ruloz.cursor()
				cursor.execute("SELECT identidad FROM ESTUDIANTES_3 WHERE identidad = '%s'" % (iden))
				y = cursor.fetchall()
				yy = 0
				for i in y:
					yy = i[0]
				if int(yy) != int(iden):
					valores = (n, a, n1, a1, did, iden, ge, fe, ed, rhh, c, direc, salud, tsa, co1, t1, na, n1a, apa, ap1a, paren, ocup,c2, direc2, co2, t2, did2, iden2)
					cursor.execute("INSERT INTO ESTUDIANTES_3 (nombre,nombre2,apellido,apellido2,doc_id,identidad,genero,fecha_nacimiento,edad,rh,ciudad,direccion,salud,entidad,correo,telefono,acudiente,nombre2a,apellidoa,apellido2a,parentesco,ocupacion,ciudad2,direccion2,correo2,telefono2,doc_id2,identidad2)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (valores))
					messagebox.showinfo('GUARDAR', message='DATOS GUARDADOS CON EXITO')
				else:
					messagebox.showerror('ERROR', message='  YA EXISTE ESE NUMERO DE IDENTIDAD ')
				ruloz.commit()
				cursor.close()
				vcerrar.destroy()
			elif gra=='10':
				ruloz = sqlite3.connect("matriculas.db")
				cursor = ruloz.cursor()
				cursor.execute("SELECT identidad FROM ESTUDIANTES_3 WHERE identidad = '%s'" % (iden))
				y = cursor.fetchall()
				yy = 0
				for i in y:
					yy = i[0]
				if int(yy) != int(iden):
					valores = (n, a, n1, a1, did, iden, ge, fe, ed, rhh, c, direc, salud, tsa, co1, t1, na, n1a, apa, ap1a, paren, ocup,c2, direc2, co2, t2, did2, iden2)
					cursor.execute("INSERT INTO ESTUDIANTES_3 (nombre,nombre2,apellido,apellido2,doc_id,identidad,genero,fecha_nacimiento,edad,rh,ciudad,direccion,salud,entidad,correo,telefono,acudiente,nombre2a,apellidoa,apellido2a,parentesco,ocupacion,ciudad2,direccion2,correo2,telefono2,doc_id2,identidad2)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (valores))
					messagebox.showinfo('GUARDAR', message='DATOS GUARDADOS CON EXITO')
				else:
					messagebox.showerror('ERROR', message='  YA EXISTE ESE NUMERO DE IDENTIDAD ')
				ruloz.commit()
				cursor.close()
				vcerrar.destroy()
			elif gra=='11':
				ruloz = sqlite3.connect("matriculas.db")
				cursor = ruloz.cursor()
				cursor.execute("SELECT identidad FROM ESTUDIANTES_3 WHERE identidad = '%s'" % (iden))
				y = cursor.fetchall()
				yy = 0
				for i in y:
					yy = i[0]
				if int(yy) != int(iden):
					valores = (n, a, n1, a1, did, iden, ge, fe, ed, rhh, c, direc, salud, tsa, co1, t1, na, n1a, apa, ap1a, paren, ocup,c2, direc2, co2, t2, did2, iden2)
					cursor.execute("INSERT INTO ESTUDIANTES_3 (nombre,nombre2,apellido,apellido2,doc_id,identidad,genero,fecha_nacimiento,edad,rh,ciudad,direccion,salud,entidad,correo,telefono,acudiente,nombre2a,apellidoa,apellido2a,parentesco,ocupacion,ciudad2,direccion2,correo2,telefono2,doc_id2,identidad2)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (valores))
					messagebox.showinfo('GUARDAR', message='DATOS GUARDADOS CON EXITO')
				else:
					messagebox.showerror('ERROR', message='  YA EXISTE ESE NUMERO DE IDENTIDAD ')
				ruloz.commit()
				cursor.close()
				vcerrar.destroy()
			else:
				messagebox.showerror('ERROR', message='INGRESE UN GRADO EXISTENTE\n NO EXISTE GRADO')
			#nombre,nombre2,apellido,apellido2,doc_id,identidad,genero,fecha_nacimiento,edad,rh,ciudad,direccion,salud,entidad,correo,telefono,acudiente,nombre2a,apellidoa,apellido2a,parentesco,ocupacion,ciudad2,direccion2,correo2,telefono2
     		#'n,a,n1,a1,doid,iden,ge,d,m,añ,ed,rhh,c,direc,salud,tsa,co1,t1,na,n1a,apa,ap1a,paren,ocup,c2,direc2,co2,t2,did2,iden2'
     		#cursor.execute("INSERT INTO ESTUDIANTES VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",valores)
		def fmostrar(ventedit, buscar, busgrado):
			mn = ""
			mn1 = ""
			ma = ""
			ma1 = ""
			mdid = ""
			miden = ""
			mge = ""
			mfe = ""
			med = ""
			mrhh = ""
			mc = ""
			mdirec = ""
			msa = ""
			mtsa = ""
			mco1 = ""
			mt1 = ""
			mna = ""
			mapa = ""
			mn1a = ""
			map1a = ""
			mparen = ""
			mocup = ""
			mc2 = ""
			mdirec2 = ""
			mco2 = ""
			mt2 = ""
			mdid2 = ""
			miden2 = ""

			buscgrado = busgrado.get()
			busqueda = buscar.get()
			ruloz = sqlite3.connect("matriculas.db")
			cursor = ruloz.cursor()
			permi = 2
			if buscgrado == '1':
				cursor.execute("SELECT identidad FROM ESTUDIANTES_1 WHERE identidad = '%s'" % (busqueda))
				y = cursor.fetchall()
				yy = 0
				for i in y:
					yy = i[0]
				if int(yy) != int(busqueda) or yy == 0:
					messagebox.showerror('ERROR', message='NO EXISTE ESE NUMERO DE IDENTIDAD')
					permi = 1
				else:
					cursor.execute("SELECT * FROM ESTUDIANTES_1 WHERE identidad = '%s'" % (busqueda))
					permi = 0
			elif buscgrado == '2':
				cursor.execute("SELECT identidad FROM ESTUDIANTES_2 WHERE identidad = '%s'" % (busqueda))
				y = cursor.fetchall()
				yy = 0
				for i in y:
					yy = i[0]
				if yy != int(busqueda):
					messagebox.showerror('ERROR', message='NO EXISTE ESE NUMERO DE IDENTIDAD')
					permi = 1
				else:
					cursor.execute("SELECT * FROM ESTUDIANTES_2 WHERE identidad = '%s'" % (busqueda))
					permi = 0
			elif buscgrado == '3':
				cursor.execute("SELECT identidad FROM ESTUDIANTES_3 WHERE identidad = '%s'" % (busqueda))
				y = cursor.fetchall()
				yy = 0
				for i in y:
					yy = i[0]
				if yy != int(busqueda):
					messagebox.showerror('ERROR', message='NO EXISTE ESE NUMERO DE IDENTIDAD')
					permi = 1
				else:
					cursor.execute("SELECT * FROM ESTUDIANTES_3 WHERE identidad = '%s'" % (busqueda))
					permi = 0
			elif buscgrado == '4':
				cursor.execute("SELECT identidad FROM ESTUDIANTES_4 WHERE identidad = '%s'" % (busqueda))
				y = cursor.fetchall()
				yy = 0
				for i in y:
					yy = i[0]
				if yy != int(busqueda):
					messagebox.showerror('ERROR', message='NO EXISTE ESE NUMERO DE IDENTIDAD')
					permi = 1
				else:
					cursor.execute("SELECT * FROM ESTUDIANTES_4 WHERE identidad = '%s'" % (busqueda))
					permi = 0
			elif buscgrado == '5':
				cursor.execute("SELECT identidad FROM ESTUDIANTES_5 WHERE identidad = '%s'" % (busqueda))
				y = cursor.fetchall()
				yy = 0
				for i in y:
					yy = i[0]
				if yy != int(busqueda):
					messagebox.showerror('ERROR', message='NO EXISTE ESE NUMERO DE IDENTIDAD')
					permi = 1
				else:
					cursor.execute("SELECT * FROM ESTUDIANTES_5 WHERE identidad = '%s'" % (busqueda))
					permi = 0
			elif buscgrado == '6':
				cursor.execute("SELECT identidad FROM ESTUDIANTES_6 WHERE identidad = '%s'" % (busqueda))
				y = cursor.fetchall()
				yy = 0
				for i in y:
					yy = i[0]
				if yy != int(busqueda):
					messagebox.showerror('ERROR', message='NO EXISTE ESE NUMERO DE IDENTIDAD')
					permi = 1
				else:
					cursor.execute("SELECT * FROM ESTUDIANTES_6 WHERE identidad = '%s'" % (busqueda))
					permi = 0
			elif buscgrado == '7':
				cursor.execute("SELECT identidad FROM ESTUDIANTES_7 WHERE identidad = '%s'" % (busqueda))
				y = cursor.fetchall()
				yy = 0
				for i in y:
					yy = i[0]
				if yy != int(busqueda):
					messagebox.showerror('ERROR', message='NO EXISTE ESE NUMERO DE IDENTIDAD')
					permi = 1
				else:
					cursor.execute("SELECT * FROM ESTUDIANTES_7 WHERE identidad = '%s'" % (busqueda))
					permi = 0
			elif buscgrado == '8':
				cursor.execute("SELECT identidad FROM ESTUDIANTES_8 WHERE identidad = '%s'" % (busqueda))
				y = cursor.fetchall()
				yy = 0
				for i in y:
					yy = i[0]
				if yy != int(busqueda):
					messagebox.showerror('ERROR', message='NO EXISTE ESE NUMERO DE IDENTIDAD')
					permi = 1
				else:
					cursor.execute("SELECT * FROM ESTUDIANTES_8 WHERE identidad = '%s'" % (busqueda))
					permi = 0
			elif buscgrado == '9':
				cursor.execute("SELECT identidad FROM ESTUDIANTES_9 WHERE identidad = '%s'" % (busqueda))
				y = cursor.fetchall()
				yy = 0
				for i in y:
					yy = i[0]
				if yy != int(busqueda):
					messagebox.showerror('ERROR', message='NO EXISTE ESE NUMERO DE IDENTIDAD')
					permi = 1
				else:
					cursor.execute("SELECT * FROM ESTUDIANTES_9 WHERE identidad = '%s'" % (busqueda))
					permi = 0
			elif buscgrado == '10':
				cursor.execute("SELECT identidad FROM ESTUDIANTES_10 WHERE identidad = '%s'" % (busqueda))
				y = cursor.fetchall()
				yy = 0
				for i in y:
					yy = i[0]
				if yy != int(busqueda):
					messagebox.showerror('ERROR', message='NO EXISTE ESE NUMERO DE IDENTIDAD')
					permi = 1
				else:
					cursor.execute("SELECT * FROM ESTUDIANTES_10 WHERE identidad = '%s'" % (busqueda))
					permi = 0
			elif buscgrado == '11':
				cursor.execute("SELECT identidad FROM ESTUDIANTES_11 WHERE identidad = '%s'" % (busqueda))
				y = cursor.fetchall()
				yy = 0
				for i in y:
					yy = i[0]
				if yy != int(busqueda):
					messagebox.showerror('ERROR', message='NO EXISTE ESE NUMERO DE IDENTIDAD')
					permi = 1
				else:
					cursor.execute("SELECT * FROM ESTUDIANTES_11 WHERE identidad = '%s'" % (busqueda))
					permi = 0
			x = cursor.fetchall()
			if permi == 0:
				for i in x:
					mn = i[0]
					mn1 = i[1]
					ma = i[2]
					ma1 = i[3]
					mdid = i[4]
					miden = i[5]
					mge = i[6]
					mfe = i[7]
					med = i[8]
					mrhh = i[9]
					mc = i[10]
					mdirec = i[11]
					msa = i[12]
					mtsa = i[13]
					mco1 = i[14]
					mt1 = i[15]
					mna = i[16]
					mapa = i[17]
					mn1a = i[18]
					map1a = i[19]
					mparen = i[20]
					mocup = i[21]
					mc2 = i[22]
					mdirec2 = i[23]
					mco2 = i[24]
					mt2 = i[25]
					mdid2 = i[26]
					miden2 = i[27]
			cursor.close()
			if permi == 0:
				vnuevo = Toplevel()
				vnuevo.geometry("1350x690+0+0")
				vnuevo.title("Menu de matricula")
				vnuevo.configure(bg='light gray')
				Label(vnuevo, text='', bg='light gray').grid(row=1, column=0)
				Label(vnuevo, text='', bg='light gray').grid(row=2, column=0)
				Label(vnuevo, text='', bg='light gray').grid(row=3, column=0)
				Label(vnuevo, text='', bg='light gray').grid(row=4, column=0)
				Label(vnuevo, text='', bg='light gray').grid(row=5, column=0)
				Label(vnuevo, text='              ', bg='light gray').grid(row=6, column=1)
				Label(vnuevo, text='              ', bg='light gray').grid(row=7, column=1)
				Label(vnuevo, text='              ', bg='light gray').grid(row=8, column=1)
				Label(vnuevo, text='', bg='light gray').grid(row=10, column=0)
				Label(vnuevo, text='', bg='light gray').grid(row=11, column=0)
				Label(vnuevo, text='', bg='light gray').grid(row=12, column=0)
				Label(vnuevo, text='', bg='light gray').grid(row=13, column=1)
				Label(vnuevo, text='', bg='light gray').grid(row=14, column=1)
				Label(vnuevo, text='', bg='light gray').grid(row=15, column=1)
				Label(vnuevo, text='', bg='light gray').grid(row=16, column=1)
				Label(vnuevo, text='', bg='light gray').grid(row=17, column=1)
				Label(vnuevo, text='', bg='light gray').grid(row=18, column=1)
				Label(vnuevo, text='', bg='light gray').grid(row=19, column=1)
				Label(vnuevo, text=' DATOS  ', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=4,
																											   column=4)
				Label(vnuevo, text='DE   EST', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=4,
																											   column=5)
				Label(vnuevo, text='UDIANTE', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=4,
																											  column=6)
				# Entada nombre1
				Label(vnuevo, text='Grado entrante: ', font=(15), bg='light gray', fg='dodger blue').grid(row=6,
																										  column=2)
				grado = Entry(vnuevo, textvariable=StringVar(value=buscgrado), state='readonly')
				grado.focus()
				grado.grid(row=6, column=3)
				Label(vnuevo, text='Primer nombre: ', font=(15), bg='light gray', fg='dodger blue').grid(row=7,
																										 column=2)
				nombre = Entry(vnuevo, textvariable=StringVar(value=mn), state='readonly')
				nombre.focus()
				nombre.grid(row=7, column=3)
				# Entrada nomre2
				Label(vnuevo, text='Segundo nombre: ', font=(15), bg='light gray', fg='dodger blue').grid(row=7,
																										  column=4)
				nombre1 = Entry(vnuevo, textvariable=StringVar(value=mn1), state='readonly')
				nombre1.grid(row=7, column=5)
				# Entrada de apellido1
				Label(vnuevo, text='Primer apellido: ', font=(15), bg='light gray', fg='dodger blue').grid(row=7,
																										   column=6)
				apellido = Entry(vnuevo, textvariable=StringVar(value=ma), state='readonly')
				apellido.grid(row=7, column=7)
				# Entrada de apellido2
				Label(vnuevo, text='Segundo apellido: ', font=(15), bg='light gray', fg='dodger blue').grid(row=7,
																											column=8)
				apellido1 = Entry(vnuevo, textvariable=StringVar(value=ma1), state='readonly')
				apellido1.grid(row=7, column=9)
				# Entrada de identidad
				Label(vnuevo, text='Doc. id: ', font=(15), bg='light gray', fg='dodger blue').grid(row=8, column=2)
				did = StringVar()
				combo = Entry(vnuevo, textvariable=StringVar(value=mdid), state='readonly')
				combo.grid(row=8, column=3)
				# combo.current(1)
				Label(vnuevo, text='Numero de identidad: ', font=(15), bg='light gray', fg='dodger blue').grid(row=8,
																											   column=4)
				identidad = Entry(vnuevo, textvariable=StringVar(value=miden), state='readonly')
				identidad.grid(row=8, column=5)
				Label(vnuevo, text='Genero: ', font=(15), bg='light gray', fg='dodger blue').grid(row=8, column=6)
				genero = Entry(vnuevo, textvariable=StringVar(value=mge), state='readonly')
				genero.grid(row=8, column=7)
				Label(vnuevo, text='RH : ', font=(15), bg='light gray', fg='dodger blue').grid(row=8, column=8)
				rh = Entry(vnuevo, textvariable=StringVar(value=mrhh), state='readonly')
				rh.grid(row=8, column=9)
				# Entradad fecha de nacimiento
				Label(vnuevo, text='Fecha de nacimiento: ', font=(15), bg='light gray', fg='dodger blue').grid(row=9,
																											   column=2)
				fecha = Entry(vnuevo, textvariable=StringVar(value=mfe), state='readonly')
				fecha.grid(row=9, column=3)
				Label(vnuevo, text='Edad : ', font=(15), bg='light gray', fg='dodger blue').grid(row=9, column=4)
				edad = Entry(vnuevo, textvariable=StringVar(value=med), state='readonly')
				edad.grid(row=9, column=5)
				Label(vnuevo, text='Salud : ', font=(15), bg='light gray', fg='dodger blue').grid(row=9, column=6)
				salud = StringVar()
				combo2 = Entry(vnuevo, textvariable=StringVar(value=msa), state='readonly')
				combo2.grid(row=9, column=7)
				# combo2.current(0)
				Label(vnuevo, text='Cual: ', font=(15), bg='light gray', fg='dodger blue').grid(row=9, column=8)
				tsalud = Entry(vnuevo, textvariable=StringVar(value=mtsa), state='readonly')
				tsalud.grid(row=9, column=9)
				# Entrada de ciudad
				Label(vnuevo, text='Ciudad: ', font=(15), bg='light gray', fg='dodger blue').grid(row=10, column=2)
				ciudad = Entry(vnuevo, textvariable=StringVar(value=mc), state='readonly')
				ciudad.grid(row=10, column=3)
				Label(vnuevo, text='Direccion: ', font=(15), bg='light gray', fg='dodger blue').grid(row=10, column=4)
				direccion = Entry(vnuevo, textvariable=StringVar(value=mdirec), state='readonly')
				direccion.grid(row=10, column=5)
				Label(vnuevo, text='Correo electronico: ', font=(15), bg='light gray', fg='dodger blue').grid(row=11,
																											  column=2)
				correo1 = Entry(vnuevo, textvariable=StringVar(value=mco1), state='readonly')
				correo1.grid(row=11, column=3)
				Label(vnuevo, text='Telefono: ', font=(15), bg='light gray', fg='dodger blue').grid(row=11, column=4)
				telefono1 = Entry(vnuevo, textvariable=StringVar(value=mt1), state='readonly')
				telefono1.grid(row=11, column=5)
				# Datos acudiente
				# Entada nombre1
				Label(vnuevo, text='  DATOS ', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=16,
																											   column=4)
				Label(vnuevo, text='  DE    AC', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=16,
																												 column=5)
				Label(vnuevo, text='UDIENTE', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=16,
																											  column=6)
				Label(vnuevo, text='Primer nombre: ', font=(15), bg='light gray', fg='dodger blue').grid(row=19,
																										 column=2)
				nombrea = Entry(vnuevo, textvariable=StringVar(value=mn1a), state='readonly')
				nombrea.focus()
				nombrea.grid(row=19, column=3)
				# Entrada nomre2
				Label(vnuevo, text='Segundo nombre: ', font=(15), bg='light gray', fg='dodger blue').grid(row=19,
																										  column=4)
				nombre1a = Entry(vnuevo, textvariable=StringVar(value=mna), state='readonly')
				nombre1a.grid(row=19, column=5)
				# Entrada de apellido1
				Label(vnuevo, text='Primer apellido: ', font=(15), bg='light gray', fg='dodger blue').grid(row=19,
																										   column=6)
				apellidoa = Entry(vnuevo, textvariable=StringVar(value=mapa), state='readonly')
				apellidoa.grid(row=19, column=7)
				# Entrada de apellido2
				Label(vnuevo, text='Segundo apellido: ', font=(15), bg='light gray', fg='dodger blue').grid(row=19,
																											column=8)
				apellido1a = Entry(vnuevo, textvariable=StringVar(value=map1a), state='readonly')
				apellido1a.grid(row=19, column=9)
				Label(vnuevo, text='Parentesco: ', font=(15), bg='light gray', fg='dodger blue').grid(row=20, column=2)
				parentesco = Entry(vnuevo, textvariable=StringVar(value=mparen), state='readonly')
				parentesco.grid(row=20, column=3)
				Label(vnuevo, text='Ocupacion: ', font=(15), bg='light gray', fg='dodger blue').grid(row=20, column=4)
				ocupacion = Entry(vnuevo, textvariable=StringVar(value=mocup), state='readonly')
				ocupacion.grid(row=20, column=5)
				Label(vnuevo, text='Ciudad: ', font=(15), bg='light gray', fg='dodger blue').grid(row=20, column=6)
				ciudad2 = Entry(vnuevo, textvariable=StringVar(value=mc2), state='readonly')
				ciudad2.grid(row=20, column=7)
				Label(vnuevo, text='Direccion: ', font=(15), bg='light gray', fg='dodger blue').grid(row=20, column=8)
				direccion2 = Entry(vnuevo, textvariable=StringVar(value=mdirec2), state='readonly')
				direccion2.grid(row=20, column=9)
				Label(vnuevo, text='Correo electronico: ', font=(15), bg='light gray', fg='dodger blue').grid(row=21,
																											  column=2)
				correo2 = Entry(vnuevo, textvariable=StringVar(value=mco2), state='readonly')
				correo2.grid(row=21, column=3)
				Label(vnuevo, text='Telefono: ', font=(15), bg='light gray', fg='dodger blue').grid(row=21, column=4)
				telefono2 = Entry(vnuevo, textvariable=StringVar(value=mt2), state='readonly')
				telefono2.grid(row=21, column=5)
				did2 = StringVar()
				Label(vnuevo, text='Doc. id: ', font=(15), bg='light gray', fg='dodger blue').grid(row=21, column=6)
				combo3 = Entry(vnuevo, textvariable=StringVar(value=mdid2), state='readonly')
				combo3.grid(row=21, column=7)
				# combo.current(1)
				Label(vnuevo, text='Numero de identidad: ', font=(15), bg='light gray', fg='dodger blue').grid(row=21,
																											   column=8)
				identidad2 = Entry(vnuevo, textvariable=StringVar(value=miden2), state='readonly')
				identidad2.grid(row=21, column=9)
				Button(vnuevo, text='EDITAR',
					   command=lambda: f_editar(vnuevo, buscgrado, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med, mrhh,
												mc, mdirec, msa,
												mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2,
												mco2, mt2,
												mdid2, miden2), font=(30), bg='#56cd63', width="25", fg='white',
					   height='2').place(x=250, y=600)
				Button(vnuevo, text='ELIMINAR', command=lambda: feliminar(vnuevo, buscgrado, busqueda), font=(30),
					   bg='#56cd63',
					   width="25", fg='white', height='2').place(x=790, y=600)
			else:
				pass
			ventedit.destroy()

		def feliminar(borrar, buscgrado, busqueda):
			ruloz = sqlite3.connect("matriculas.db")
			cursor = ruloz.cursor()
			if buscgrado == '1':
				mb = messagebox.askyesno('CONFIRMAR', message='¿ESTA SEGURO DE ELIMINAR ESTE CONTACTO?')
				if mb == True:
					cursor.execute("DELETE FROM ESTUDIANTES_1  WHERE identidad='%s'" % (busqueda))
					borrar.destroy
			elif buscgrado == '2':
				mb = messagebox.askyesno('CONFIRMAR', message='¿ESTA SEGURO DE ELIMINAR ESTE CONTACTO?')
				if mb == True:
					cursor.execute("DELETE FROM ESTUDIANTES_2  WHERE identidad='%s'" % (busqueda))
					borrar.destroy
			elif buscgrado == '3':
				mb = messagebox.askyesno('CONFIRMAR', message='¿ESTA SEGURO DE ELIMINAR ESTE CONTACTO?')
				if mb == True:
					cursor.execute("DELETE FROM ESTUDIANTES_3  WHERE identidad='%s'" % (busqueda))
					borrar.destroy
			elif buscgrado == '4':
				mb = messagebox.askyesno('CONFIRMAR', message='¿ESTA SEGURO DE ELIMINAR ESTE CONTACTO?')
				if mb == True:
					cursor.execute("DELETE FROM ESTUDIANTES_4  WHERE identidad='%s'" % (busqueda))
					borrar.destroy
			elif buscgrado == '5':
				mb = messagebox.askyesno('CONFIRMAR', message='¿ESTA SEGURO DE ELIMINAR ESTE CONTACTO?')
				if mb == True:
					cursor.execute("DELETE FROM ESTUDIANTES_5  WHERE identidad='%s'" % (busqueda))
					borrar.destroy
			elif buscgrado == '6':
				mb = messagebox.askyesno('CONFIRMAR', message='¿ESTA SEGURO DE ELIMINAR ESTE CONTACTO?')
				if mb == True:
					cursor.execute("DELETE FROM ESTUDIANTES_6  WHERE identidad='%s'" % (busqueda))
					borrar.destroy
			elif buscgrado == '7':
				mb = messagebox.askyesno('CONFIRMAR', message='¿ESTA SEGURO DE ELIMINAR ESTE CONTACTO?')
				if mb == True:
					cursor.execute("DELETE FROM ESTUDIANTES_7  WHERE identidad='%s'" % (busqueda))
					borrar.destroy
			elif buscgrado == '8':
				mb = messagebox.askyesno('CONFIRMAR', message='¿ESTA SEGURO DE ELIMINAR ESTE CONTACTO?')
				if mb == True:
					cursor.execute("DELETE FROM ESTUDIANTES_8  WHERE identidad='%s'" % (busqueda))
					borrar.destroy
			elif buscgrado == '9':
				mb = messagebox.askyesno('CONFIRMAR', message='¿ESTA SEGURO DE ELIMINAR ESTE CONTACTO?')
				if mb == True:
					cursor.execute("DELETE FROM ESTUDIANTES_9  WHERE identidad='%s'" % (busqueda))
					borrar.destroy
			elif buscgrado == '10':
				mb = messagebox.askyesno('CONFIRMAR', message='¿ESTA SEGURO DE ELIMINAR ESTE CONTACTO?')
				if mb == True:
					cursor.execute("DELETE FROM ESTUDIANTES_10  WHERE identidad='%s'" % (busqueda))
					borrar.destroy
			elif buscgrado == '11':
				mb = messagebox.askyesno('CONFIRMAR', message='¿ESTA SEGURO DE ELIMINAR ESTE CONTACTO?')
				if mb == True:
					cursor.execute("DELETE FROM ESTUDIANTES_11  WHERE identidad='%s'" % (busqueda))
					borrar.destroy
			ruloz.commit()
			cursor.close()

		def f_editar(vnuevo, buscgrado, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med, mrhh, mc, mdirec, msa, mtsa, mco1,
					 mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2, mco2, mt2, mdid2, miden2):
			vnuevo.destroy()
			v_editar = Toplevel()
			v_editar.geometry("1350x690+0+0")
			v_editar.title("Menu de matricula")
			v_editar.configure(bg='light gray')

			Label(v_editar, text='', bg='light gray').grid(row=1, column=0)
			Label(v_editar, text='', bg='light gray').grid(row=2, column=0)
			Label(v_editar, text='', bg='light gray').grid(row=3, column=0)
			Label(v_editar, text='', bg='light gray').grid(row=4, column=0)
			Label(v_editar, text='', bg='light gray').grid(row=5, column=0)
			Label(v_editar, text='              ', bg='light gray').grid(row=6, column=1)
			Label(v_editar, text='              ', bg='light gray').grid(row=7, column=1)
			Label(v_editar, text='              ', bg='light gray').grid(row=8, column=1)
			Label(v_editar, text='', bg='light gray').grid(row=10, column=0)
			Label(v_editar, text='', bg='light gray').grid(row=11, column=0)
			Label(v_editar, text='', bg='light gray').grid(row=12, column=0)
			Label(v_editar, text='', bg='light gray').grid(row=13, column=1)
			Label(v_editar, text='', bg='light gray').grid(row=14, column=1)
			Label(v_editar, text='', bg='light gray').grid(row=15, column=1)
			Label(v_editar, text='', bg='light gray').grid(row=16, column=1)
			Label(v_editar, text='', bg='light gray').grid(row=17, column=1)
			Label(v_editar, text='', bg='light gray').grid(row=18, column=1)
			Label(v_editar, text='', bg='light gray').grid(row=19, column=1)
			Label(v_editar, text=' DATOS  ', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=4,column=4)
			Label(v_editar, text='DE   EST', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=4,column=5)
			Label(v_editar, text='UDIANTE', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=4,column=6)
			# Entada nombre1
			Label(v_editar, text='Grado entrante: ', font=(15), bg='light gray', fg='dodger blue').grid(row=6, column=2)
			grado = Entry(v_editar, textvariable=StringVar(value=buscgrado), state='readonly')
			grado.focus()
			grado.grid(row=6, column=3)
			Label(v_editar, text='Primer nombre: ', font=(15), bg='light gray', fg='dodger blue').grid(row=7, column=2)
			nombre = Entry(v_editar, textvariable=StringVar(value=mn))
			nombre.focus()
			nombre.grid(row=7, column=3)
			# Entrada nomre2
			Label(v_editar, text='Segundo nombre: ', font=(15), bg='light gray', fg='dodger blue').grid(row=7, column=4)
			nombre1 = Entry(v_editar, textvariable=StringVar(value=mn1))
			nombre1.grid(row=7, column=5)
			# Entrada de apellido1
			Label(v_editar, text='Primer apellido: ', font=(15), bg='light gray', fg='dodger blue').grid(row=7,column=6)
			apellido = Entry(v_editar, textvariable=StringVar(value=ma))
			apellido.grid(row=7, column=7)
			# Entrada de apellido2
			Label(v_editar, text='Segundo apellido: ', font=(15), bg='light gray', fg='dodger blue').grid(row=7,column=8)
			apellido1 = Entry(v_editar, textvariable=StringVar(value=ma1))
			apellido1.grid(row=7, column=9)
			# Entrada de identidad
			Label(v_editar, text='Doc. id: ', font=(15), bg='light gray', fg='dodger blue').grid(row=8, column=2)
			did = StringVar()
			combo = Entry(v_editar, textvariable=StringVar(value=mdid))
			combo = ttk.Combobox(v_editar, textvariable=did)
			combo.grid(row=8, column=3)
			# combo.current(1)
			combo['values'] = ['R.C', 'T.I', 'C.C', 'C.E']
			# combo.current(1)
			Label(v_editar, text='Numero de identidad: ', font=(15), bg='light gray', fg='dodger blue').grid(row=8,column=4)
			identidad = Entry(v_editar, textvariable=StringVar(value=miden), state='readonly')
			identidad.grid(row=8, column=5)
			Label(v_editar, text='Genero: ', font=(15), bg='light gray', fg='dodger blue').grid(row=8, column=6)
			genero = Entry(v_editar, textvariable=StringVar(value=mge))
			genero.grid(row=8, column=7)
			Label(v_editar, text='RH : ', font=(15), bg='light gray', fg='dodger blue').grid(row=8, column=8)
			rh = Entry(v_editar, textvariable=StringVar(value=mrhh))
			rh.grid(row=8, column=9)
			# Entradad fecha de nacimiento
			Label(v_editar, text='Fecha de nacimiento: ', font=(15), bg='light gray', fg='dodger blue').grid(row=9,column=2)
			fecha = Entry(v_editar, textvariable=StringVar(value=mfe))
			fecha.grid(row=9, column=3)
			Label(v_editar, text='Edad : ', font=(15), bg='light gray', fg='dodger blue').grid(row=9, column=4)
			edad = Entry(v_editar, textvariable=StringVar(value=med))
			edad.grid(row=9, column=5)
			Label(v_editar, text='Salud : ', font=(15), bg='light gray', fg='dodger blue').grid(row=9, column=6)
			salud = StringVar()
			combo2 = Entry(v_editar, textvariable=StringVar(value=msa))
			combo2 = ttk.Combobox(v_editar, textvariable=salud)
			combo2.grid(row=9, column=7)
			# combo2.current(0)
			combo2['values'] = ('EPS', 'SISBEN', 'ARL')
			Label(v_editar, text='Cual: ', font=(15), bg='light gray', fg='dodger blue').grid(row=9, column=8)
			tsalud = Entry(v_editar, textvariable=StringVar(value=mtsa))
			tsalud.grid(row=9, column=9)
			# Entrada de ciudad
			Label(v_editar, text='Ciudad: ', font=(15), bg='light gray', fg='dodger blue').grid(row=10, column=2)
			ciudad = Entry(v_editar, textvariable=StringVar(value=mc))
			ciudad.grid(row=10, column=3)
			Label(v_editar, text='Direccion: ', font=(15), bg='light gray', fg='dodger blue').grid(row=10, column=4)
			direccion = Entry(v_editar, textvariable=StringVar(value=mdirec))
			direccion.grid(row=10, column=5)
			Label(v_editar, text='Correo electronico: ', font=(15), bg='light gray', fg='dodger blue').grid(row=11,column=2)
			correo1 = Entry(v_editar, textvariable=StringVar(value=mco1))
			correo1.grid(row=11, column=3)
			Label(v_editar, text='Telefono: ', font=(15), bg='light gray', fg='dodger blue').grid(row=11, column=4)
			telefono1 = Entry(v_editar, textvariable=StringVar(value=mt1))
			telefono1.grid(row=11, column=5)
			# Datos acudiente
			# Entada nombre1
			Label(v_editar, text='  DATOS ', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=16,column=4)
			Label(v_editar, text='  DE    AC', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=16,column=5)
			Label(v_editar, text='UDIENTE', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=16,column=6)
			Label(v_editar, text='Primer nombre: ', font=(15), bg='light gray', fg='dodger blue').grid(row=19, column=2)
			nombrea = Entry(v_editar, textvariable=StringVar(value=mn1a))
			nombrea.focus()
			nombrea.grid(row=19, column=3)
			# Entrada nomre2
			Label(v_editar, text='Segundo nombre: ', font=(15), bg='light gray', fg='dodger blue').grid(row=19,column=4)
			nombre1a = Entry(v_editar, textvariable=StringVar(value=mna))
			nombre1a.grid(row=19, column=5)
			# Entrada de apellido1
			Label(v_editar, text='Primer apellido: ', font=(15), bg='light gray', fg='dodger blue').grid(row=19,column=6)
			apellidoa = Entry(v_editar, textvariable=StringVar(value=mapa))
			apellidoa.grid(row=19, column=7)
			# Entrada de apellido2
			Label(v_editar, text='Segundo apellido: ', font=(15), bg='light gray', fg='dodger blue').grid(row=19,column=8)
			apellido1a = Entry(v_editar, textvariable=StringVar(value=map1a))
			apellido1a.grid(row=19, column=9)
			Label(v_editar, text='Parentesco: ', font=(15), bg='light gray', fg='dodger blue').grid(row=20, column=2)
			parentesco = Entry(v_editar, textvariable=StringVar(value=mparen))
			parentesco.grid(row=20, column=3)
			Label(v_editar, text='Ocupacion: ', font=(15), bg='light gray', fg='dodger blue').grid(row=20, column=4)
			ocupacion = Entry(v_editar, textvariable=StringVar(value=mocup))
			ocupacion.grid(row=20, column=5)
			Label(v_editar, text='Ciudad: ', font=(15), bg='light gray', fg='dodger blue').grid(row=20, column=6)
			ciudad2 = Entry(v_editar, textvariable=StringVar(value=mc2))
			ciudad2.grid(row=20, column=7)
			Label(v_editar, text='Direccion: ', font=(15), bg='light gray', fg='dodger blue').grid(row=20, column=8)
			direccion2 = Entry(v_editar, textvariable=StringVar(value=mdirec2))
			direccion2.grid(row=20, column=9)
			Label(v_editar, text='Correo electronico: ', font=(15), bg='light gray', fg='dodger blue').grid(row=21,
																											column=2)
			correo2 = Entry(v_editar, textvariable=StringVar(value=mco2))
			correo2.grid(row=21, column=3)
			Label(v_editar, text='Telefono: ', font=(15), bg='light gray', fg='dodger blue').grid(row=21, column=4)
			telefono2 = Entry(v_editar, textvariable=StringVar(value=mt2))
			telefono2.grid(row=21, column=5)
			did2 = StringVar()
			Label(v_editar, text='Doc. id: ', font=(15), bg='light gray', fg='dodger blue').grid(row=21, column=6)
			combo3 = Entry(v_editar, textvariable=StringVar(value=mdid2))
			combo3 = ttk.Combobox(v_editar, textvariable=did2)
			combo3.grid(row=21, column=7)
			# combo.current(1)
			combo3['values'] = ['C.C', 'C.E']
			# combo.current(1)
			Label(v_editar, text='Numero de identidad: ', font=(15), bg='light gray', fg='dodger blue').grid(row=21,column=8)
			identidad2 = Entry(v_editar, textvariable=StringVar(value=miden2))
			identidad2.grid(row=21, column=9)
			# Boton guardar
			# ttk.Button(ventana1,text='Guardar').grid(row=7,column=4, sticky = W+E)
			Button(v_editar, text='ACTUALIZAR',
				   command=lambda: factualizar(v_editar, buscgrado, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med, mrhh,mc, mdirec
											   , msa, mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2,mdirec2, mco2, mt2, mdid2, miden2, nombre.get(), apellido.get()
											   , nombre1.get(), apellido1.get(), did.get(), identidad.get(),genero.get(), fecha.get(), edad.get(), rh.get(), ciudad.get(),
											   direccion.get(), salud.get(), tsalud.get(), correo1.get(), telefono1.get(), nombrea.get(), apellidoa.get(),
											   nombre1a.get(), apellido1a.get(), parentesco.get(), ocupacion.get(),ciudad2.get(), direccion2.get(), correo2.get(),
											   telefono2.get(), did2.get(), identidad2.get()), font=(15),
				   bg='dodger blue', width="30", fg='white', height='2').place(x=500, y=600)

		def factualizar(v_editar, buscgrado, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med, mrhh, mc, mdirec, msa, mtsa,mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2, mco2, mt2, mdid2, miden2,
						nombre, apellido, nombre1, apellido1, did, identidad, genero, fecha, edad, rh, ciudad,direccion, salud, tsalud, correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a,
						parentesco, ocupacion, ciudad2, direccion2, correo2, telefono2, did2, identidad2):
			ruloz = sqlite3.connect("matriculas.db")
			cursor = ruloz.cursor()
			if buscgrado == '1':
				cursor.execute(
					"UPDATE ESTUDIANTES_1 SET nombre='%s', nombre2='%s',apellido='%s',apellido2='%s' , doc_id='%s',identidad='%s'"
					",genero='%s',fecha_nacimiento='%s',edad='%s',rh='%s',ciudad='%s',direccion='%s' ,salud='%s',entidad='%s',correo='%s'"
					",telefono='%s',acudiente='%s',nombre2a='%s',apellidoa='%s',apellido2a='%s' ,parentesco='%s',ocupacion='%s',ciudad2='%s',direccion2='%s',correo2='%s',telefono2='%s',doc_id2='%s',identidad2='%s'"
					"WHERE nombre='%s' AND nombre2='%s' AND apellido='%s' AND apellido2='%s' AND  doc_id='%s' AND identidad='%s'AND genero='%s' AND fecha_nacimiento='%s' "
					"AND edad='%s' AND rh='%s' AND ciudad='%s' AND direccion='%s' AND salud='%s' AND entidad='%s' AND correo='%s' AND telefono='%s' "
					"AND acudiente='%s' AND nombre2a='%s' AND apellidoa='%s' AND apellido2a='%s'AND parentesco='%s' AND ocupacion='%s' AND "
					"ciudad2='%s' AND direccion2='%s' AND correo2='%s' AND telefono2='%s' AND doc_id2='%s' AND identidad2='%s' " % (
					nombre, apellido, nombre1, apellido1, did, identidad, genero, fecha, edad, rh, ciudad, direccion,
					salud, tsalud, correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a, parentesco, ocupacion,
					ciudad2, direccion2, correo2, telefono2, did2, identidad2, mn, mn1, ma, ma1, mdid, miden, mge, mfe,
					med, mrhh, mc, mdirec, msa, mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2,
					mco2, mt2, mdid2, miden2))
				ruloz.commit()
				cursor.close()
			elif buscgrado == '2':
				cursor.execute(
					"UPDATE ESTUDIANTES_2 SET nombre='%s', nombre2='%s',apellido='%s',apellido2='%s' , doc_id='%s',identidad='%s'" ",genero='%s',fecha_nacimiento='%s',edad='%s',rh='%s',ciudad='%s',direccion='%s' ,salud='%s',entidad='%s',correo='%s'"
					",telefono='%s',acudiente='%s',nombre2a='%s',apellidoa='%s',apellido2a='%s' ,parentesco='%s',ocupacion='%s',ciudad2='%s',direccion2='%s',correo2='%s',telefono2='%s',doc_id2='%s',identidad2='%s'"
					"WHERE nombre='%s' AND nombre2='%s' AND apellido='%s' AND apellido2='%s' AND  doc_id='%s' AND identidad='%s'AND genero='%s' AND fecha_nacimiento='%s' "
					"AND edad='%s' AND rh='%s' AND ciudad='%s' AND direccion='%s' AND salud='%s' AND entidad='%s' AND correo='%s' AND telefono='%s' "
					"AND acudiente='%s' AND nombre2a='%s' AND apellidoa='%s' AND apellido2a='%s'AND parentesco='%s' AND ocupacion='%s' AND "
					"ciudad2='%s' AND direccion2='%s' AND correo2='%s' AND telefono2='%s' AND doc_id2='%s' AND identidad2='%s' " % (
					nombre, apellido, nombre1, apellido1, did, identidad, genero, fecha, edad, rh, ciudad, direccion,
					salud, tsalud, correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a, parentesco, ocupacion,
					ciudad2, direccion2, correo2, telefono2, did2, identidad2, mn, mn1, ma, ma1, mdid, miden, mge, mfe,
					med, mrhh, mc, mdirec, msa, mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2,
					mco2, mt2, mdid2, miden2))
				ruloz.commit()
				cursor.close()
			elif buscgrado == '3':
				cursor.execute("UPDATE ESTUDIANTES_3 SET nombre='%s', nombre2='%s',apellido='%s',apellido2='%s' , doc_id='%s',identidad='%s'" ",genero='%s',fecha_nacimiento='%s',edad='%s',rh='%s',ciudad='%s',direccion='%s' ,salud='%s',entidad='%s',correo='%s'"
					",telefono='%s',acudiente='%s',nombre2a='%s',apellidoa='%s',apellido2a='%s' ,parentesco='%s',ocupacion='%s',ciudad2='%s',direccion2='%s',correo2='%s',telefono2='%s',doc_id2='%s',identidad2='%s'"
					"WHERE nombre='%s' AND nombre2='%s' AND apellido='%s' AND apellido2='%s' AND  doc_id='%s' AND identidad='%s'AND genero='%s' AND fecha_nacimiento='%s' "
					"AND edad='%s' AND rh='%s' AND ciudad='%s' AND direccion='%s' AND salud='%s' AND entidad='%s' AND correo='%s' AND telefono='%s' "
					"AND acudiente='%s' AND nombre2a='%s' AND apellidoa='%s' AND apellido2a='%s'AND parentesco='%s' AND ocupacion='%s' AND "
					"ciudad2='%s' AND direccion2='%s' AND correo2='%s' AND telefono2='%s' AND doc_id2='%s' AND identidad2='%s' " % (
						nombre, apellido, nombre1, apellido1, did, identidad, genero, fecha, edad, rh, ciudad,direccion, salud,
						tsalud, correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a, parentesco, ocupacion,ciudad2,
						direccion2, correo2, telefono2, did2, identidad2, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med,mrhh, mc,
						mdirec, msa, mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2, mco2, mt2,mdid2,miden2))
				ruloz.commit()
				cursor.close()
			elif buscgrado == '4':
				cursor.execute("UPDATE ESTUDIANTES_4 SET nombre='%s', nombre2='%s',apellido='%s',apellido2='%s' , doc_id='%s',identidad='%s'" ",genero='%s',fecha_nacimiento='%s',edad='%s',rh='%s',ciudad='%s',direccion='%s' ,salud='%s',entidad='%s',correo='%s'"
					",telefono='%s',acudiente='%s',nombre2a='%s',apellidoa='%s',apellido2a='%s' ,parentesco='%s',ocupacion='%s',ciudad2='%s',direccion2='%s',correo2='%s',telefono2='%s',doc_id2='%s',identidad2='%s'"
					"WHERE nombre='%s' AND nombre2='%s' AND apellido='%s' AND apellido2='%s' AND  doc_id='%s' AND identidad='%s'AND genero='%s' AND fecha_nacimiento='%s' "
					"AND edad='%s' AND rh='%s' AND ciudad='%s' AND direccion='%s' AND salud='%s' AND entidad='%s' AND correo='%s' AND telefono='%s' "
					"AND acudiente='%s' AND nombre2a='%s' AND apellidoa='%s' AND apellido2a='%s'AND parentesco='%s' AND ocupacion='%s' AND "
					"ciudad2='%s' AND direccion2='%s' AND correo2='%s' AND telefono2='%s' AND doc_id2='%s' AND identidad2='%s' " % (
						nombre, apellido, nombre1, apellido1, did, identidad, genero, fecha, edad, rh, ciudad,direccion, salud,
						tsalud, correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a, parentesco, ocupacion,ciudad2,
						direccion2, correo2, telefono2, did2, identidad2, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med,mrhh, mc,
						mdirec, msa, mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2, mco2, mt2,mdid2,miden2))
				ruloz.commit()
				cursor.close()
			elif buscgrado == '5':
				cursor.execute("UPDATE ESTUDIANTES_5 SET nombre='%s', nombre2='%s',apellido='%s',apellido2='%s' , doc_id='%s',identidad='%s'" ",genero='%s',fecha_nacimiento='%s',edad='%s',rh='%s',ciudad='%s',direccion='%s' ,salud='%s',entidad='%s',correo='%s'"
					",telefono='%s',acudiente='%s',nombre2a='%s',apellidoa='%s',apellido2a='%s' ,parentesco='%s',ocupacion='%s',ciudad2='%s',direccion2='%s',correo2='%s',telefono2='%s',doc_id2='%s',identidad2='%s'"
					"WHERE nombre='%s' AND nombre2='%s' AND apellido='%s' AND apellido2='%s' AND  doc_id='%s' AND identidad='%s'AND genero='%s' AND fecha_nacimiento='%s' "
					"AND edad='%s' AND rh='%s' AND ciudad='%s' AND direccion='%s' AND salud='%s' AND entidad='%s' AND correo='%s' AND telefono='%s' "
					"AND acudiente='%s' AND nombre2a='%s' AND apellidoa='%s' AND apellido2a='%s'AND parentesco='%s' AND ocupacion='%s' AND "
					"ciudad2='%s' AND direccion2='%s' AND correo2='%s' AND telefono2='%s' AND doc_id2='%s' AND identidad2='%s' " % (
						nombre, apellido, nombre1, apellido1, did, identidad, genero, fecha, edad, rh, ciudad,direccion, salud,
						tsalud, correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a, parentesco, ocupacion,ciudad2,
						direccion2, correo2, telefono2, did2, identidad2, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med,mrhh, mc,
						mdirec, msa, mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2, mco2, mt2,mdid2,miden2))
				ruloz.commit()
				cursor.close()
			elif buscgrado == '6':
				cursor.execute("UPDATE ESTUDIANTES_6 SET nombre='%s', nombre2='%s',apellido='%s',apellido2='%s' , doc_id='%s',identidad='%s'" ",genero='%s',fecha_nacimiento='%s',edad='%s',rh='%s',ciudad='%s',direccion='%s' ,salud='%s',entidad='%s',correo='%s'"
					",telefono='%s',acudiente='%s',nombre2a='%s',apellidoa='%s',apellido2a='%s' ,parentesco='%s',ocupacion='%s',ciudad2='%s',direccion2='%s',correo2='%s',telefono2='%s',doc_id2='%s',identidad2='%s'"
					"WHERE nombre='%s' AND nombre2='%s' AND apellido='%s' AND apellido2='%s' AND  doc_id='%s' AND identidad='%s'AND genero='%s' AND fecha_nacimiento='%s' "
					"AND edad='%s' AND rh='%s' AND ciudad='%s' AND direccion='%s' AND salud='%s' AND entidad='%s' AND correo='%s' AND telefono='%s' "
					"AND acudiente='%s' AND nombre2a='%s' AND apellidoa='%s' AND apellido2a='%s'AND parentesco='%s' AND ocupacion='%s' AND "
					"ciudad2='%s' AND direccion2='%s' AND correo2='%s' AND telefono2='%s' AND doc_id2='%s' AND identidad2='%s' " % (
						nombre, apellido, nombre1, apellido1, did, identidad, genero, fecha, edad, rh, ciudad,direccion, salud,
						tsalud, correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a, parentesco, ocupacion,ciudad2,
						direccion2, correo2, telefono2, did2, identidad2, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med,mrhh, mc,
						mdirec, msa, mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2, mco2, mt2,mdid2,miden2))
				ruloz.commit()
				cursor.close()
			elif buscgrado == '7':
				cursor.execute("UPDATE ESTUDIANTES_7 SET nombre='%s', nombre2='%s',apellido='%s',apellido2='%s' , doc_id='%s',identidad='%s'" ",genero='%s',fecha_nacimiento='%s',edad='%s',rh='%s',ciudad='%s',direccion='%s' ,salud='%s',entidad='%s',correo='%s'"
					",telefono='%s',acudiente='%s',nombre2a='%s',apellidoa='%s',apellido2a='%s' ,parentesco='%s',ocupacion='%s',ciudad2='%s',direccion2='%s',correo2='%s',telefono2='%s',doc_id2='%s',identidad2='%s'"
					"WHERE nombre='%s' AND nombre2='%s' AND apellido='%s' AND apellido2='%s' AND  doc_id='%s' AND identidad='%s'AND genero='%s' AND fecha_nacimiento='%s' "
					"AND edad='%s' AND rh='%s' AND ciudad='%s' AND direccion='%s' AND salud='%s' AND entidad='%s' AND correo='%s' AND telefono='%s' "
					"AND acudiente='%s' AND nombre2a='%s' AND apellidoa='%s' AND apellido2a='%s'AND parentesco='%s' AND ocupacion='%s' AND "
					"ciudad2='%s' AND direccion2='%s' AND correo2='%s' AND telefono2='%s' AND doc_id2='%s' AND identidad2='%s' " % (
						nombre, apellido, nombre1, apellido1, did, identidad, genero, fecha, edad, rh, ciudad,direccion, salud,
						tsalud, correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a, parentesco, ocupacion,ciudad2,
						direccion2, correo2, telefono2, did2, identidad2, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med,mrhh, mc,
						mdirec, msa, mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2, mco2, mt2,mdid2,miden2))
				ruloz.commit()
				cursor.close()
			elif buscgrado == '8':
				cursor.execute("UPDATE ESTUDIANTES_8 SET nombre='%s', nombre2='%s',apellido='%s',apellido2='%s' , doc_id='%s',identidad='%s'" ",genero='%s',fecha_nacimiento='%s',edad='%s',rh='%s',ciudad='%s',direccion='%s' ,salud='%s',entidad='%s',correo='%s'"
					",telefono='%s',acudiente='%s',nombre2a='%s',apellidoa='%s',apellido2a='%s' ,parentesco='%s',ocupacion='%s',ciudad2='%s',direccion2='%s',correo2='%s',telefono2='%s',doc_id2='%s',identidad2='%s'"
					"WHERE nombre='%s' AND nombre2='%s' AND apellido='%s' AND apellido2='%s' AND  doc_id='%s' AND identidad='%s'AND genero='%s' AND fecha_nacimiento='%s' "
					"AND edad='%s' AND rh='%s' AND ciudad='%s' AND direccion='%s' AND salud='%s' AND entidad='%s' AND correo='%s' AND telefono='%s' "
					"AND acudiente='%s' AND nombre2a='%s' AND apellidoa='%s' AND apellido2a='%s'AND parentesco='%s' AND ocupacion='%s' AND "
					"ciudad2='%s' AND direccion2='%s' AND correo2='%s' AND telefono2='%s' AND doc_id2='%s' AND identidad2='%s' " % (
						nombre, apellido, nombre1, apellido1, did, identidad, genero, fecha, edad, rh, ciudad,direccion, salud,
						tsalud, correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a, parentesco, ocupacion,ciudad2,
						direccion2, correo2, telefono2, did2, identidad2, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med,
						mrhh, mc,mdirec, msa, mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2, mco2, mt2,mdid2,miden2))
				ruloz.commit()
				cursor.close()
			elif buscgrado == '9':
				cursor.execute(
					"UPDATE ESTUDIANTES_9 SET nombre='%s', nombre2='%s',apellido='%s',apellido2='%s' , doc_id='%s',identidad='%s'" ",genero='%s',fecha_nacimiento='%s',edad='%s',rh='%s',ciudad='%s',direccion='%s' ,salud='%s',entidad='%s',correo='%s'"
					",telefono='%s',acudiente='%s',nombre2a='%s',apellidoa='%s',apellido2a='%s' ,parentesco='%s',ocupacion='%s',ciudad2='%s',direccion2='%s',correo2='%s',telefono2='%s',doc_id2='%s',identidad2='%s'"
					"WHERE nombre='%s' AND nombre2='%s' AND apellido='%s' AND apellido2='%s' AND  doc_id='%s' AND identidad='%s'AND genero='%s' AND fecha_nacimiento='%s' "
					"AND edad='%s' AND rh='%s' AND ciudad='%s' AND direccion='%s' AND salud='%s' AND entidad='%s' AND correo='%s' AND telefono='%s' "
					"AND acudiente='%s' AND nombre2a='%s' AND apellidoa='%s' AND apellido2a='%s'AND parentesco='%s' AND ocupacion='%s' AND "
					"ciudad2='%s' AND direccion2='%s' AND correo2='%s' AND telefono2='%s' AND doc_id2='%s' AND identidad2='%s' " % (
						nombre, apellido, nombre1, apellido1, did, identidad, genero, fecha, edad, rh, ciudad,direccion, salud,
						tsalud, correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a, parentesco, ocupacion,ciudad2,
						direccion2, correo2, telefono2, did2, identidad2, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med,mrhh, mc,
						mdirec, msa, mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2, mco2, mt2,mdid2,miden2))
				ruloz.commit()
				cursor.close()
			elif buscgrado == '10':
				cursor.execute("UPDATE ESTUDIANTES_10 SET nombre='%s', nombre2='%s',apellido='%s',apellido2='%s' , doc_id='%s',identidad='%s'" ",genero='%s',fecha_nacimiento='%s',edad='%s',rh='%s',ciudad='%s',direccion='%s' ,salud='%s',entidad='%s',correo='%s'"
					",telefono='%s',acudiente='%s',nombre2a='%s',apellidoa='%s',apellido2a='%s' ,parentesco='%s',ocupacion='%s',ciudad2='%s',direccion2='%s',correo2='%s',telefono2='%s',doc_id2='%s',identidad2='%s'"
					"WHERE nombre='%s' AND nombre2='%s' AND apellido='%s' AND apellido2='%s' AND  doc_id='%s' AND identidad='%s'AND genero='%s' AND fecha_nacimiento='%s' "
					"AND edad='%s' AND rh='%s' AND ciudad='%s' AND direccion='%s' AND salud='%s' AND entidad='%s' AND correo='%s' AND telefono='%s' "
					"AND acudiente='%s' AND nombre2a='%s' AND apellidoa='%s' AND apellido2a='%s'AND parentesco='%s' AND ocupacion='%s' AND "
					"ciudad2='%s' AND direccion2='%s' AND correo2='%s' AND telefono2='%s' AND doc_id2='%s' AND identidad2='%s' " % (
						nombre, apellido, nombre1, apellido1, did, identidad, genero, fecha, edad, rh, ciudad,direccion, salud,
						tsalud, correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a, parentesco, ocupacion,ciudad2,
						direccion2, correo2, telefono2, did2, identidad2, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med,mrhh, mc,
						mdirec, msa, mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2, mco2, mt2,mdid2,miden2))
				ruloz.commit()
				cursor.close()
			elif buscgrado == '11':
				cursor.execute("UPDATE ESTUDIANTES_11 SET nombre='%s', nombre2='%s',apellido='%s',apellido2='%s' , doc_id='%s',identidad='%s'" ",genero='%s',fecha_nacimiento='%s',edad='%s',rh='%s',ciudad='%s',direccion='%s' ,salud='%s',entidad='%s',correo='%s'"
					",telefono='%s',acudiente='%s',nombre2a='%s',apellidoa='%s',apellido2a='%s' ,parentesco='%s',ocupacion='%s',ciudad2='%s',direccion2='%s',correo2='%s',telefono2='%s',doc_id2='%s',identidad2='%s'"
					"WHERE nombre='%s' AND nombre2='%s' AND apellido='%s' AND apellido2='%s' AND  doc_id='%s' AND identidad='%s'AND genero='%s' AND fecha_nacimiento='%s' "
					"AND edad='%s' AND rh='%s' AND ciudad='%s' AND direccion='%s' AND salud='%s' AND entidad='%s' AND correo='%s' AND telefono='%s' "
					"AND acudiente='%s' AND nombre2a='%s' AND apellidoa='%s' AND apellido2a='%s'AND parentesco='%s' AND ocupacion='%s' AND "
					"ciudad2='%s' AND direccion2='%s' AND correo2='%s' AND telefono2='%s' AND doc_id2='%s' AND identidad2='%s' " % (
						nombre, apellido, nombre1, apellido1, did, identidad, genero, fecha, edad, rh, ciudad,direccion, salud,
						tsalud, correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a, parentesco, ocupacion,ciudad2,
						direccion2, correo2, telefono2, did2, identidad2, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med,mrhh, mc,
						mdirec, msa, mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2, mco2, mt2,mdid2,miden2))
				ruloz.commit()
				cursor.close()

			messagebox.showinfo(' GOOD ', message='SE ACTUALIZARON LOS DATOS CON EXITO')
			v_editar.destroy()
		
		fmenu()


	vadministrativo=Tk()
	vadministrativo.title('Administrativo')
	vadministrativo.config(bg='AliceBlue')

	conexion = sqlite3.connect('Base_total')
	cursor = conexion.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS PROFESORES (CODIGO INTEGER PRIMARY KEY AUTOINCREMENT,
						NOMBRE VARCHAR,
						MATERIAS VARCHAR,
						CONTRASEÑA VARCHAR,
						VOTO INTEGER)""")
	cursor.close()
	conexion.close()

	conexion = sqlite3.connect('Base_total')
	cursor = conexion.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS ESTUDIANTES (CODIGO INTEGER PRIMARY KEY AUTOINCREMENT,
					NOMBRE VARCHAR,
					CARRERA VARCHAR,
					CONTRASEÑA VARCHAR,
					VOTO INTEGER,
					MATERIAS VARCHAR,
					MATERIASINGRESADA INTEGER)""")
	cursor.close()
	conexion.close()

	lista_estudiantes=0
	lista_profesores=0
	Label(vadministrativo, text='BIENVENIDO', bg='AliceBlue').grid(row=0, column=0,columnspan=10,padx=5,pady=5)
	texto1=Label(vadministrativo,text='Seleccione una opcion' , bg ='AliceBlue').grid(row=1, column=0,padx=5,pady=5)
	botonProfesor=Button(vadministrativo,text='Profesores',width='15', command=lambda:(vadministrativo.destroy(),profesor())).grid(row=2, column=0,padx=5,pady=5)
	botonEstudiantes=Button(vadministrativo,text='Estudiantes',width='15',command=lambda:(vadministrativo.destroy(),estudiantes())).grid(row=3, column=0,padx=5,pady=5)
	botonBiblioteca=Button(vadministrativo,text='Biblioteca',width='15', command=lambda:(vadministrativo.destroy(),BibliotecaA())).grid(row=4, column=0,padx=5,pady=5)
	botonAdministrativo=Button(vadministrativo,text='Administrativo',width='15', command=lambda:(vadministrativo.destroy(),administradores())).grid(row=5, column=0,padx=5,pady=5)


	Label(vadministrativo,text='   			 ',bg='AliceBlue').grid(row=1, column=1,padx=5,pady=5)
	Label(vadministrativo,text='Numero de usuarios ',bg='AliceBlue').grid(row=1, column=2,padx=5,pady=5)
	Label(vadministrativo,text='Profesores:',bg='AliceBlue').grid(row=2, column=2,padx=5,pady=5)
	Label(vadministrativo,text='Estudiantes:',bg='AliceBlue').grid(row=3, column=2,padx=5,pady=5)
	Label(vadministrativo,text='Administadores:',bg='AliceBlue').grid(row=4, column=2,padx=5,pady=5)
	Label(vadministrativo,text='   			 ',bg='AliceBlue').grid(row=6, column=1,padx=5,pady=5)
	Button(vadministrativo, text='Crear Encuesta',width='15', command=lambda:(vadministrativo.destroy(),CrearEncuestas())).grid(row=6, column=0,padx=5,pady=5)
	Button(vadministrativo, text='Salir', bg='AliceBlue', command=lambda:(vadministrativo.destroy(), inicioP())).grid(row=9, column=0, columnspan=5,padx=5,pady=5)
	Button(vadministrativo, text='Matricula',width='15', command=lambda:(vadministrativo.destroy(), matricula())).grid(row=8, column=0,padx=5,pady=5)

	CargarMaterias()
	cargarAdmi()
	vadministrativo.mainloop()


#Ventana Votaciones
#################################
###################################
conexion=sqlite3.connect("Base_total")
micursor=conexion.cursor()
micursor.execute("CREATE TABLE IF NOT EXISTS CANDIDATOSP(CANDIDATO VANCHAR UNIQUE PRIMARY KEY, VOTO INTEGER)")
micursor.execute("CREATE TABLE IF NOT EXISTS CANDIDATOSE(CANDIDATO VANCHAR UNIQUE PRIMARY KEY, VOTO INTEGER)")
micursor.execute("SELECT * FROM CANDIDATOSP")
votose=micursor.fetchall()

if len(votose)==0:
	agregarcandp=[("c1",0),("c2",0),("c3",0),("voto en blanco",0)]
	micursor.executemany("INSERT INTO CANDIDATOSP VALUES (?,?)",agregarcandp)

micursor.execute("SELECT * from CANDIDATOSE")
votosp=micursor.fetchall()

if len(votosp)==0:
	agregarcande=[("c1",0),("c2",0),("c3",0),("voto en blanco",0)]
	micursor.executemany("INSERT INTO CANDIDATOSE VALUES (?,?)",agregarcande)
	
conexion.commit()
micursor.close()
conexion.close()

def votose(Usuario,candidato):
	conexion=sqlite3.connect("Base_total")
	micursor=conexion.cursor()
	if candidato=="c1":
		micursor.execute("UPDATE CANDIDATOSE SET VOTO=VOTO+1 WHERE CANDIDATO=?",(candidato,))
		micursor.execute("UPDATE ESTUDIANTES SET VOTO=VOTO+1 WHERE CODIGO=?",(Usuario,))
		messagebox.showwarning("SISTEMA VOTACIONES", "VOTO FUE REGISTRADO PARA EL CANDIDATO 1")
	elif candidato=="c2":
		micursor.execute("UPDATE CANDIDATOSE SET VOTO=VOTO+1 WHERE CANDIDATO=?",(candidato,))
		micursor.execute("UPDATE ESTUDIANTES SET VOTO=VOTO+1 WHERE CODIGO=?",(Usuario,))
		messagebox.showwarning("SISTEMA VOTACIONES", "VOTO FUE REGISTRADO PARA EL CANDIDATO 2")
	elif candidato=="c3":
		micursor.execute("UPDATE CANDIDATOSE SET VOTO=VOTO+1 WHERE CANDIDATO=?",(candidato,))
		micursor.execute("UPDATE ESTUDIANTES SET VOTO=VOTO+1 WHERE CODIGO=?",(Usuario,))
		messagebox.showwarning("SISTEMA VOTACIONES", "VOTO FUE REGISTRADO PARA EL CANDIDATO 3")
	elif candidato=="voto en blanco":
		micursor.execute("UPDATE CANDIDATOSE SET VOTO=VOTO+1 WHERE CANDIDATO=?",(candidato,))
		micursor.execute("UPDATE ESTUDIANTES SET VOTO=VOTO+1 WHERE CODIGO=?",(Usuario,))
		messagebox.showwarning("SISTEMA VOTACIONES", "VOTO FUE REGISTRADO PARA VOTO EN BLANCO")
	conexion.commit()
	micursor.close()
	conexion.close()

def votosp(Usuario,candidato):
	conexion=sqlite3.connect("Base_total")
	micursor=conexion.cursor()

	if candidato=="c1":
		micursor.execute("UPDATE CANDIDATOSP SET VOTO=VOTO+1 WHERE CANDIDATO=?",(candidato,))
		micursor.execute("UPDATE PROFESORES SET VOTO=VOTO+1 WHERE CODIGO=?",(Usuario,))
		messagebox.showwarning("SISTEMA VOTACIONES", "VOTO FUE REGISTRADO PARA EL CANDIDATO 1")
	elif candidato=="c2":
		micursor.execute("UPDATE CANDIDATOSP SET VOTO=VOTO+1 WHERE CANDIDATO=?",(candidato,))
		micursor.execute("UPDATE PROFESORES SET VOTO=VOTO+1 WHERE CODIGO=?",(Usuario,))
		messagebox.showwarning("SISTEMA VOTACIONES", "VOTO FUE REGISTRADO PARA EL CANDIDATO 2")
	elif candidato=="c3":
		micursor.execute("UPDATE CANDIDATOSP SET VOTO=VOTO+1 WHERE CANDIDATO=?",(candidato,))
		micursor.execute("UPDATE PROFESORES SET VOTO=VOTO+1 WHERE CODIGO=?",(Usuario,))
		messagebox.showwarning("SISTEMA VOTACIONES", "VOTO FUE REGISTRADO PARA EL CANDIDATO 3")
	elif candidato=="voto en blanco":
		micursor.execute("UPDATE CANDIDATOSP SET VOTO=VOTO+1 WHERE CANDIDATO=?",(candidato,))
		micursor.execute("UPDATE PROFESORES SET VOTO=VOTO+1 WHERE CODIGO=?",(Usuario,))
		messagebox.showwarning("SISTEMA VOTACIONES", "VOTO FUE REGISTRADO PARA VOTO EN BLANCO")
	conexion.commit()
	micursor.close()
	conexion.close()

def votacionesP(Usuario):
	raizx=Toplevel()
	raizx.title("VOTACIONES")
	raizx.geometry("1000x650+0+0")
	raizx.resizable(width=False, height=False)
	raizx.iconbitmap("Logo_uis.ico")

	raiz=Frame(raizx,width=700, height=700)
	raiz.pack()
	titulo=Label(raiz, text="CANDIDATOS PROFESORES",font=("Times New Roman",20))
	titulo.grid(row=0, column=0,pady=50, columnspan=10)
	imagen0=PhotoImage(file="Foto_CandidatoP1.png")
	lblimagen0=Label(raiz, image=imagen0)
	lblimagen0.grid(row=1, column=0,pady=30)

	imagen1=PhotoImage(file="Foto_CandidatoP2.png")
	lblimagen0=Label(raiz, image=imagen1)
	lblimagen0.grid(row=1, column=1,pady=30)

	imagen2=PhotoImage(file="Foto_CandidatoP3.png")
	lblimagen0=Label(raiz, image=imagen2)
	lblimagen0.grid(row=1, column=2,pady=30)

	imagen3=PhotoImage(file="Voto_en_blanco.png")
	lblimagen0=Label(raiz, image=imagen3)
	lblimagen0.grid(row=1, column=3,pady=30)

	botonc1=Button(raiz, text=" VOTAR ", font=("Times New Roman",15), command=lambda:[votosp(Usuario,candidato="c1"),raizx.destroy()])
	botonc1.grid(row=2, column=0, pady=10)

	botonc2=Button(raiz, text=" VOTAR ", font=("Times New Roman",15),command=lambda:[votosp(Usuario,candidato="c2"),raizx.destroy()])
	botonc2.grid(row=2, column=1, pady=10)

	botonc3=Button(raiz, text=" VOTAR ", font=("Times New Roman",15),command=lambda:[votosp(Usuario,candidato="c3"),raizx.destroy()])
	botonc3.grid(row=2, column=2, pady=10)

	botonc4=Button(raiz, text=" VOTAR ", font=("Times New Roman",15),command=lambda:[votosp(Usuario,candidato="voto en blanco"),raizx.destroy()])
	botonc4.grid(row=2, column=3, pady=10)

	raiz.mainloop()

def votacionesE(Usuario):
	raize=Toplevel()
	raize.title("VOTACIONES")
	raize.geometry("1000x650+0+0")
	raize.resizable(width=False, height=False)
	raize.iconbitmap("Logo_uis.ico")

	imagenp=PhotoImage(file="uis fondo.gif")
	lblimagenx=Label(raize, image=imagenp)

	raiz=Frame(raize, width=700, height=700)
	raiz.pack()

	titulo=Label(raiz, text="CANDIDATOS ESTUDIANTES",font=("Times New Roman",20))
	titulo.grid(row=0, column=0,pady=50,padx=2,columnspan=10)

	imagen0=PhotoImage(file="Foto_CandidatoE1.png")

	lblimagen0=Label(raiz, image=imagen0)
	lblimagen0.grid(row=1, column=0,pady=30)

	imagen1=PhotoImage(file="Foto_CandidatoE2.png")
	lblimagen0=Label(raiz, image=imagen1)
	lblimagen0.grid(row=1, column=1,pady=30)

	imagen2=PhotoImage(file="Foto_CandidatoE3.png")
	lblimagen0=Label(raiz, image=imagen2)
	lblimagen0.grid(row=1, column=2,pady=30)

	imagen3=PhotoImage(file="Voto_en_blanco.png")
	lblimagen0=Label(raiz, image=imagen3)
	lblimagen0.grid(row=1, column=3,pady=30)

	botonc1=Button(raiz, text=" VOTAR ", font=("Times New Roman",15), command=lambda:[votose(Usuario,candidato="c1"),raize.destroy()])
	botonc1.grid(row=2, column=0, pady=10)

	botonc2=Button(raiz, text=" VOTAR ", font=("Times New Roman",15),command=lambda:[votose(Usuario,candidato="c2"),raize.destroy()])
	botonc2.grid(row=2, column=1, pady=10)

	botonc3=Button(raiz, text=" VOTAR ", font=("Times New Roman",15),command=lambda:[votose(Usuario,candidato="c3"),raize.destroy()])
	botonc3.grid(row=2, column=2, pady=10)

	botonc4=Button(raiz, text=" VOTAR ", font=("Times New Roman",15),command=lambda:[votose(Usuario,candidato="voto en blanco"),raize.destroy()])
	botonc4.grid(row=2, column=3, pady=10)

	raiz.mainloop()

def inisiar_secionU(Usuario,Contraseña,tipov):
	conexion=sqlite3.connect("Base_total")
	micursor=conexion.cursor()
	if tipov=="Estudiantes":
		micursor.execute("SELECT * FROM ESTUDIANTES WHERE CODIGO=? AND CONTRASEÑA=?",(Usuario,Contraseña))
		if micursor.fetchall():
			votoe=0
			micursor.execute("SELECT VOTO FROM ESTUDIANTES WHERE CODIGO=? AND CONTRASEÑA=? AND VOTO=?",(Usuario,Contraseña,votoe))
			if micursor.fetchall():
				votacionesE(Usuario)
			else:messagebox.showwarning("ERROR", "EL USUARIO YA TIENE VOTO REGISTRADO EN ESTUDIANTES")
		else:
			messagebox.showwarning("ERROR", "USUARIO O CONTRASEÑA INCORRECTA")
	elif tipov=="Profesores":
		micursor.execute("SELECT * FROM PROFESORES WHERE CODIGO=? AND CONTRASEÑA=?",(Usuario,Contraseña))
		if micursor.fetchall():
			votop=0
			micursor.execute("SELECT VOTO FROM PROFESORES WHERE CODIGO=? AND CONTRASEÑA=? AND VOTO=?",(Usuario,Contraseña,votop))
			if micursor.fetchall():
				votacionesP(Usuario)
			else:messagebox.showwarning("ERROR", "EL USUARIO YA TIENE VOTO REGISTRADO EN PROFESORES")      
		else:
			messagebox.showwarning("ERROR", "USUARIO O CONTRASEÑA INCORRECTA")
	micursor.close()
	conexion.commit()
	conexion.close()

def texto(Textusu,TextCon,tipov):
	Usuario=Textusu.get()
	Contraseña=TextCon.get()
	Textusu.delete(0,END)
	TextCon.delete(0,END)
	inisiar_secionU(Usuario,Contraseña,tipov)

def estudiantes():
	raizr=Toplevel()
	raizr.geometry("650x650+0+0")
	raizr.resizable(width=False, height=False)
	raizr.iconbitmap("Logo_uis.ico")

	raiz=Frame(raizr,width=300, height=300)
	raiz.pack(pady=150)

	tipov="Estudiantes"
	TituloPrin=Label(raiz,text="Estudiantes", font=("Times New Roman",20))
	TituloPrin.grid(row=0, column=0,padx=0, pady=30)

	TituloUsu=Label(raiz,text="Nombre de usuario: ", font=("Times New Roman",16))
	TituloUsu.grid(row=1, column=0)

	Textusu=Entry(raiz)
	Textusu.grid(row=2, column=0,sticky="w",ipadx=26,ipady=3)

	TituloCon=Label(raiz,text="Contraseña:", font=("Times New Roman",16))
	TituloCon.grid(row=3, column=0,sticky="w")

	TextCon=Entry(raiz, show="*")
	TextCon.grid(row=4,column=0,sticky="w",ipadx=26,ipady=3)

	BotonInise=Button(raiz, text="INICIAR SESIÓN",command=lambda:texto(Textusu,TextCon,tipov),font=("Time New Roman",10))
	BotonInise.grid(row=5, column=0,pady=10, sticky="e")
		
	BotonRegre=Button(raiz, text="Regresar", font=("Time New Roman",10),command=lambda:raizr.destroy())
	BotonRegre.grid(row=6, column=0, sticky="e")

def profesores():
	raizd=Toplevel()
	raizd.title("SISTEMA DE VOTACIONES")
	raizd.geometry("650x650+0+0")
	raizd.resizable(width=False, height=False)
	raizd.iconbitmap("Logo_uis.ico")
	raiz=Frame(raizd, width=300, height=300)
	raiz.pack(pady=150)
	tipov="Profesores"
	TituloPrin=Label(raiz,text="Votaciones de Profesores", font=("Times New Roman",20))
	TituloPrin.grid(row=0, column=0, pady=30,columnspan=10)

	TituloUsu=Label(raiz,text="Nombre de usuario: ", font=("Times New Roman",16))
	TituloUsu.grid(row=1, column=0,sticky="w",padx=50)

	Textusu=Entry(raiz)
	Textusu.grid(row=2, column=0,sticky="w",ipadx=26,ipady=3,padx=50)

	TituloCon=Label(raiz,text="Contraseña:", font=("Times New Roman",16))
	TituloCon.grid(row=3, column=0,sticky="w",padx=50)

	TextCon=Entry(raiz, show="*")
	TextCon.grid(row=4,column=0,sticky="w",ipadx=26,ipady=3,padx=50)

	BotonInise=Button(raiz, text="INICIAR SESIÓN",command=lambda:texto(Textusu,TextCon,tipov), font=("Time New Roman",10))
	BotonInise.grid(row=5, column=0,pady=10, sticky="e",padx=50)

	BotonRegre=Button(raiz, text="Regresar", font=("Time New Roman",10),command=lambda:[ventanaprim,raizd.destroy()])
	BotonRegre.grid(row=6, column=0, sticky="e",padx=50)

	raiz.mainloop()

def ventanaprim():
	raizvp=Tk()
	raizvp.title("SISTEMA DE VOTACION UIS")
	raizvp.iconbitmap("Logo_uis.ico")
	raizvp.geometry("650x650+0+0")
	raizvp.resizable(width=False, height=False)
	imagen1=PhotoImage(file="Logo_Uis.png", master=raizvp)
	imagen2=PhotoImage(file="Fondo_nuevo.png", master=raizvp)
	imagenx=imagen2.subsample(1,1)
	lblimagen=Label(raizvp,image=imagen2)
	
	lblimagen.place(x=-3,y=-3)

	Botonadmin=Button(raizvp,image=imagen1,command=lambda:admin())
	Botonadmin.place(x=0,y=0)
	Botonadmin.config(relief=FLAT,bg="#466496")

	raiz=Frame(raizvp,width=300, height=500)
	raiz.pack(pady=150)
	raiz.config(bg="#343444")

	Titulo=Label(raiz, text="Sistema De Votaciones", font=("Times New Roman",20),fg="White")
	Titulo.grid(row=0, column=0, padx=10,pady=50)
	Titulo.config(bg="#343444")

	Boton_Profe=Button(raiz, text="Profesores",state=ACTIVE, font=("Times New Roman",16),fg="White", command=lambda:profesores())
	Boton_Profe.grid(row=1, column=0, padx=10,pady=10)
	Boton_Profe.config(bg="#343444")


	Boton_Alum=Button(raiz, text="Estudiantes",state=ACTIVE, font=("Times New Roman",16),fg="White",command=lambda:estudiantes())
	Boton_Alum.grid(row=2, column=0,padx=10,pady=30)
	Boton_Alum.config(bg="#343444")

	Button(raizvp, text='Salir', font=("Times New Roman",16),fg="White",bg="#343444", command=lambda:(raizvp.destroy(), inicioP())).place(x=590, y=600)

	def admin():
		raizprin=Toplevel()
		raizprin.title("ADMINISTRADOR")
		raizprin.geometry("650x650+0+0")
		raizprin.resizable(width=False, height=False)
		raizprin.iconbitmap("Logo_uis.ico")
		imagen=PhotoImage(file="Logo_Uis_H.png")
		lblimagen1=Label(raizprin,image=imagen)
		lblimagen1.place(x=0,y=0)

		def inicio():
			vinicio=Frame(raizprin,width=700, height=700)
			vinicio.pack(pady=100)
			titulo=Label(vinicio, text="Administrador",font=("Times New Roman",20))
			titulo.grid(row=0, column=0, columnspan=10,pady=50)
			TituloUsu=Label(vinicio,text="Nombre de usuario: ", font=("Times New Roman",16))
			TituloUsu.grid(row=1, column=0,sticky="w",padx=50)

			Textusu=Entry(vinicio)
			Textusu.grid(row=2, column=0,sticky="w",ipadx=26,ipady=3,padx=50)

			TituloCon=Label(vinicio,text="Contraseña:", font=("Times New Roman",16))
			TituloCon.grid(row=3, column=0,sticky="w",padx=50)

			TextCon=Entry(vinicio, show="*")
			TextCon.grid(row=4,column=0,sticky="w",ipadx=26,ipady=3,padx=50)

			BotonInise=Button(vinicio, text="INICIAR SESIÓN",command=lambda:[inicio_seciona(Textusu,TextCon),vinicio.destroy()], font=("Time New Roman",10))
			BotonInise.grid(row=5, column=0,pady=10, sticky="e",padx=50)

			BotonRegre=Button(vinicio, text="Regresar", font=("Time New Roman",10),command=lambda:[ventanaprim,raizprin.destroy()])
			BotonRegre.grid(row=6, column=0, sticky="e",padx=50)

		def inicio_seciona(Textusu,TextCon):
			Usuario=Textusu.get()
			Contraseña=TextCon.get()
			
			conexion=sqlite3.connect("Base_total")
			micursor=conexion.cursor()
			micursor.execute("SELECT * FROM ADMINISTRATIVO WHERE USUARIO=? AND CONTRASEÑA=?",(Usuario,Contraseña))

			if micursor.fetchall():
				verificado(Usuario)
			else:
				inicio()
				messagebox.showwarning("ERROR", "USUARIO O CONTRASEÑA INCORRECTA")

		def verificado(Usuario):
			v2=Frame(raizprin,width=700, height=700)
			v2.pack(pady=100)

			titulo=Label(v2, text="Administrador",font=("Times New Roman",20))
			titulo.grid(row=0, column=0, columnspan=10,pady=50)

			HabilitarEs=Button(v2, text="Habilitar Votaciones Estudiantes", font=("Times New Roman",14),command=lambda:habilitarE())
			HabilitarEs.grid(row=1, column=0, pady=10,padx=10)
			HabilitarEs.config(width=28)

			DesabilitarEs=Button(v2, text="Deshabilitar Votaciones Estudiantes", font=("Times New Roman",14),command=lambda:deshabilitarE())
			DesabilitarEs.grid(row=2, column=0, pady=10,padx=10)
			DesabilitarEs.config(width=28)

			#agregarcanEs=Button(v2, text=" Agregar Candidato Estudiantes", font=("Times New Roman",14))
			#agregarcanEs.grid(row=3, column=0, pady=10,padx=10)
			#agregarcanEs.config(width=28)

			HabilitarPr=Button(v2, text="Habilitar Votaciones Profesores", font=("Times New Roman",14),command=lambda:habilitarP())
			HabilitarPr.grid(row=1, column=1, pady=10,padx=10)
			HabilitarPr.config(width=28)
			DesabilitarPr=Button(v2, text="Deshabilitar Votaciones Profesores", font=("Times New Roman",14),command=lambda:deshabilitarP())
			DesabilitarPr.grid(row=2, column=1, pady=10,padx=10)
			DesabilitarPr.config(width=28)

			#agregarcanPr=Button(v2, text=" Agregar Candidato Profesores", font=("Times New Roman",14))
			#agregarcanPr.grid(row=3, column=1, pady=10,padx=10)
			#agregarcanPr.config(width=28)

			menuprin=Button(v2,text="Menu Principal",font=("Times New Roman",14),command=lambda:[ventanaprim,raizprin.destroy()])
			menuprin.grid(row=6, columnspan=3, pady=10)
			menuprin.config(width=18)
		inicio()
		raizprin.mainloop()

	def habilitarE():
		Boton_Alum.config(state=ACTIVE)
		messagebox.showinfo("Votaciones","Votacion de Estudiantes Activada")
	def habilitarP():
		Boton_Profe.config(state=ACTIVE)
		messagebox.showinfo("Votaciones","Votacion de Profesores Activada")
	def deshabilitarP():
		Boton_Profe.config(state=DISABLED)
		messagebox.showinfo("Votaciones","Votacion de Estudiantes Deshabilitada")
	def deshabilitarE():
		Boton_Alum.config(state=DISABLED)
		messagebox.showinfo("Votaciones","Votacion de Estudiantes Deshabilitada")
	raiz.mainloop()

################################### Adriana Rodriguez #############################################

def AdrianaR():
	def consulta_notas():
		conn = sqlite3.connect('Base_total')
		c = conn.cursor()

		c.execute(
			"SELECT SABER,SABERHACER,SER,MATERIAQ FROM NOTAS INNER JOIN ESTUDIANTES ON "
			" ESTUDIANTES.CODIGO = NOTAS.CODIGON WHERE CODIGO = '{}'".format(
				username_verify.get()))

		table = c.fetchall()

		conn.close()
		return table, username_verify.get()

	def login():
		"""
        Funcion para verificar si el correo y contraseña suministrados están
        efectivamente en la base de datos
        """
		global username_verify, password_verify
		correo, clave = username_verify.get(), password_verify.get()
		conn = sqlite3.connect('Base_total')
		c = conn.cursor()
		sql1 = "SELECT CODIGO FROM ESTUDIANTES WHERE CODIGO = '{}'".format(correo)
		sql2 = "SELECT CONTRASEÑA FROM ESTUDIANTES WHERE CONTRASEÑA = '{}'".format(clave)

		c.execute(sql1)
		correo_bd = c.fetchone()
		c.execute(sql2)
		clave_bd = c.fetchone()
		conn.close()

		if correo_bd == None or clave_bd == None:
			login_fail()
		else:
			login_sucess()

	def salir():
		login_success_screen.destroy()


	def login_sucess():
		global main_screen, login_success_screen, user_get
		login_success_screen = Toplevel(main_screen)
		login_success_screen.title("Success")
		login_success_screen.resizable(0, 0)
		table, user_get = consulta_notas()
		print(table)

		conn = sqlite3.connect('Base_total')
		c = conn.cursor()
		sql1 = "SELECT NOMBRE FROM ESTUDIANTES WHERE CODIGO = '{}'".format(user_get)
		c.execute(sql1)
		nombre_bd = c.fetchone()
		conn.close()

		Label(login_success_screen, text='Bienvenido ' + nombre_bd[0]).grid(row=0, column=0, padx=5, pady=5,
																			columnspan=5)

		Tabla = ttk.Treeview(login_success_screen, columns=(1, 2, 3, 4), show='headings', height='5')
		Tabla.grid(row=1, column=0, padx=5, pady=5, columnspan=5)


		Tabla.heading(1, text='Saber')
		Tabla.heading(2, text='Saber Hacer ')
		Tabla.heading(3, text='Ser')
		Tabla.heading(4, text='Materia')

		rueda = Scrollbar(login_success_screen, command=Tabla.yview)
		rueda.grid(row=1, column=7, sticky='nsew')
		Tabla.config(yscrollcommand=rueda.set)

		Dat = Tabla.get_children()
		for i in Dat:
			Tabla.delete(i)

		for i in table:
			Tabla.insert('', 'end', values=i)

		Button(login_success_screen, text='Datos', command=editar) \
			.grid(row=3, column=1, sticky='we', padx=5, pady=5)
		Button(login_success_screen, text='Salir', command=lambda: salir()) \
			.grid(row=3, column=3, sticky='we', padx=5, pady=5)

		username_login_entry.delete(0, 'end')
		password__login_entry.delete(0, 'end')

	def login_fail():
		messagebox.askretrycancel('Error', 'Usuario o contraseña incorrecta')

	def get_values(user):
		conn = sqlite3.connect('Base_total')
		c = conn.cursor()
		c.execute("SELECT * FROM ESTUDIANTES WHERE CODIGO = '{}'".format(user))
		table = c.fetchall()
		conn.close()

		return table

	def actualizar_bd():


		global primer_nombre_entry, segundo_nombre, primer_apellido, segundo_apellido, tipo_documento, numero_documento, nombre_padre, nombre_madre, telefono, eps, puntaje_sisben, correo, direccion, clave, edit_screen
		ans = get_values(user_get)

		if len(primer_nombre_entry.get()) == 0:
			primer_nombre1 = ans[0][0]
		else:
			primer_nombre1 = primer_nombre_entry.get()

		if len(segundo_nombre_entry.get()) == 0:
			segundo_nombre1 = ans[0][1]
		else:
			segundo_nombre1 = segundo_nombre_entry.get()
		if len(primer_apellido_entry.get()) == 0:
			primer_apellido1 = ans[0][2]
		else:
			primer_apellido1 = primer_apellido_entry.get()

		if len(segundo_apellido_entry.get()) == 0:
			segundo_apellido1 = ans[0][3]
		else:
			segundo_apellido1 = segundo_apellido_entry.get()

		if len(tipo_documento_entry.get()) == 0:
			tipo_documento1 = ans[0][4]
		else:
			tipo_documento1 = tipo_documento_entry.get()
		if len(numero_documento_entry.get()) == 0:
			numero_documento1 = int(ans[0][5])
		else:
			numero_documento1 = int(numero_documento_entry.get())
		if len(nombre_padre_entry.get()) == 0:
			nombre_padre1 = ans[0][6]
		else:
			nombre_padre1 = nombre_padre_entry.get()
		if len(nombre_madre_entry.get()) == 0:
			nombre_madre1 = ans[0][7]
		else:
			nombre_madre1 = nombre_madre_entry.get()
		if len(telefono_entry.get()) == 0:
			telefono1 = int(ans[0][8])
		else:
			telefono1 = int(telefono_entry.get())

		if len(eps_entry.get()) == 0:
			eps1 = ans[0][9]
		else:
			eps1 = eps_entry.get()

		if len(puntaje_sisben_entry.get()) == 0:
			puntaje_sisben1 = float(ans[0][10])
		else:
			puntaje_sisben1 = float(puntaje_sisben_entry.get())
		if len(correo_entry.get()) == 0:
			correo1 = ans[0][11]
		else:
			correo1 = correo_entry.get()
		if len(direccion_entry.get()) == 0:
			direccion1 = ans[0][12]
		else:
			direccion1 = direccion_entry.get()

		if len(clave_entry.get()) == 0:
			clave1 = ans[0][13]
		else:
			clave1 = clave_entry.get()
		conn = sqlite3.connect('test.db')
		c = conn.cursor()
		sql = "UPDATE ESTUDIANTE SET primer_nombre = '{}',segundo_nombre = '{}',primer_apellido = '{}',segundo_apellido = '{}',tipo_documento = '{}',numero_documento = {},nombre_padre = '{}',nombre_madre = '{}',telefono = {},eps = '{}',puntaje_sisben = {},correo = '{}',direccion = '{}',clave = '{}' WHERE numero_documento = {} ".format(
			primer_nombre1, segundo_nombre1, primer_apellido1, segundo_apellido1, tipo_documento1,
			numero_documento1, nombre_padre1, nombre_madre1, telefono1, eps1, puntaje_sisben1, correo1, direccion1,
			clave1, user_get)
		c.execute(sql)
		conn.commit()
		conn.close()
		edit_screen.destroy()

	def editar():
		global primer_nombre_entry, segundo_nombre_entry, primer_apellido_entry, segundo_apellido_entry, tipo_documento_entry, numero_documento_entry, nombre_padre_entry, nombre_madre_entry, telefono_entry, eps_entry, puntaje_sisben_entry, correo_entry, direccion_entry, clave_entry, edit_screen, user_get
		edit_screen = Tk()
		edit_screen.geometry("800x600")
		edit_screen.title("Editar")
		edit_screen.resizable(0, 0)

		ans = get_values(user_get)
		i = 0

		primer_nombre = StringVar()
		segundo_nombre = StringVar()
		primer_apellido = StringVar()
		segundo_apellido = StringVar()
		tipo_documento = StringVar()
		numero_documento = StringVar()
		nombre_padre = StringVar()
		nombre_madre = StringVar()
		telefono = StringVar()
		eps = StringVar()
		puntaje_sisben = StringVar()
		correo = StringVar()
		direccion = StringVar()
		clave = StringVar()

		Label(edit_screen, text="Primer Nombre").pack()
		primer_nombre_entry = Entry(edit_screen, textvariable=primer_nombre)
		primer_nombre_entry.insert(END, ans[0][i])
		i += 1
		primer_nombre_entry.pack()
		Label(edit_screen, text="").pack()

		Label(edit_screen, text="Segundo Nombre").pack()
		segundo_nombre_entry = Entry(edit_screen, textvariable=segundo_nombre)
		segundo_nombre_entry.insert(END, ans[0][i])
		i += 1
		segundo_nombre_entry.pack()
		Label(edit_screen, text="").pack()

		Label(edit_screen, text="Primer Apellido").pack()
		primer_apellido_entry = Entry(edit_screen, textvariable=primer_apellido)
		primer_apellido_entry.insert(END, ans[0][i])
		i += 1
		primer_apellido_entry.pack()
		Label(edit_screen, text="").pack()

		Label(edit_screen, text="Segundo Apellido").pack()
		segundo_apellido_entry = Entry(edit_screen, textvariable=segundo_apellido)
		segundo_apellido_entry.insert(END, ans[0][i])
		i += 1
		segundo_apellido_entry.pack()
		Label(edit_screen, text="").pack()

		Label(edit_screen, text="Tipo Documento").pack()
		tipo_documento_entry = Entry(edit_screen, textvariable=tipo_documento)
		tipo_documento_entry.insert(END, ans[0][i])
		i += 1
		tipo_documento_entry.pack()
		Label(edit_screen, text="").pack()

		Label(edit_screen, text="Numero Documento").pack()
		numero_documento_entry = Entry(edit_screen, textvariable=numero_documento)
		numero_documento_entry.insert(END, ans[0][i])
		i += 1
		numero_documento_entry.pack()
		Label(edit_screen, text="").pack()

		Label(edit_screen, text="Nombre Padre").pack()
		nombre_padre_entry = Entry(edit_screen, textvariable=nombre_padre)
		nombre_padre_entry.insert(END, ans[0][i])
		i += 1
		nombre_padre_entry.pack()
		Label(edit_screen, text="").pack()

		Label(edit_screen, text="Nombre Madre").pack()
		nombre_madre_entry = Entry(edit_screen, textvariable=nombre_madre)
		nombre_madre_entry.insert(END, ans[0][i])
		i += 1
		nombre_madre_entry.pack()
		Label(edit_screen, text="").pack()

		Label(edit_screen, text="Telefono").pack()
		telefono_entry = Entry(edit_screen, textvariable=telefono)
		telefono_entry.insert(END, ans[0][i])
		i += 1
		telefono_entry.pack()
		Label(edit_screen, text="").pack()

		l1 = Label(edit_screen, text="Eps").place(x=550, y=0)
		eps_entry = Entry(edit_screen, textvariable=eps)
		eps_entry.place(x=500, y=20)
		Entry(edit_screen, textvariable=eps).insert(END, ans[0][i])
		i += 1

		Label(edit_screen, text="").pack()

		Label(edit_screen, text="Puntaje Sisben").place(x=500, y=50)
		puntaje_sisben_entry = Entry(edit_screen, textvariable=puntaje_sisben)
		puntaje_sisben_entry.place(x=500, y=80)
		Entry(edit_screen, textvariable=puntaje_sisben).insert(END, ans[0][i])
		i += 1
		Label(edit_screen, text="").pack()

		Label(edit_screen, text="Correo").place(x=540, y=120)
		correo_entry = Entry(edit_screen, textvariable=correo)
		correo_entry.place(x=500, y=140)
		Entry(edit_screen, textvariable=correo).insert(END, ans[0][i])
		i += 1
		Label(edit_screen, text="").pack()

		Label(edit_screen, text="Direccion").place(x=540, y=180)
		direccion_entry = Entry(edit_screen, textvariable=direccion)
		direccion_entry.place(x=500, y=200)
		Entry(edit_screen, textvariable=direccion).insert(END, ans[0][i])
		i += 1
		Label(edit_screen, text="").pack()

		Label(edit_screen, text="Clave").place(x=525, y=240)
		clave_entry = Entry(edit_screen, textvariable=clave)
		clave_entry.place(x=500, y=265)
		Entry(edit_screen, textvariable=clave).insert(END, ans[0][i])
		i += 1

		Label(edit_screen, text="").pack()
		Button(edit_screen, text="Actualizar", width=10, height=1, command=actualizar_bd).place(x=400, y=550)
		edit_screen.mainloop()

	def main():
		global username_verify, password_verify, main_screen, username_login_entry, password__login_entry
		main_screen = Tk()
		main_screen.geometry("500x200")
		main_screen.title("Login")

		username_verify = StringVar()
		password_verify = StringVar()

		Label(main_screen, text="Usuario").pack()
		username_login_entry = Entry(main_screen, textvariable=username_verify)
		username_login_entry.pack()
		Label(main_screen, text="").pack()
		Label(main_screen, text="Contraseña * ").pack()
		password__login_entry = Entry(main_screen, textvariable=password_verify, show='*')
		password__login_entry.pack()
		Label(main_screen, text="").pack()
		Button(main_screen, text="Login", width=10, height=1, command=login).pack()

		Label(main_screen, text="").pack()
		Button(main_screen, text="Salir", width=10, height=1, command=lambda: (main_screen.destroy(),inicioP())).pack()
		main_screen.mainloop()

	main()
	
###################################Camilo Fuquen Crear Encuestas###################################
def CrearEncuestas():
	coneccion = sqlite3.connect("Base_total")
	cursor = coneccion.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS ENCUESTAS (ENCUESTA INTEGER PRIMARY KEY AUTOINCREMENT,
    	NOMBRE TEXT,
    	PREGUNTA1 TEXT,
    	PREGUNTA2 TEXT,
    	PREGUNTA3 TEXT,
    	PREGUNTA4 TEXT,
    	PREGUNTA5 TEXT,
    	PREGUNTA6 TEXT,
    	PREGUNTA7 TEXT,
    	PREGUNTA8 TEXT,
    	PREGUNTA9 TEXT,
    	PREGUNTA10 TEXT,
    	TIPO INTEGER)""")
	cursor.close()
	coneccion.close()
	nuevo=Tk()
	nuevo.title("CREAR ENCUESTAS")
	nuevo.config(bg='AliceBlue')

	Label(nuevo,text='Selecione el tipo de respuesta\n que desea implementar',bg='AliceBlue').grid(row=0,column=0)
	Button(nuevo,text='Seleccion multiple',command=lambda:(nuevo.destroy(),preguntasM()),bg='AliceBlue').grid(row=1,column=0,pady=5,padx=5)
	Button(nuevo,text='Respuesta abierta',command=lambda:(nuevo.destroy(),preguntasA()),bg='AliceBlue').grid(row=2,column=0,pady=5,padx=5)
	Button(nuevo, text='Volver', command=lambda:(nuevo.destroy(),administrativo() )).grid(row=3,column=0,pady=5,padx=5)
	nuevo.mainloop()
def preguntasM():#multiple
        def guardar():
                coneccion = sqlite3.connect("Base_total")
                cursor = coneccion.cursor()
                cursor.execute("INSERT INTO ENCUESTAS(ENCUESTA,NOMBRE,PREGUNTA1,PREGUNTA2,PREGUNTA3,PREGUNTA4,PREGUNTA5,PREGUNTA6,PREGUNTA7,PREGUNTA8,PREGUNTA9,PREGUNTA10,TIPO) VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,1)",(nombre.get(), preguntas.get(),preguntas2.get(),preguntas3.get(),preguntas4.get(),preguntas5.get(),preguntas6.get(),preguntas7.get(),preguntas8.get(),preguntas9.get(),preguntas10.get()))
                coneccion.commit()
                cursor.close()
                coneccion.close()
                messagebox.showinfo('Encuesta Creada', 'Encuesta creada correctamente.')

        crear=Tk()
        crear.title("ENCUESTA NUEVA")
        crear.config(bg='AliceBlue')

      
        nombre = StringVar()
        preguntas = StringVar()
        preguntas2 = StringVar()
        preguntas3 = StringVar()
        preguntas4 = StringVar()
        preguntas5 = StringVar()
        preguntas6 = StringVar()
        preguntas7 = StringVar()
        preguntas8 = StringVar()
        preguntas9 = StringVar()
        preguntas10 = StringVar()
    
        Label(crear, text="Nombre de la encuesta: ",bg='AliceBlue').grid(row=0,column=0, pady=10, padx=10)
        Entry(crear, width=20, textvariable=nombre).grid(row=0,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="1) ",bg='AliceBlue').grid(row=1,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas).grid(row=1,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="2) ",bg='AliceBlue').grid(row=2,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas2).grid(row=2,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="3) ",bg='AliceBlue').grid(row=3,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas3).grid(row=3,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="4) ",bg='AliceBlue').grid(row=4,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas4).grid(row=4,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="5) ",bg='AliceBlue').grid(row=5,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas5).grid(row=5,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="6) ",bg='AliceBlue').grid(row=6,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas6).grid(row=6,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="7) ",bg='AliceBlue').grid(row=7,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas7).grid(row=7,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="8) ",bg='AliceBlue').grid(row=8,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas8).grid(row=8,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="9) ",bg='AliceBlue').grid(row=9,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas9).grid(row=9,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="10) ",bg='AliceBlue').grid(row=10,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas10).grid(row=10,column=1, sticky='w',padx=10,pady=10)
				
        Button(crear, text="Crear", command=lambda:(guardar(),crear.destroy(), CrearEncuestas())).grid(row=11,column=1, pady=10, padx=10)
        Button(crear, text="Volver", command=lambda:(crear.destroy(), CrearEncuestas())).grid(row=11,column=0, pady=10, padx=10)
        crear.mainloop()

def preguntasA():#abierta
        def guardar():
                coneccion = sqlite3.connect("Base_total")
                cursor = coneccion.cursor()
                cursor.execute("INSERT INTO ENCUESTAS(ENCUESTA,NOMBRE,PREGUNTA1,PREGUNTA2,PREGUNTA3,PREGUNTA4,PREGUNTA5,PREGUNTA6,PREGUNTA7,PREGUNTA8,PREGUNTA9,PREGUNTA10,TIPO) VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,2)",(nombre.get(), preguntas.get(),preguntas2.get(),preguntas3.get(),preguntas4.get(),preguntas5.get(),preguntas6.get(),preguntas7.get(),preguntas8.get(),preguntas9.get(),preguntas10.get()))
                coneccion.commit()
                cursor.close()
                coneccion.close()
                messagebox.showinfo('Encuesta Creada', 'Encuesta creada correctamente.')

        crear=Tk()
        crear.title("ENCUESTA NUEVA")
        crear.config(bg='AliceBlue')

  

        nombre = StringVar()
        preguntas = StringVar()
        preguntas2 = StringVar()
        preguntas3 = StringVar()
        preguntas4 = StringVar()
        preguntas5 = StringVar()
        preguntas6 = StringVar()
        preguntas7 = StringVar()
        preguntas8 = StringVar()
        preguntas9 = StringVar()
        preguntas10 = StringVar()
    
        Label(crear, text="Nombre de la encuesta: ",bg='AliceBlue').grid(row=0,column=0, pady=10, padx=10)
        Entry(crear, width=20, textvariable=nombre).grid(row=0,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="1) ",bg='AliceBlue').grid(row=1,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas).grid(row=1,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="2) ",bg='AliceBlue').grid(row=2,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas2).grid(row=2,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="3) ",bg='AliceBlue').grid(row=3,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas3).grid(row=3,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="4) ",bg='AliceBlue').grid(row=4,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas4).grid(row=4,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="5) ",bg='AliceBlue').grid(row=5,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas5).grid(row=5,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="6) ",bg='AliceBlue').grid(row=6,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas6).grid(row=6,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="7) ",bg='AliceBlue').grid(row=7,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas7).grid(row=7,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="8) ",bg='AliceBlue').grid(row=8,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas8).grid(row=8,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="9) ",bg='AliceBlue').grid(row=9,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas9).grid(row=9,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="10) ",bg='AliceBlue').grid(row=10,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas10).grid(row=10,column=1, sticky='w',padx=10,pady=10)
				
        Button(crear, text="Crear", command=lambda:(guardar(),crear.destroy(),CrearEncuestas())).grid(row=11,column=1, pady=10, padx=10)
        Button(crear, text="Volver", command=lambda:(crear.destroy(),CrearEncuestas())).grid(row=11,column=0, pady=10, padx=10)

        crear.mainloop()
###############################Camilo Valcarcel  Estudiantes  #####################################

class Biblioteca:

    def __init__(self):

        self.ven = Tk()
        self.ven.title('Biblioteca')
        self.ven.geometry('1000x668')
        self.ven.resizable(0, 0)
        self.Mensaje = Label()

        q = PhotoImage(file="Imagen3.gif")
        Label(self.ven, image=q).place(x=0, y=0)

        Label(self.ven, text='BIENVENIDOS',bg='#E59049', fg='white', font=('', 30)).place(x=100, y=55)
        Label(self.ven, text='BIBLIOTECA VIRTUAL',bg='#E59049', fg='white', font=('', 30)).place(x=200, y=115)


        Button(self.ven, text='Volver', command=(lambda:(self.ven.destroy(), inicioP())) , font=('', 12), fg='#3DC370').place(x=920,y=600)

        self.Sistema_Busqueda()

        self.ven.mainloop()

    def Sistema_Busqueda(self):
        try:
            self.ven_nuevo.destroy()
        except AttributeError:
            pass

        self.ven_nuevo = Frame(self.ven)
        self.ven_nuevo.place(x=310, y=260)

        Label(self.ven_nuevo, text='SISTEMA DE CONSULTA',fg='#4E944E',font=('', 16))\
            .grid(row=0, column=0, padx=15, pady=15, columnspan=4)

        self.textobuscar = StringVar()
        cuadronombre = Entry(self.ven_nuevo, textvariable=self.textobuscar)
        cuadronombre.grid(row=1, column=0, columnspan=3, padx=15, pady=5, sticky=W + E)
        cuadronombre.config(fg='blue', justify='center')

        buscar = Button(self.ven_nuevo, text='Buscar', command=lambda: self.Buscador(), font=('', 12), fg='#3DC370')
        buscar.grid(row=1, column=3, sticky='', padx=5, pady=5)

        self.Valor_rb = IntVar()
        Radiobutton(self.ven_nuevo, text='Didacticos',fg='#5EA0A2', variable=self.Valor_rb, value=1, font=('', 12)) \
            .grid(row=2, column=0, sticky='', padx=5, pady=5)
        Radiobutton(self.ven_nuevo, text='Folletos',fg='#5EA0A2', variable=self.Valor_rb, value=2, font=('', 12)) \
            .grid(row=2, column=1, sticky='', padx=5, pady=5)
        Radiobutton(self.ven_nuevo, text='Libros',fg='#5EA0A2', variable=self.Valor_rb, value=3, font=('', 12)) \
            .grid(row=2, column=2, sticky='', padx=5, pady=5)
        Radiobutton(self.ven_nuevo, text='Revistas', fg='#5EA0A2', variable=self.Valor_rb, value=4, font=('', 12)) \
            .grid(row=2, column=3, sticky='', padx=5, pady=5)

        Label(self.ven_nuevo, text='                                                            ', font=('', 16))\
            .grid(row=3, column=0, sticky=W + E, padx=5, pady=5, columnspan=4)

    def Buscador(self):
        f = self.Valor_rb.get()
        if (f == 1  > 0 or f == 2 or f == 3 or  f == 4) and len(self.textobuscar.get()):

            time.sleep(1.5)
            self.ven_nuevo.destroy()
            self.Resultados()

        else:
            Label(self.ven_nuevo, text='Digite una palabra y seleccione una opción',fg='#F07010', font=('', 10))\
                .grid(row=3, column=0, sticky=W + E, padx=5, pady=5, columnspan=4)

    def Resultados(self):
        try:
            self.ven_nuevo.destroy()
        except AttributeError:
            pass

        self.ven_nuevo = Frame(self.ven)
        self.ven_nuevo.place(x=90, y=260)

        Label(self.ven_nuevo, text='Resultados').grid(row=0, column=0, padx=5, pady=5, columnspan=5)

        self.Tabla = ttk.Treeview(self.ven_nuevo, columns=(1, 2, 3, 4), show='headings', height='10')
        self.Tabla.grid(row=1, column=0, padx=5, pady=5, columnspan=5)

        rueda = Scrollbar(self.ven_nuevo, command=self.Tabla.yview)
        rueda.grid(row=1, column=7, sticky='nsew')
        self.Tabla.config(yscrollcommand=rueda.set)


        libros = self.Tabla.get_children()
        for i in libros:
            self.Tabla.delete(i)



        if self.Valor_rb.get() == 3:

            self.Tabla.heading(1, text='Codigo')
            self.Tabla.heading(2, text='Titulo')
            self.Tabla.heading(3, text='Autor')
            self.Tabla.heading(4, text='Tipo')



            consulta = 'SELECT * FROM Libros ORDER BY Titulo ASC'
            filas = self.Conexion(consulta)
            for i in filas:
                self.Tabla.insert('', 'end', values=i)

        elif self.Valor_rb.get() == 1:

            self.Tabla.heading(1, text='Codigo')
            self.Tabla.heading(2, text='Nombre')
            self.Tabla.heading(3, text='Referencia')
            self.Tabla.heading(4, text='Tipo')


            consulta = 'SELECT * FROM Didacticos ORDER BY Nombre ASC'
            filas = self.Conexion(consulta)
            for i in filas:
                self.Tabla.insert('', 'end', values=i)

        elif self.Valor_rb.get() == 2:

            self.Tabla.heading(1, text='Codigo')
            self.Tabla.heading(2, text='Nombre')
            self.Tabla.heading(3, text='Referencia')
            self.Tabla.heading(4, text='Tipo')

            consulta = 'SELECT * FROM Folletos ORDER BY Nombre ASC'
            filas = self.Conexion(consulta)
            for i in filas:
                self.Tabla.insert('', 'end', values=i)

        elif self.Valor_rb.get() == 4:

            self.Tabla.heading(1, text='Codigo')
            self.Tabla.heading(2, text='Nombre')
            self.Tabla.heading(3, text='Referencia')
            self.Tabla.heading(4, text='Tipo')

            consulta = 'SELECT * FROM Revistas ORDER BY Nombre ASC'
            filas = self.Conexion(consulta)
            for i in filas:
                self.Tabla.insert('', 'end', values=i)

        Label(self.ven_nuevo, text='', fg='green').grid(row=5, column=0, padx=5, pady=5, columnspan=5, sticky='')

        Button(self.ven_nuevo, text='Salir', command=lambda: self.Sistema_Busqueda())\
            .grid(row=6, column=2, sticky='we', padx=5,pady=5)

    def Conexion(self, consulta, parametros=()):

        with sqlite3.connect('Base_total') as conn:
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS Folletos(Codigo NUMERIC,'
                           'Nombre TEXT , Referencia TEXT, Tipo TEXT, Adquirido TEXT )')
            cursor.execute('CREATE TABLE IF NOT EXISTS Didacticos(Codigo Codigo NUMERIC,'
                           'Nombre TEXT , Referencia TEXT, Tipo TEXT, Adquirido TEXT)')
            cursor.execute('CREATE TABLE IF NOT EXISTS Libros(Codigo Codigo NUMERIC,'
                           'Titulo TEXT , Autor TEXT, Tipo TEXT, Adquirido TEXT)')
            cursor.execute('CREATE TABLE IF NOT EXISTS Revistas(Codigo Codigo NUMERIC ,'
                           'Nombre TEXT , Referencia TEXT, Tipo TEXT,Adquirido TEXT)')

            resultado = cursor.execute(consulta, parametros)
            conn.commit()
        return resultado

    def Validar(self, z, x, c, v, b):

        a = False

        if len(z) > 0 and len(x) > 0 and len(c) > 0 and len(v) > 0 and len(b) > 0 and \
                len(z) < 20 and len(x) < 20 and len(c) < 20 and len(v) < 20 and len(b) < 20:
            a = True

        return a

    def Validar_entero(self, valor):

        b = 0
        while True:
            try:
                b = int(valor)
                return b
            except ValueError:
                break
        return b

###############################Fuquen Responder Encuentas##########################################
def ResponderEncuestas():
	def verificacion():
		global encontrarENCUESTA
		if ENCUESTA.get().isdigit():
			coneccion=sqlite3.connect("Base_total")
			cursor=coneccion.cursor()
			cursor.execute("SELECT * FROM ENCUESTAS WHERE ENCUESTA='%s'"%(int(ENCUESTA.get())))
			encuesta=cursor.fetchall()
			cursor.close()
			coneccion.close()
			for i in range(len(encuesta)):
				if int(ENCUESTA.get())==encuesta[i][0]:
					encuesta_encontrada=encuesta[i]
					encontrarENCUESTA=True
			if encontrarENCUESTA:
				nombre.set(encuesta_encontrada[1])
				preguntas.set(encuesta_encontrada[2])
				preguntas2.set(encuesta_encontrada[3])
				preguntas3.set(encuesta_encontrada[4])
				preguntas4.set(encuesta_encontrada[5])
				preguntas5.set(encuesta_encontrada[6])
				preguntas6.set(encuesta_encontrada[7])
				preguntas7.set(encuesta_encontrada[8])
				preguntas8.set(encuesta_encontrada[9])
				preguntas9.set(encuesta_encontrada[10])
				preguntas10.set(encuesta_encontrada[11])
				tipo.set(encuesta_encontrada[12])
			else:
				if messagebox.askretrycancel('ENCUESTA incorrecta','Por favor verifique que la ENCUESTA exista'):
					pass
				else:
					Buscar.destroy()
					inicioP()
		else:
			if messagebox.askretrycancel('ENCUESTA incorrecta','Por favor verifique que la ENCUESTA sea un numero.'):
				pass
			else:
				Buscar.destroy()
				inicioP()

	def actualizar():
		textID.delete('1.0','end')
		textNombre.delete('1.0','end')
		coneccion=sqlite3.connect("Base_total")
		cursor=coneccion.cursor()
		cursor.execute("SELECT * FROM ENCUESTAS")
		encuesta=cursor.fetchall()
		for i in encuesta:
			textID.insert(INSERT,i[0])
			textID.insert(INSERT,'\n')
			textNombre.insert(INSERT,i[1]+'\n')
		cursor.close()
		coneccion.close()

	coneccion = sqlite3.connect("Base_total")
	cursor = coneccion.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS ENCUESTAS (ENCUESTA INTEGER PRIMARY KEY AUTOINCREMENT,
    	NOMBRE TEXT,
    	PREGUNTA1 TEXT,
    	PREGUNTA2 TEXT,
    	PREGUNTA3 TEXT,
    	PREGUNTA4 TEXT,
    	PREGUNTA5 TEXT,
    	PREGUNTA6 TEXT,
    	PREGUNTA7 TEXT,
    	PREGUNTA8 TEXT,
    	PREGUNTA9 TEXT,
    	PREGUNTA10 TEXT,
    	TIPO INTEGER)""")
	cursor.close()
	coneccion.close()

	coneccion = sqlite3.connect("Base_total")
	cursor = coneccion.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS RESPUESTAS (NOMBRE TEXT,
    	PREGUNTA1 TEXT,
    	PREGUNTA2 TEXT,
    	PREGUNTA3 TEXT,
    	PREGUNTA4 TEXT,
    	PREGUNTA5 TEXT,
    	PREGUNTA6 TEXT,
    	PREGUNTA7 TEXT,
    	PREGUNTA8 TEXT,
    	PREGUNTA9 TEXT,
    	PREGUNTA10 TEXT,
    	TIPO INTEGER)""")
	cursor.close()
	coneccion.close()

	Buscar=Tk()
	Buscar.title("BUSCAR ENCUESTA")
	Buscar.config(bg='AliceBlue')

	global nombre, preguntas, preguntas2, preguntas3, preguntas4, preguntas5, preguntas6, preguntas7, preguntas8, preguntas9, preguntas10, tipo
	ENCUESTA=StringVar()
	nombre=StringVar()
	preguntas=StringVar()
	preguntas2=StringVar()
	preguntas3=StringVar()
	preguntas4=StringVar()
	preguntas5=StringVar()
	preguntas6=StringVar()
	preguntas7=StringVar()
	preguntas8=StringVar()
	preguntas9=StringVar()
	preguntas10=StringVar()
	tipo=IntVar()
	global encontrarENCUESTA
	encontrarENCUESTA=False

	global textNombre, textID

	Label(Buscar,text='', bg='AliceBlue').grid(row=1,column=0)
	Label(Buscar,text='ID', bg='AliceBlue').grid(row=1,column=0)
	Label(Buscar,text='Nombre', bg='AliceBlue').grid(row=1,column=1)

	textID = Text(Buscar,width=3, height=15)
	textNombre = Text(Buscar,width=15, height=15)

	textID.grid(row=2,column=0)
	textNombre.grid(row=2,column=1)

	Button(Buscar,text='Actualizar',command=lambda:actualizar() ).grid(row=3,column=0,columnspan=7)
	Label(Buscar,text='Ingrese el numero de encuesta que desea responder:  ', bg='AliceBlue').grid(row=4,column=0, sticky='w',padx=5,pady=5)
	Entry(Buscar, width=20, textvariable=ENCUESTA).grid(row=4,column=1, sticky='w',padx=5,pady=5)
	Button(Buscar,text='Buscar',command=lambda:verificacion()).grid(row=4,column=2,columnspan=2)
	Label(Buscar, text="Nombre: ", bg='AliceBlue').grid(row=5,column=0, pady=10, padx=10)
	Label(Buscar, width=20, textvariable=nombre,bd=0, bg='AliceBlue').grid(row=5, column=1, sticky='w',padx=5,pady=5)

	Button(Buscar,text='Responder',command=lambda:(Buscar.destroy(),rta())).grid(row=6,column=1,columnspan=2)
	Button(Buscar, text='Volver', command=lambda:(Buscar.destroy(), inicioP())).grid(row=6, column=0)
	Buscar.mainloop()

def rta():
	def guardarRespuesta():
		conexion = sqlite3.connect("Base_total")
		cursor = conexion.cursor()
		cursor.execute("""INSERT INTO RESPUESTAS VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""",(nombre.get(),pregunta.get(),pregunta2.get(),pregunta3.get(),pregunta4.get(),pregunta5.get(),pregunta6.get(),pregunta7.get(),pregunta8.get(),pregunta9.get(),pregunta10.get(),tipo.get()))
		conexion.commit()
		cursor.close()
		conexion.close()
		messagebox.showinfo('Encuesta Guardada', 'Encuesta guardada correctamente.')
	def siguiente1():
		res=Tk()
		res.title("RESPONDER ENCUESTA")
		res.config(bg='AliceBlue')
		global pregunta6,pregunta7,pregunta8,pregunta9,pregunta10
		pregunta6=IntVar(0)
		pregunta7=IntVar(0)
		pregunta8=IntVar(0)
		pregunta9=IntVar(0)
		pregunta10=IntVar(0)
		Label(res, width=50, text=preguntas6.get(),bd=0,bg='AliceBlue').grid(row=0,column=0, sticky='w',padx=5,pady=5)
		Radiobutton(res,text='Si',variable=pregunta6,value=1,bg='AliceBlue').grid(row=1,column=0, pady=10, padx=10)
		Radiobutton(res,text='No',variable=pregunta6,value=2,bg='AliceBlue').grid(row=2,column=0, pady=10, padx=10)
		Label(res, width=50, text=preguntas7.get(),bd=0,bg='AliceBlue').grid(row=3,column=0, sticky='w',padx=5,pady=5)
		Radiobutton(res,text='Si',variable=pregunta7,value=1,bg='AliceBlue').grid(row=4,column=0, pady=10, padx=10)
		Radiobutton(res,text='No',variable=pregunta7,value=2,bg='AliceBlue').grid(row=5,column=0, pady=10, padx=10)
		Label(res, width=50, text=preguntas8.get(),bd=0,bg='AliceBlue').grid(row=6,column=0, sticky='w',padx=5,pady=5)
		Radiobutton(res,text='Si',variable=pregunta8,value=1,bg='AliceBlue').grid(row=7,column=0, pady=10, padx=10)
		Radiobutton(res,text='No',variable=pregunta8,value=2,bg='AliceBlue').grid(row=8,column=0, pady=10, padx=10)
		Label(res, width=50, text=preguntas9.get(),bd=0,bg='AliceBlue').grid(row=9,column=0, sticky='w',padx=5,pady=5)
		Radiobutton(res,text='Si',variable=pregunta9,value=1,bg='AliceBlue').grid(row=10,column=0, pady=10, padx=10)
		Radiobutton(res,text='No',variable=pregunta9,value=2,bg='AliceBlue').grid(row=11,column=0, pady=10, padx=10)
		Label(res, width=50, text=preguntas10.get(),bd=0,bg='AliceBlue').grid(row=12,column=0, sticky='w',padx=5,pady=5)
		Radiobutton(res,text='Si',variable=pregunta10,value=1,bg='AliceBlue').grid(row=13,column=0, pady=10, padx=10)
		Radiobutton(res,text='No',variable=pregunta10,value=2,bg='AliceBlue').grid(row=14,column=0, pady=10, padx=10)
		Button(res,text='Guardar',command=lambda:(guardarRespuesta(),res.destroy(),ResponderEncuestas())).grid(row=15,column=0)
		res.mainloop()

	def siguiente2():
		res=Tk()
		res.title("RESPONDER ENCUESTA")
		res.config(bg='AliceBlue')
		global pregunta6,pregunta7,pregunta8,pregunta9,pregunta10
		pregunta6=StringVar()
		pregunta7=StringVar()
		pregunta8=StringVar()
		pregunta9=StringVar()
		pregunta10=StringVar()
		Label(res, width=50, text=preguntas6.get(),bd=0,bg='AliceBlue').grid(row=1,column=0, sticky='w',padx=5,pady=5)
		Entry(res, width=50, textvariable=pregunta6).grid(row=2,column=0, sticky='w',padx=5,pady=5)
		Label(res, width=50, text=preguntas7.get(),bd=0,bg='AliceBlue').grid(row=3,column=0, sticky='w',padx=5,pady=5)
		Entry(res, width=50, textvariable=pregunta7).grid(row=4,column=0, sticky='w',padx=5,pady=5)
		Label(res, width=50, text=preguntas8.get(),bd=0,bg='AliceBlue').grid(row=5,column=0, sticky='w',padx=5,pady=5)
		Entry(res, width=50, textvariable=pregunta8).grid(row=6,column=0, sticky='w',padx=5,pady=5)
		Label(res, width=50, text=preguntas9.get(),bd=0,bg='AliceBlue').grid(row=7,column=0, sticky='w',padx=5,pady=5)
		Entry(res, width=50, textvariable=pregunta9).grid(row=8,column=0, sticky='w',padx=5,pady=5)
		Label(res, width=50, text=preguntas10.get(),bd=0,bg='AliceBlue').grid(row=9,column=0, sticky='w',padx=5,pady=5)
		Entry(res, width=50, textvariable=pregunta10).grid(row=10,column=0, sticky='w',padx=5,pady=5)
		Button(res,text='Guardar',command=lambda:(guardarRespuesta(),res.destroy(), ResponderEncuestas())).grid(row=11,column=0)
		res.mainloop()

	if encontrarENCUESTA:
		if tipo.get()==1:
			res=Tk()
			res.title("RESPONDER ENCUESTA")
			res.config(bg='AliceBlue')

			pregunta=IntVar(0)
			pregunta2=IntVar(0)
			pregunta3=IntVar(0)
			pregunta4=IntVar(0)
			pregunta5=IntVar(0)
			

			Label(res, width=50, text=preguntas.get(),bd=0,bg='AliceBlue').grid(row=1,column=0, sticky='w',padx=5,pady=5)
			Radiobutton(res,text='Si',variable=pregunta,value=1,bg='AliceBlue').grid(row=2,column=0, pady=10, padx=10)
			Radiobutton(res,text='No',variable=pregunta,value=2,bg='AliceBlue').grid(row=3,column=0, pady=10, padx=10)
				
			Label(res, width=50, text=preguntas2.get(),bd=0,bg='AliceBlue').grid(row=4,column=0, sticky='w',padx=5,pady=5)
			Radiobutton(res,text='Si',variable=pregunta2,value=1,bg='AliceBlue').grid(row=5,column=0, pady=10, padx=10)
			Radiobutton(res,text='No',variable=pregunta2,value=2,bg='AliceBlue').grid(row=6,column=0, pady=10, padx=10)
				
			Label(res, width=50, text=preguntas3.get(),bd=0,bg='AliceBlue').grid(row=7,column=0, sticky='w',padx=5,pady=5)
			Radiobutton(res,text='Si',variable=pregunta3,value=1,bg='AliceBlue').grid(row=8,column=0, pady=10, padx=10)
			Radiobutton(res,text='No',variable=pregunta3,value=2,bg='AliceBlue').grid(row=9,column=0, pady=10, padx=10)

			Label(res, width=50, text=preguntas4.get(),bd=0,bg='AliceBlue').grid(row=10,column=0, sticky='w',padx=5,pady=5)
			Radiobutton(res,text='Si',variable=pregunta4,value=1,bg='AliceBlue').grid(row=11,column=0, pady=10, padx=10)
			Radiobutton(res,text='No',variable=pregunta4,value=2,bg='AliceBlue').grid(row=12,column=0, pady=10, padx=10)

			Label(res, width=50, text=preguntas5.get(),bd=0,bg='AliceBlue').grid(row=13,column=0, sticky='w',padx=5,pady=5)
			Radiobutton(res,text='Si',variable=pregunta5,value=1,bg='AliceBlue').grid(row=14,column=0, pady=10, padx=10)
			Radiobutton(res,text='No',variable=pregunta5,value=2,bg='AliceBlue').grid(row=15,column=0, pady=10, padx=10)

			Button(res,text='Volver', command=lambda:(res.destroy(),ResponderEncuestas())).grid(row=16, column=0,sticky='w')
			Button(res,text='Siguiente',command=lambda:(res.destroy(),siguiente1())).grid(row=16,column=0,sticky='n')

			res.mainloop()
		elif tipo.get()==2:
			res=Tk()
			res.title("RESPONDER ENCUESTA")
			res.config(bg='AliceBlue')
			pregunta=StringVar()
			pregunta2=StringVar()
			pregunta3=StringVar()
			pregunta4=StringVar()
			pregunta5=StringVar()
			

			
			Label(res, width=50, text=preguntas.get(),bd=0,bg='AliceBlue').grid(row=1,column=0, sticky='w',padx=5,pady=5)
			Entry(res, width=50, textvariable=pregunta).grid(row=2,column=0, sticky='w',padx=5,pady=5)
			Label(res, width=50, text=preguntas2.get(),bd=0,bg='AliceBlue').grid(row=3,column=0, sticky='w',padx=5,pady=5)
			Entry(res, width=50, textvariable=pregunta2).grid(row=4,column=0, sticky='w',padx=5,pady=5)
			Label(res, width=50, text=preguntas3.get(),bd=0,bg='AliceBlue').grid(row=5,column=0, sticky='w',padx=5,pady=5)
			Entry(res, width=50, textvariable=pregunta3).grid(row=6,column=0, sticky='w',padx=5,pady=5)
			Label(res, width=50, text=preguntas4.get(),bd=0,bg='AliceBlue').grid(row=7,column=0, sticky='w',padx=5,pady=5)
			Entry(res, width=50, textvariable=pregunta4).grid(row=8,column=0, sticky='w',padx=5,pady=5)
			Label(res, width=50, text=preguntas5.get(),bd=0,bg='AliceBlue').grid(row=9,column=0, sticky='w',padx=5,pady=5)
			Entry(res, width=50, textvariable=pregunta5).grid(row=10,column=0, sticky='w',padx=5,pady=5)
			Button(res,text='Volver', command=lambda:(res.destroy(),ResponderEncuestas())).grid(row=11, column=0,sticky='w')
			Button(res,text='Siguiente',command=lambda:(res.destroy(),siguiente2())).grid(row=11,column=0,sticky='n')
			res.mainloop()

	else:
		ResponderEncuestas()

#############################  Adriana la Rotta Profesores ########################################
class notas:
    def __init__(self):
        self.wind = Tk()
        self.wind.title('Bienvenido Docente')
        imagen = PhotoImage(file='profesor.gif')
        Label(self.wind, image=imagen).grid(row=0, column=0)

        frame = LabelFrame(self.wind, text='Bienvenido', fg='red',font=("Courier", 16, "italic"))
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        Label(frame, text='Usuario:', fg='blue',font=("Cambria", 12, "italic")).grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1)
        Label(frame, text='contraseña:', fg='blue',font=("Cambria", 12, "italic")).grid(row=2, column=0)
        self.contra = Entry(frame, show='*')
        self.contra.grid(row=2, column=1)

        Button(frame, text='Ingresar',font=("Courier New CYR", 12, "italic"), command=lambda:self.ingresar()).grid(row=3, columnspan=2, sticky=W + E)
        Button(frame, text='salir', fg='red',font=("Courier New CYR", 12, "italic"), command=lambda:(self.wind.destroy(), inicioP())).grid(row=4, columnspan=2, sticky=W + E)
        self.wind.mainloop()

    def conexion(self, query, parametros=()):


        '''conexion base de datos'''
        with sqlite3.connect('Base_total') as conn:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS PROFESORES (CODIGO INTEGER PRIMARY KEY AUTOINCREMENT,
                       NOMBRE VARCHAR,MATERIAS VARCHAR,CONTRASEÑA VARCHAR,VOTO INTEGER)""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS NOTAS (CODIGON INTEGER ,NOMBRE VARCHAR,CARRERA VARCHAR,
                            SABER VARCHAR,SABERHACER VARCHAR,SER VARCHAR,MATERIAQ)""")

            result = cursor.execute(query, parametros)
            conn.commit()
        return result


    def validacion(self):
        return len(self.name.get()) != 0, len(self.contra.get()) != 0

    def ingresar(self):
        if self.validacion():
            consulta='SELECT * FROM PROFESORES WHERE NOMBRE = ? AND CONTRASEÑA = ?'
            parametros=(self.name.get(), self.contra.get())
            self.profesor=self.conexion(consulta, parametros)
            if self.profesor.fetchall():
                print("Usuario y contraseña correctos")
                self.materias()

            else:
                print("Usuario o contraseña incorrecta")
                messagebox.showwarning('cuidado',"Usuario o contraseña incorrecta")


            self.profesor.close()
        else:
            print('incorrecto')
    def materias(self):
        try:
            self.win.destroy()
        except AttributeError:
            pass
        self.win=Toplevel()

        Label(self.win,text='Bienvenido', fg='red',font=("Courier", 16, "italic")).grid(row=0, column=0,columnspan=3,sticky='we')
        self.tabla = ttk.Treeview(self.win, columns=(1, 2, 3), show='headings', height='1')
        self.tabla.grid(row=1, column=0, columnspan=3)
        self.tabla.heading(1, text='Codigo')
        self.tabla.heading(2, text='Nombre')
        self.tabla.heading(3, text='Materia')

        print(self.profesor)
        consulta='SELECT * FROM PROFESORES WHERE NOMBRE = ? AND CONTRASEÑA = ?'
        parametros=(self.name.get(), self.contra.get())
        q=self.conexion(consulta,parametros)


        for k in q:
            self.m=k[2]
            self.tabla.insert('', 'end', values=k)
        Button(self.win, text='Ingresar a la Materia', fg='green', command=lambda: self.materia()).grid(row=2, column=0)
        


    def materia(self):
        try:
            self.win.destroy()
        except AttributeError:
            pass
        self.win=Toplevel()



        Label(self.win,text=self.m,fg='blue',font=("Courier", 16, "italic")).grid(row=0, column=0,columnspan=3,sticky='we')
        self.tabla2 = ttk.Treeview(self.win, columns=(1, 2, 3, 4, 5, 6), show='headings', height='10')
        self.tabla2.grid(row=1, column=0, columnspan=3)
        self.tabla2.heading(1, text='Codigo')
        self.tabla2.heading(2, text='Nombre')
        self.tabla2.heading(3, text='CARRERA')
        self.tabla2.heading(4, text='SABER')
        self.tabla2.heading(5, text='SABER HACER')
        self.tabla2.heading(6, text='SER')
        consulta='SELECT * FROM NOTAS'
        q=self.conexion(consulta)
        for k in q:
            if k[6] == self.m:
                self.tabla2.insert('', 'end', values=k)

        Label(self.win,text='').grid(row=1,column=0,columnspan=3,sticky='we')
        Button(self.win, text='Editar notas', fg='red',font=("Comic Sans MS", 12, "italic"), command=lambda: self.editarnotas()).grid(row=2, column=1)
        Button(self.win, text='Volver', fg='red',font=("Comic Sans MS", 12, "italic"), command=lambda: self.materias()).grid(row=2, column=1,sticky='w')



    def editarnotas(self):
        print(self.tabla2.item(self.tabla2.selection()))
        try:
            self.tabla2.item(self.tabla2.selection())['values'][0]
        except IndexError as e:
            Label(self.win, text='seleccione un estudiante').grid(row=1, column=0, columnspan=3, sticky='we')
            return
        try:
            self.win1.destroy()
        except AttributeError:
            pass



        self.win1 = Toplevel()
        self.win1.title('Editar')
        Label(self.win1, text='Codigo').grid(row=1, column=0)
        Label(self.win1, text='SABER').grid(row=2, column=0)
        Label(self.win1, text='SABER HACER ').grid(row=3, column=0)
        Label(self.win1, text='SER').grid(row=4, column=0)

        self.cd=StringVar(self.win1,value=self.tabla2.item(self.tabla2.selection())['values'][0])
        self.nota1nueva=StringVar(self.win1,value=self.tabla2.item(self.tabla2.selection())['values'][3])
        self.nota2nueva=StringVar(self.win1,value=self.tabla2.item(self.tabla2.selection())['values'][4])
        self.nota3nueva=StringVar(self.win1,value=self.tabla2.item(self.tabla2.selection())['values'][5])

        Entry(self.win1, textvariable=self.cd,state='readonly').grid(row=1, column=1)
        Entry(self.win1,textvariable=self.nota1nueva).grid(row=2, column=1)
        Entry(self.win1, textvariable=self.nota2nueva).grid(row=3, column=1)
        Entry(self.win1, textvariable=self.nota3nueva).grid(row=4, column=1)

        Label(self.win1, text='').grid(row=5, column=0, columnspan=3, sticky='we')
        Button(self.win1, text='Guardar Notas', fg='red',font=("Comic Sans MS", 12, "italic"), command=lambda: self.guardarnotas()).grid(row=6, column=1)


    def guardarnotas(self):
        try:

            parametros = (self.nota1nueva.get(), self.nota2nueva.get(), self.nota3nueva.get(),
                          self.tabla2.item(self.tabla2.selection())['values'][3],
                          self.tabla2.item(self.tabla2.selection())['values'][4],
                          self.tabla2.item(self.tabla2.selection())['values'][5], self.cd.get() , self.m)
            consulta = 'UPDATE NOTAS SET SABER=?,SABERHACER=?,SER=? WHERE SABER=? AND SABERHACER=? AND SER=? AND CODIGON=? AND MATERIAQ=?'

            self.conexion(consulta, parametros)
            float(self.nota1nueva.get())
            float(self.nota2nueva.get())
            float(self.nota3nueva.get())
            messagebox.showinfo('Aviso', 'Nota Actualizada')
            self.win1.destroy()
            self.materia()



        except:
            if messagebox.askretrycancel('Nota incorrecta','Por favor verifique que la Nota sea un numero.'):
                pass
            else:
                print('')


#Ventana Principal 
def inicioP():
	raizm =Tk()
	raizm.title('UIS')
	raizm.iconbitmap('UISIcono.ico')	
	raizm.geometry('800x400')
	barraMenu=Menu()
	raizm.config(menu=barraMenu, bg='AliceBlue')
	imagen=PhotoImage(file="UisPantalla.png", master=raizm)
	imgaen=imagen.subsample(1,1)
	Label(raizm, image=imagen).place(x=0,y=0, relwidth=1.0, relheight=1.0)

	inicioMenu=Menu(barraMenu,tearoff=0)
	barraMenu.add_cascade(label='Inicio',menu=inicioMenu)

	encuestasMenu=Menu(barraMenu,tearoff=0)
	barraMenu.add_cascade(label='Encuestas',menu=encuestasMenu)
	encuestasMenu.add_command(label='Responder Encuestas', command=lambda:(raizm.destroy(), ResponderEncuestas() ))

	profesorMenu=Menu(barraMenu,tearoff=0)
	barraMenu.add_cascade(label='Profesor',menu=profesorMenu)
	profesorMenu.add_command(label='Ingresar', command=lambda:(raizm.destroy(), notas()))

	estudianteMenu=Menu(barraMenu,tearoff=0)
	barraMenu.add_cascade(label='Estudiante',menu=estudianteMenu)
	estudianteMenu.add_command(label='Ingresar',command=lambda:(raizm.destroy(), AdrianaR()))

	bibliotecaMenu=Menu(barraMenu,tearoff=0)
	barraMenu.add_cascade(label='Biblioteca',menu=bibliotecaMenu)
	bibliotecaMenu.add_command(label='Biblioteca', command=lambda:(raizm.destroy(),Biblioteca() ))

	administrativoMenu=Menu(barraMenu,tearoff=0)
	barraMenu.add_cascade(label='Administrativo',menu=administrativoMenu)
	administrativoMenu.add_command(label='Acceder', command=lambda:(raizm.destroy(), Acceder()))

	Button(raizm, text='Votaciones', command= lambda:(raizm.destroy(),ventanaprim())).place(x=20,y=100)

	raizm.mainloop()


############### Camilo admi #########################
class BibliotecaA:

    def __init__(self):

        self.ven = Tk()
        self.ven.title('Biblioteca')
        self.ven.geometry('1000x668')
        self.ven.resizable(0, 0)
        self.Mensaje = Label()

        q = PhotoImage(file="Imagen4.gif", master= self.ven)
        Label(self.ven, image=q).place(x=0, y=0)

        Barra = Menu(self.ven)
        self.ven.config(menu=Barra)

        Nuevo = Menu(Barra, tearoff=0,fg='#3E73A4')
        Nuevo.add_command(label='Didacticos', command=lambda: self.Didactico_Nuevo())
        Nuevo.add_command(label='Folletos', command=lambda: self.Folleto_Nuevo())
        Nuevo.add_command(label='Libros',command=lambda: self.Libro_Nuevo())
        Nuevo.add_command(label='Revistas',command=lambda: self.Revista_Nuevo())

        Editar = Menu(Barra, tearoff=0,fg='#D18C11')
        Editar.add_command(label='Buscar', command=lambda: self.Sistema_Busqueda())

        Barra.add_cascade(label='Nuevo', menu=Nuevo)
        Barra.add_cascade(label='Editar', menu=Editar)

        Label(self.ven, text='BIENVENIDOS',bg='#E59049', fg='white', font=('', 30)).place(x=100, y=55)
        Label(self.ven, text='BIBLIOTECA VIRTUAL',bg='#E59049', fg='white', font=('', 30)).place(x=200, y=115)

        Button(self.ven, text='Volver', command=(lambda:(self.ven.destroy(), administrativo())) , font=('', 12), fg='#3DC370').place(x=920,y=600)

        self.ven.mainloop()

        

    def Conexion(self, consulta, parametros=()):

        with sqlite3.connect('Base_total') as conn:
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS Folletos(Codigo NUMERIC,'
                           'Nombre TEXT , Referencia TEXT, Tipo TEXT, Adquirido TEXT )')
            cursor.execute('CREATE TABLE IF NOT EXISTS Didacticos(Codigo Codigo NUMERIC,'
                           'Nombre TEXT , Referencia TEXT, Tipo TEXT, Adquirido TEXT)')
            cursor.execute('CREATE TABLE IF NOT EXISTS Libros(Codigo Codigo NUMERIC,'
                           'Titulo TEXT , Autor TEXT, Tipo TEXT, Adquirido TEXT)')
            cursor.execute('CREATE TABLE IF NOT EXISTS Revistas(Codigo Codigo NUMERIC ,'
                           'Nombre TEXT , Referencia TEXT, Tipo TEXT,Adquirido TEXT)')

            resultado = cursor.execute(consulta, parametros)
            conn.commit()
        return resultado

    def Libro_Nuevo(self):

        self.Tipo_guardar = 1
        try:
            self.ven_nuevo.destroy()
        except AttributeError:
            pass
        self.ven_nuevo = Frame(self.ven)
        self.ven_nuevo.place(x=280, y=260)

        Label(self.ven_nuevo, text='Por favor digite los siguientes datos del libro: ',fg='#4E944E',font=('', 16))\
            .grid(row=0, column=0, padx=15, pady=15, columnspan=3)

        self.Titulo, self.Autor, self.tipo, self.adquirido, self.cantidad = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()

        Label(self.ven_nuevo, text='Título: ',fg='#3E73A4',font=('', 16)).grid(row=1, column=0, padx=5, pady=1)
        Entry(self.ven_nuevo, textvariable=self.Titulo, fg='#4B5253', justify='center').grid(row=1, column=1, padx=5, pady=1, columnspan=2, sticky='we')

        Label(self.ven_nuevo, text='Autor: ',fg='#3E73A4',font=('', 16)).grid(row=2, column=0, padx=5, pady=1)
        Entry(self.ven_nuevo, textvariable=self.Autor, fg='#4B5253', justify='center').grid(row=2, column=1, padx=5, pady=1, columnspan=2, sticky='we')

        Label(self.ven_nuevo, text='Tipo: ',fg='#3E73A4',font=('', 16)).grid(row=3, column=0, padx=5, pady=1)
        Entry(self.ven_nuevo, textvariable=self.tipo, fg='#4B5253', justify='center').grid(row=3, column=1, padx=5, pady=1, columnspan=2, sticky='we')

        Label(self.ven_nuevo, text='Adquirido: ', fg='#3E73A4', font=('', 16)).grid(row=4, column=0, padx=5, pady=1)
        Entry(self.ven_nuevo, textvariable=self.adquirido, fg='#4B5253', justify='center').grid(row=4, column=1, padx=5, pady=1, columnspan=2,sticky='we')


        Label(self.ven_nuevo, text='Cantidad: ',fg='#3E73A4',font=('', 16)).grid(row=5, column=0, padx=5, pady=1)
        Entry(self.ven_nuevo, textvariable=self.cantidad, fg='#4B5253', justify='center').grid(row=5, column=1, padx=5, pady=1, columnspan=2, sticky='we')

        Label(self.ven_nuevo, text='   ', fg='red',font=('', 16)).grid(row=6, column=0, padx=5, pady=5, columnspan=3)

        Button(self.ven_nuevo, text="Guardar", fg='#4E944E', font=('', 16), command=lambda: self.Guardar())\
            .grid(row=7, column=0, padx=5, pady=15, sticky='', columnspan=3)

    def Folleto_Nuevo(self):

        self.Tipo_guardar = 2
        try:
            self.ven_nuevo.destroy()
        except AttributeError:
            pass
        self.ven_nuevo = Frame(self.ven)
        self.ven_nuevo.place(x=270, y=260)

        Label(self.ven_nuevo, text='Por favor digite los siguientes datos del folleto: ', fg='#4E944E', font=('', 16)) \
            .grid(row=0, column=0, padx=15, pady=15, columnspan=3)

        self.Nombre_F, self.Referencia_F, self.tipo_F, self.adquirido_F, self.cantidad_F = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()

        Label(self.ven_nuevo, text='Nombre: ', fg='#3E73A4', font=('', 16)).grid(row=1, column=0, padx=5, pady=1)
        Entry(self.ven_nuevo, textvariable=self.Nombre_F, fg='#4B5253', justify='center')\
            .grid(row=1, column=1, padx=5,pady=1, columnspan=2,sticky='we')

        Label(self.ven_nuevo, text='Referencia: ', fg='#3E73A4', font=('', 16)).grid(row=2, column=0, padx=5, pady=1)
        Entry(self.ven_nuevo, textvariable=self.Referencia_F, fg='#4B5253', justify='center')\
            .grid(row=2, column=1, padx=5, pady=1, columnspan=2, sticky='we')

        Label(self.ven_nuevo, text='Tipo: ', fg='#3E73A4', font=('', 16)).grid(row=3, column=0, padx=5, pady=1)
        Entry(self.ven_nuevo, textvariable=self.tipo_F, fg='#4B5253', justify='center')\
            .grid(row=3, column=1, padx=5,pady=1, columnspan=2,sticky='we')

        Label(self.ven_nuevo, text='Adquirido: ', fg='#3E73A4', font=('', 16))\
            .grid(row=4, column=0, padx=5, pady=1)
        Entry(self.ven_nuevo, textvariable=self.adquirido_F, fg='#4B5253', justify='center')\
            .grid(row=4, column=1, padx=5, pady=1, columnspan=2,sticky='we')

        Label(self.ven_nuevo, text='Cantidad: ', fg='#3E73A4', font=('', 16))\
            .grid(row=5, column=0, padx=5, pady=1)
        Entry(self.ven_nuevo, textvariable=self.cantidad_F, fg='#4B5253', justify='center')\
            .grid(row=5, column=1, padx=5,pady=1, columnspan=2,sticky='we')

        Label(self.ven_nuevo, text='   ', fg='red', font=('', 16)).grid(row=6, column=0, padx=5, pady=5, columnspan=3)

        Button(self.ven_nuevo, text="Guardar", fg='#4E944E', font=('', 16), command=lambda: self.Guardar()) \
            .grid(row=7, column=0, padx=5, pady=15, sticky='', columnspan=3)

    def Revista_Nuevo(self):

        self.Tipo_guardar = 3
        try:
            self.ven_nuevo.destroy()
        except AttributeError:
            pass
        self.ven_nuevo = Frame(self.ven)
        self.ven_nuevo.place(x=250, y=260)

        Label(self.ven_nuevo, text='Por favor digite los siguientes datos de la Revista: ', fg='#4E944E', font=('', 16)) \
            .grid(row=0, column=0, padx=15, pady=15, columnspan=3)

        self.Nombre_R, self.Referencia_R, self.tipo_R, self.adquirido_R, self.cantidad_R = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()

        Label(self.ven_nuevo, text='Nombre: ', fg='#3E73A4', font=('', 16)).grid(row=1, column=0, padx=5, pady=1)
        Entry(self.ven_nuevo, textvariable=self.Nombre_R, fg='#4B5253', justify='center')\
            .grid(row=1, column=1, padx=5,pady=1, columnspan=2,sticky='we')

        Label(self.ven_nuevo, text='Referencia: ', fg='#3E73A4', font=('', 16)).grid(row=2, column=0, padx=5, pady=1)
        Entry(self.ven_nuevo, textvariable=self.Referencia_R, fg='#4B5253', justify='center')\
            .grid(row=2, column=1, padx=5, pady=1, columnspan=2, sticky='we')

        Label(self.ven_nuevo, text='Tipo: ', fg='#3E73A4', font=('', 16)).grid(row=3, column=0, padx=5, pady=1)
        Entry(self.ven_nuevo, textvariable=self.tipo_R, fg='#4B5253', justify='center')\
            .grid(row=3, column=1, padx=5,pady=1, columnspan=2,sticky='we')

        Label(self.ven_nuevo, text='Adquirido: ', fg='#3E73A4', font=('', 16))\
            .grid(row=4, column=0, padx=5, pady=1)
        Entry(self.ven_nuevo, textvariable=self.adquirido_R, fg='#4B5253', justify='center')\
            .grid(row=4, column=1, padx=5, pady=1, columnspan=2,sticky='we')

        Label(self.ven_nuevo, text='Cantidad: ', fg='#3E73A4', font=('', 16))\
            .grid(row=5, column=0, padx=5, pady=1)
        Entry(self.ven_nuevo, textvariable=self.cantidad_R, fg='#4B5253', justify='center')\
            .grid(row=5, column=1, padx=5,pady=1, columnspan=2,sticky='we')

        Label(self.ven_nuevo, text='   ', fg='red', font=('', 16)).grid(row=6, column=0, padx=5, pady=5, columnspan=3)

        Button(self.ven_nuevo, text="Guardar", fg='#4E944E', font=('', 16), command=lambda: self.Guardar()) \
            .grid(row=7, column=0, padx=5, pady=15, sticky='', columnspan=3)

    def Didactico_Nuevo(self):

        self.Tipo_guardar = 4
        try:
            self.ven_nuevo.destroy()
        except AttributeError:
            pass
        self.ven_nuevo = Frame(self.ven)
        self.ven_nuevo.place(x=210, y=260)

        Label(self.ven_nuevo, text='Por favor digite los siguientes datos del Material Didactico: ', fg='#4E944E', font=('', 16)) \
            .grid(row=0, column=0, padx=15, pady=15, columnspan=3)

        self.Nombre_D, self.Referencia_D, self.tipo_D, self.adquirido_D, self.cantidad_D = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()

        Label(self.ven_nuevo, text='Nombre: ', fg='#3E73A4', font=('', 16)).grid(row=1, column=0, padx=5, pady=1)
        Entry(self.ven_nuevo, textvariable=self.Nombre_D, fg='#4B5253', justify='center') \
            .grid(row=1, column=1, padx=5, pady=1, columnspan=2, sticky='we')

        Label(self.ven_nuevo, text='Referencia: ', fg='#3E73A4', font=('', 16)).grid(row=2, column=0, padx=5, pady=1)
        Entry(self.ven_nuevo, textvariable=self.Referencia_D, fg='#4B5253', justify='center') \
            .grid(row=2, column=1, padx=5, pady=1, columnspan=2, sticky='we')

        Label(self.ven_nuevo, text='Tipo: ', fg='#3E73A4', font=('', 16)).grid(row=3, column=0, padx=5, pady=1)
        Entry(self.ven_nuevo, textvariable=self.tipo_D, fg='#4B5253', justify='center') \
            .grid(row=3, column=1, padx=5, pady=1, columnspan=2, sticky='we')

        Label(self.ven_nuevo, text='Adquirido: ', fg='#3E73A4', font=('', 16)) \
            .grid(row=4, column=0, padx=5, pady=1)
        Entry(self.ven_nuevo, textvariable=self.adquirido_D, fg='#4B5253', justify='center') \
            .grid(row=4, column=1, padx=5, pady=1, columnspan=2, sticky='we')

        Label(self.ven_nuevo, text='Cantidad: ', fg='#3E73A4', font=('', 16)) \
            .grid(row=5, column=0, padx=5, pady=1)
        Entry(self.ven_nuevo, textvariable=self.cantidad_D, fg='#4B5253', justify='center') \
            .grid(row=5, column=1, padx=5, pady=1, columnspan=2, sticky='we')

        Label(self.ven_nuevo, text='   ', fg='red', font=('', 16)).grid(row=6, column=0, padx=5, pady=5, columnspan=3)

        Button(self.ven_nuevo, text="Guardar", fg='#4E944E', font=('', 16), command=lambda: self.Guardar()) \
            .grid(row=7, column=0, padx=5, pady=15, sticky='', columnspan=3)

    def Guardar(self):

        if self.Tipo_guardar == 1:

            z, x = self.Validar(self.Titulo.get(), self.Autor.get(), self.tipo.get(), self.adquirido.get(),
                                self.cantidad.get()), self.Validar_entero(self.cantidad.get())

            if x > 1 and z == True:

                for i in range(0, x, 1):
                    Codigo = self.Codigos()
                    consulta = 'INSERT INTO Libros(Codigo, Titulo, Autor, Tipo, Adquirido) VALUES(?, ?, ?, ?, ?)'
                    parametros = (Codigo, self.Titulo.get(), self.Autor.get(), self.tipo.get(), self.adquirido.get())
                    self.Conexion(consulta, parametros)

                time.sleep(2)
                messagebox.showinfo('Aviso', 'Guardados')
                self.ven_nuevo.destroy()

            elif x == 1 and z == True:

                Codigo = self.Codigos()
                consulta = 'INSERT INTO Libros(Codigo, Titulo, Autor, Tipo, Adquirido) VALUES(?, ?, ?, ?, ?)'
                parametros = (Codigo, self.Titulo.get(), self.Autor.get(), self.tipo.get(), self.adquirido.get())
                self.Conexion(consulta, parametros)
                time.sleep(1)
                messagebox.showinfo('Aviso', 'Guardado')
                self.ven_nuevo.destroy()

            elif x == 0 and z == True:
                Label(self.ven_nuevo, text='            Error en cantidad            ', fg='red', font=('', 12)) \
                    .grid(row=6, column=0, padx=5, pady=5, columnspan=3)

            else:
                Label(self.ven_nuevo, text=' Debe llenar todos los campos  ', fg='red', font=('', 12)) \
                    .grid(row=6, column=0, padx=5, pady=5, columnspan=3)

        elif self.Tipo_guardar == 2:
            z, x = self.Validar(self.Nombre_F.get(), self.Referencia_F.get(), self.tipo_F.get(), self.adquirido_F.get(),
                                self.cantidad_F.get()), self.Validar_entero(self.cantidad_F.get())

            if x > 1 and z == True:

                for i in range(0, x, 1):
                    Codigos = self.Codigos()
                    consulta = 'INSERT INTO Folletos(Codigo, Nombre, Referencia, Tipo, Adquirido) VALUES(?, ?, ?, ?, ?)'
                    parametros = (Codigos, self.Nombre_F.get(), self.Referencia_F.get(), self.tipo_F.get(), self.adquirido_F.get())
                    self.Conexion(consulta, parametros)

                time.sleep(2)
                messagebox.showinfo('Aviso', 'Guardados')
                self.ven_nuevo.destroy()

            elif x == 1 and z == True:

                Codigos = self.Codigos()
                consulta = 'INSERT INTO Folletos(Codigo, Nombre, Referencia, Tipo, Adquirido) VALUES(?, ?, ?, ?, ?)'
                parametros = (
                Codigos, self.Nombre_F.get(), self.Referencia_F.get(), self.tipo_F.get(), self.adquirido_F.get())
                self.Conexion(consulta, parametros)
                time.sleep(1)
                messagebox.showinfo('Aviso', 'Guardado')
                self.ven_nuevo.destroy()

            elif x == 0 and z == True:
                Label(self.ven_nuevo, text='            Error en cantidad            ', fg='red', font=('', 12)) \
                    .grid(row=6, column=0, padx=5, pady=5, columnspan=3)

            else:
                Label(self.ven_nuevo, text=' Debe llenar todos los campos  ', fg='red', font=('', 12)) \
                    .grid(row=6, column=0, padx=5, pady=5, columnspan=3)

        elif self.Tipo_guardar == 3:
            z, x = self.Validar(self.Nombre_R.get(), self.Referencia_R.get(), self.tipo_R.get(), self.adquirido_R.get(),
                                self.cantidad_R.get()), self.Validar_entero(self.cantidad_R.get())

            if x > 1 and z == True:

                for i in range(0, x, 1):
                    Codigos = self.Codigos()
                    consulta = 'INSERT INTO Revistas(Codigo, Nombre, Referencia, Tipo, Adquirido) VALUES(?, ?, ?, ?,? )'
                    parametros = (Codigos,self.Nombre_R.get(), self.Referencia_R.get(), self.tipo_R.get(), self.adquirido_R.get())
                    self.Conexion(consulta, parametros)

                time.sleep(2)
                messagebox.showinfo('Aviso', 'Guardados')
                self.ven_nuevo.destroy()

            elif x == 1 and z == True:

                Codigos = self.Codigos()
                consulta = 'INSERT INTO Revistas(Codigo, Nombre, Referencia, Tipo, Adquirido) VALUES(?, ?, ?, ?,? )'
                parametros = (
                Codigos, self.Nombre_R.get(), self.Referencia_R.get(), self.tipo_R.get(), self.adquirido_R.get())
                self.Conexion(consulta, parametros)
                time.sleep(1)
                messagebox.showinfo('Aviso', 'Guardado')
                self.ven_nuevo.destroy()

            elif x == 0 and z == True:
                Label(self.ven_nuevo, text='            Error en cantidad            ', fg='red', font=('', 12)) \
                    .grid(row=6, column=0, padx=5, pady=5, columnspan=3)

            else:
                Label(self.ven_nuevo, text=' Debe llenar todos los campos  ', fg='red', font=('', 12)) \
                    .grid(row=6, column=0, padx=5, pady=5, columnspan=3)

        elif self.Tipo_guardar == 4:
            z, x = self.Validar(self.Nombre_D.get(), self.Referencia_D.get(), self.tipo_D.get(), self.adquirido_D.get(),
                                self.cantidad_D.get()), self.Validar_entero(self.cantidad_D.get())

            if x > 1 and z == True:

                for i in range(0, x, 1):
                    Codigos = self.Codigos()
                    consulta = 'INSERT INTO Didacticos(Codigo, Nombre, Referencia, Tipo, Adquirido) VALUES(?, ?, ?, ?, ?)'
                    parametros = (Codigos, self.Nombre_D.get(), self.Referencia_D.get(), self.tipo_D.get(), self.adquirido_D.get())
                    self.Conexion(consulta, parametros)

                time.sleep(2)
                messagebox.showinfo('Aviso', 'Guardados')
                self.ven_nuevo.destroy()

            elif x == 1 and z == True:

                Codigos = self.Codigos()
                consulta = 'INSERT INTO Didacticos(Codigo, Nombre, Referencia, Tipo, Adquirido) VALUES(?, ?, ?, ?, ?)'
                parametros = ( Codigos, self.Nombre_D.get(), self.Referencia_D.get(), self.tipo_D.get(), self.adquirido_D.get())
                self.Conexion(consulta, parametros)
                time.sleep(1)
                messagebox.showinfo('Aviso', 'Guardado')
                self.ven_nuevo.destroy()

            elif x == 0 and z == True:
                Label(self.ven_nuevo, text='            Error en cantidad            ', fg='red', font=('', 12)) \
                    .grid(row=6, column=0, padx=5, pady=5, columnspan=3)

            else:
                Label(self.ven_nuevo, text=' Debe llenar todos los campos  ', fg='red', font=('', 12)) \
                    .grid(row=6, column=0, padx=5, pady=5, columnspan=3)

    def Sistema_Busqueda(self):
        try:
            self.ven_nuevo.destroy()
        except AttributeError:
            pass

        self.ven_nuevo = Frame(self.ven)
        self.ven_nuevo.place(x=310, y=260)

        Label(self.ven_nuevo, text='SISTEMA DE CONSULTA',fg='#4E944E',font=('', 16))\
            .grid(row=0, column=0, padx=15, pady=15, columnspan=4)

        self.textobuscar = StringVar()
        cuadronombre = Entry(self.ven_nuevo, textvariable=self.textobuscar)
        cuadronombre.grid(row=1, column=0, columnspan=3, padx=15, pady=5, sticky=W + E)
        cuadronombre.config(fg='blue', justify='center')

        buscar = Button(self.ven_nuevo, text='Buscar', command=lambda: self.Buscador(), font=('', 12), fg='#3DC370')
        buscar.grid(row=1, column=3, sticky='', padx=5, pady=5)

        self.Valor_rb = IntVar()
        Radiobutton(self.ven_nuevo, text='Didacticos',fg='#5EA0A2', variable=self.Valor_rb, value=1, font=('', 12)) \
            .grid(row=2, column=0, sticky='', padx=5, pady=5)
        Radiobutton(self.ven_nuevo, text='Folletos',fg='#5EA0A2', variable=self.Valor_rb, value=2, font=('', 12)) \
            .grid(row=2, column=1, sticky='', padx=5, pady=5)
        Radiobutton(self.ven_nuevo, text='Libros',fg='#5EA0A2', variable=self.Valor_rb, value=3, font=('', 12)) \
            .grid(row=2, column=2, sticky='', padx=5, pady=5)
        Radiobutton(self.ven_nuevo, text='Revistas', fg='#5EA0A2', variable=self.Valor_rb, value=4, font=('', 12)) \
            .grid(row=2, column=3, sticky='', padx=5, pady=5)

        Label(self.ven_nuevo, text='                                                            ', font=('', 16))\
            .grid(row=3, column=0, sticky=W + E, padx=5, pady=5, columnspan=4)

    def Buscador(self):
        f = self.Valor_rb.get()
        if (f == 1  > 0 or f == 2 or f == 3 or  f == 4) and len(self.textobuscar.get()):

            time.sleep(1.5)
            self.ven_nuevo.destroy()
            self.Resultados()

        else:
            Label(self.ven_nuevo, text='Digite una palabra y seleccione una opción',fg='#F07010', font=('', 10))\
                .grid(row=3, column=0, sticky=W + E, padx=5, pady=5, columnspan=4)

    def Resultados(self):
        try:
            self.ven_nuevo.destroy()
        except AttributeError:
            pass

        self.ven_nuevo = Frame(self.ven)
        self.ven_nuevo.place(x=90, y=260)

        Label(self.ven_nuevo, text='Resultados').grid(row=0, column=0, padx=5, pady=5, columnspan=5)

        self.Tabla = ttk.Treeview(self.ven_nuevo, columns=(1, 2, 3, 4), show='headings', height='10')
        self.Tabla.grid(row=1, column=0, padx=5, pady=5, columnspan=5)

        rueda = Scrollbar(self.ven_nuevo, command=self.Tabla.yview)
        rueda.grid(row=1, column=7, sticky='nsew')
        self.Tabla.config(yscrollcommand=rueda.set)


        libros = self.Tabla.get_children()
        for i in libros:
            self.Tabla.delete(i)



        if self.Valor_rb.get() == 3:

            self.Tabla.heading(1, text='Codigo')
            self.Tabla.heading(2, text='Titulo')
            self.Tabla.heading(3, text='Autor')
            self.Tabla.heading(4, text='Tipo')



            consulta = 'SELECT * FROM Libros ORDER BY Titulo ASC'
            filas = self.Conexion(consulta)
            for i in filas:
                self.Tabla.insert('', 'end', values=i)

        elif self.Valor_rb.get() == 1:

            self.Tabla.heading(1, text='Codigo')
            self.Tabla.heading(2, text='Nombre')
            self.Tabla.heading(3, text='Referencia')
            self.Tabla.heading(4, text='Tipo')


            consulta = 'SELECT * FROM Didacticos ORDER BY Nombre ASC'
            filas = self.Conexion(consulta)
            for i in filas:
                self.Tabla.insert('', 'end', values=i)

        elif self.Valor_rb.get() == 2:

            self.Tabla.heading(1, text='Codigo')
            self.Tabla.heading(2, text='Nombre')
            self.Tabla.heading(3, text='Referencia')
            self.Tabla.heading(4, text='Tipo')

            consulta = 'SELECT * FROM Folletos ORDER BY Nombre ASC'
            filas = self.Conexion(consulta)
            for i in filas:
                self.Tabla.insert('', 'end', values=i)

        elif self.Valor_rb.get() == 4:

            self.Tabla.heading(1, text='Codigo')
            self.Tabla.heading(2, text='Nombre')
            self.Tabla.heading(3, text='Referencia')
            self.Tabla.heading(4, text='Tipo')

            consulta = 'SELECT * FROM Revistas ORDER BY Nombre ASC'
            filas = self.Conexion(consulta)
            for i in filas:
                self.Tabla.insert('', 'end', values=i)

        Label(self.ven_nuevo, text='', fg='green').grid(row=5, column=0, padx=5, pady=5, columnspan=5, sticky='')

        Button(self.ven_nuevo, text='Editar', command=lambda: self.Editar())\
            .grid(row=6, column=1, sticky='we', padx=5,pady=5)
        Button(self.ven_nuevo, text='Eliminar', command=lambda: self.Eliminar())\
            .grid(row=6, column=3, sticky='we', padx=5, pady=5)

    def Editar(self):


        print(self.Tabla.item(self.Tabla.selection()))
        try:
            self.Tabla.item(self.Tabla.selection())['values'][0]
        except IndexError as e:
            Label(self.ven_nuevo, text='Seleccione Elemento', fg='#727D8E')\
                .grid(row=5, column=0, padx=5, pady=5, columnspan=5, sticky='')
            return

        try:
            self.ven_nuevo1.destroy()
        except AttributeError:
            pass

        self.ven_nuevo1 = Toplevel(self.ven)
        self.ven_nuevo1.title('Editar')
        self.ven_nuevo1.resizable(0, 0)

        if self.Valor_rb.get() == 3:

            Label(self.ven_nuevo1, text='Titulo: ').grid(row=0, column=0, padx=5, pady=5)
            Label(self.ven_nuevo1, text='Autor: ').grid(row=1, column=0, padx=5, pady=5)
            Label(self.ven_nuevo1, text='Tipo: ').grid(row=2, column=0, padx=5, pady=5)
            Label(self.ven_nuevo1, text='Adquirido: ').grid(row=3, column=0, padx=5, pady=5)

        elif self.Valor_rb.get() == 1 or self.Valor_rb.get() == 2 or self.Valor_rb.get() == 4:

            Label(self.ven_nuevo1, text='Nombre: ').grid(row=0, column=0, padx=5, pady=5)
            Label(self.ven_nuevo1, text='Referencia: ').grid(row=1, column=0, padx=5, pady=5)
            Label(self.ven_nuevo1, text='Tipo: ').grid(row=2, column=0, padx=5, pady=5)
            Label(self.ven_nuevo1, text='Adquirido: ').grid(row=3, column=0, padx=5, pady=5)

        self.Titulo2 = StringVar(self.ven_nuevo1, value=self.Tabla.item(self.Tabla.selection())['values'][1])
        self.Autor2 = StringVar(self.ven_nuevo1, value=self.Tabla.item(self.Tabla.selection())['values'][2])
        self.Tipo2 = StringVar(self.ven_nuevo1, value=self.Tabla.item(self.Tabla.selection())['values'][3])
        self.Adquirido2 = StringVar(self.ven_nuevo1, value=self.Tabla.item(self.Tabla.selection())['values'][4])

        Entry(self.ven_nuevo1, textvariable=self.Titulo2).grid(row=0, column=1, pady=5, padx=5)
        Entry(self.ven_nuevo1, textvariable=self.Autor2).grid(row=1, column=1, pady=5, padx=5)
        Entry(self.ven_nuevo1, textvariable=self.Tipo2).grid(row=2, column=1, pady=5, padx=5)
        Entry(self.ven_nuevo1, textvariable=self.Adquirido2).grid(row=3, column=1, pady=5, padx=5)

        Label(self.ven_nuevo1, text='  ').grid(row=4, column=0, padx=5, pady=5, columnspan=2)
        Button(self.ven_nuevo1, text="Guardar", command=lambda: self.Actualizar()) \
            .grid(row=5, column=0, sticky='', padx=5, pady=5, columnspan=2)

    def Actualizar(self):

        if self.Valor_rb.get() == 3 and self.Validar(self.Titulo2.get(), self.Autor2.get(), self.Tipo2.get(),
                                                     self.Adquirido2.get(), '21'):

            parametros = (self.Titulo2.get(), self.Autor2.get(), self.Tipo2.get(), self.Adquirido2.get(),
                          self.Tabla.item(self.Tabla.selection())['values'][1], self.Tabla.item(self.Tabla.selection())['values'][2],
                          self.Tabla.item(self.Tabla.selection())['values'][3], self.Tabla.item(self.Tabla.selection())['values'][4],
                          self.Tabla.item(self.Tabla.selection())['values'][0])

            Consulta = 'UPDATE Libros SET Titulo = ?, Autor = ?, Tipo = ?, Adquirido = ? WHERE Titulo = ? AND' \
                       ' Autor = ? AND Tipo = ? AND Adquirido = ? AND Codigo = ?'
            self.Conexion(Consulta, parametros)
            time.sleep(2)
            messagebox.showinfo('Aviso', 'Guardado')
            self.ven_nuevo1.destroy()
            self.Resultados()

        elif self.Valor_rb.get() == 1 and self.Validar(self.Titulo2.get(), self.Autor2.get(), self.Tipo2.get(),
                                                     self.Adquirido2.get(), '21'):

            parametros = (self.Titulo2.get(), self.Autor2.get(), self.Tipo2.get(), self.Adquirido2.get(),
                          self.Tabla.item(self.Tabla.selection())['values'][1], self.Tabla.item(self.Tabla.selection())['values'][2],
                          self.Tabla.item(self.Tabla.selection())['values'][3], self.Tabla.item(self.Tabla.selection())['values'][4],
                          self.Tabla.item(self.Tabla.selection())['values'][0])

            Consulta = 'UPDATE Didacticos SET Nombre = ?, Referencia = ?, Tipo = ?, Adquirido = ? WHERE Nombre = ? AND' \
                       ' Referencia = ? AND Tipo = ? AND Adquirido = ? AND Codigo = ?'
            self.Conexion(Consulta, parametros)
            time.sleep(2)
            messagebox.showinfo('Aviso', 'Guardado')
            self.ven_nuevo1.destroy()
            self.Resultados()

        elif self.Valor_rb.get() == 2 and self.Validar(self.Titulo2.get(), self.Autor2.get(), self.Tipo2.get(),
                                                     self.Adquirido2.get(), '21'):

            parametros = (self.Titulo2.get(), self.Autor2.get(), self.Tipo2.get(), self.Adquirido2.get(),
                          self.Tabla.item(self.Tabla.selection())['values'][1], self.Tabla.item(self.Tabla.selection())['values'][2],
                          self.Tabla.item(self.Tabla.selection())['values'][3], self.Tabla.item(self.Tabla.selection())['values'][4],
                          self.Tabla.item(self.Tabla.selection())['values'][0])

            Consulta = 'UPDATE Folletos SET Nombre = ?, Referencia = ?, Tipo = ?, Adquirido = ? WHERE Nombre = ? AND' \
                       ' Referencia = ? AND Tipo = ? AND Adquirido = ? AND Codigo = ?'
            self.Conexion(Consulta, parametros)
            time.sleep(2)
            messagebox.showinfo('Aviso', 'Guardado')
            self.ven_nuevo1.destroy()
            self.Resultados()

        elif self.Valor_rb.get() == 4 and self.Validar(self.Titulo2.get(), self.Autor2.get(), self.Tipo2.get(),
                                                     self.Adquirido2.get(), '21'):

            parametros = (self.Titulo2.get(), self.Autor2.get(), self.Tipo2.get(), self.Adquirido2.get(),
                          self.Tabla.item(self.Tabla.selection())['values'][1], self.Tabla.item(self.Tabla.selection())['values'][2],
                          self.Tabla.item(self.Tabla.selection())['values'][3], self.Tabla.item(self.Tabla.selection())['values'][4],
                          self.Tabla.item(self.Tabla.selection())['values'][0])

            Consulta = 'UPDATE Revistas SET Nombre = ?, Referencia = ?, Tipo = ?, Adquirido = ? WHERE Nombre = ? AND' \
                       ' Referencia = ? AND Tipo = ? AND Adquirido = ? AND Codigo = ?'
            self.Conexion(Consulta, parametros)
            time.sleep(2)
            messagebox.showinfo('Aviso', 'Guardado')
            self.ven_nuevo1.destroy()
            self.Resultados()
        else:
            Label(self.ven_nuevo1, text=' Debe llenar todos los campos  ', fg='red').grid(row=4, column=0, padx=5, pady=5,columnspan=2)

    def Eliminar(self):
        try:

            self.Tabla.item(self.Tabla.selection())['values'][0]

        except IndexError as e:
            Label(self.ven_nuevo, text='Seleccione Elemento', fg='green').grid(row=5, column=0, padx=5, pady=5, columnspan=5, sticky='')
            return

        print(self.Tabla.item(self.Tabla.selection()))
        print(self.Tabla.item(self.Tabla.selection())['values'][0])

        Preguntar = messagebox.askquestion('Eliminar', '¿Está segur@?')

        if self.Valor_rb.get() == 3 and Preguntar == 'yes':
            Consulta = 'DELETE FROM Libros WHERE Codigo = ?'
            self.Conexion(Consulta, (self.Tabla.item(self.Tabla.selection())['values'][0],))
            self.Resultados()

        elif self.Valor_rb.get() == 1 and Preguntar == 'yes':
            Consulta = 'DELETE FROM Didacticos WHERE Codigo = ?'
            self.Conexion(Consulta, (self.Tabla.item(self.Tabla.selection())['values'][0],))
            self.Resultados()

        elif self.Valor_rb.get() == 2 and Preguntar == 'yes':
            Consulta = 'DELETE FROM Folletos WHERE Codigo = ?'
            self.Conexion(Consulta, (self.Tabla.item(self.Tabla.selection())['values'][0],))
            self.Resultados()

        elif self.Valor_rb.get() == 4 and Preguntar == 'yes':
            Consulta = 'DELETE FROM Revistas WHERE Codigo = ?'
            self.Conexion(Consulta, (self.Tabla.item(self.Tabla.selection())['values'][0],))
            self.Resultados()

    def Validar(self, z, x, c, v, b):

        a = False

        if len(z) > 0 and len(x) > 0 and len(c) > 0 and len(v) > 0 and len(b) > 0 and\
                len(z) < 20 and len(x) < 20 and len(c) < 20 and len(v)  < 20 and len(b) < 20 :
            a = True

        return a

    def Validar_entero(self, valor):

        b = 0
        while True:
            try:
                b = int(valor)
                return b
            except ValueError:
                break
        return b

    def Codigos(self):

        if self.Tipo_guardar == 1:
            consulta = 'SELECT * FROM Libros ORDER BY Codigo ASC'
            filas = self.Conexion(consulta)
            Codigo = 10000

            for i in filas:

                if i[0] == 0:
                    return Codigo
                if Codigo == i[0]:
                    Codigo += 1
            return Codigo

        elif self.Tipo_guardar == 2:
            consulta = 'SELECT * FROM Folletos ORDER BY Codigo ASC'
            filas = self.Conexion(consulta)
            Codigo = 20000

            for i in filas:
                print(i[0])
                if i[0] == 0:
                    return Codigo
                if Codigo == i[0]:
                    Codigo += 1
            return Codigo

        elif self.Tipo_guardar == 3:
            consulta = 'SELECT * FROM Revistas ORDER BY Codigo ASC'
            filas = self.Conexion(consulta)
            Codigo = 30000

            for i in filas:
                print(i[0])
                if i[0] == 0:
                    return Codigo
                if Codigo == i[0]:
                    Codigo += 1
            return Codigo

        elif self.Tipo_guardar == 4:
            consulta = 'SELECT * FROM Didacticos ORDER BY Codigo ASC'
            filas = self.Conexion(consulta)
            Codigo = 40000

            for i in filas:
                print(i[0])
                if i[0] == 0:
                    return Codigo
                if Codigo == i[0]:
                    Codigo += 1
            return Codigo
#verifica si hay base de datos

if len(lista_admi)==0:
	def verificarA():
		if len(usuario.get())>0 and len(contraseña.get())>0:
			guardar()

	def guardar():
		
		conexion=sqlite3.connect('Base_total')
		cursor=conexion.cursor()
		cursor.execute("INSERT INTO ADMINISTRATIVO VALUES(NULL,?,?)",(usuario.get(), contraseña.get()))
		messagebox.showinfo('Administrador', 'Administrador ingresado correctamete.')
		conexion.commit()
		cursor.close()
		conexion.close()
		raizs.destroy()
		inicioP()

	raizs=Tk()
	usuario=StringVar()
	contraseña=StringVar()
	raizs.title('UIS')
	raizs.iconbitmap('UISIcono.ico')
	raizs.config(bg='AliceBlue')
	Label(raizs,text='Bienvenido',bg='AliceBlue',font=18).grid(row=0,column=0, columnspan=3)
	Label(raizs, text='Por favor ingrese los datos para crear el usuario del administrador',bg='AliceBlue').grid(row=1,column=0, columnspan=3)
	Label(raizs, text="Usuario:",bg='AliceBlue').grid(row=2,column=0)
	Entry(raizs, textvariable=usuario).grid(row=2, column=1)
	Label(raizs, text="Contraseña: ",bg='AliceBlue').grid(row=3, column=0)
	Entry(raizs, textvariable=contraseña).grid(row=3, column=1)
	Button(raizs, text='Guardar', command=lambda:verificarA()).grid(row=4, column=0, columnspan=3)
	raizs.mainloop()
else:
	inicioP()
