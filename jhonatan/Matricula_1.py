import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
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
     #Entada nombre1
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
             valores = (
             n, a, n1, a1, did, iden, ge, fe, ed, rhh, c, direc, salud, tsa, co1, t1, na, n1a, apa, ap1a, paren, ocup,c2, direc2, co2, t2, did2, iden2)
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
         cursor.execute("SELECT identidad FROM ESTUDIANTES_4 WHERE identidad = '%s'" % (iden))
         y = cursor.fetchall()
         yy = 0
         for i in y:
             yy = i[0]
         if int(yy) != int(iden):
             valores = (n, a, n1, a1, did, iden, ge, fe, ed, rhh, c, direc, salud, tsa, co1, t1, na, n1a, apa, ap1a, paren, ocup,c2, direc2, co2, t2, did2, iden2)
             cursor.execute("INSERT INTO ESTUDIANTES_4 (nombre,nombre2,apellido,apellido2,doc_id,identidad,genero,fecha_nacimiento,edad,rh,ciudad,direccion,salud,entidad,correo,telefono,acudiente,nombre2a,apellidoa,apellido2a,parentesco,ocupacion,ciudad2,direccion2,correo2,telefono2,doc_id2,identidad2)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (valores))
             messagebox.showinfo('GUARDAR', message='DATOS GUARDADOS CON EXITO')
         else:
             messagebox.showerror('ERROR', message='  YA EXISTE ESE NUMERO DE IDENTIDAD ')
         ruloz.commit()
         cursor.close()
         vcerrar.destroy()
     elif gra=='5':
         ruloz = sqlite3.connect("matriculas.db")
         cursor = ruloz.cursor()
         cursor.execute("SELECT identidad FROM ESTUDIANTES_5 WHERE identidad = '%s'" % (iden))
         y = cursor.fetchall()
         yy = 0
         for i in y:
             yy = i[0]
         if int(yy) != int(iden):
             valores = (n, a, n1, a1, did, iden, ge, fe, ed, rhh, c, direc, salud, tsa, co1, t1, na, n1a, apa, ap1a, paren, ocup,c2, direc2, co2, t2, did2, iden2)
             cursor.execute("INSERT INTO ESTUDIANTES_5 (nombre,nombre2,apellido,apellido2,doc_id,identidad,genero,fecha_nacimiento,edad,rh,ciudad,direccion,salud,entidad,correo,telefono,acudiente,nombre2a,apellidoa,apellido2a,parentesco,ocupacion,ciudad2,direccion2,correo2,telefono2,doc_id2,identidad2)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (valores))
             messagebox.showinfo('GUARDAR', message='DATOS GUARDADOS CON EXITO')
         else:
             messagebox.showerror('ERROR', message='  YA EXISTE ESE NUMERO DE IDENTIDAD ')
         ruloz.commit()
         cursor.close()
         vcerrar.destroy()
     elif gra=='6':
         ruloz = sqlite3.connect("matriculas.db")
         cursor = ruloz.cursor()
         cursor.execute("SELECT identidad FROM ESTUDIANTES_6 WHERE identidad = '%s'" % (iden))
         y = cursor.fetchall()
         yy = 0
         for i in y:
             yy = i[0]
         if int(yy) != int(iden):
             valores = (n, a, n1, a1, did, iden, ge, fe, ed, rhh, c, direc, salud, tsa, co1, t1, na, n1a, apa, ap1a, paren, ocup,c2, direc2, co2, t2, did2, iden2)
             cursor.execute("INSERT INTO ESTUDIANTES_6 (nombre,nombre2,apellido,apellido2,doc_id,identidad,genero,fecha_nacimiento,edad,rh,ciudad,direccion,salud,entidad,correo,telefono,acudiente,nombre2a,apellidoa,apellido2a,parentesco,ocupacion,ciudad2,direccion2,correo2,telefono2,doc_id2,identidad2)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (valores))
             messagebox.showinfo('GUARDAR', message='DATOS GUARDADOS CON EXITO')
         else:
             messagebox.showerror('ERROR', message='  YA EXISTE ESE NUMERO DE IDENTIDAD ')
         ruloz.commit()
         cursor.close()
         vcerrar.destroy()
     elif gra=='7':
         ruloz = sqlite3.connect("matriculas.db")
         cursor = ruloz.cursor()
         cursor.execute("SELECT identidad FROM ESTUDIANTES_7 WHERE identidad = '%s'" % (iden))
         y = cursor.fetchall()
         yy = 0
         for i in y:
             yy = i[0]
         if int(yy) != int(iden):
             valores = (n, a, n1, a1, did, iden, ge, fe, ed, rhh, c, direc, salud, tsa, co1, t1, na, n1a, apa, ap1a, paren, ocup,c2, direc2, co2, t2, did2, iden2)
             cursor.execute("INSERT INTO ESTUDIANTES_7 (nombre,nombre2,apellido,apellido2,doc_id,identidad,genero,fecha_nacimiento,edad,rh,ciudad,direccion,salud,entidad,correo,telefono,acudiente,nombre2a,apellidoa,apellido2a,parentesco,ocupacion,ciudad2,direccion2,correo2,telefono2,doc_id2,identidad2)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (valores))
             messagebox.showinfo('GUARDAR', message='DATOS GUARDADOS CON EXITO')
         else:
             messagebox.showerror('ERROR', message='  YA EXISTE ESE NUMERO DE IDENTIDAD ')
         ruloz.commit()
         cursor.close()
         vcerrar.destroy()
     elif gra=='8':
         ruloz = sqlite3.connect("matriculas.db")
         cursor = ruloz.cursor()
         cursor.execute("SELECT identidad FROM ESTUDIANTES_8 WHERE identidad = '%s'" % (iden))
         y = cursor.fetchall()
         yy = 0
         for i in y:
             yy = i[0]
         if int(yy) != int(iden):
             valores = (n, a, n1, a1, did, iden, ge, fe, ed, rhh, c, direc, salud, tsa, co1, t1, na, n1a, apa, ap1a, paren, ocup,c2, direc2, co2, t2, did2, iden2)
             cursor.execute("INSERT INTO ESTUDIANTES_8 (nombre,nombre2,apellido,apellido2,doc_id,identidad,genero,fecha_nacimiento,edad,rh,ciudad,direccion,salud,entidad,correo,telefono,acudiente,nombre2a,apellidoa,apellido2a,parentesco,ocupacion,ciudad2,direccion2,correo2,telefono2,doc_id2,identidad2)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (valores))
             messagebox.showinfo('GUARDAR', message='DATOS GUARDADOS CON EXITO')
         else:
             messagebox.showerror('ERROR', message='  YA EXISTE ESE NUMERO DE IDENTIDAD ')
         ruloz.commit()
         cursor.close()
         vcerrar.destroy()
     elif gra=='9':
         ruloz = sqlite3.connect("matriculas.db")
         cursor = ruloz.cursor()
         cursor.execute("SELECT identidad FROM ESTUDIANTES_9 WHERE identidad = '%s'" % (iden))
         y = cursor.fetchall()
         yy = 0
         for i in y:
             yy = i[0]
         if int(yy) != int(iden):
             valores = (n, a, n1, a1, did, iden, ge, fe, ed, rhh, c, direc, salud, tsa, co1, t1, na, n1a, apa, ap1a, paren, ocup,c2, direc2, co2, t2, did2, iden2)
             cursor.execute("INSERT INTO ESTUDIANTES_9 (nombre,nombre2,apellido,apellido2,doc_id,identidad,genero,fecha_nacimiento,edad,rh,ciudad,direccion,salud,entidad,correo,telefono,acudiente,nombre2a,apellidoa,apellido2a,parentesco,ocupacion,ciudad2,direccion2,correo2,telefono2,doc_id2,identidad2)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (valores))
             messagebox.showinfo('GUARDAR', message='DATOS GUARDADOS CON EXITO')
         else:
             messagebox.showerror('ERROR', message='  YA EXISTE ESE NUMERO DE IDENTIDAD ')
         ruloz.commit()
         cursor.close()
         vcerrar.destroy()
     elif gra=='10':
         ruloz = sqlite3.connect("matriculas.db")
         cursor = ruloz.cursor()
         cursor.execute("SELECT identidad FROM ESTUDIANTES_10 WHERE identidad = '%s'" % (iden))
         y = cursor.fetchall()
         yy = 0
         for i in y:
             yy = i[0]
         if int(yy) != int(iden):
             valores = (n, a, n1, a1, did, iden, ge, fe, ed, rhh, c, direc, salud, tsa, co1, t1, na, n1a, apa, ap1a, paren, ocup,c2, direc2, co2, t2, did2, iden2)
             cursor.execute("INSERT INTO ESTUDIANTES_10 (nombre,nombre2,apellido,apellido2,doc_id,identidad,genero,fecha_nacimiento,edad,rh,ciudad,direccion,salud,entidad,correo,telefono,acudiente,nombre2a,apellidoa,apellido2a,parentesco,ocupacion,ciudad2,direccion2,correo2,telefono2,doc_id2,identidad2)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (valores))
             messagebox.showinfo('GUARDAR', message='DATOS GUARDADOS CON EXITO')
         else:
             messagebox.showerror('ERROR', message='  YA EXISTE ESE NUMERO DE IDENTIDAD ')
         ruloz.commit()
         cursor.close()
         vcerrar.destroy()
     elif gra=='11':
         ruloz = sqlite3.connect("matriculas.db")
         cursor = ruloz.cursor()
         cursor.execute("SELECT identidad FROM ESTUDIANTES_11 WHERE identidad = '%s'" % (iden))
         y = cursor.fetchall()
         yy = 0
         for i in y:
             yy = i[0]
         if int(yy) != int(iden):
             valores = (n, a, n1, a1, did, iden, ge, fe, ed, rhh, c, direc, salud, tsa, co1, t1, na, n1a, apa, ap1a, paren, ocup,c2, direc2, co2, t2, did2, iden2)
             cursor.execute("INSERT INTO ESTUDIANTES_11 (nombre,nombre2,apellido,apellido2,doc_id,identidad,genero,fecha_nacimiento,edad,rh,ciudad,direccion,salud,entidad,correo,telefono,acudiente,nombre2a,apellidoa,apellido2a,parentesco,ocupacion,ciudad2,direccion2,correo2,telefono2,doc_id2,identidad2)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (valores))
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
def fmenu():
    ventana=tkinter.Tk()
    ventana.geometry("920x698+0+0")
    ventana.title("Menu de matricula")
    fondo=PhotoImage(file="menus.PNG")
    Label(ventana,image=fondo).place(x=0,y=0)
    #main_title=Label(text="BIENVENIDO", font=(20),bg='#56cd63',width="250",fg='white',height='2')
    #Botones GUARDAR, EDITAR, SALIR, NUEVO,
    bedita=Button(ventana, text='EDITAR',command=feditar,font=('Agency FB',28),width="30",bg='ivory3').place(x=350, y=312)
    bnuevoo=Button(ventana, text='NUEVO',command=fnuevo,font=('Agency FB',28),width="30",bg='ivory3').place(x=350, y=145)
    bsalirr=Button(ventana, text='SALIR',command=fsalir,font=('Agency FB',28),width="30",bg='ivory3').place(x=350, y=486)
    ventana.mainloop()
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

def fmostrar(ventedit,buscar,busgrado):
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
        if int(yy) != int(busqueda) or yy==0 :
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
        Label(vnuevo, text=' DATOS  ', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=4, column=4)
        Label(vnuevo, text='DE   EST', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=4, column=5)
        Label(vnuevo, text='UDIANTE', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=4, column=6)
        # Entada nombre1
        Label(vnuevo, text='Grado entrante: ', font=(15), bg='light gray', fg='dodger blue').grid(row=6, column=2)
        grado = Entry(vnuevo, textvariable=StringVar(value=buscgrado), state='readonly')
        grado.focus()
        grado.grid(row=6, column=3)
        Label(vnuevo, text='Primer nombre: ', font=(15), bg='light gray', fg='dodger blue').grid(row=7, column=2)
        nombre = Entry(vnuevo, textvariable=StringVar(value=mn), state='readonly')
        nombre.focus()
        nombre.grid(row=7, column=3)
        # Entrada nomre2
        Label(vnuevo, text='Segundo nombre: ', font=(15), bg='light gray', fg='dodger blue').grid(row=7, column=4)
        nombre1 = Entry(vnuevo, textvariable=StringVar(value=mn1), state='readonly')
        nombre1.grid(row=7, column=5)
        # Entrada de apellido1
        Label(vnuevo, text='Primer apellido: ', font=(15), bg='light gray', fg='dodger blue').grid(row=7, column=6)
        apellido = Entry(vnuevo, textvariable=StringVar(value=ma), state='readonly')
        apellido.grid(row=7, column=7)
        # Entrada de apellido2
        Label(vnuevo, text='Segundo apellido: ', font=(15), bg='light gray', fg='dodger blue').grid(row=7, column=8)
        apellido1 = Entry(vnuevo, textvariable=StringVar(value=ma1), state='readonly')
        apellido1.grid(row=7, column=9)
        # Entrada de identidad
        Label(vnuevo, text='Doc. id: ', font=(15), bg='light gray', fg='dodger blue').grid(row=8, column=2)
        did = StringVar()
        combo = Entry(vnuevo, textvariable=StringVar(value=mdid), state='readonly')
        combo.grid(row=8, column=3)
        # combo.current(1)
        Label(vnuevo, text='Numero de identidad: ', font=(15), bg='light gray', fg='dodger blue').grid(row=8, column=4)
        identidad = Entry(vnuevo, textvariable=StringVar(value=miden), state='readonly')
        identidad.grid(row=8, column=5)
        Label(vnuevo, text='Genero: ', font=(15), bg='light gray', fg='dodger blue').grid(row=8, column=6)
        genero = Entry(vnuevo, textvariable=StringVar(value=mge), state='readonly')
        genero.grid(row=8, column=7)
        Label(vnuevo, text='RH : ', font=(15), bg='light gray', fg='dodger blue').grid(row=8, column=8)
        rh = Entry(vnuevo, textvariable=StringVar(value=mrhh), state='readonly')
        rh.grid(row=8, column=9)
        # Entradad fecha de nacimiento
        Label(vnuevo, text='Fecha de nacimiento: ', font=(15), bg='light gray', fg='dodger blue').grid(row=9, column=2)
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
        Label(vnuevo, text='Correo electronico: ', font=(15), bg='light gray', fg='dodger blue').grid(row=11, column=2)
        correo1 = Entry(vnuevo, textvariable=StringVar(value=mco1), state='readonly')
        correo1.grid(row=11, column=3)
        Label(vnuevo, text='Telefono: ', font=(15), bg='light gray', fg='dodger blue').grid(row=11, column=4)
        telefono1 = Entry(vnuevo, textvariable=StringVar(value=mt1), state='readonly')
        telefono1.grid(row=11, column=5)
        # Datos acudiente
        # Entada nombre1
        Label(vnuevo, text='  DATOS ', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=16, column=4)
        Label(vnuevo, text='  DE    AC', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=16,
                                                                                                         column=5)
        Label(vnuevo, text='UDIENTE', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=16, column=6)
        Label(vnuevo, text='Primer nombre: ', font=(15), bg='light gray', fg='dodger blue').grid(row=19, column=2)
        nombrea = Entry(vnuevo, textvariable=StringVar(value=mn1a), state='readonly')
        nombrea.focus()
        nombrea.grid(row=19, column=3)
        # Entrada nomre2
        Label(vnuevo, text='Segundo nombre: ', font=(15), bg='light gray', fg='dodger blue').grid(row=19, column=4)
        nombre1a = Entry(vnuevo, textvariable=StringVar(value=mna), state='readonly')
        nombre1a.grid(row=19, column=5)
        # Entrada de apellido1
        Label(vnuevo, text='Primer apellido: ', font=(15), bg='light gray', fg='dodger blue').grid(row=19, column=6)
        apellidoa = Entry(vnuevo, textvariable=StringVar(value=mapa), state='readonly')
        apellidoa.grid(row=19, column=7)
        # Entrada de apellido2
        Label(vnuevo, text='Segundo apellido: ', font=(15), bg='light gray', fg='dodger blue').grid(row=19, column=8)
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
        Label(vnuevo, text='Correo electronico: ', font=(15), bg='light gray', fg='dodger blue').grid(row=21, column=2)
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
        Label(vnuevo, text='Numero de identidad: ', font=(15), bg='light gray', fg='dodger blue').grid(row=21, column=8)
        identidad2 = Entry(vnuevo, textvariable=StringVar(value=miden2), state='readonly')
        identidad2.grid(row=21, column=9)
        Button(vnuevo, text='EDITAR',command=lambda: f_editar(vnuevo,buscgrado, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med, mrhh, mc, mdirec, msa,
                                        mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2, mco2, mt2,
                                        mdid2, miden2), font=(30), bg='#56cd63', width="25", fg='white',
               height='2').place(x=250, y=600)
        Button(vnuevo, text='ELIMINAR', command=lambda: feliminar(vnuevo, buscgrado, busqueda), font=(30), bg='#56cd63',
               width="25", fg='white', height='2').place(x=790, y=600)
    else:
        pass
    ventedit.destroy()
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

def f_editar(vnuevo,buscgrado,mn,mn1,ma,ma1,mdid,miden,mge,mfe,med,mrhh,mc,mdirec,msa,mtsa,mco1,mt1,mna,mapa,mn1a,map1a,mparen,mocup,mc2,mdirec2,mco2,mt2,mdid2,miden2):
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
    Label(v_editar, text=' DATOS  ', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=4, column=4)
    Label(v_editar, text='DE   EST', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=4, column=5)
    Label(v_editar, text='UDIANTE', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=4, column=6)
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
    Label(v_editar, text='Primer apellido: ', font=(15), bg='light gray', fg='dodger blue').grid(row=7, column=6)
    apellido = Entry(v_editar, textvariable=StringVar(value=ma))
    apellido.grid(row=7, column=7)
    # Entrada de apellido2
    Label(v_editar, text='Segundo apellido: ', font=(15), bg='light gray', fg='dodger blue').grid(row=7, column=8)
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
    Label(v_editar, text='Numero de identidad: ', font=(15), bg='light gray', fg='dodger blue').grid(row=8, column=4)
    identidad = Entry(v_editar, textvariable=StringVar(value=miden), state='readonly')
    identidad.grid(row=8, column=5)
    Label(v_editar, text='Genero: ', font=(15), bg='light gray', fg='dodger blue').grid(row=8, column=6)
    genero = Entry(v_editar, textvariable=StringVar(value=mge))
    genero.grid(row=8, column=7)
    Label(v_editar, text='RH : ', font=(15), bg='light gray', fg='dodger blue').grid(row=8, column=8)
    rh = Entry(v_editar, textvariable=StringVar(value=mrhh))
    rh.grid(row=8, column=9)
    # Entradad fecha de nacimiento
    Label(v_editar, text='Fecha de nacimiento: ', font=(15), bg='light gray', fg='dodger blue').grid(row=9, column=2)
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
    Label(v_editar, text='Correo electronico: ', font=(15), bg='light gray', fg='dodger blue').grid(row=11, column=2)
    correo1 = Entry(v_editar, textvariable=StringVar(value=mco1))
    correo1.grid(row=11, column=3)
    Label(v_editar, text='Telefono: ', font=(15), bg='light gray', fg='dodger blue').grid(row=11, column=4)
    telefono1 = Entry(v_editar, textvariable=StringVar(value=mt1))
    telefono1.grid(row=11, column=5)
    # Datos acudiente
    # Entada nombre1
    Label(v_editar, text='  DATOS ', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=16, column=4)
    Label(v_editar, text='  DE    AC', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=16,column=5)
    Label(v_editar, text='UDIENTE', font=('Vineta BT', 15), bg='light gray', fg='dodger blue').grid(row=16, column=6)
    Label(v_editar, text='Primer nombre: ', font=(15), bg='light gray', fg='dodger blue').grid(row=19, column=2)
    nombrea = Entry(v_editar, textvariable=StringVar(value=mn1a))
    nombrea.focus()
    nombrea.grid(row=19, column=3)
    # Entrada nomre2
    Label(v_editar, text='Segundo nombre: ', font=(15), bg='light gray', fg='dodger blue').grid(row=19, column=4)
    nombre1a = Entry(v_editar, textvariable=StringVar(value=mna))
    nombre1a.grid(row=19, column=5)
    # Entrada de apellido1
    Label(v_editar, text='Primer apellido: ', font=(15), bg='light gray', fg='dodger blue').grid(row=19, column=6)
    apellidoa = Entry(v_editar, textvariable=StringVar(value=mapa))
    apellidoa.grid(row=19, column=7)
    # Entrada de apellido2
    Label(v_editar, text='Segundo apellido: ', font=(15), bg='light gray', fg='dodger blue').grid(row=19, column=8)
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
    Label(v_editar, text='Correo electronico: ', font=(15), bg='light gray', fg='dodger blue').grid(row=21, column=2)
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
    Button(v_editar, text='ACTUALIZAR',command=lambda: factualizar(v_editar,buscgrado,mn,mn1,ma,ma1,mdid,miden,mge,mfe,med,mrhh,mc,mdirec
                ,msa,mtsa,mco1,mt1,mna,mapa,mn1a,map1a,mparen,mocup,mc2,mdirec2,mco2,mt2,mdid2,miden2, nombre.get(), apellido.get()
                ,nombre1.get(), apellido1.get(), did.get(),identidad.get(), genero.get(), fecha.get(), edad.get(), rh.get(), ciudad.get(), direccion.get(),salud.get(),tsalud.get()
                ,correo1.get(),telefono1.get(),nombrea.get(),apellidoa.get(),nombre1a.get(),apellido1a.get(),parentesco.get(), ocupacion.get(), ciudad2.get(), direccion2.get(),correo2.get(),
                telefono2.get(),did2.get(), identidad2.get()), font=(15), bg='dodger blue', width="30",fg='white', height='2').place(x=500, y=600)

def factualizar(v_editar,buscgrado,mn,mn1,ma,ma1,mdid,miden,mge,mfe,med,mrhh,mc,mdirec,msa,mtsa,mco1,mt1,mna,mapa,mn1a,map1a,mparen,mocup,mc2,mdirec2,mco2,mt2,mdid2,miden2, nombre, apellido, nombre1, apellido1, did,identidad, genero, fecha, edad, rh, ciudad, direccion,salud,tsalud,correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a,parentesco, ocupacion,ciudad2,direccion2, correo2, telefono2,did2, identidad2):
    print('hola')
    ruloz = sqlite3.connect("matriculas.db")
    cursor = ruloz.cursor()
    if buscgrado == '1':
        cursor.execute("UPDATE ESTUDIANTES_1 SET nombre='%s', nombre2='%s',apellido='%s',apellido2='%s' , doc_id='%s',identidad='%s'"
               ",genero='%s',fecha_nacimiento='%s',edad='%s',rh='%s',ciudad='%s',direccion='%s' ,salud='%s',entidad='%s',correo='%s'"
               ",telefono='%s',acudiente='%s',nombre2a='%s',apellidoa='%s',apellido2a='%s' ,parentesco='%s',ocupacion='%s',ciudad2='%s',direccion2='%s',correo2='%s',telefono2='%s',doc_id2='%s',identidad2='%s'"
               "WHERE nombre='%s' AND nombre2='%s' AND apellido='%s' AND apellido2='%s' AND  doc_id='%s' AND identidad='%s'AND genero='%s' AND fecha_nacimiento='%s' "
               "AND edad='%s' AND rh='%s' AND ciudad='%s' AND direccion='%s' AND salud='%s' AND entidad='%s' AND correo='%s' AND telefono='%s' "
               "AND acudiente='%s' AND nombre2a='%s' AND apellidoa='%s' AND apellido2a='%s'AND parentesco='%s' AND ocupacion='%s' AND "
               "ciudad2='%s' AND direccion2='%s' AND correo2='%s' AND telefono2='%s' AND doc_id2='%s' AND identidad2='%s' " %(nombre, apellido, nombre1, apellido1, did ,identidad, genero, fecha, edad, rh, ciudad, direccion ,salud ,tsalud,correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a ,parentesco, ocupacion ,ciudad2 ,direccion2, correo2, telefono2 ,did2, identidad2 ,mn ,mn1 ,ma ,ma1 ,mdid ,miden ,mge ,mfe ,med ,mrhh ,mc ,mdirec ,msa ,mtsa ,mco1,mt1 ,mna ,mapa ,mn1a ,map1a ,mparen ,mocup ,mc2 ,mdirec2 ,mco2 ,mt2 ,mdid2,miden2))
        ruloz.commit()
        cursor.close()
    elif buscgrado == '2':
        cursor.execute("UPDATE ESTUDIANTES_2 SET nombre='%s', nombre2='%s',apellido='%s',apellido2='%s' , doc_id='%s',identidad='%s'" ",genero='%s',fecha_nacimiento='%s',edad='%s',rh='%s',ciudad='%s',direccion='%s' ,salud='%s',entidad='%s',correo='%s'"
            ",telefono='%s',acudiente='%s',nombre2a='%s',apellidoa='%s',apellido2a='%s' ,parentesco='%s',ocupacion='%s',ciudad2='%s',direccion2='%s',correo2='%s',telefono2='%s',doc_id2='%s',identidad2='%s'"
            "WHERE nombre='%s' AND nombre2='%s' AND apellido='%s' AND apellido2='%s' AND  doc_id='%s' AND identidad='%s'AND genero='%s' AND fecha_nacimiento='%s' "
            "AND edad='%s' AND rh='%s' AND ciudad='%s' AND direccion='%s' AND salud='%s' AND entidad='%s' AND correo='%s' AND telefono='%s' "
            "AND acudiente='%s' AND nombre2a='%s' AND apellidoa='%s' AND apellido2a='%s'AND parentesco='%s' AND ocupacion='%s' AND "
            "ciudad2='%s' AND direccion2='%s' AND correo2='%s' AND telefono2='%s' AND doc_id2='%s' AND identidad2='%s' " % (nombre, apellido, nombre1, apellido1, did, identidad, genero, fecha, edad, rh, ciudad, direccion, salud,tsalud, correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a, parentesco, ocupacion, ciudad2,direccion2, correo2, telefono2, did2, identidad2, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med, mrhh, mc,mdirec, msa, mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2, mco2, mt2, mdid2,miden2))
        ruloz.commit()
        cursor.close()
    elif buscgrado == '3':
        cursor.execute(
            "UPDATE ESTUDIANTES_3 SET nombre='%s', nombre2='%s',apellido='%s',apellido2='%s' , doc_id='%s',identidad='%s'" ",genero='%s',fecha_nacimiento='%s',edad='%s',rh='%s',ciudad='%s',direccion='%s' ,salud='%s',entidad='%s',correo='%s'"
            ",telefono='%s',acudiente='%s',nombre2a='%s',apellidoa='%s',apellido2a='%s' ,parentesco='%s',ocupacion='%s',ciudad2='%s',direccion2='%s',correo2='%s',telefono2='%s',doc_id2='%s',identidad2='%s'"
            "WHERE nombre='%s' AND nombre2='%s' AND apellido='%s' AND apellido2='%s' AND  doc_id='%s' AND identidad='%s'AND genero='%s' AND fecha_nacimiento='%s' "
            "AND edad='%s' AND rh='%s' AND ciudad='%s' AND direccion='%s' AND salud='%s' AND entidad='%s' AND correo='%s' AND telefono='%s' "
            "AND acudiente='%s' AND nombre2a='%s' AND apellidoa='%s' AND apellido2a='%s'AND parentesco='%s' AND ocupacion='%s' AND "
            "ciudad2='%s' AND direccion2='%s' AND correo2='%s' AND telefono2='%s' AND doc_id2='%s' AND identidad2='%s' " % (
            nombre, apellido, nombre1, apellido1, did, identidad, genero, fecha, edad, rh, ciudad, direccion, salud,
            tsalud, correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a, parentesco, ocupacion, ciudad2,
            direccion2, correo2, telefono2, did2, identidad2, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med, mrhh, mc,
            mdirec, msa, mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2, mco2, mt2, mdid2,
            miden2))
        ruloz.commit()
        cursor.close()
    elif buscgrado == '4':
        cursor.execute(
            "UPDATE ESTUDIANTES_4 SET nombre='%s', nombre2='%s',apellido='%s',apellido2='%s' , doc_id='%s',identidad='%s'" ",genero='%s',fecha_nacimiento='%s',edad='%s',rh='%s',ciudad='%s',direccion='%s' ,salud='%s',entidad='%s',correo='%s'"
            ",telefono='%s',acudiente='%s',nombre2a='%s',apellidoa='%s',apellido2a='%s' ,parentesco='%s',ocupacion='%s',ciudad2='%s',direccion2='%s',correo2='%s',telefono2='%s',doc_id2='%s',identidad2='%s'"
            "WHERE nombre='%s' AND nombre2='%s' AND apellido='%s' AND apellido2='%s' AND  doc_id='%s' AND identidad='%s'AND genero='%s' AND fecha_nacimiento='%s' "
            "AND edad='%s' AND rh='%s' AND ciudad='%s' AND direccion='%s' AND salud='%s' AND entidad='%s' AND correo='%s' AND telefono='%s' "
            "AND acudiente='%s' AND nombre2a='%s' AND apellidoa='%s' AND apellido2a='%s'AND parentesco='%s' AND ocupacion='%s' AND "
            "ciudad2='%s' AND direccion2='%s' AND correo2='%s' AND telefono2='%s' AND doc_id2='%s' AND identidad2='%s' " % (
            nombre, apellido, nombre1, apellido1, did, identidad, genero, fecha, edad, rh, ciudad, direccion, salud,
            tsalud, correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a, parentesco, ocupacion, ciudad2,
            direccion2, correo2, telefono2, did2, identidad2, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med, mrhh, mc,
            mdirec, msa, mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2, mco2, mt2, mdid2,
            miden2))
        ruloz.commit()
        cursor.close()
    elif buscgrado == '5':
        cursor.execute(
            "UPDATE ESTUDIANTES_5 SET nombre='%s', nombre2='%s',apellido='%s',apellido2='%s' , doc_id='%s',identidad='%s'" ",genero='%s',fecha_nacimiento='%s',edad='%s',rh='%s',ciudad='%s',direccion='%s' ,salud='%s',entidad='%s',correo='%s'"
            ",telefono='%s',acudiente='%s',nombre2a='%s',apellidoa='%s',apellido2a='%s' ,parentesco='%s',ocupacion='%s',ciudad2='%s',direccion2='%s',correo2='%s',telefono2='%s',doc_id2='%s',identidad2='%s'"
            "WHERE nombre='%s' AND nombre2='%s' AND apellido='%s' AND apellido2='%s' AND  doc_id='%s' AND identidad='%s'AND genero='%s' AND fecha_nacimiento='%s' "
            "AND edad='%s' AND rh='%s' AND ciudad='%s' AND direccion='%s' AND salud='%s' AND entidad='%s' AND correo='%s' AND telefono='%s' "
            "AND acudiente='%s' AND nombre2a='%s' AND apellidoa='%s' AND apellido2a='%s'AND parentesco='%s' AND ocupacion='%s' AND "
            "ciudad2='%s' AND direccion2='%s' AND correo2='%s' AND telefono2='%s' AND doc_id2='%s' AND identidad2='%s' " % (
            nombre, apellido, nombre1, apellido1, did, identidad, genero, fecha, edad, rh, ciudad, direccion, salud,
            tsalud, correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a, parentesco, ocupacion, ciudad2,
            direccion2, correo2, telefono2, did2, identidad2, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med, mrhh, mc,
            mdirec, msa, mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2, mco2, mt2, mdid2,
            miden2))
        ruloz.commit()
        cursor.close()
    elif buscgrado == '6':
        cursor.execute(
            "UPDATE ESTUDIANTES_6 SET nombre='%s', nombre2='%s',apellido='%s',apellido2='%s' , doc_id='%s',identidad='%s'" ",genero='%s',fecha_nacimiento='%s',edad='%s',rh='%s',ciudad='%s',direccion='%s' ,salud='%s',entidad='%s',correo='%s'"
            ",telefono='%s',acudiente='%s',nombre2a='%s',apellidoa='%s',apellido2a='%s' ,parentesco='%s',ocupacion='%s',ciudad2='%s',direccion2='%s',correo2='%s',telefono2='%s',doc_id2='%s',identidad2='%s'"
            "WHERE nombre='%s' AND nombre2='%s' AND apellido='%s' AND apellido2='%s' AND  doc_id='%s' AND identidad='%s'AND genero='%s' AND fecha_nacimiento='%s' "
            "AND edad='%s' AND rh='%s' AND ciudad='%s' AND direccion='%s' AND salud='%s' AND entidad='%s' AND correo='%s' AND telefono='%s' "
            "AND acudiente='%s' AND nombre2a='%s' AND apellidoa='%s' AND apellido2a='%s'AND parentesco='%s' AND ocupacion='%s' AND "
            "ciudad2='%s' AND direccion2='%s' AND correo2='%s' AND telefono2='%s' AND doc_id2='%s' AND identidad2='%s' " % (
            nombre, apellido, nombre1, apellido1, did, identidad, genero, fecha, edad, rh, ciudad, direccion, salud,
            tsalud, correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a, parentesco, ocupacion, ciudad2,
            direccion2, correo2, telefono2, did2, identidad2, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med, mrhh, mc,
            mdirec, msa, mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2, mco2, mt2, mdid2,
            miden2))
        ruloz.commit()
        cursor.close()
    elif buscgrado == '7':
        cursor.execute(
            "UPDATE ESTUDIANTES_7 SET nombre='%s', nombre2='%s',apellido='%s',apellido2='%s' , doc_id='%s',identidad='%s'" ",genero='%s',fecha_nacimiento='%s',edad='%s',rh='%s',ciudad='%s',direccion='%s' ,salud='%s',entidad='%s',correo='%s'"
            ",telefono='%s',acudiente='%s',nombre2a='%s',apellidoa='%s',apellido2a='%s' ,parentesco='%s',ocupacion='%s',ciudad2='%s',direccion2='%s',correo2='%s',telefono2='%s',doc_id2='%s',identidad2='%s'"
            "WHERE nombre='%s' AND nombre2='%s' AND apellido='%s' AND apellido2='%s' AND  doc_id='%s' AND identidad='%s'AND genero='%s' AND fecha_nacimiento='%s' "
            "AND edad='%s' AND rh='%s' AND ciudad='%s' AND direccion='%s' AND salud='%s' AND entidad='%s' AND correo='%s' AND telefono='%s' "
            "AND acudiente='%s' AND nombre2a='%s' AND apellidoa='%s' AND apellido2a='%s'AND parentesco='%s' AND ocupacion='%s' AND "
            "ciudad2='%s' AND direccion2='%s' AND correo2='%s' AND telefono2='%s' AND doc_id2='%s' AND identidad2='%s' " % (
            nombre, apellido, nombre1, apellido1, did, identidad, genero, fecha, edad, rh, ciudad, direccion, salud,
            tsalud, correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a, parentesco, ocupacion, ciudad2,
            direccion2, correo2, telefono2, did2, identidad2, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med, mrhh, mc,
            mdirec, msa, mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2, mco2, mt2, mdid2,
            miden2))
        ruloz.commit()
        cursor.close()
    elif buscgrado == '8':
        cursor.execute(
            "UPDATE ESTUDIANTES_8 SET nombre='%s', nombre2='%s',apellido='%s',apellido2='%s' , doc_id='%s',identidad='%s'" ",genero='%s',fecha_nacimiento='%s',edad='%s',rh='%s',ciudad='%s',direccion='%s' ,salud='%s',entidad='%s',correo='%s'"
            ",telefono='%s',acudiente='%s',nombre2a='%s',apellidoa='%s',apellido2a='%s' ,parentesco='%s',ocupacion='%s',ciudad2='%s',direccion2='%s',correo2='%s',telefono2='%s',doc_id2='%s',identidad2='%s'"
            "WHERE nombre='%s' AND nombre2='%s' AND apellido='%s' AND apellido2='%s' AND  doc_id='%s' AND identidad='%s'AND genero='%s' AND fecha_nacimiento='%s' "
            "AND edad='%s' AND rh='%s' AND ciudad='%s' AND direccion='%s' AND salud='%s' AND entidad='%s' AND correo='%s' AND telefono='%s' "
            "AND acudiente='%s' AND nombre2a='%s' AND apellidoa='%s' AND apellido2a='%s'AND parentesco='%s' AND ocupacion='%s' AND "
            "ciudad2='%s' AND direccion2='%s' AND correo2='%s' AND telefono2='%s' AND doc_id2='%s' AND identidad2='%s' " % (
            nombre, apellido, nombre1, apellido1, did, identidad, genero, fecha, edad, rh, ciudad, direccion, salud,
            tsalud, correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a, parentesco, ocupacion, ciudad2,
            direccion2, correo2, telefono2, did2, identidad2, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med, mrhh, mc,
            mdirec, msa, mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2, mco2, mt2, mdid2,
            miden2))
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
            nombre, apellido, nombre1, apellido1, did, identidad, genero, fecha, edad, rh, ciudad, direccion, salud,
            tsalud, correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a, parentesco, ocupacion, ciudad2,
            direccion2, correo2, telefono2, did2, identidad2, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med, mrhh, mc,
            mdirec, msa, mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2, mco2, mt2, mdid2,
            miden2))
        ruloz.commit()
        cursor.close()
    elif buscgrado == '10':
        cursor.execute(
            "UPDATE ESTUDIANTES_10 SET nombre='%s', nombre2='%s',apellido='%s',apellido2='%s' , doc_id='%s',identidad='%s'" ",genero='%s',fecha_nacimiento='%s',edad='%s',rh='%s',ciudad='%s',direccion='%s' ,salud='%s',entidad='%s',correo='%s'"
            ",telefono='%s',acudiente='%s',nombre2a='%s',apellidoa='%s',apellido2a='%s' ,parentesco='%s',ocupacion='%s',ciudad2='%s',direccion2='%s',correo2='%s',telefono2='%s',doc_id2='%s',identidad2='%s'"
            "WHERE nombre='%s' AND nombre2='%s' AND apellido='%s' AND apellido2='%s' AND  doc_id='%s' AND identidad='%s'AND genero='%s' AND fecha_nacimiento='%s' "
            "AND edad='%s' AND rh='%s' AND ciudad='%s' AND direccion='%s' AND salud='%s' AND entidad='%s' AND correo='%s' AND telefono='%s' "
            "AND acudiente='%s' AND nombre2a='%s' AND apellidoa='%s' AND apellido2a='%s'AND parentesco='%s' AND ocupacion='%s' AND "
            "ciudad2='%s' AND direccion2='%s' AND correo2='%s' AND telefono2='%s' AND doc_id2='%s' AND identidad2='%s' " % (
            nombre, apellido, nombre1, apellido1, did, identidad, genero, fecha, edad, rh, ciudad, direccion, salud,
            tsalud, correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a, parentesco, ocupacion, ciudad2,
            direccion2, correo2, telefono2, did2, identidad2, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med, mrhh, mc,
            mdirec, msa, mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2, mco2, mt2, mdid2,
            miden2))
        ruloz.commit()
        cursor.close()
    elif buscgrado == '11':
        cursor.execute(
            "UPDATE ESTUDIANTES_11 SET nombre='%s', nombre2='%s',apellido='%s',apellido2='%s' , doc_id='%s',identidad='%s'" ",genero='%s',fecha_nacimiento='%s',edad='%s',rh='%s',ciudad='%s',direccion='%s' ,salud='%s',entidad='%s',correo='%s'"
            ",telefono='%s',acudiente='%s',nombre2a='%s',apellidoa='%s',apellido2a='%s' ,parentesco='%s',ocupacion='%s',ciudad2='%s',direccion2='%s',correo2='%s',telefono2='%s',doc_id2='%s',identidad2='%s'"
            "WHERE nombre='%s' AND nombre2='%s' AND apellido='%s' AND apellido2='%s' AND  doc_id='%s' AND identidad='%s'AND genero='%s' AND fecha_nacimiento='%s' "
            "AND edad='%s' AND rh='%s' AND ciudad='%s' AND direccion='%s' AND salud='%s' AND entidad='%s' AND correo='%s' AND telefono='%s' "
            "AND acudiente='%s' AND nombre2a='%s' AND apellidoa='%s' AND apellido2a='%s'AND parentesco='%s' AND ocupacion='%s' AND "
            "ciudad2='%s' AND direccion2='%s' AND correo2='%s' AND telefono2='%s' AND doc_id2='%s' AND identidad2='%s' " % (
            nombre, apellido, nombre1, apellido1, did, identidad, genero, fecha, edad, rh, ciudad, direccion, salud,
            tsalud, correo1, telefono1, nombrea, apellidoa, nombre1a, apellido1a, parentesco, ocupacion, ciudad2,
            direccion2, correo2, telefono2, did2, identidad2, mn, mn1, ma, ma1, mdid, miden, mge, mfe, med, mrhh, mc,
            mdirec, msa, mtsa, mco1, mt1, mna, mapa, mn1a, map1a, mparen, mocup, mc2, mdirec2, mco2, mt2, mdid2,
            miden2))
        ruloz.commit()
        cursor.close()

    messagebox.showinfo(' GOOD ', message='SE ACTUALIZARON LOS DATOS CON EXITO')
    v_editar.destroy()

def fsalir():
     vent_salir=Tk()
     vent_salir.geometry("400x200+0+0")
     vent_salir.title("Salir")
     vent_salir= LabelFrame(vent_salir, text='SALIR')
     vent_salir.grid(row= 0, column=0, columnspan=10, pady=10)
     sip=Button(vent_salir, text='SI',command=fsalida,font=(10),bg='#56cd63',width="20",fg='white',height='1')
     sip.grid(row=0,column=2, sticky = W+E)
     nop=Button(vent_salir, text='NO',command=fmenu,font=(10),bg='#56cd63',width="20",fg='white',height='1')
     nop.grid(row=0,column=4, sticky = W+E)

     vent_salir.mainloop()
def fsalida():
     pass
fmenu()
