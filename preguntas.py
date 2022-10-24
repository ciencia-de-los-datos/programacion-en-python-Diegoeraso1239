"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
class Contador(object):

  def __init__(self, inicial=0):
    self.numero = inicial

  def siguiente(self):
    self.numero += 1
    return self.numero
  
def load_and_preprocess():
  import os
  data_dir = "data.csv"
  os.stat(data_dir)
  with open(data_dir, "r") as file:
    data_example = file.readlines()
    data_example = [line.replace("\n", "") for line in data_example]
    data_example = [line.split("\t")for line in data_example]
    
  return data_example

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    data = load_and_preprocess()
    targets = [int(row[1]) for row in data]
    
    return sum(targets)


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    data = load_and_preprocess()
    sol = []
    arra_vocals = ["A","B","C","D","E"]
    for i in arra_vocals:
      targets = [row for row in data if row[0] == i]
      tupla = (i,len(targets))
      sol.append(tupla)
    return sol


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
  
    """
    data = load_and_preprocess()
    sol = []
    counting = 0
    arra_vocals = ["A","B","C","D","E"]
    for i in arra_vocals:
      for row in data:
        if row[0]==i:
           counting = counting + int(row[1])
      tupla = (i, counting)
      counting = 0
      sol.append(tupla)
    return sol


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]
    
    """
    data = load_and_preprocess()
    sol = []
    arra_months = ["01","02","03","04","05","06","07","08","09","10","11","12"]

    targets = [[line.split("-") for line in row][2] for row in data]

    for i in arra_months:
      filter_per_month = [row for row in targets if row[1] == i]
      tupla = (i,len(filter_per_month))
      sol.append(tupla)
    return sol


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    data = load_and_preprocess()
    targets = []
    sol = []
    arra_vocals = ["A","B","C","D","E"]
    for i in arra_vocals:
      for row in data:
        if row[0] == i:
          targets.append(int(row[1]))
      tupla = (i,max(targets),min(targets))
      targets = []
      sol.append(tupla)
    return sol


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    data =  load_and_preprocess()
    targets = [row[4] for row in data ]
    start = ["aaa:","bbb:","ccc:","ddd:","eee:","fff:","ggg:","hhh:","iii:","jjj:"]
    end = ','
    extraction = 1
    arr_extraction = []
    sol = []

    for st in start:
      for i in targets:
        if i.find(st) != -1:
          extraction = i.split(st)[1].split(end)[0]
        arr_extraction.append(int(extraction))
      tupla = (st[:3],min(arr_extraction),max(arr_extraction))
      sol.append(tupla)
      arr_extraction = []
    return sol


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]
    
    """
    data = load_and_preprocess()
    arr_numbers = ['0','1','2','3','4','5','6','7','8','9']
    sol = []
    for i in arr_numbers:
      targets = [row[0] for row in data if row[1] == i]
      tupla = (int(i),targets)
      sol.append(tupla)
    return sol


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    data = load_and_preprocess()
    arr_number = ['0','1','2','3','4','5','6','7','8','9']
    sol = []

    for i in arr_number:
      targets = [row[0] for row in data if row[1] == i]
      not_repetition = []
      [not_repetition.append(x) for x in targets if x not in not_repetition]
      not_repetition.sort()
      tupla = (int(i),not_repetition)
      sol.append(tupla)
    return sol


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    data =  load_and_preprocess()
    targets = [row[4] for row in data ]
    start = ["aaa","bbb","ccc","ddd","eee","fff","ggg","hhh","iii","jjj"]
    sol = {}
    for st in start:
      cuenta = Contador()
      for i in targets:
        if i.find(st) != -1:
          cuenta.siguiente()
      sol[st]=cuenta.numero

      cuenta.numero = 0
      
    return sol


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


      """
    data = load_and_preprocess()
    arr_vocals = ['A','B','C','D','E']
    sol = []
    for row in data:
      targets = row[3:5]
      tupla = (row[0],len(targets[0].split(',')),len(targets[1].split(',')))
      sol.append(tupla)
      
    return sol


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    data = load_and_preprocess()
    arr_vocals = ['a','b','c','d','e','f','g']
    sum = 0
    sol = []
    for st in arr_vocals:
      for row in data:
        if row[3].find(st) != -1:
          sum = sum + int(row[1])
      tupla = (st,sum)
      sol.append(tupla)  
      sum = 0
      
    return sol


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    data = load_and_preprocess()
    arr_vocals = ['A','B','C','D','E']
    sum, start, end = 0,':',','
    dicc = {}
    for st in arr_vocals:
      for row in data:
          if  row[0]==st:
            targets = row[4].split(',')
            for tar in targets:
              extract = tar.split(start)[1].split(end)[0]
              sum = sum + int(extract)

      dicc[st] = sum
      sum = 0
    return sol
