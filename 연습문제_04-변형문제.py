from Origin_linkedQueue import LinkedQueue

class TwoQueueStack:
  def __init__(self):
    self.__q1 = LinkedQueue()
    self.__q2 = LinkedQueue()    
    
  def __move_elements(self, fromQueue, toQueue):  #'fromQueue'의 모든 Queue 값을 'toQueue'로 옮기는 함수
    while not fromQueue.isEmpty():
      toQueue.enqueue(fromQueue.dequeue())
      
  def __get_end(self, wantQueue, temporayQueue):  #'wantQueue'의 마지막 값을 가져오는 함수
    while not wantQueue.isEmpty():
      element = wantQueue.dequeue()  #'wantQueue'의 첫번째 값을 dequeue() 함수를 이용해 변수 'element'에 저장
      if wantQueue.isEmpty():  #'wantQueue'가 Empty이면
        self.__move_elements(temporayQueue, wantQueue)  #'temporaryQueue'의 모든 값들을 wantQueue로 되돌려줌
        return element  #초기 'wantQueue'의 마지막 값을 저장했던 변수 'element'를 return
      else:
        temporayQueue.enqueue(element)  #'temporaryQueue'에다가 'element' 값을 임시저장
        
  def push(self, x):
    self.__q1.enqueue(x)
    
  def pop(self):
    return self.__get_end(self.__q1, self.__q2)

if __name__ == '__main__':
  st = TwoQueueStack()
  for i in range(1, 4):
    st.push(i)
  for j in range(1, 4):
    print(st.pop())