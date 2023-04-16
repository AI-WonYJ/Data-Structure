from Modify_linkedStack import LinkedStack

class TwoStackQueue:
  def __init__(self):
    self.__q1 = LinkedStack()
    self.__q2 = LinkedStack()    
  
  def enqueue(self, Data):
    while not self.__q1.isEmpty():
      self.__q2.push(self.__q1.pop())
    self.__q1.push(Data)
    while not self.__q2.isEmpty():
      self.__q1.push(self.__q2.pop())
    
  def dequeue(self):
    return self.__q1.pop()
  
if __name__ == '__main__':
  st = TwoStackQueue()
  for i in range(1, 4):
    st.enqueue(i)
  for j in range(1, 4):
    print(st.dequeue())