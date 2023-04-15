from Origin_linkedQueue import LinkedQueue

class TwoQueueStack:
  def __init__(self):
    self.__queue1 = LinkedQueue()
    self.__queue2 = LinkedQueue()
    
  def __move_elements(self, fromQueue, toQueue):  #'fromQueue'의 모든 Queue 값을 'toQueue'로 옮기는 함수
    while not fromQueue.isEmpty():
      toQueue.enqueue(fromQueue.dequeue())
  
  def push(self, x):
    self.__move_elements(self.__queue1, self.__queue2)
    self.__queue1.enqueue(x)
    self.__move_elements(self.__queue2, self.__queue1)
    
  def pop(self):
    return self.__queue1.dequeue()
  
if __name__ == '__main__':
  st = TwoQueueStack()
  for i in range(1, 4):
    st.push(i)
  for j in range(1, 4):
    print(st.pop())