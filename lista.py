#from Matriz import matriz
from Node import node


class matriz:
  def __init__(self, m, n, nombre, dato):
    self.m = m
    self.n = n
    self.nombre = nombre
   
    self.head = None 



class listaCircular:
  
  def __init__(self, head=None):
    self.head = head
    self.size = 0

  def insertar (self, matriz):
    if self.size == 0:
      self.head = node(matriz=matriz)
      self.head.next = self.head
    else:
      new_node = node(matriz=matriz, next=self.head.next)
      self.head.next = new_node
    self.size += 1

  def imprimir (self):
    if self.head is None:
      return
    node = self.head
    print(node.matriz.nombre, end = " => ")
    while node.next != self.head:
      node = node.next
      print(node.matriz.nombre, end = " => ")

  def eliminar (self, nombre):
    node = self.head
    previous = None

    while True:
      if node.matriz.nombre == nombre:
        if previous is not None:
          previous.next = node.next
        else:
          while node.next != self.head:
            node = node.next
          node.next = self.head.next
          self.head = self.head.next
        self.size -= 1
        return True
      elif node.next == self.head:
        return False
      
      previous = node
      node = node.next
        
