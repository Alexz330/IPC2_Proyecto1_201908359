from node import node
from matriz import*

class linked_list:
  def __init__(self):
    self.head = None

  def insertar(self, matriz):
    if not self.head:
      self.head = node(matriz=matriz)
      return
    current = self.head
    while current.next:
      current = current.next
    current.next = node(matriz=matriz)

  def imprimir(self):
    node = self.head
    while node != None:
      print(node.matriz.nombre, end = " => ")
      node = node.next

  def eliminar(self, nombre):
    current = self.head
    previous = None

    while current and current.matriz.nombre != nombre:
      previous = current
      current = current.next
    if previous is None:
      self.head = current.next
    elif current:
      previous.next = current.next
      current.next = None
        
