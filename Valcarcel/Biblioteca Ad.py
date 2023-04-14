from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import sqlite3
import time


class BibliotecaA:

    def __init__(self):

        self.ven = Tk()
        self.ven.title('Biblioteca')
        self.ven.geometry('1000x668')
        self.ven.resizable(0, 0)
        self.Mensaje = Label()

        q = PhotoImage(file="Imagen3.gif")
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

if __name__ == '__main__':
    BibliotecaA()



