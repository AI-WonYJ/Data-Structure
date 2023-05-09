from Modify_quickSort import *
from Origin_mergeSort import *

def do_sort(input_file):
  
  data_file = open(input_file)
  A = []
  data_dict = {}
  for line in data_file.readlines():
    lpn = line.split()[0]
    if lpn not in data_dict.keys():
      data_dict[lpn] = len(data_dict)
      A.append([lpn, 1])
    else:
      A[data_dict.get(lpn)][1] += 1
    
  for i in range(0, 10): # len(A)):
    if A[i][0] == '0':
      print(A[i])
    # print(A[i], end = " ")
    # print("")
  quickSort(A, 0, len(A)- 1)
  print("DID")
  # mergeSort(A, 0 , len(A)-1)
  
  # for i in range(10):
  #   print(A[i], end=" ")
  #   print("")
  A.reverse()
  print(A)
  
if __name__ == "__main__":
  do_sort("4th_20221797_원영진/linkbench_short.trc")

# A = [['115268', 1], ['115340', 1333], ['115345', 541]]
# print(A)
# quickSort(A, 0, len(A)- 1)
# print(A)