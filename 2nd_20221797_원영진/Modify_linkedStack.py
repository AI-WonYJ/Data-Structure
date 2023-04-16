class LinkedStack:
  def __init__(self):
    self.__stack = []
        
  def push(self, newItem):
    self.__stack.insert(0, newItem)
    
  def pop(self):
    return self.__stack.pop(0)
  
  def top(self):
    if self.isEmpty():
      return None
    else:
      return self.__stack.get(0)
    
  def isEmpty(self) -> bool:
    return not bool(self.__stack)
  
  def popAll(self):
    self.__stack.clear()
    
  def printStack(self):
    print("Stack from top:", end = ' ')
    for i in range(len(self.__stack)-1, -1, -1):
      print(self.__stack[i], end = ' ')
    print()