#1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que 
#devuelva el área del rectángulo.

"""class rectangulo():
    def __init__(self, base, altura):
        self.base= base
        self.altura= altura
    
    def area(self):
        calculo= self.base * self.altura
        print(f"el area es: {calculo})

rec= rectangulo(10,5)
rec.area()"""

#2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. 
#La clase debe contener como miembros:

"""o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
o Un atributo para el estado (lleno o vacío).
o Un atributo n, que indica la cantidad máxima de cebadas.
o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
“Advertencia: el mate está lavado.” pero no se debe lanzar una excepción."""

"""class mate():
    def __init__(self, cebadas):
        self.cebadas_restantes= int(cebadas)
        self.cebadas= int(cebadas)
        self.estado= False

    def cebar(self):
        if self.estado==True:
            print("¡Cuidado! ¡Te quemaste! ")
        else:
            print("se lleno con excito! ")
            self.estado= True

    def beber(self):
        if self.estado is False:
            print("el mate esta bacio! ")
        if self.estado is True:
            self.cebadas_restantes= self.cebadas_restantes -1
            self.estado= False
            print(f"el numero de cebadas dispinible es: {self.cebadas_restantes}")
            if self.cebadas_restantes==0:
                print("Advertencia: el mate está lavado. ")

mate4= mate(4)
mate4.cebar()
mate4.beber()
mate4.cebar()
mate4.beber()
mate4.beber()
mate4.cebar()
mate4.beber()
mate4.cebar()
mate4.cebar()
mate4.beber()"""

#3) Botella y Sacacorchos
""" Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
 Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está
destapada.
 Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el
sacacorchos ya contiene un corcho.
 Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya
un corcho."""

class corcho():
    def __init__(self, bodega):
        self.bodega= bodega

class botella():
    def __init__(self, corcho=None):
        self.corcho= corcho

class saca_corcho():
    def __init__(self):
        self.corcho= None

    def destapar(self):
        if self.corcho is not None:
            print("el sacacorcho ya tine un corcho ")

        if botella.corcho is None:
            print("la botella ya esta destapada ")
            self.corcho= botella.corcho

        else:
            print("se destapo corectamente! ")

    def limpiar(self):
        if self.corcho is True:
            print("ya se limpio el saca corcho! ")
            self.corcho= False

        else:
            print("el saca corcho ya esta limpio ")

#no entendi mi codigo ahora :((

corc= corcho("Del Valle")
bote= botella(corc)
#saca= saca_corcho()

#saca.destapar(bote)
#saca.limpiar()
#saca.destapar()

           
#4) Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos:
#restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un
#método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase
#Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los
#sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame
#al método. 

"""class restaurante():
    def __init__(self, nombre, comida):
        self.nombre= nombre
        self.comida= comida
        self.estado= "cerrado"

    def describir_res(self):
        print(f"Restaurante: {self.nombre}")
        print(f"Tipo de comida: {self.comida}")

    def abrir_res(self):
        if self.estado == "cerrado":
            print(f"el restaurante {self.nombre} esta abierto ")
            self.estado= "abierto"
        else:
            print("ya esta abierto! ")

class heladeria(restaurante):
    def __init__(self, nombre, comida):
        super().__init__(nombre, comida)
        self.sabores= []

    def los_sabor(self):
        if self.sabores:
            print("Sabores disponibles: ")
            for sabor in self.sabores:
                print(f"- {sabor}")
        else:
            print("no hay sabores disponibles. ")

hela= heladeria("grido", "helados")
hela.sabores= ["vainilla", "granizado", "frutilla"]

hela.describir_res()
hela.abrir_res()
hela.los_sabor()"""

#5) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que
#reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover
#que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
# Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro
#personaje, al que le debe hacer el daño indicado por el atributo ataque.
# Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que
#devuelva la cantidad cosechada

