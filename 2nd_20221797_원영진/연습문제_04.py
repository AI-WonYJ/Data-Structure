from linkedQueue import LinkedQueue

class TwoQueueStack:
  def __init__(self):
    self.__q = LinkedQueue()
    self.__tq = LinkedQueue()
    
  def __move_elements(self, q, tq):
    while not q.isEmpty():
      tq.enqueue(q.dequeue())
  
  def push(self, x):
    self.__move_elements(self.__q, self.__tq)
    self.__q.enqueue(x)
    self.__move_elements(self.__tq, self.__q)
    
  def pop(self):
    return self.__q.dequeue()
  
if __name__ == '__main__':
  st = TwoQueueStack()
  for i in range(1, 4):
    st.push(i)
  for j in range(1, 4):
    print(st.pop())