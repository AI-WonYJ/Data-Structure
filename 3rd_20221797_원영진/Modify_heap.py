class MinHeap:
  def __init__(self, *args):
    if len(args) != 0:
      self.__A = args[0]
    else:
      self.__A = []

  def Insert(self, x):
    self.__A.append(x)
    i = len(self.__A) - 1
    parent = (i - 1)  // 2
    if i > 0 and self.__A[i][1] > self.__A[parent][1]:
      self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
      i =  parent
      parent = (i - 1)  // 2

  def UpdateHeap(self, key):
    for i in range(0, len(self.__A)):
      if self.__A[i][0] == key:
        self.__A[i][1] += 1
        self.__percolateDown(i)
        break

  def UpdateMin(self , data):
      self.__A[0] = data
      self.__percolateDown(0)

  def __percolateDown(self , i:int):
    child = 2 * i + 1
    rightChild = 2 * i + 2
    if child <= len(self.__A) - 1:
      if rightChild <= len(self.__A) - 1 and self.__A[child][1] > self.__A[rightChild][1]:
        child = rightChild
      if self.__A[i][1] > self.__A[child][1]:
        self.__A[i] , self.__A[child] = self.__A[child] , self.__A[i]
        self.__percolateDown(child)
        
  def CacheIn(self , data) -> bool:
    result = False
    for i in range(0, len(self.__A)):
      if self.__A[i][0] == data:
        result = True
        break
    return result
    
  def size(self) -> int :
    return len(self.__A)