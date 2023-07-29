"""1) Escribir una clase llamada Rectángulo que contenga una base y una altura, 
y que contenga un método que devuelva el área
del rectángulo."""

"""class Rectangulo:
    
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
        
    def area(self):
        return self.base*self.altura
    
    
# Creación de una instancia de la clase Rectangulo con base=5 y altura=10
rectangulo1 = Rectangulo(5, 10)

# Cálculo del área utilizando el método area()
area_rectangulo1 = rectangulo1.area()

print(f"El área del rectángulo es: {area_rectangulo1}")    """

#____________________________________________________________________________________

"""class Triangulo:
    
    def __init__(self,base,altura,lado):
        self.base=base
        self.altura=altura
        self.lado=lado
        
    def Perimetro(self):
        return self.base+self.altura+self.lado
    
    def area(self):
        return self.base * self.altura /2
    
# creacion de la intancia de la clase triangulo con base=5 altura=10 y lado =10

triangulo=Triangulo(int(input(" Ingrese la base del triangulo: ")),int(input(" Ingrese la altura del triangulo : ")),int(input(" Ingrese el lado del triangulo : ")))

perimetro_del_Triangulo=triangulo.Perimetro()

area_del_Triangulo=triangulo.area()

print(f"El Perimetro del  triangulo es: {perimetro_del_Triangulo } ,el area del Triangulo es:  {area_del_Triangulo}")      
"""
#____________________________________________________________________________________________________________

"""2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. 
La clase debe contener como miembros:
o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
o Un atributo para el estado (lleno o vacío).
o Un atributo n, que indica la cantidad máxima de cebadas.
o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
“Advertencia: el mate está lavado.” pero no se debe lanzar una excepción.
"""

"""class Mate:
    def __init__(self, cantidad_cebadas,cantidad_maxima_cebadas=10,lleno=False,vacio=False):
        
        self.cantidad_cebadas=cantidad_cebadas
        self.lleno=lleno
        self.vacio=vacio
        self.cantidad_maxima_cebadas=cantidad_maxima_cebadas
        
    def cebar(self):
        
        if self.cantidad_cebadas >=0 and self.cantidad_cebadas<=10 :
            
            if self.cantidad_cebadas==0 and self.vacio==True:
               
               
               print(" cuidado, todavia el mate esta vacio ")
               print(" La paba esta calentando")
                  
            
            else:
                print(" comenzamos a cargar el mate que estaba vacio ")
                self.vacio=False
                
                print(" Empezamos a tomar unos ricos mates con amigos ")
                
        elif self.cantidad_cebadas >= self.cantidad_maxima_cebadas:
            raise Exception("¡Cuidado! ¡Te quemaste!")
        
        else:
            self.vacio=True
            
            print(" Se termino de cebar unos mates para los amigos, el mate esta lavado!!!")
    def beber(self):
        if self.cantidad_cebadas ==0:
            print(" el mate esta lavado")
        else:
            self.cantidad_cebadas-=1   
            if self.cantidad_cebadas==0:
              self.vacio=True
              
    
    
            
cantidad_cebadas = int(input("Ingrese la cantidad de cebadas para el mate: "))
nCantidad_de_cebadas = Mate(cantidad_cebadas)



nCantidad_de_cebadas.cebar()
nCantidad_de_cebadas.beber()"""

#---------------------------------------------------------------------------------------------------
"""3) Botella y Sacacorchos
 Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
 Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, 
o None si está destapada.
 Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, 
le saque el corcho y se guarde una referencia al corcho sacado. 
Debe lanzar una excepción en el caso en que la botella ya esté destapada, 
o si el sacacorchos ya contiene un corcho.
 Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción 
en el caso en el que no haya un corcho."""

"""class Corcho:
    def __init__(self,bodega):
        self.bodega=bodega
        self.bodega=bodega
        
        
class Botella:
    def __init__(self,corcho):
        self.corcho=corcho
        self.tapada=True
        
class Sacacorchos:
    def __init__(self,botella):
        self.botella = botella
        self.estado=True
        
    def destapar(self):
            if self.estado == True:
                if self.botella.tapada ==True:
                   print(" La botella esta destapada")
                   self.botella.tapada=False
                   self.estado=" lleno"
                   print(" el sacacorcho esta lleno ")
                else:
                    print(" la botella no contiene al corcho")
            else:
                print(" La botella ya esta destapada")
                
    def limpiar(self): 
            if self.estado == True:
               raise Exception(" no hay corcho en el sacacorchos")
            else:
              self.botella.corcho=True
#Creamos las instancias de los corchos y las instancias de las botelas y tambien sacacorchos

corcho1= Corcho(bodega=" Balbo")


botella1=Botella(corcho1)

sacacorcho1=Sacacorchos(botella1)
sacacorcho1.destapar()
sacacorcho1.limpiar()

print(sacacorcho1.estado)
print(corcho1.bodega)

corcho2=Corcho(corcho1)
botella2=Botella(corcho2)
sacacorcho2=Sacacorchos(botella2)
sacacorcho2.destapar()
sacacorcho2.limpiar()
print(corcho2.bodega)

"""

"""4) Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos: 
restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un 
método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase 
Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los 
sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame 
al método."""





