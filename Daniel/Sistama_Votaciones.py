from tkinter import*
import sqlite3
from tkinter import messagebox

#----------------------------------USUARIOS----------------------------------
def votose(Usuario,candidato):
    conexion=sqlite3.connect("BDD_PROYECTO.db")
    micursor=conexion.cursor()
    
    if candidato=="c1":
        micursor.execute("UPDATE CANDIDATOSE SET VOTO=VOTO+1 WHERE CANDIDATO=?",(candidato,))
        micursor.execute("UPDATE USUARIOS SET VOTOE=VOTOE+1 WHERE USUARIO=?",(Usuario,))
        messagebox.showwarning("SISTEMA VOTACIONES", "VOTO FUE REGISTRADO PARA EL CANDIDATO 1")
    elif candidato=="c2":
        micursor.execute("UPDATE CANDIDATOSE SET VOTO=VOTO+1 WHERE CANDIDATO=?",(candidato,))
        micursor.execute("UPDATE USUARIOS SET VOTOE=VOTOE+1 WHERE USUARIO=?",(Usuario,))
        messagebox.showwarning("SISTEMA VOTACIONES", "VOTO FUE REGISTRADO PARA EL CANDIDATO 2")
    elif candidato=="c3":
        micursor.execute("UPDATE CANDIDATOSE SET VOTO=VOTO+1 WHERE CANDIDATO=?",(candidato,))
        micursor.execute("UPDATE USUARIOS SET VOTOE=VOTOE+1 WHERE USUARIO=?",(Usuario,))
        messagebox.showwarning("SISTEMA VOTACIONES", "VOTO FUE REGISTRADO PARA EL CANDIDATO 3")
    elif candidato=="voto en blanco":
        micursor.execute("UPDATE CANDIDATOSE SET VOTO=VOTO+1 WHERE CANDIDATO=?",(candidato,))
        micursor.execute("UPDATE USUARIOS SET VOTOE=VOTOE+1 WHERE USUARIO=?",(Usuario,))
        messagebox.showwarning("SISTEMA VOTACIONES", "VOTO FUE REGISTRADO PARA VOTO EN BLANCO")
    
    conexion.commit()
    micursor.close()
    conexion.close()
    
def votosp(Usuario,candidato):
    conexion=sqlite3.connect("BDD_PROYECTO.db")
    micursor=conexion.cursor()
    
    if candidato=="c1":
        micursor.execute("UPDATE CANDIDATOSP SET VOTO=VOTO+1 WHERE CANDIDATO=?",(candidato,))
        micursor.execute("UPDATE USUARIOS SET VOTOP=VOTOP+1 WHERE USUARIO=?",(Usuario,))
        messagebox.showwarning("SISTEMA VOTACIONES", "VOTO FUE REGISTRADO PARA EL CANDIDATO 1")
    elif candidato=="c2":
        micursor.execute("UPDATE CANDIDATOSP SET VOTO=VOTO+1 WHERE CANDIDATO=?",(candidato,))
        micursor.execute("UPDATE USUARIOS SET VOTOP=VOTOP+1 WHERE USUARIO=?",(Usuario,))
        messagebox.showwarning("SISTEMA VOTACIONES", "VOTO FUE REGISTRADO PARA EL CANDIDATO 2")
    elif candidato=="c3":
        micursor.execute("UPDATE CANDIDATOSP SET VOTO=VOTO+1 WHERE CANDIDATO=?",(candidato,))
        micursor.execute("UPDATE USUARIOS SET VOTOP=VOTOP+1 WHERE USUARIO=?",(Usuario,))
        messagebox.showwarning("SISTEMA VOTACIONES", "VOTO FUE REGISTRADO PARA EL CANDIDATO 3")
    elif candidato=="voto en blanco":
        micursor.execute("UPDATE CANDIDATOSP SET VOTO=VOTO+1 WHERE CANDIDATO=?",(candidato,))
        micursor.execute("UPDATE USUARIOS SET VOTOP=VOTOP+1 WHERE USUARIO=?",(Usuario,))
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

    micursor.execute("SELECT * FROM CODIGO WHERE USUARIO=? AND CONTRASEÑA=?",(Usuario,Contraseña))
    if micursor.fetchall():
        if tipov=="Estudiantes":
            votoe=0
            micursor.execute("SELECT VOTOE FROM USUARIOS WHERE USUARIO=? AND CONTRASEÑA=? AND VOTOE=?",(Usuario,Contraseña,votoe))
            if micursor.fetchall():
                votacionesE(Usuario)
            else:messagebox.showwarning("ERROR", "EL USUARIO YA TIENE VOTO REGISTRADO EN ESTUDIANTES")
        elif tipov=="Profesores":
            votop=0
            micursor.execute("SELECT VOTOP FROM USUARIOS WHERE USUARIO=? AND CONTRASEÑA=? AND VOTOP=?",(Usuario,Contraseña,votop))
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
    imagen1=PhotoImage(file="Logo_Uis.png")
    imagen2=PhotoImage(file="Fondo_nuevo.png")
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
            
            conexion=sqlite3.connect("BDD_PROYECTO.db")
            micursor=conexion.cursor()

            micursor.execute("SELECT * FROM ADMINISTRADORES WHERE ADMINISTRADOR=? AND CONTRASEÑA=?",(Usuario,Contraseña))

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

            agregarcanEs=Button(v2, text=" Agregar Candidato Estudiantes", font=("Times New Roman",14))
            agregarcanEs.grid(row=3, column=0, pady=10,padx=10)
            agregarcanEs.config(width=28)

            HabilitarPr=Button(v2, text="Habilitar Votaciones Profesores", font=("Times New Roman",14),command=lambda:habilitarP())
            HabilitarPr.grid(row=1, column=1, pady=10,padx=10)
            HabilitarPr.config(width=28)

            DesabilitarPr=Button(v2, text="Deshabilitar Votaciones Profesores", font=("Times New Roman",14),command=lambda:deshabilitarP())
            DesabilitarPr.grid(row=2, column=1, pady=10,padx=10)
            DesabilitarPr.config(width=28)

            agregarcanPr=Button(v2, text=" Agregar Candidato Profesores", font=("Times New Roman",14))
            agregarcanPr.grid(row=3, column=1, pady=10,padx=10)
            agregarcanPr.config(width=28)

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

ventanaprim()
    
    
