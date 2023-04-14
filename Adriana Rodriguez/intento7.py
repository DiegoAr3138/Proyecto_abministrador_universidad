import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def consulta_notas():
        conn = sqlite3.connect('Base_total') 
        c = conn.cursor() 
        
        c.execute("SELECT nombre_asignatura,saber,saber_hacer,ser FROM NOTAS INNER JOIN ESTUDIANTE ON  ESTUDIANTE.numero_documento = NOTAS.documento_estudiante WHERE numero_documento = '{}'".format(username_verify.get()))
        table = c.fetchall()

        conn.close()
        return table,username_verify.get()

def login():
    """
    Funcion para verificar si el correo y contraseña suministrados están
    efectivamente en la base de datos
    """
    global username_verify,password_verify
    correo,clave = username_verify.get(),password_verify.get() 
    conn = sqlite3.connect('Base_total') 
    c = conn.cursor() 
    sql1 = "SELECT  CODIGO FROM ESTUDIANTES WHERE CODIGO = '{}'".format(correo) 
    sql2 = "SELECT CONTRASEÑA FROM ESTUDIANTES WHERE CONTRASEÑA = '{}'".format(clave)  

    c.execute(sql1)
    correo_bd = c.fetchone()
    c.execute(sql2)
    clave_bd = c.fetchone()
    conn.close()

    if correo_bd==None or clave_bd==None:
        login_fail() 
    else:
        login_sucess()

def salir():
    login_success_screen.destroy()


def login_sucess():
    global main_screen,login_success_screen,user_get
    login_success_screen = Toplevel(main_screen) 
    login_success_screen.title("Success")
    login_success_screen.resizable(0, 0)
    table,user_get = consulta_notas() 
    print(table)

    conn = sqlite3.connect('Base_total') 
    c = conn.cursor() 
    sql1 = "SELECT primer_nombre FROM ESTUDIANTES WHERE numero_documento = '{}'".format(user_get) 
    c.execute(sql1)
    nombre_bd = c.fetchone()
    conn.close()

    Label(login_success_screen, text='Bienvenido '+ nombre_bd[0]).grid(row=0, column=0, padx=5, pady=5, columnspan=5)


    Tabla = ttk.Treeview(login_success_screen, columns=(1, 2, 3, 4), show='headings', height='5')
    Tabla.grid(row=1, column=0, padx=5, pady=5, columnspan=5)

    Tabla.heading(1, text='Materia')
    Tabla.heading(2, text='Saber')
    Tabla.heading(3, text='Saber Hacer ')
    Tabla.heading(4, text='Ser')

    rueda = Scrollbar(login_success_screen, command=Tabla.yview)
    rueda.grid(row=1, column=7, sticky='nsew')
    Tabla.config(yscrollcommand=rueda.set)

    Dat = Tabla.get_children()
    for i in Dat:
        Tabla.delete(i)


    for i in table:
        Tabla.insert('', 'end', values=i)

    Button(login_success_screen, text='Datos', command = editar) \
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
    c.execute("SELECT * FROM ESTUDIANTES WHERE numero_documento = '{}'".format(user))
    table = c.fetchall()
    conn.close()

    return table

def actualizar_bd():
    global primer_nombre_entry,segundo_nombre,primer_apellido,segundo_apellido,tipo_documento,numero_documento,nombre_padre,nombre_madre,telefono,eps,puntaje_sisben,correo,direccion,clave,edit_screen
    ans = get_values(user_get)

    if len(primer_nombre_entry.get())==0:
        primer_nombre1 = ans[0][0]
    else:
        primer_nombre1 = primer_nombre_entry.get()
    
    if len(segundo_nombre_entry.get())==0:
        segundo_nombre1 = ans[0][1]
    else:
        segundo_nombre1 = segundo_nombre_entry.get()
    if len(primer_apellido_entry.get())==0:
        primer_apellido1 = ans[0][2]
    else:
        primer_apellido1 = primer_apellido_entry.get()

    if len(segundo_apellido_entry.get())==0:
        segundo_apellido1 = ans[0][3]
    else:
        segundo_apellido1 = segundo_apellido_entry.get()

    if len(tipo_documento_entry.get())==0:
        tipo_documento1 = ans[0][4]
    else:
        tipo_documento1   = tipo_documento_entry.get()
    if len(numero_documento_entry.get())==0:
        numero_documento1 = int(ans[0][5])
    else:
        numero_documento1  = int(numero_documento_entry.get())
    if len(nombre_padre_entry.get())==0:
        nombre_padre1 = ans[0][6]
    else:
        nombre_padre1  = nombre_padre_entry.get()
    if len(nombre_madre_entry.get())==0:
        nombre_madre1 = ans[0][7]
    else:
        nombre_madre1 =  nombre_madre_entry.get()
    if len(telefono_entry.get())==0:
        telefono1 = int(ans[0][8])
    else:
        telefono1 =  int(telefono_entry.get())

    if len(eps_entry.get())==0:
        eps1 = ans[0][9]
    else:
        eps1 =  eps_entry.get()

    if len(puntaje_sisben_entry.get())==0:
        puntaje_sisben1 = float(ans[0][10])
    else:
        puntaje_sisben1 =  float(puntaje_sisben_entry.get())
    if len(correo_entry.get())==0:
        correo1 = ans[0][11]
    else:
        correo1 =  correo_entry.get()
    if len(direccion_entry.get())==0:
        direccion1 = ans[0][12]
    else:
        direccion1 =  direccion_entry.get()
    
    if len(clave_entry.get())==0:
        clave1 = ans[0][13]
    else:
        clave1 = clave_entry.get()
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    sql = "UPDATE ESTUDIANTE SET primer_nombre = '{}',segundo_nombre = '{}',primer_apellido = '{}',segundo_apellido = '{}',tipo_documento = '{}',numero_documento = {},nombre_padre = '{}',nombre_madre = '{}',telefono = {},eps = '{}',puntaje_sisben = {},correo = '{}',direccion = '{}',clave = '{}' WHERE numero_documento = {} ".format(
        primer_nombre1,segundo_nombre1,primer_apellido1,segundo_apellido1,tipo_documento1,
        numero_documento1,nombre_padre1,nombre_madre1,telefono1,eps1,puntaje_sisben1,correo1,direccion1,clave1,user_get)
    c.execute(sql)
    conn.commit()
    conn.close()
    edit_screen.destroy()







def main():
    global username_verify,password_verify,main_screen,username_login_entry,password__login_entry
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
    password__login_entry = Entry(main_screen, textvariable=password_verify, show= '*')
    password__login_entry.pack()
    Label(main_screen, text="").pack()
    Button(main_screen, text="Login", width=10, height=1, command=login).pack() 

    Label(main_screen, text="").pack()
    Button(main_screen, text="Salir", width=10, height=1, command=exit).pack()
    main_screen.mainloop()


main()
