import mysql.connector
import tkinter as tk
from PIL import Image,ImageTk,ImageFilter
from tkinter import messagebox
from boleto import *
import time

# Conectar la base de datos y obtener el cursor
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="CinesUnidos"
)
mycursor = mydb.cursor()

class Application:
    def __init__(self):

        #Información básica para la ventana.
        self.window=tk.Tk()
        self.window.title("Boletos Cine")
        self.window.geometry("1000x700")
        self.window.resizable(False,False) #Así no se podrá colocar pantalla completa.
        

        # Reloj.
        self.reloj_label = tk.Label(self.window, text="", font=("Arial", 40), pady=5, padx=5,bg="white")
        self.reloj_label.place(x=770, y=5)
        # Para que constantemente se actualice.
        self.actualizar_reloj()

        #Fondo del sistema.
        self.bg=Image.open("CUV.jpg")
        width = 1000 #Ancho
        height = 700 #Alto
        self.bg=self.bg.filter(ImageFilter.GaussianBlur(radius=4))
        self.bg = self.bg.resize((width, height),resample=Image.LANCZOS)
        self.bg_tk=ImageTk.PhotoImage(self.bg)
        self.Label_bg=tk.Label(self.window,image=self.bg_tk)
        self.Label_bg.place(x=0,y=0,relwidth=1,relheight=1) #Posicionar Imagen
        self.Label_bg.lower()

        #Fondo Estático.
        self.img=Image.new("RGB",(300,700),(230,230,230)) #(Tipo de color,(Ancho,Alto),(R,G,B))
        self.img_tk=ImageTk.PhotoImage(self.img)
        self.Label_img=tk.Label(self.window,image=self.img_tk)
        self.Label_img.place(x=50,y=0)
        self.Label_img.lift()

        #Logo Empresa
        self.im001=Image.open("Logo.png") #Búsqueda de imagen.
        width = 300 #Ancho
        height = 115 #Ancho
        self.im001 = self.im001.resize((width, height),resample=Image.LANCZOS)
        self.im001_tk=ImageTk.PhotoImage(self.im001)
        self.Label_im001=tk.Label(self.window,image=self.im001_tk)
        self.Label_im001.place(x=50,y=5) #Centrar Imagen
        self.Label_im001.lift()

        #Tasa BCV
        self.im002=Image.open("BCV.jpg") #Búsqueda de imagen.
        width = 350 #Ancho
        height = 350 #Ancho
        self.im002 = self.im002.resize((width, height),resample=Image.LANCZOS)
        self.im002_tk=ImageTk.PhotoImage(self.im002)
        self.Label_im002=tk.Label(self.window,image=self.im002_tk)
        self.Label_im002.place(x=500,y=140) #Centrar Imagen
        self.Label_im002.lift()

        #Formulario
        self.labelNroFactura=tk.Label(self.window,text="Número de Factura:",font=("Helvetica",12,"bold"),fg="black")
        self.labelNroFactura.place(x=50,y=150)
        self.entryNroFactura = tk.Entry(self.window,font=("Helvetica",13))
        self.entryNroFactura.place(x=209,y=150,width=144)

        self.labelNombrePelicula=tk.Label(self.window,text="Película:",font=("Helvetica",12,"bold"),fg="black")
        self.labelNombrePelicula.place(x=50,y=175)
        self.entryNombrePelicula = tk.Entry(self.window,font=("Helvetica",13))
        self.entryNombrePelicula.place(x=120,y=175,width=232)

        self.labelCICliente=tk.Label(self.window,text="Cédula del Cliente:",font=("Helvetica",12,"bold"),fg="black")
        self.labelCICliente.place(x=50,y=200)
        self.entryCICliente = tk.Entry(self.window,font=("Helvetica",13))
        self.entryCICliente.place(x=204,y=200,width=148)

        self.labelNombreCliente=tk.Label(self.window,text="Nombre del Cliente:",font=("Helvetica",12,"bold"),fg="black")
        self.labelNombreCliente.place(x=50,y=225)
        self.entryNombreCliente = tk.Entry(self.window,font=("Helvetica",13))
        self.entryNombreCliente.place(x=208,y=225,width=146)

        self.labelApellidoCliente=tk.Label(self.window,text="Apellido del Cliente:",font=("Helvetica",12,"bold"),fg="black")
        self.labelApellidoCliente.place(x=50,y=250)
        self.entryApellidoCliente = tk.Entry(self.window,font=("Helvetica",13))
        self.entryApellidoCliente.place(x=208,y=250,width=146)

        self.labelSexoC=tk.Label(self.window,text="Sexo:",font=("Helvetica",12,"bold"),fg="black")
        self.labelSexoC.place(x=50,y=275)
        self.entrySexoC = tk.Entry(self.window,font=("Helvetica",13))
        self.entrySexoC.place(x=101,y=275,width=30)

        self.labelEdad=tk.Label(self.window,text="Edad:",font=("Helvetica",12,"bold"),fg="black")
        self.labelEdad.place(x=50,y=300)
        self.entryEdad = tk.Entry(self.window,font=("Helvetica",13))
        self.entryEdad.place(x=104,y=300,width=30)

        self.labelTipoEstudiante=tk.Label(self.window,text="Tipo Estudiante:",font=("Helvetica",12,"bold"),fg="black")
        self.labelTipoEstudiante.place(x=50,y=325)
        self.entryTipoEstudiante = tk.Entry(self.window,font=("Helvetica",13))
        self.entryTipoEstudiante.place(x=185,y=325,width=30)

        self.labelDiaSemana=tk.Label(self.window,text="Día de la semana:",font=("Helvetica",12,"bold"),fg="black")
        self.labelDiaSemana.place(x=50,y=350)
        self.entryDiaSemana = tk.Entry(self.window,font=("Helvetica",13))
        self.entryDiaSemana.place(x=190,y=350,width=40)

        self.labelFechaDia=tk.Label(self.window,text="Fecha (Día):",font=("Helvetica",12,"bold"),fg="black")
        self.labelFechaDia.place(x=50,y=375)
        self.entryFechaDia = tk.Entry(self.window,font=("Helvetica",13))
        self.entryFechaDia.place(x=150,y=375,width=30)

        self.labelFechaMes=tk.Label(self.window,text="Fecha (Mes):",font=("Helvetica",12,"bold"),fg="black")
        self.labelFechaMes.place(x=50,y=400)
        self.entryFechaMes = tk.Entry(self.window,font=("Helvetica",13))
        self.entryFechaMes.place(x=155,y=400,width=30)

        self.labelFechaAño=tk.Label(self.window,text="Fecha (Año):",font=("Helvetica",12,"bold"),fg="black")
        self.labelFechaAño.place(x=50,y=425)
        self.entryFechaAño = tk.Entry(self.window,font=("Helvetica",13))
        self.entryFechaAño.place(x=155,y=425,width=60)

        self.labelCantidadBoletos=tk.Label(self.window,text="Cantidad de Boletos:",font=("Helvetica",12,"bold"),fg="black")
        self.labelCantidadBoletos.place(x=50,y=450)
        self.entryCantidadBoletos = tk.Entry(self.window,font=("Helvetica",13))
        self.entryCantidadBoletos.place(x=220,y=450,width=60)

        self.labelPrecioBoleto=tk.Label(self.window,text="Precio de Boleto:",font=("Helvetica",12,"bold"),fg="black")
        self.labelPrecioBoleto.place(x=50,y=475)
        self.entryPrecioBoleto = tk.Entry(self.window,font=("Helvetica",13))
        self.entryPrecioBoleto.place(x=188,y=475,width=30)

        self.labelCambioBS=tk.Label(self.window,text="Cambio BS:",font=("Helvetica",12,"bold"),fg="black")
        self.labelCambioBS.place(x=50,y=500)
        self.entryCambioBS = tk.Entry(self.window,font=("Helvetica",13))
        self.entryCambioBS.place(x=150,y=500,width=100)

        self.labelTotalPagar=tk.Label(self.window,text="Total a pagar (USD):",font=("Helvetica",12,"bold"),fg="black")
        self.labelTotalPagar.place(x=50,y=525)
        self.entryTotalPagar = tk.Entry(self.window,font=("Helvetica",13))
        self.entryTotalPagar.place(x=210,y=525,width=110)

        self.labelTotalBS=tk.Label(self.window,text="Total a pagar (BS):",font=("Helvetica",12,"bold"),fg="black")
        self.labelTotalBS.place(x=50,y=550)
        self.entryTotalBS = tk.Entry(self.window,font=("Helvetica",13))
        self.entryTotalBS.place(x=200,y=550,width=100)

        self.labelIVA=tk.Label(self.window,text="IVA:",font=("Helvetica",10,"bold"),fg="black")
        self.labelIVA.place(x=50,y=575)
        self.entryIVA = tk.Entry(self.window,font=("Helvetica",13))
        self.entryIVA.place(x=80,y=575,width=100)

        #Botones.
        self.buttonAdd=tk.Button(self.window, text="Añadir", command=self.funcAdd,font=("Helvetica",20,"bold"),fg="white",bg="red")
        self.buttonAdd.place(x=60,y=620)
        self.buttonUpdate=tk.Button(self.window, text="Actualizar", command=self.funcUpdate,font=("Helvetica",20,"bold"),fg="white",bg="red")
        self.buttonUpdate.place(x=190,y=620)
        self.buttonDelete=tk.Button(self.window, text="Eliminación Física", command=self.funcDelete,font=("Helvetica",20,"bold"),fg="white",bg="red")
        self.buttonDelete.place(x=380,y=620)
        self.buttonSearch=tk.Button(self.window, text="Buscar", command=self.funcSearch,font=("Helvetica",20,"bold"),fg="white",bg="red")
        self.buttonSearch.place(x=690,y=620)
        self.buttonClear=tk.Button(self.window, text="Limpiar", command=self.funcClear,font=("Helvetica",20,"bold"),fg="white",bg="red")
        self.buttonClear.place(x=830,y=620)



        self.window.mainloop()

