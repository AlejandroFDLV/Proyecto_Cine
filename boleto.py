class Boleto():
    def __init__(self):
        pass
    nroFactura=0 #00055200
    nombrePelicula="" # "Destino Final 6"
    CICliente="" #Ej: V-3XXXXXXX.
    nombreCliente="" #Ej Alejandro.
    apellidoCliente="" #Ej Fajardo.
    sexoC="" #"H"=Hombre,"M"=Mujer
    edad="" #Niño <= 14, General>14, Mayor de edad=>60
    tipoEstudiante="" #"S"=Si,"N"=No, 25% desc. de martes a viernes.
    diaSemana="" #L,Mar,Mier,J,V,S,D
    fechaDia=0 #Del 1 al 31
    fechaMes=0 #Del 1 al 12
    fechaAño=0 #2XXX
    cantidadBoletos=0 #Superior a 0.
    precioBoleto=0.0 #"3" Normal, "4" 3D Normal, "5" Premium, "6" 3D Premium.
    totalPagar=0 #Se calcula al añadir la información.
    
    cambioBS=0 #Se calcula en el código.
    status="A"