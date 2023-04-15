from Origin_linkedQueue import LinkedQueue

class TwoQueueStack:
  def __init__(self):
    self.__q1 = LinkedQueue()
    self.__q2 = LinkedQueue()    
  
  def enqueue(self, Data):
    self.__q1.enqueue(Data)
    
  def dequeue(self):
    return self.__q1.dequeue()
  
if __name__ == '__main__':
  st = TwoQueueStack()
  for i in range(1, 4):
    st.enqueue(i)
  for j in range(1, 4):
    print(st.dequeue())