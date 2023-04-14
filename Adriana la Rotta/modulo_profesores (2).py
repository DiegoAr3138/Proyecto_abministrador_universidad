from tkinter import ttk
from tkinter import *
import sqlite3
import tkinter as tk
from tkinter import messagebox
import tkinter

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

        Button(frame, text='Ingresar',font=("Courier New CYR", 12, "italic"), command=self.ingresar).grid(row=3, columnspan=2, sticky=W + E)
        self.wind.mainloop()

    def conexion(self, query, parametros=()):
        '''conexion base de datos'''
        with sqlite3.connect('Base_total') as conn:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS PROFESORES (CODIGO INTEGER PRIMARY KEY AUTOINCREMENT,
                       NOMBRE VARCHAR,MATERIAS VARCHAR,CONTRASEÑA VARCHAR,VOTO INTEGER)""")
            cursor.execute("""CREATE TABLE IF NOT EXISTS NOTAS (CODIGO INTEGER ,NOMBRE VARCHAR,CARRERA VARCHAR,
                            SABER VARCHAR,SABERHACER INTEGER,SER VARCHAR,MATERIA)""")

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
            self.tabla.insert('', 'end', values=k)
            self.materiaprofesor=k[2]
            print(self.materiaprofesor)
        Button(self.win, text='Ingresar a la Materia', fg='green', command=lambda: self.materia()).grid(row=2, column=0)


    def materia(self):
        try:
            self.win.destroy()
        except AttributeError:
            pass
        self.win=Toplevel()



        Label(self.win,text='Materia1').grid(row=0, column=0,columnspan=3,sticky='we')
        self.tabla2 = ttk.Treeview(self.win, columns=(1, 2, 3, 4, 5, 6), show='headings', height='10')
        self.tabla2.grid(row=1, column=0, columnspan=3)
        self.tabla2.heading(1, text='Codigo')
        self.tabla2.heading(2, text='Nombre')
        self.tabla2.heading(3, text='CARRERA')
        self.tabla2.heading(4, text='SABER')
        self.tabla2.heading(5, text='SABER HACER')
        self.tabla2.heading(6, text='SER')
        parametros=(self.materiaprofesor)
        consulta='SELECT * FROM NOTAS WHERE MATERIA = ?'
        q=self.conexion(consulta , parametros)


        for k in q:
            self.tabla2.insert('', 'end', values=k)

        Label(self.win,text='').grid(row=1,column=0,columnspan=3,sticky='we')
        Button(self.win, text='Editar notas', fg='red', command=lambda: self.editarnotas()).grid(row=2, column=1)


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
        Button(self.win1, text='Guardar Notas', fg='red', command=lambda: self.guardarnotas()).grid(row=6, column=1)


    def guardarnotas(self):
        try:
            float(self.nota1nueva.get())
            parametros = (self.nota1nueva.get(), self.nota2nueva.get(), self.nota3nueva.get(),
                          self.tabla2.item(self.tabla2.selection())['values'][3],
                          self.tabla2.item(self.tabla2.selection())['values'][4],
                          self.tabla2.item(self.tabla2.selection())['values'][5], self.cd.get())
            consulta = 'UPDATE NOTAS SET SABER=?,SABERHACER=?,SER=? WHERE SABER=? AND SABERHACER=? AND SER=? AND CODIGO=?'

            self.conexion(consulta, parametros)
            messagebox.showinfo('Aviso', 'Nota Actualizada')
            self.win1.destroy()
            self.materia()



        except:
            if messagebox.askretrycancel('Nota incorrecta','Por favor verifique que la Nota sea un numero.'):
                pass
            else:
                print('')





notas()
