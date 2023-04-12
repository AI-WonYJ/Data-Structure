class CircularDoublyLinkedListFilter:
  def __init__(self, sheet, value):
    self.__head = sheet.getNode(-1)
    self.loc = self.__head.next
    self.value = value
    
  def find(self, value):
    curr = self.loc
    filter_list = []
    while curr != self.__head:
      if curr.item[1] == value:
        filter_list.append(curr.item)
      curr = curr.next
    # print(filter_list)
    return filter_list
  
  