class Atleta():
  def __init__ (self,nombre,apellido,altura,peso,telefono): #habia un ultimo parametro el cual no va aca (indice de masa corporal), explicacion abajo
    
    self._nombre=nombre
    self.__apellido=apellido
    
    
  def get_altura(self):
    return self.__altura
  def get_peso(self):
    return self.__peso
  def get_telefono(self):
    return self.__telefono
  
  
  def get_imc(self): 
    return self.__peso / self.__altura**2 #imc

  def decir_indice(self):
    i=self.get_imc()
    if i <26:
      print("peso bajo")
    elif i < 40:
      print("peso normal")
    elif i<60:
      print("peso excesivo")
    else:
      print("sobrepeso")

  #para cmabiar nombre de PRIVADO a PÚBLICO hacemos lo siguiente

  def cambiar_nombre(self, nombre):
    self.__nombre = nombre

  def cambiar_apellido(self, apellido):
    self.__apellido = apellido
  
  #crecer en cm

  def crecer(self, crece):
    self.__crece = crece
  
  #cambiar de peso en gramos

  def bajar_de_peso(self, A):
    self.__peso -= A/100
  
  def subir_de_peso(self, B):
    self.__peso += B/100
  

  #cambiar telefono

  def cambiar_telefono(self, telefono):
    self.__telefono = telefono