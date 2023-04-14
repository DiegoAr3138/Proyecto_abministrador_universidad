from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import sqlite3
import time


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

if __name__ == '__main__':
     Biblioteca()