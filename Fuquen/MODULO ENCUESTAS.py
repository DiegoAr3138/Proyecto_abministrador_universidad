from tkinter import *
from tkinter import messagebox
import sqlite3
import time

coneccion = sqlite3.connect("ENCUESTAS")
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
    PREGUNTA10 TEXT)""")
cursor.close()
coneccion.close()

respuestasDesercionU=list()
respuestasDesercionU.append('Nombre&Pregunta 1&Pregunta 2&Pregunta 3&Pregunta 4&Pregunta 5&Pregunta 6&Pregunta 7&Pregunta 8&Pregunta 9&Pregunta 10')
def desercionU():
	def guardar():
		global respuestasDesercionU
		n=nombre.get()
		#e=edad.get()
		#c=carrera.get()
		p1=preguntas1.get()
		p2=preguntas2.get()
		p3=preguntas3.get()
		p4=preguntas4.get()
		p5=preguntas5.get()
		p6=preguntas6.get()
		p7=preguntas7.get()
		p8=preguntas8.get()
		p9=preguntas9.get()
		p10=preguntas10.get()


		#'Nombre&Edad&Carrera&Pregunta 1&Pregunta 2&Pregunta 3&Pregunta 4&Pregunta 5&Pregunta 6&Pregunta 7&Pregunta 8&Pregunta 9&Pregunta 10'
		#[Nombre , Edad , Carrera , Pregunta,..., Pregunta 10]
		
		respuestasDesercionU.append(n+'&'+e+'&'+c+'&'+p1+'&'+str(p2)+'&'+str(p3)+'&'+str(p4)+'&'+str(p5)+'&'+str(p6)+'&'+str(p7)+'&'+str(p8)+'&'+str(p9)+'&'+str(p10))

	def siguiente():
		#respuestasDesercionU.append(n+'&'+e+'&'+c+'&'+p1+'&'+str(p2)+'&'+str(p3)+'&'+str(p4)+'&'+str(p5))
		vDesercion=Toplevel()
		vDesercion.geometry("700x600")
		vDesercion.config(bg='AliceBlue')
	
#preunta 6
		Label(vDesercion,text='6.¿Quien eligio su carrera?').place(x=20,y=20)
		Radiobutton(vDesercion,text='yo',variable=pregunta6,value=1).place(x=22,y=50)
		Radiobutton(vDesercion,text='Mis padres',variable=pregunta6,value=2).place(x=22,y=80)
		Radiobutton(vDesercion,text='Mis amigos',variable=pregunta6,value=3).place(x=22,y=110)
		Radiobutton(vDesercion,text='Otros',variable=pregunta6,value=4).place(x=22,y=140)
#pregunta 7
		Label(vDesercion,text='7.¿Cual es la forma en que finacia sus estudios?').place(x=20,y=170)
		Radiobutton(vDesercion,text='Recursos propios',variable=pregunta7,value=1).place(x=22,y=200)
		Radiobutton(vDesercion,text='Recursos familiares',variable=pregunta7,value=2).place(x=22,y=230)
		Radiobutton(vDesercion,text='Otros',variable=pregunta7,value=3).place(x=22,y=260)
#pregunta 8
		Label(vDesercion,text='8.¿Condicion laboral?').place(x=20,y=290)
		Radiobutton(vDesercion,text='Trabajando',variable=pregunta8,value=1).place(x=22,y=320)
		Radiobutton(vDesercion,text='Buscando Trabajo',variable=pregunta8,value=2).place(x=22,y=350)
		Radiobutton(vDesercion,text='no trabajo',variable=pregunta8,value=3).place(x=22,y=380)
#pregunta 9
		Label(vDesercion,text='9.¿Se siente satisfecho con sus estudios universitarios?').place(x=20,y=410)
		Radiobutton(vDesercion,text='Si',variable=pregunta9,value=1).place(x=22,y=440)
		Radiobutton(vDesercion,text='No',variable=pregunta9,value=2).place(x=22,y=470)
#preunta 10
		Label(vDesercion,text='10.¿Conoce a alguien que deserto?').place(x=20,y=500)
		Radiobutton(vDesercion,text='Si',variable=pregunta10,value=1).place(x=22,y=530)
		Radiobutton(vDesercion,text='No',variable=pregunta10,value=2).place(x=22,y=560)


		Button(vDesercion,text='Enviar',command=lambda:(guardar(),vDesercion.destroy())).place(x=350,y=590)

	
	nombre=StringVar()
	edad=StringVar()
	carrera=StringVar()
	pregunta1=StringVar()
	pregunta2=IntVar()
	pregunta3=IntVar()
	pregunta4=IntVar()
	pregunta5=IntVar()
	pregunta6=IntVar()
	pregunta7=IntVar()
	pregunta8=IntVar()
	pregunta9=IntVar()
	pregunta10=IntVar()

	vDesercion=Toplevel()
	vDesercion.geometry("700x600")
	vDesercion.config(bg='AliceBlue')


	Label(vDesercion,text='Nombre').place(x=20,y=20)
	Entry(vDesercion,textvariable=nombre).place(x=100,y=20)

	Label(vDesercion,text='Edad').place(x=250,y=20)
	Entry(vDesercion,textvariable=edad).place(x=300,y=20)

	Label(vDesercion,text='Carrera').place(x=20,y=50)
	Entry(vDesercion,textvariable=carrera).place(x=100,y=50)
#//////////////////////////////////////////////////////////////////////////////////////////////////
	Label(vDesercion,text='1. Que opina cerca de la desercion universitaria').place(x=20,y=80)
	Entry(vDesercion,textvariable=pregunta1,width=90).place(x=20,y=110)
#preunta 2
	Label(vDesercion,text='2.¿Que causas cree que influyen en la desercion universitaria?').place(x=20,y=140)
	Radiobutton(vDesercion,text='Dinero',variable=pregunta2,value=1).place(x=22,y=170)
	Radiobutton(vDesercion,text='Tiempo',variable=pregunta2,value=2).place(x=22,y=200)
	Radiobutton(vDesercion,text='Trabajo',variable=pregunta2,value=3).place(x=22,y=230)
	Radiobutton(vDesercion,text='Otro',variable=pregunta2,value=4).place(x=22,y=260)
#pregunta 3
	Label(vDesercion,text='3.¿Usted cree que el bajo desempeño se un factor de desercion universitaria?').place(x=20,y=290)
	Radiobutton(vDesercion,text='Si',variable=pregunta3,value=1).place(x=22,y=320)
	Radiobutton(vDesercion,text='No',variable=pregunta3,value=2).place(x=22,y=350)
#pregunta 4
	Label(vDesercion,text='4.¿Penso usted alguna vez en dejar sus estudios universitarios?').place(x=20,y=380)
	Radiobutton(vDesercion,text='Si',variable=pregunta4,value=1).place(x=22,y=410)
	Radiobutton(vDesercion,text='No',variable=pregunta4,value=2).place(x=22,y=440)
#pregunta 5
	Label(vDesercion,text='5.¿Se siente satisfecho con sus estudios universitarios?').place(x=20,y=470)
	Radiobutton(vDesercion,text='Si',variable=pregunta5,value=1).place(x=22,y=500)
	Radiobutton(vDesercion,text='No',variable=pregunta5,value=2).place(x=22,y=530)

	Button(vDesercion,text='Next',command=lambda:(siguiente(),vDesercion.destroy())).place(x=350,y=560)




'''def encuestas():
	vEncuestas=Toplevel()
	vEncuestas.config(bg='AliceBlue')
	
	Label(vEncuestas,text='Selecione una encuesta').grid(row=0,column=0)
	Button(vEncuestas,text='Desercion Universitaria',command=lambda:(desercionU(),vEncuestas.destroy())).grid(row=1,column=0,pady=5,padx=5)
	Button(vEncuestas,text='otro').grid(row=2,column=0,pady=5,padx=5)
	Button(vEncuestas,text='otro').grid(row=3,column=0,pady=5,padx=5)
	Button(vEncuestas,text='otro').grid(row=4,column=0,pady=5,padx=5)'''


def crear():
	nuevo=Toplevel()
	nuevo.title("CREAR ENCUESTAS")
	nuevo.config(bg='AliceBlue')

	Label(nuevo,text='Selecione el tipo de respuesta\n que desea implementar').grid(row=0,column=0)
	Button(nuevo,text='Seleccion multiple',command=lambda:preguntas1()).grid(row=1,column=0,pady=5,padx=5)
	Button(nuevo,text='Respuesta abierta',command=lambda:preguntas2()).grid(row=2,column=0,pady=5,padx=5)
	

def preguntas1():
        def guardar():
                coneccion = sqlite3.connect("ENCUESTAS")
                cursor = coneccion.cursor()
                cursor.execute("INSERT INTO ENCUESTAS(ENCUESTA,NOMBRE,PREGUNTA1,PREGUNTA2,PREGUNTA3,PREGUNTA4,PREGUNTA5,PREGUNTA6,PREGUNTA7,PREGUNTA8,PREGUNTA9,PREGUNTA10) VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?)",(nombre.get(), preguntas.get(),preguntas2.get(),preguntas3.get(),preguntas4.get(),preguntas5.get(),preguntas6.get(),preguntas7.get(),preguntas8.get(),preguntas9.get(),preguntas10.get()))
                coneccion.commit()
                cursor.close()
                coneccion.close()
                crear.destroy()
                messagebox.showinfo('Encuesta Creada', 'Encuesta creada correctamente.')

        crear=Toplevel()
        crear.title("ENCUESTA NUEVA")
        crear.config(bg='AliceBlue')

        global nombre, preguntas, preguntas2, preguntas3, preguntas4, preguntas5, preguntas6, preguntas7, preguntas8, preguntas9, preguntas10

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
    
        Label(crear, text="Nombre de la encuesta: ").grid(row=0,column=0, pady=10, padx=10)
        Entry(crear, width=20, textvariable=nombre).grid(row=0,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="1) ").grid(row=1,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas).grid(row=1,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="2) ").grid(row=2,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas2).grid(row=2,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="3) ").grid(row=3,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas3).grid(row=3,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="4) ").grid(row=4,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas4).grid(row=4,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="5) ").grid(row=5,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas5).grid(row=5,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="6) ").grid(row=6,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas6).grid(row=6,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="7) ").grid(row=7,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas7).grid(row=7,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="8) ").grid(row=8,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas8).grid(row=8,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="9) ").grid(row=9,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas9).grid(row=9,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="10) ").grid(row=10,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas10).grid(row=10,column=1, sticky='w',padx=10,pady=10)
				
        Button(crear, text="Crear", command=lambda:(guardar(),crear.destroy())).grid(row=11,column=1, pady=10, padx=10)

def preguntas2():
        def guardar():
                coneccion = sqlite3.connect("ENCUESTAS")
                cursor = coneccion.cursor()
                cursor.execute("INSERT INTO ENCUESTAS(ENCUESTA,NOMBRE,PREGUNTA1,PREGUNTA2,PREGUNTA3,PREGUNTA4,PREGUNTA5,PREGUNTA6,PREGUNTA7,PREGUNTA8,PREGUNTA9,PREGUNTA10) VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?)",(nombre.get(), preguntas.get(),preguntas2.get(),preguntas3.get(),preguntas4.get(),preguntas5.get(),preguntas6.get(),preguntas7.get(),preguntas8.get(),preguntas9.get(),preguntas10.get()))
                coneccion.commit()
                cursor.close()
                coneccion.close()
                crear.destroy()
                messagebox.showinfo('Encuesta Creada', 'Encuesta creada correctamente.')

        crear=Toplevel()
        crear.title("ENCUESTA NUEVA")
        crear.config(bg='AliceBlue')

        global nombre, preguntas, preguntas2, preguntas3, preguntas4, preguntas5, preguntas6, preguntas7, preguntas8, preguntas9, preguntas10

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
    
        Label(crear, text="Nombre de la encuesta: ").grid(row=0,column=0, pady=10, padx=10)
        Entry(crear, width=20, textvariable=nombre).grid(row=0,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="1) ").grid(row=1,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas).grid(row=1,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="2) ").grid(row=2,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas2).grid(row=2,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="3) ").grid(row=3,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas3).grid(row=3,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="4) ").grid(row=4,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas4).grid(row=4,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="5) ").grid(row=5,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas5).grid(row=5,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="6) ").grid(row=6,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas6).grid(row=6,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="7) ").grid(row=7,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas7).grid(row=7,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="8) ").grid(row=8,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas8).grid(row=8,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="9) ").grid(row=9,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas9).grid(row=9,column=1, sticky='w',padx=10,pady=10)

        Label(crear, text="10) ").grid(row=10,column=0, pady=10, padx=10)
        Entry(crear, width=90, textvariable=preguntas10).grid(row=10,column=1, sticky='w',padx=10,pady=10)
				
        Button(crear, text="Crear", command=lambda:(guardar(),crear.destroy())).grid(row=11,column=1, pady=10, padx=10)

def responder():
        eleccion=Toplevel()
        eleccion.title("CUAL ENCUESTA DESEA RESPONDER")
        eleccion.config(bg='AliceBlue')

        Label(eleccion, text="Elija la respuesta con la que\n decidio crear la encuesta").grid(row=0,column=1, pady=10, padx=10)
        Button(eleccion, text="Seleccion multiple", command=lambda:(responder1(),eleccion.destroy())).grid(row=3,column=1, pady=10, padx=10)
        Button(eleccion, text="Respuesta abierta", command=lambda:(responder2(),eleccion.destroy())).grid(row=5,column=1, pady=10, padx=10)

def responder1():
        def verificacion():
                if ENCUESTA.get().isdigit():
                        coneccion=sqlite3.connect("ENCUESTAS")
                        cursor=coneccion.cursor()
                        cursor.execute("SELECT * FROM ENCUESTAS WHERE ENCUESTA='%s'"%(int(ENCUESTA.get())))
                        encuesta=cursor.fetchall()
                        cursor.close()
                        coneccion.close()
                        global encontrarENCUESTA

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

                        else:
                                if messagebox.askretrycancel('ENCUESTA incorrecta','Por favor verifique que la ENCUESTA exista'):
                                        pass
                                else:
                                        Buscar.destroy()
                else:
                        if messagebox.askretrycancel('ENCUESTA incorrecta','Por favor verifique que la ENCUESTA sea un numero.'):
                                pass
                        else:
                                Buscar.destroy()

        def mostrar():
                if telefono.get().isdigit():
                        coneccion = sqlite3.connect("ENCUESTAS")
                        cursor = coneccion.cursor()
                        cursor.execute("""SELECT * FROM CONTACTOS WHERE ENCUESTA='%s' """%(int(ENCUESTA.get())))
                        coneccion.commit()
                        cursor.close()
                        coneccion.close()
                        Buscar.destroy()
                else:
                        pass

        def actualizar():
                textID.delete('1.0','end')
                textNombre.delete('1.0','end')

                coneccion=sqlite3.connect("ENCUESTAS")
                cursor=coneccion.cursor()
                cursor.execute("SELECT * FROM ENCUESTAS")

                encuesta=cursor.fetchall()

                for i in encuesta:
                        textID.insert(INSERT,i[0])
                        textID.insert(INSERT,'\n')
                        textNombre.insert(INSERT,i[1]+'\n')

                cursor.close()
                coneccion.close()
			

        global nombre, preguntas, preguntas2, preguntas3, preguntas4, preguntas5, preguntas6, preguntas7, preguntas8, preguntas9, preguntas10

        ENCUESTA=StringVar()
        nombre=StringVar()
        preguntas=IntVar()
        preguntas2=IntVar()
        preguntas3=IntVar()
        preguntas4=IntVar()
        preguntas5=IntVar()
        preguntas6=IntVar()
        preguntas7=IntVar()
        preguntas8=IntVar()
        preguntas9=IntVar()
        preguntas10=IntVar()

        pregunta=IntVar()
        pregunta2=IntVar()
        pregunta3=IntVar()
        pregunta4=IntVar()
        pregunta5=IntVar()
        pregunta6=IntVar()
        pregunta7=IntVar()
        pregunta8=IntVar()
        pregunta9=IntVar()
        pregunta10=IntVar()

        Buscar=Toplevel()
        Buscar.title("BUSCAR ENCUESTA")
        Buscar.config(bg='AliceBlue')
        global encontrarENCUESTA
        encontrarENCUESTA=False

        global textNombre, textID

        Label(Buscar,text='').grid(row=1,column=0)

        Label(Buscar,text='ID',bg='AliceBlue').grid(row=1,column=0)
        Label(Buscar,text='Nombre',bg='AliceBlue').grid(row=1,column=1)

        textID = Text(Buscar,width=3, height=15)
        textNombre = Text(Buscar,width=15, height=15)

        textID.grid(row=2,column=0)
        textNombre.grid(row=2,column=1)

        Button(Buscar,text='Actualizar',command=lambda:actualizar() ).grid(row=3,column=0,columnspan=7)

        Label(Buscar,text='Ingrese el numero de encuesta que desea responder:  ',bg='AliceBlue').grid(row=4,column=0, sticky='w',padx=5,pady=5)
        Entry(Buscar, width=20, textvariable=ENCUESTA).grid(row=4,column=1, sticky='w',padx=5,pady=5)
        Button(Buscar,text='Buscar',command=lambda:verificacion()).grid(row=4,column=2,columnspan=2)

        Label(Buscar, text="Nombre: ",bg='AliceBlue').grid(row=5,column=0, pady=10, padx=10)
        Label(Buscar, width=20, textvariable=nombre,bd=0,bg='AliceBlue').grid(row=5, column=1, sticky='w',padx=5,pady=5)

        Button(Buscar,text='Responder',command=lambda:(rta())).grid(row=6,column=1,columnspan=2)

        def rta():
            if encontrarENCUESTA:
                res=Toplevel()
                res.title("RESPONDER ENCUESTA")
                res.config(bg='AliceBlue')
                
                Label(res, width=50, textvariable=preguntas,bd=0).grid(row=1,column=0, sticky='w',padx=5,pady=5)
                Radiobutton(res,text='Si',variable=pregunta,value=1).grid(row=2,column=0, pady=10, padx=10)
                Radiobutton(res,text='No',variable=pregunta,value=2).grid(row=3,column=0, pady=10, padx=10)

                Label(res, width=50, textvariable=preguntas2,bd=0).grid(row=4,column=0, sticky='w',padx=5,pady=5)
                Radiobutton(res,text='Si',variable=pregunta2,value=1).grid(row=5,column=0, pady=10, padx=10)
                Radiobutton(res,text='No',variable=pregunta2,value=2).grid(row=6,column=0, pady=10, padx=10)

                Label(res, width=50, textvariable=preguntas3,bd=0).grid(row=7,column=0, sticky='w',padx=5,pady=5)
                Radiobutton(res,text='Si',variable=pregunta3,value=1).grid(row=8,column=0, pady=10, padx=10)
                Radiobutton(res,text='No',variable=pregunta3,value=2).grid(row=9,column=0, pady=10, padx=10)

                Label(res, width=50, textvariable=preguntas4,bd=0).grid(row=10,column=0, sticky='w',padx=5,pady=5)
                Radiobutton(res,text='Si',variable=pregunta4,value=1).grid(row=11,column=0, pady=10, padx=10)
                Radiobutton(res,text='No',variable=pregunta4,value=2).grid(row=12,column=0, pady=10, padx=10)

                Label(res, width=50, textvariable=preguntas5,bd=0).grid(row=13,column=0, sticky='w',padx=5,pady=5)
                Radiobutton(res,text='Si',variable=pregunta5,value=1).grid(row=14,column=0, pady=10, padx=10)
                Radiobutton(res,text='No',variable=pregunta5,value=2).grid(row=15,column=0, pady=10, padx=10)

                Button(res,text='Siguiente',command=lambda:(siguiente1(),res.destroy())).grid(row=16,column=0)

        def siguiente1():
                res=Toplevel()
                res.title("RESPONDER ENCUESTA")
                res.config(bg='AliceBlue')

                Label(res, width=50, textvariable=preguntas6,bd=0).grid(row=0,column=0, sticky='w',padx=5,pady=5)
                Radiobutton(res,text='Si',variable=pregunta6,value=1).grid(row=1,column=0, pady=10, padx=10)
                Radiobutton(res,text='No',variable=pregunta6,value=2).grid(row=2,column=0, pady=10, padx=10)

                Label(res, width=50, textvariable=preguntas7,bd=0).grid(row=3,column=0, sticky='w',padx=5,pady=5)
                Radiobutton(res,text='Si',variable=pregunta7,value=1).grid(row=4,column=0, pady=10, padx=10)
                Radiobutton(res,text='No',variable=pregunta7,value=2).grid(row=5,column=0, pady=10, padx=10)

                Label(res, width=50, textvariable=preguntas8,bd=0).grid(row=6,column=0, sticky='w',padx=5,pady=5)
                Radiobutton(res,text='Si',variable=pregunta8,value=1).grid(row=7,column=0, pady=10, padx=10)
                Radiobutton(res,text='No',variable=pregunta8,value=2).grid(row=8,column=0, pady=10, padx=10)

                Label(res, width=50, textvariable=preguntas9,bd=0).grid(row=9,column=0, sticky='w',padx=5,pady=5)
                Radiobutton(res,text='Si',variable=pregunta9,value=1).grid(row=10,column=0, pady=10, padx=10)
                Radiobutton(res,text='No',variable=pregunta9,value=2).grid(row=11,column=0, pady=10, padx=10)

                Label(res, width=50, textvariable=preguntas10,bd=0).grid(row=12,column=0, sticky='w',padx=5,pady=5)
                Radiobutton(res,text='Si',variable=pregunta10,value=1).grid(row=13,column=0, pady=10, padx=10)
                Radiobutton(res,text='No',variable=pregunta10,value=2).grid(row=14,column=0, pady=10, padx=10)

                Button(res,text='Guardar',command=lambda:(guardar1(),res.destroy())).grid(row=15,column=0)
                                
        def guardar1():
                global respuestasDesercionU
                n=nombre.get()
                p1=pregunta.get()
                p2=pregunta2.get()
                p3=pregunta3.get()
                p4=pregunta4.get()
                p5=pregunta5.get()
                p6=pregunta6.get()
                p7=pregunta7.get()
                p8=pregunta8.get()
                p9=pregunta9.get()
                p10=pregunta10.get()

                respuestasDesercionU.append(n+'&'+str(p1)+'&'+str(p2)+'&'+str(p3)+'&'+str(p4)+'&'+str(p5)+'&'+str(p6)+'&'+str(p7)+'&'+str(p8)+'&'+str(p9)+'&'+str(p10))

def responder2():
        def verificacion():
                if ENCUESTA.get().isdigit():
                        global encontrarENCUESTA

                        encontrarENCUESTA=False

                        coneccion=sqlite3.connect("ENCUESTAS")
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

                        else:
                                if messagebox.askretrycancel('ENCUESTA incorrecta','Por favor verifique que la ENCUESTA exista'):
                                        pass
                                else:
                                        Buscar.destroy()
                else:
                        if messagebox.askretrycancel('ENCUESTA incorrecta','Por favor verifique que la ENCUESTA sea un numero.'):
                                pass
                        else:
                                Buscar.destroy()

        def mostrar():
                if telefono.get().isdigit():
                        coneccion = sqlite3.connect("ENCUESTAS")
                        cursor = coneccion.cursor()
                        cursor.execute("""SELECT * FROM CONTACTOS WHERE ENCUESTA='%s' """%(int(ENCUESTA.get())))
                        coneccion.commit()
                        cursor.close()
                        coneccion.close()
                        Buscar.destroy()
                else:
                        pass
			

        global nombre, preguntas, preguntas2, preguntas3, preguntas4, preguntas5, preguntas6, preguntas7, preguntas8, preguntas9, preguntas10

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

        pregunta=StringVar()
        pregunta2=StringVar()
        pregunta3=StringVar()
        pregunta4=StringVar()
        pregunta5=StringVar()
        pregunta6=StringVar()
        pregunta7=StringVar()
        pregunta8=StringVar()
        pregunta9=StringVar()
        pregunta10=StringVar()

        Buscar=Toplevel()
        Buscar.title("BUSCAR ENCUESTA")
        Buscar.config(bg='AliceBlue')

        global textNombre, textID

        Label(Buscar,text='').grid(row=1,column=0)

        Label(Buscar,text='ID').grid(row=1,column=0)
        Label(Buscar,text='Nombre').grid(row=1,column=1)

        textID = Text(Buscar,width=3, height=15)
        textNombre = Text(Buscar,width=15, height=15)

        textID.grid(row=2,column=0)
        textNombre.grid(row=2,column=1)

        Button(Buscar,text='Actualizar',command=lambda:actualizar() ).grid(row=3,column=0,columnspan=7)

        def actualizar():
                textID.delete('1.0','end')
                textNombre.delete('1.0','end')

                coneccion=sqlite3.connect("ENCUESTAS")
                cursor=coneccion.cursor()
                cursor.execute("SELECT * FROM ENCUESTAS")

                encuesta=cursor.fetchall()

                for i in encuesta:
                        textID.insert(INSERT,i[0])
                        textID.insert(INSERT,'\n')
                        textNombre.insert(INSERT,i[1]+'\n')

                cursor.close()
                coneccion.close()

        Label(Buscar,text='Ingrese el numero de encuesta que desea responder:  ').grid(row=4,column=0, sticky='w',padx=5,pady=5)
        Entry(Buscar, width=20, textvariable=ENCUESTA).grid(row=4,column=1, sticky='w',padx=5,pady=5)
        Button(Buscar,text='Buscar',command=lambda:verificacion()).grid(row=4,column=2,columnspan=2)

        Label(Buscar, text="Nombre: ").grid(row=5,column=0, pady=10, padx=10)
        Label(Buscar, width=20, textvariable=nombre,bd=0).grid(row=5, column=1, sticky='w',padx=5,pady=5)

        Button(Buscar,text='Responder',command=lambda:rta()).grid(row=6,column=1,columnspan=2)

        def rta():
                res=Toplevel()
                res.title("RESPONDER ENCUESTA")
                res.config(bg='AliceBlue')
                
                Label(res, width=50, textvariable=preguntas,bd=0).grid(row=1,column=0, sticky='w',padx=5,pady=5)
                Entry(res, width=50, textvariable=pregunta).grid(row=2,column=0, sticky='w',padx=5,pady=5)

                Label(res, width=50, textvariable=preguntas2,bd=0).grid(row=3,column=0, sticky='w',padx=5,pady=5)
                Entry(res, width=50, textvariable=pregunta2).grid(row=4,column=0, sticky='w',padx=5,pady=5)
                
                Label(res, width=50, textvariable=preguntas3,bd=0).grid(row=5,column=0, sticky='w',padx=5,pady=5)
                Entry(res, width=50, textvariable=pregunta3).grid(row=6,column=0, sticky='w',padx=5,pady=5)

                Label(res, width=50, textvariable=preguntas4,bd=0).grid(row=7,column=0, sticky='w',padx=5,pady=5)
                Entry(res, width=50, textvariable=pregunta4).grid(row=8,column=0, sticky='w',padx=5,pady=5)
                
                Label(res, width=50, textvariable=preguntas5,bd=0).grid(row=9,column=0, sticky='w',padx=5,pady=5)
                Entry(res, width=50, textvariable=pregunta5).grid(row=10,column=0, sticky='w',padx=5,pady=5)

                Button(res,text='Siguiente',command=lambda:(siguiente1(),res.destroy())).grid(row=11,column=0)

        def siguiente1():
                res=Toplevel()
                res.title("RESPONDER ENCUESTA")
                res.config(bg='AliceBlue')
                
                Label(res, width=50, textvariable=preguntas6,bd=0).grid(row=1,column=0, sticky='w',padx=5,pady=5)
                Entry(res, width=50, textvariable=pregunta6).grid(row=2,column=0, sticky='w',padx=5,pady=5)

                Label(res, width=50, textvariable=preguntas7,bd=0).grid(row=3,column=0, sticky='w',padx=5,pady=5)
                Entry(res, width=50, textvariable=pregunta7).grid(row=4,column=0, sticky='w',padx=5,pady=5)

                Label(res, width=50, textvariable=preguntas8,bd=0).grid(row=5,column=0, sticky='w',padx=5,pady=5)
                Entry(res, width=50, textvariable=pregunta8).grid(row=6,column=0, sticky='w',padx=5,pady=5)

                Label(res, width=50, textvariable=preguntas9,bd=0).grid(row=7,column=0, sticky='w',padx=5,pady=5)
                Entry(res, width=50, textvariable=pregunta9).grid(row=8,column=0, sticky='w',padx=5,pady=5)

                Label(res, width=50, textvariable=preguntas10,bd=0).grid(row=9,column=0, sticky='w',padx=5,pady=5)
                Entry(res, width=50, textvariable=pregunta10).grid(row=10,column=0, sticky='w',padx=5,pady=5)

                Button(res,text='Guardar',command=lambda:(guardar1(),res.destroy())).grid(row=11,column=0)

        def guardar1():
                global respuestasDesercionU
                n=nombre.get()
                p1=pregunta.get()
                p2=pregunta2.get()
                p3=pregunta3.get()
                p4=pregunta4.get()
                p5=pregunta5.get()
                p6=pregunta6.get()
                p7=pregunta7.get()
                p8=pregunta8.get()
                p9=pregunta9.get()
                p10=pregunta10.get()

                respuestasDesercionU.append(n+'&'+p1+'&'+p2+'&'+p3+'&'+p4+'&'+p5+'&'+p6+'&'+p7+'&'+p8+'&'+p9+'&'+p10)

def respuestas():
	def ventanasDesercion():

		n=Text(vrespustas,width=10, height=15)
		#e=Text(vrespustas,width=10, height=15)
		#c=Text(vrespustas,width=10, height=15)
		p1=Text(vrespustas,width=10, height=15)
		p2=Text(vrespustas,width=10, height=15)
		p3=Text(vrespustas,width=10, height=15)
		p4=Text(vrespustas,width=10, height=15)
		p5=Text(vrespustas,width=10, height=15)
		p6=Text(vrespustas,width=10, height=15)
		p7=Text(vrespustas,width=10, height=15)
		p8=Text(vrespustas,width=10, height=15)
		p9=Text(vrespustas,width=10, height=15)
		p10=Text(vrespustas,width=11, height=15)


		
		for elemento in respuestasDesercionU:
			arreglo=elemento.split('&')

			n.insert(INSERT,arreglo[0]+'\n')
			#e.insert(INSERT,arreglo[1]+'\n')
			#c.insert(INSERT,arreglo[2]+'\n')
			p1.insert(INSERT,arreglo[1]+'\n')
			p2.insert(INSERT,arreglo[2]+'\n')
			p3.insert(INSERT,arreglo[3]+'\n')
			p4.insert(INSERT,arreglo[4]+'\n')
			p5.insert(INSERT,arreglo[5]+'\n')
			p6.insert(INSERT,arreglo[6]+'\n')
			p7.insert(INSERT,arreglo[7]+'\n')
			p8.insert(INSERT,arreglo[8]+'\n')
			p9.insert(INSERT,arreglo[9]+'\n')
			p10.insert(INSERT,arreglo[10]+'\n')

		n.grid(row=6,column=1)
		#e.grid(row=6,column=2)
		#c.grid(row=6,column=3)
		p1.grid(row=6,column=4)
		p2.grid(row=6,column=5)
		p3.grid(row=6,column=6)
		p4.grid(row=6,column=7)
		p5.grid(row=6,column=8)
		p6.grid(row=6,column=9)
		p7.grid(row=6,column=10)
		p8.grid(row=6,column=11)
		p9.grid(row=6,column=12)
		p10.grid(row=6,column=13)



	vrespustas=Toplevel()
	vrespustas.config(bg='AliceBlue')
	vrespustas.geometry("950x400")
	valores = []
	

	Button(vrespustas,text='RESULTADO DE LAS ENCUESTAS',command=ventanasDesercion).place(x=400,y=180)
	

#--------principal-------------------------------

raiz=Tk()
raiz.title("MODULO ENCUESTAS")
raiz.config(bg='AliceBlue')

Label(raiz, text='BIENVENIDO AL MODULO DE ENCUESTAS', font=("Calibri",15)).grid(row=0, column=0, pady=10, padx=10)
Label(raiz, text="PROGRAMACIÓN DE COMPUTADORES II", font=("Calibri",15)).grid(row=1, column=0, pady=10, padx=10)
Button(raiz,text='CREAR ENCUESTAS',command=crear).grid(row=2, column=0, pady=10, padx=10, sticky="news")
Button(raiz,text='RESPONDER ENCUESTAS',command=responder).grid(row=3, column=0, pady=10, padx=10, sticky="news")
Button(raiz,text='CONSULTAR RESPUESTAS',command=respuestas).grid(row=4, column=0, pady=10, padx=10, sticky="news")
Button(raiz, text="SALIR", command=lambda:raiz.destroy()).grid(row=5, column=0, pady=10, padx=10)
raiz.mainloop()