"""class personaje():
    def __init__(self, vida, posicion, velocidad):
        self.vida= vida
        self.posicion= posicion  #una lista [x,y]
        self.velocidad= velocidad
    
    def recibir_ataque(self, cantidad):
        self.vida= self.vida - cantidad
        print(f"el personaje a recibido un ataque de: {cantidad}. la vida restante es: {self.vida} ")
        if self.vida == 0:
            print(f"el personaje a muerto! ")
        elif self.vida < 0:
            print(f"el personaje esta a 100m bajo tierra ")
    
    def mover(self, direcc):
        if direcc == "arriba" :
            self.posicion[1] += self.velocidad
        elif direcc == "abajo" :
            self.posicion[1] -= self.velocidad
        elif direcc == "izquierda" :
            self.posicion[0] -= self.velocidad
        elif direcc == "derecha" :
            self.posicion[0] += self.velocidad
        else:
            print("direccion no valida")
        print(f"el personaje se movio a la posicion: {self.posicion} ")
        

class soldado(personaje):
    def __init__(self, vida, posicion, velocidad,ataque):
        super().__init__(vida, posicion, velocidad)
        self.ataque= ataque

    def atacar(self, objetivo):
        if isinstance(objetivo, personaje):
            print(f"el soldado ataca con un daño de: {self.ataque}")
            objetivo.recibir_ataque(self.ataque)
        else:
            print("no es valido")


class campesino(personaje):
    def __init__(self, vida, posicion, velocidad,cosecha):
        super().__init__(vida, posicion, velocidad)
        self.cosecha= cosecha
    
    def coschar(self):
        print(f"el campesino a cosechado: {self.cosecha} ")

solda= soldado(vida=100, posicion=[0,0], velocidad=2, ataque=20)
capo= campesino(vida=100, posicion=[5,5], velocidad=1, cosecha=30)

#soldado mueve para atacar a campesino
solda.mover("derecha")
solda.mover("arriba")
solda.atacar(capo)

#campesino esta cosechando
capo_cosecha= capo.coschar()"""

#6) Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente
#se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del
#usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
#Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno.

"""class user():
    def __init__(self, nombre, apellido, edad,DNI, email, contraseña):
        self.nombre= nombre
        self.apellido= apellido
        self.edad= edad
        self.dni= DNI
        self.email= email
        self.contraseña= contraseña

    def describir(self):
        print(f"Usuario: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")
        print(f"Email: {self.email}")
        print(f"Contraseña: {self.contraseña}")

    def saludar(self):
        print(f"¡bienvenido {self.nombre} {self.apellido} ! un gusto conocerte. " )"""

"""usuario1= user("Ana", "Gomez", 17, 53827, "anagom@56", 282736 )
usuario2= user("Carlos", "Martinez", 25, 72635, "carlos@23", 22457)
usuario3= user("Jesus", "Burgos", 56, 8762, "luca@726", 82736)

usuario1.describir()
usuario1.saludar()

usuario2.describir()
usuario2.saludar()

usuario3.describir()
usuario3.saludar()"""

#7) Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase
#Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede
#postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que
#muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método.

"""class admin(user):
    def __init__(self, nombre, apellido, edad, DNI, email, contraseña):
        super().__init__(nombre, apellido, edad, DNI, email, contraseña)
        self.privilegios= [
            "puede postear en el foro",
            "puede borrar un post" ,
            "puede banear usuario"
        ]

    def mostrar_pri(self):
        print(f"Privilegios del administrador: {self.nombre} ")
        for privilegio in self.privilegios:
            print(f"- {privilegio} ")


admi1= admin("Laura", "Fernandez", 22, 6257, "laura@627", 837362 )

admi1.describir()
admi1.mostrar_pri()"""

#8) Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene una lista de strings
#con los privilegios de manera similar a la del ejercicio 7. Mueva el método mostrar_privilegios() de ese ejercicio a esta
#clase, y haga que una instancia de esta clase sea un atributo de la clase Admin. Cree una nueva instancia de Admin y use
#el método para mostrar privilegios.

"""class Privilegios():
    def __init__(self):
        self.privilegios= [
            "puede postear en el foro",
            "puede borrar un post" ,
            "puede banear usuario"
        ]

    def mostrar_pri(self):
        print("privilegios: ")
        for privilegio in self.privilegios:
            print(f"- {privilegio} ")

class adm(user):
    def __init__(self, nombre, apellido, edad, DNI, email, contraseña):
        super().__init__(nombre, apellido, edad, DNI, email, contraseña)
        self.privilegios= Privilegios()

admis1= adm("Marcos", "Vega", 18, 82774, "vegas@82", 82864 )

admis1.describir()
admis1.privilegios.mostrar_pri()"""

#9) Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4, e impórtela
#al módulo actual. Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse que la importación
#funcionó.

"""from restauran import restaurante

restau= restaurante("Roman", "Pizza")

restau.describir_res()
restau.abrir_res()"""

#10) (Opcional): Repita el ejercicio anterior pero esta vez importando la clase Heladeria.
#Qué se necesita para que funcione la importación.

"""from restauran import heladeria

hela= heladeria("Grido", "Helados")

hela.sabores= ["vainilla", "granizado", "frutilla"]
hela.describir_res()
hela.los_sabor()"""