#Funciones / Añadir campos.
    def funcAdd(self):            
        #Crear Objeto
        boleto=Boleto()
        boleto.nroFactura=self.entryNroFactura.get()
        boleto.nombrePelicula=self.entryNombrePelicula.get()
        boleto.CICliente = self.entryCICliente.get()
        boleto.nombreCliente = self.entryNombreCliente.get()
        boleto.apellidoCliente = self.entryApellidoCliente.get()
        boleto.sexoC=self.entrySexoC.get()
        boleto.edad=self.entryEdad.get()
        boleto.tipoEstudiante=self.entryTipoEstudiante.get()
        boleto.diaSemana = self.entryDiaSemana.get()
        boleto.fechaDia=self.entryFechaDia.get()
        boleto.fechaMes=self.entryFechaMes.get()
        boleto.fechaAño=self.entryFechaAño.get()
        boleto.cantidadBoletos = self.entryCantidadBoletos.get()
        boleto.precioBoleto = self.entryPrecioBoleto.get()

        #En caso de tener campos vacíos.
        if self.entryNroFactura.get()=="":
            messagebox.showinfo("Atención.","Ingrese Número de Factura." )
            return

        if self.entryNombrePelicula.get()=="":
            messagebox.showinfo("Atención.","Ingrese Nombre de la película." )
            return
        
        if self.entryCICliente.get()=="":
            messagebox.showinfo("Atención.","Ingrese Cédula del Cliente." )
            return
        
        if self.entryNombreCliente.get()=="":
            messagebox.showinfo("Atención.","Ingrese Nombre del Cliente." )
            return
        
        if self.entryApellidoCliente.get()=="":
            messagebox.showinfo("Atención.","Ingrese Apellido del Cliente." )
            return
        
        if self.entrySexoC.get()not in["H","M"]:
            messagebox.showinfo("Atención.","Ingrese H para indicar que el cliente es hombre.\nIngrese M para indicar que el cliente es mujer.\nNo deje el campo vacío." )
            return
        
        if self.entryEdad.get()=="":
            messagebox.showinfo("Atención.","Ingrese la edad del cliente." )
            return
        
        if self.entryTipoEstudiante.get()not in["A","I"]:
            messagebox.showinfo("Atención.","Indique si el cliente es o no un estudiante actualmente.\nA si es un estudiante activo.\nI si no es un estudiante activo." )
            return

        if self.entryCantidadBoletos.get()=="":
            messagebox.showinfo("Atención.","No deje la cantidad de boletos sin rellenar." )
            return
        if float(self.entryCantidadBoletos.get())<=0:
            messagebox.showinfo("Atención.","La cantidad de boletos debe ser superior a 0.")
            return
        
        if self.entryDiaSemana.get() not in ["L","Mar","Mier","J","V","S","D"]:
            messagebox.showinfo("Atención.","Ingrese una de las siguientes opciones:\n\nL = Lunes\nMar = Martes\nMier = Miércoles\nJ = Jueves\nV = Viernes\nS = Sábado\nD = Domingo")
            return
        
        if self.entryPrecioBoleto.get() not in ["3","4","5","6"]:
            messagebox.showinfo("Atención.","Ingrese el precio del boleto.\n3 = Sala normal.\n4 = Sala 3D Normal.\n5 = Sala Premium.\n6 = Sala 3D Premium." )
            return
        
        if self.entryFechaDia.get()not in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]:
            messagebox.showinfo("Atención.","Los días van desde el 1 hasta el 31." )
            return
        
        if self.entryFechaMes.get()not in ["1","2","3","4","5","6","7","8","9","10","11","12"]:
                    messagebox.showinfo("Atención.","Ingrese un mes desde el 1 al 12" )
                    return

        if self.entryFechaAño.get()=="":
                    messagebox.showinfo("Atención.","Ingrese el año correspondiente." )
                    return

        if self.entryCambioBS.get()=="":
            messagebox.showinfo("Atención.","El cambio a Bs. no puede ser menor a cero.\nEl cambio a Bs. debe ser un campo a rellenar." )
            return
        
        #Precio General.
        precio=float(self.entryPrecioBoleto.get())*int(self.entryCantidadBoletos.get())

        #Entrada General
        if self.entryDiaSemana.get() not in["L","J"]: boleto.TotalPagar=float(precio)
        #Lunes Popular 50%
        if self.entryDiaSemana.get() =="L":boleto.TotalPagar=float(precio/2)
        #Miércoles para ti 35% de desc.
        if self.entryDiaSemana.get() =="Mier": boleto.TotalPagar=float(precio*0.65)
        #Tipo estudiante 25% de desc. Martes y Viernes.
        if self.entryTipoEstudiante.get()=="A" and self.entryDiaSemana.get()in["Mar","V"]:boleto.TotalPagar=float(precio*0.75)
        #Jueves del 30% de desc.
        if self.entryDiaSemana.get() =="J" and (self.entryTipoEstudiante.get()=="A" or self.entryTipoEstudiante.get()=="I"): boleto.TotalPagar=float(precio*0.7)
        #Descuento para ellas 40% de desc. los viernes.
        if self.entryDiaSemana.get() =="V" and self.entrySexoC.get()=="M": boleto.TotalPagar=int(precio*0.60)
        #Mayores de 60 y menores de 14 años.
        if self.entryDiaSemana.get()in["L","Mar","Mier","J","V","S","D"] and float(self.entryEdad.get())>=60.00 or float(self.entryEdad.get())<=14.00:boleto.TotalPagar=float(precio/2)

        boleto.cambioBS=float(self.entryCambioBS.get())
        boleto.TotalBS=(boleto.TotalPagar*boleto.cambioBS)
        boleto.iva=(boleto.TotalPagar*boleto.cambioBS)*0.16


        #Evitar campos repetidos.
        sql="SELECT * FROM boletosCine  WHERE NroFactura = %s"
        val=(boleto.nroFactura,)
        mycursor.execute(sql, val)
        boletos = mycursor.fetchall()
        if len(boletos) > 0:
            messagebox.showerror("Atención","Este boleto ya fue registrado.")
            return
        
        #Sentencia que añade los campos.
        sql= "INSERT INTO boletosCine  (nroFactura,nombrePelicula,CICliente, nombreCliente, apellidoCliente, sexoC,edad,tipoEstudiante,diaSemana, fechaDia,fechaMes,fechaAño,cantidadBoletos, precioBoleto, TotalPagar, cambioBS,totalBS,IVA,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"
        val=(boleto.nroFactura,boleto.nombrePelicula,boleto.CICliente,boleto.nombreCliente,boleto.apellidoCliente,boleto.sexoC,boleto.edad,boleto.tipoEstudiante,boleto.diaSemana,boleto.fechaDia,boleto.fechaMes,boleto.fechaAño,boleto.cantidadBoletos, boleto.precioBoleto, boleto.TotalPagar,boleto.cambioBS,boleto.TotalBS, boleto.iva, boleto.status)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Proceso Exitoso","Boleto añadido satisfactoriamente.")

