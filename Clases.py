import pandas as pd

class saludo:
    def __init__(self, nombre,apellido, edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad


    def guardar(self,clientes):
        diccionario=dict(Nombre=self.nombre, Apellido=self.apellido, Edad=self.edad)
        clientes.append(diccionario)

    def data_csv(clientes):
        lista_total=[]
        for archivo in clientes:
            lista_total.append({
                'Nombre': archivo['Nombre'],
                'Apellido': archivo['Apellido'],
                'Edad': archivo['Edad']
            })
        columns=['id','Nombre','Apellido','Edad']
        df = pd.DataFrame(lista_total, columns=columns)
        df.to_csv('datos.csv')








class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)