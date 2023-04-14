from tkinter import *
from tkinter import messagebox
import sqlite3

raiz =Tk()

raiz.title('UIS')
raiz.iconbitmap('UISIcono.ico')
raiz.geometry('800x400')
barraMenu=Menu()
raiz.config(menu=barraMenu, bg='AliceBlue')


#---------------------------variables--------------------------------
usuario=StringVar('')
contrasena=StringVar('')
listaUsuariosA={'Diego':'1234'}
listaEstudiantes=[{'Nombre':'Diego','Codigo':'20000','Carrera':'Ingeneria electronica'}]
generadorCodigos=20000


#------------------------Funciones----------------------------------
def verificar():
	if usuario.get() in listaUsuariosA and listaUsuariosA[usuario.get()]==contrasena.get():
		administrativo()
	else:
		opcion=messagebox.askretrycancel('Error', 'Usuario o contraseña incorrecta')
		if opcion==True:
			Acceder()


def Acceder():

	global usuario
	global contrasena
	usuario=StringVar('')
	contrasena=StringVar('')

	vAcceder=Toplevel()
	vAcceder.title('Acceder')
	vAcceder.iconbitmap('UISIcono.ico')

	textUsuario=Label(vAcceder, text='Usuario')
	textUsuario.grid(row=0,column=0, sticky='w',padx=5,pady=5)
	cuadroUsuario=Entry(vAcceder,textvariable=usuario)
	cuadroUsuario.grid(row=0,column=1)

	textContrasena=Label(vAcceder,text='Contraseña')
	textContrasena.grid(row=1,column=0, sticky='w',padx=5,pady=5)
	cuadroContrasena=Entry(vAcceder,textvariable=contrasena)
	cuadroContrasena.grid(row=1,column=1)
	cuadroContrasena.config(show='*')


	boton1=Button(vAcceder,text='Entrar',command=lambda:[verificar(),vAcceder.destroy()])
	boton1.grid(row=2,column=0,columnspan=2)
	
	

#---------------------------------------admin--------------------------------------------------------

def administrativo():
	def admin():
		global n
		global c
		n=Text(vadministrativo,width=10, height=15)
		c=Text(vadministrativo,width=10, height=15)
		for i in listaUsuariosA:
			n.insert(INSERT,i)
			c.insert(INSERT, listaUsuariosA[i])
		n.place(x=150,y=200)
		c.place(x=250,y=200)

	def estudiantes():
		global n
		global c
		global botonCrear
		try:	
			n.destroy()
			c.destroy()
		except NameError:
			pass


		def crearEstudiantes():
			carrera=IntVar()
			nombreNuevo=StringVar()
			segundoNombreNuevo=StringVar()
			apellidoPaterno=StringVar()
			apellidoMaterno=StringVar()

			nuevoEstudiante=Toplevel()
			nuevoEstudiante.title('Nuevo Estudiante')
			nuevoEstudiante.geometry('700x500')
			nuevoEstudiante.config(bg='AliceBlue')

			def guardar():
				global generadorCodigos
				
				global listaEstudiantes
				tipoCarrera=''
				nombreCompleto=nombreNuevo.get()+' '+segundoNombreNuevo.get()+''+apellidoPaterno.get()+' '+apellidoMaterno.get()
				generadorCodigos+=1

				if carrera.get()==1:
					tipoCarrera='a'
				elif carrera.get()==2:
					tipoCarrera='b'
				elif carrera.get()==3:
					tipoCarrera='c'
				elif carrera.get()==4:
					tipoCarrera='d'

				listaEstudiantes.append({'Nombre':nombreCompleto,'Codigo':str(generadorCodigos),'Carrera':tipoCarrera})

			Label(nuevoEstudiante,text='Nombre').grid(row=0,column=0)
			Entry(nuevoEstudiante,width=20,textvariable=nombreNuevo).grid(row=0,column=1)

			Label(nuevoEstudiante,text='Segundo nombre').grid(row=1,column=0)
			Entry(nuevoEstudiante,width=20,textvariable=segundoNombreNuevo).grid(row=1,column=1)

			Label(nuevoEstudiante,text='Apellido paterno').grid(row=2,column=0)
			Entry(nuevoEstudiante,width=20,textvariable=apellidoPaterno).grid(row=2,column=1)

			Label(nuevoEstudiante,text='Apellido Materno').grid(row=3,column=0)
			Entry(nuevoEstudiante,width=20,textvariable=apellidoMaterno).grid(row=3,column=1)

			Label(nuevoEstudiante,text='Seleccione la carrera').grid(row=0,column=3)
			Radiobutton(nuevoEstudiante,text='Ingeneria',variable=carrera,value=1).grid(row=1,column=3)
			Radiobutton(nuevoEstudiante,text='Ingeneria',variable=carrera,value=2).grid(row=2,column=3)
			Radiobutton(nuevoEstudiante,text='Ingeneria',variable=carrera,value=3).grid(row=3,column=3)
			Radiobutton(nuevoEstudiante,text='Ingeneria',variable=carrera,value=4).grid(row=4,column=3)

			botonGuardar=Button(nuevoEstudiante,text='Guardar',command=lambda:[guardar(),nuevoEstudiante.destroy()]).grid(row=6,column=3)



		botonCrear=Button(vadministrativo,text='Crear Estudiante', command=crearEstudiantes).place(x=350,y=150)
		nombre=Text(vadministrativo,width=10, height=15)
		codigo=Text(vadministrativo,width=10, height=15)
		carrera=Text(vadministrativo,width=22, height=15)
		for i in range(len(listaEstudiantes)):
			nombre.insert(INSERT,listaEstudiantes[i]['Nombre']+'\n')
			codigo.insert(INSERT,listaEstudiantes[i]['Codigo']+'\n')
			carrera.insert(INSERT,listaEstudiantes[i]['Carrera']+'\n')

		nombre.place(x=150,y=200)
		codigo.place(x=250,y=200)
		carrera.place(x=350,y=200)

	vadministrativo=Toplevel()
	vadministrativo.title('Administrativo')
	vadministrativo.geometry('700x500')
	vadministrativo.config(bg='AliceBlue')

	texto1=Label(vadministrativo,text='Seleccione una opcion').place(x=20,y=30)

	botonProfesor=Button(vadministrativo,text='Profesores',width='15').place(x=20,y=60)

	botonEstudiantes=Button(vadministrativo,text='Estudiantes',width='15',command=estudiantes).place(x=20,y=90)

	botonBiblioteca=Button(vadministrativo,text='Biblioteca',width='15').place(x=20,y=120)

	botonAdministrativo=Button(vadministrativo,text='Administrativo',width='15',command=admin).place(x=20,y=150)





#------------------BARRA MENU -----------------------------------------
inicioMenu=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label='Inicio',menu=inicioMenu)

encuestasMenu=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label='Encuestas',menu=encuestasMenu)

profesorMenu=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label='Profesor',menu=profesorMenu)

estudianteMenu=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label='Estudiante',menu=estudianteMenu)

bibliotecaMenu=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label='Biblioteca',menu=bibliotecaMenu)

administrativoMenu=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label='Administrativo',menu=administrativoMenu)
administrativoMenu.add_command(label='Acceder', command=lambda:Acceder())

raiz.mainloop()