# Funciones / Buscar por cédula.
    def funcSearch(self):

        #Evitamos campos sin rellenar
        if self.entryNroFactura.get()=="":
            messagebox.showinfo("Atención.","Introduzca el Nro. de Boleto.")
            return

        NroFactura=self.entryNroFactura.get()
        #Se busca el campo requerido.
        sql="SELECT * FROM boletosCine  where nroFactura=%s"
        val=(NroFactura,)
        mycursor.execute(sql,val)
        pysets=mycursor.fetchall()
        for pyset in pysets:
            #Insertar informacion en los entrys
            self.entryNombrePelicula.insert(0, pyset[1])
            self.entryCICliente.insert(0, pyset[2])
            self.entryNombreCliente.insert(0, pyset[3])
            self.entryApellidoCliente.insert(0, pyset[4])
            self.entrySexoC.insert(0, pyset[5])
            self.entryEdad.insert(0, pyset[6])
            self.entryTipoEstudiante.insert(0, pyset[7])
            self.entryDiaSemana.insert(0, pyset[8])
            self.entryFechaDia.insert(0, pyset[9])
            self.entryFechaMes.insert(0, pyset[10])
            self.entryFechaAño.insert(0, pyset[11])
            self.entryCantidadBoletos.insert(0, pyset[12])
            self.entryPrecioBoleto.insert(0, pyset[13])
            self.entryTotalPagar.insert(0, pyset[14])
            self.entryCambioBS.insert(0, pyset[15])
            self.entryTotalBS.insert(0, pyset[16])
            self.entryIVA.insert(0, pyset[17])


    def funcDelete(self):
        NroFactura=self.entryNroFactura.get()
        sql = "DELETE FROM boletosCine  WHERE NroFactura = %s"
        val = (NroFactura,)
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Atención.","Eliminación exitosa.")

    #Funciones / Actualizar campos.
    def funcUpdate(self):
        #Crear Objeto
        boleto=Boleto()
        boleto.nroFactura=self.entryNroFactura.get()
        boleto.nombrePelicula=self.entryNombrePelicula.get()
        boleto.CICliente = self.entryCICliente.get()
        boleto.nombreCliente = self.entryNombreCliente.get()
        boleto.apellidoCliente = self.entryApellidoCliente.get()
        boleto.sexoC=self.entrySexoC.get()
        boleto.edad=self.entryEdad.get()
        boleto.tipoEstudiante=self.entryTipoEstudiante.get()
        boleto.diaSemana = self.entryDiaSemana.get()
        boleto.fechaDia=self.entryFechaDia.get()
        boleto.fechaMes=self.entryFechaMes.get()
        boleto.fechaAño=self.entryFechaAño.get()
        boleto.cantidadBoletos = self.entryCantidadBoletos.get()
        boleto.precioBoleto = self.entryPrecioBoleto.get()

        #En caso de tener campos vacíos.
        if self.entryNroFactura.get()=="":
            messagebox.showinfo("Atención.","Ingrese Número de Factura." )
            return

        if self.entryNombrePelicula.get()=="":
            messagebox.showinfo("Atención.","Ingrese Nombre de la película." )
            return
        
        if self.entryCICliente.get()=="":
            messagebox.showinfo("Atención.","Ingrese Cédula del Cliente." )
            return
        
        if self.entryNombreCliente.get()=="":
            messagebox.showinfo("Atención.","Ingrese Nombre del Cliente." )
            return
        
        if self.entryApellidoCliente.get()=="":
            messagebox.showinfo("Atención.","Ingrese Apellido del Cliente." )
            return
        
        if self.entrySexoC.get()not in["H","M"]:
            messagebox.showinfo("Atención.","Ingrese H para indicar que el cliente es hombre.\nIngrese M para indicar que el cliente es mujer.\nNo deje el campo vacío." )
            return
        
        if self.entryEdad.get()=="":
            messagebox.showinfo("Atención.","Ingrese la edad del cliente." )
            return
        
        if self.entryTipoEstudiante.get()not in["A","I"]:
            messagebox.showinfo("Atención.","Indique si el cliente es o no un estudiante actualmente.\nA si es un estudiante activo.\nI si no es un estudiante activo." )
            return

        if self.entryCantidadBoletos.get()=="":
            messagebox.showinfo("Atención.","No deje la cantidad de boletos sin rellenar." )
            return
        if float(self.entryCantidadBoletos.get())<=0:
            messagebox.showinfo("Atención.","La cantidad de boletos debe ser superior a 0.")
            return
        
        if self.entryDiaSemana.get() not in ["L","Mar","Mier","J","V","S","D"]:
            messagebox.showinfo("Atención.","Ingrese una de las siguientes opciones:\n\nL = Lunes\nMar = Martes\nMier = Miércoles\nJ = Jueves\nV = Viernes\nS = Sábado\nD = Domingo")
            return
        
        if self.entryPrecioBoleto.get() not in ["3","4","5","6"]:
            messagebox.showinfo("Atención.","Ingrese el precio del boleto.\n3 = Sala normal.\n4 = Sala 3D Normal.\n5 = Sala Premium.\n6 = Sala 3D Premium." )
            return
        
        if self.entryFechaDia.get()not in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]:
            messagebox.showinfo("Atención.","Los días van desde el 1 hasta el 31." )
            return
        
        if self.entryFechaMes.get()not in ["1","2","3","4","5","6","7","8","9","10","11","12"]:
                    messagebox.showinfo("Atención.","Ingrese un mes desde el 1 al 12" )
                    return

        if self.entryFechaAño.get()=="":
                    messagebox.showinfo("Atención.","Ingrese el año correspondiente." )
                    return

        if self.entryCambioBS.get()=="":
            messagebox.showinfo("Atención.","El cambio a Bs. no puede ser menor a cero.\nEl cambio a Bs. debe ser un campo a rellenar." )
            return

        #Precio General.
        precio=float(self.entryPrecioBoleto.get())*int(self.entryCantidadBoletos.get())

        #Entrada General
        if self.entryDiaSemana.get() not in["L","J"]: boleto.TotalPagar=float(precio)
        #Lunes Popular 50%
        if self.entryDiaSemana.get() =="L":boleto.TotalPagar=float(precio/2)
        #Miércoles para ti 35% de desc.
        if self.entryDiaSemana.get() =="Mier": boleto.TotalPagar=float(precio*0.65)
        #Tipo estudiante 25% de desc. Martes y Viernes.
        if self.entryTipoEstudiante.get()=="A" and self.entryDiaSemana.get()in["Mar","V"]:boleto.TotalPagar=float(precio*0.75)
        #Jueves del 30% de desc.
        if self.entryDiaSemana.get() =="J" and (self.entryTipoEstudiante.get()=="A" or self.entryTipoEstudiante.get()=="I"): boleto.TotalPagar=float(precio*0.7)
        #Descuento para ellas 40% de desc. los viernes.
        if self.entryDiaSemana.get() =="V" and self.entrySexoC.get()=="M": boleto.TotalPagar=float(precio*0.60)
        #Mayores de 60 y menores de 14 años.
        if self.entryDiaSemana.get()in["L","Mar","Mier","J","V","S","D"] and float(self.entryEdad.get())>=60.00 or float(self.entryEdad.get())<=14.00:boleto.TotalPagar=float(precio/2)

        boleto.cambioBS=float(self.entryCambioBS.get())
        boleto.TotalBS=(boleto.TotalPagar*boleto.cambioBS)
        boleto.iva=(boleto.TotalPagar*boleto.cambioBS)*0.16
        
        #Sentencia para actualizar la base de datos.
        sql="UPDATE boletosCine SET nombrePelicula=%s,CICliente=%s,nombreCliente=%s, apellidoCliente=%s,sexoC=%s,edad=%s,tipoEstudiante=%s, diaSemana=%s, fechaDia=%s,fechaMes=%s,fechaAño=%s,cantidadBoletos=%s, precioBoleto=%s, totalPagar=%s, cambioBS=%s,totalBS=%s,IVA=%s WHERE nroFactura=%s"
        val=(boleto.nombrePelicula,boleto.CICliente,boleto.nombreCliente,boleto.apellidoCliente,boleto.sexoC,boleto.edad,boleto.tipoEstudiante,boleto.diaSemana,boleto.fechaDia,boleto.fechaMes,boleto.fechaAño,boleto.cantidadBoletos, boleto.precioBoleto, boleto.TotalPagar,boleto.cambioBS,boleto.TotalBS,boleto.iva, boleto.nroFactura)
        mycursor.execute(sql,val)
        mydb.commit()
        messagebox.showinfo("Atención.","Datos del boleto actualizado.")

    def funcClear(self):
        self.buttonAdd.configure(state="normal")
        self.buttonDelete.configure(state="normal")
        self.buttonSearch.configure(state="normal")
        self.buttonUpdate.configure(state="normal")

        self.entryNroFactura.configure(state="normal")
        self.entryNroFactura.delete(0,tk.END)

        self.entryNombrePelicula.configure(state="normal")
        self.entryNombrePelicula.delete(0,tk.END)

        self.entryCICliente.configure(state="normal")
        self.entryCICliente.delete(0,tk.END)

        self.entryNombreCliente.configure(state="normal")
        self.entryNombreCliente.delete(0,tk.END)

        self.entryApellidoCliente.configure(state="normal")
        self.entryApellidoCliente.delete(0,tk.END)

        self.entrySexoC.configure(state="normal")
        self.entrySexoC.delete(0,tk.END)

        self.entryEdad.configure(state="normal")
        self.entryEdad.delete(0,tk.END)

        self.entryTipoEstudiante.configure(state="normal")
        self.entryTipoEstudiante.delete(0,tk.END)

        self.entryDiaSemana.configure(state="normal")
        self.entryDiaSemana.delete(0,tk.END)

        self.entryFechaDia.configure(state="normal")
        self.entryFechaDia.delete(0,tk.END)

        self.entryFechaMes.configure(state="normal")
        self.entryFechaMes.delete(0,tk.END)

        self.entryFechaAño.configure(state="normal")
        self.entryFechaAño.delete(0,tk.END)

        self.entryCantidadBoletos.configure(state="normal")
        self.entryCantidadBoletos.delete(0,tk.END)

        self.entryPrecioBoleto.configure(state="normal")
        self.entryPrecioBoleto.delete(0,tk.END)

        self.entryCambioBS.configure(state="normal")
        self.entryCambioBS.delete(0,tk.END)

        self.entryTotalPagar.configure(state="normal")
        self.entryTotalPagar.delete(0,tk.END)

        self.entryTotalBS.configure(state="normal")
        self.entryTotalBS.delete(0,tk.END)

        self.entryIVA.configure(state="normal")
        self.entryIVA.delete(0,tk.END)

    def actualizar_reloj(self):
        self.hora_actual = time.strftime('%H:%M:%S') #Recordar usar import time, si no, da error. (%Hora:%Minutos:%Segundos)
        self.reloj_label.config(text=self.hora_actual)
        self.window.after(1000, self.actualizar_reloj) #Se actualiza después de 1000 milisegundos.

def main():
        app = Application()

if __name__ == "__main__":
    main()

