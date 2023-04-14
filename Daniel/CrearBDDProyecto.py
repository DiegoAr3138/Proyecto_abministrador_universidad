import sqlite3

conexion=sqlite3.connect("BDD_PROYECTO.db")
micursor=conexion.cursor()
#--------------------TABLA DE ADMINISTRADORES---------------
micursor.execute("CREATE TABLE ADMINISTRADORES(ADMINISTRADOR UNIQUE PRIMARY KEY,CONTRASEÑA VARCHAR)")

agregaradmin=[("Daniel","1234")]
micursor.executemany("INSERT INTO ADMINISTRADORES VALUES (?,?)",agregaradmin)
#--------------------TABLA DE USUARIOS----------------------
micursor.execute("CREATE TABLE USUARIOS(USUARIO VARCHAR UNIQUE PRIMARY KEY,CONTRASEÑA VANCHAR, VOTOP INTERGER, VOTOE INTEGER)")

agregarusu=[("Camilo","1234",0,0),("Felipe","0000",0,0),("Pepe","0000",0,0)]

micursor.executemany("INSERT INTO USUARIOS VALUES (?,?,?,?)",agregarusu)

#---------------------REGISTRO DE VOTOS----------------------
micursor.execute("CREATE TABLE CANDIDATOSP(CANDIDATO VANCHAR UNIQUE PRIMARY KEY, VOTO INTEGER)")
agregarcandp=[("c1",0),("c2",0),("c3",0),("voto en blanco",0)]
micursor.executemany("INSERT INTO CANDIDATOSP VALUES (?,?)",agregarcandp)

micursor.execute("CREATE TABLE CANDIDATOSE(CANDIDATO VANCHAR UNIQUE PRIMARY KEY, VOTO INTEGER)")
agregarcande=[("c1",0),("c2",0),("c3",0),("voto en blanco",0)]
micursor.executemany("INSERT INTO CANDIDATOSE VALUES (?,?)",agregarcande)

conexion.commit()
micursor.close()
conexion.close()
print("BASE DE DATOS CREADA CON EXITO")

