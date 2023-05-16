from Modify_quickSort import *
from Modify_mergeSort import *

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
  # quickSort(A, 0, len(A)- 1)
  mergeSort(A, 0, len(A)-1)
  
  for i in range(10):
    print(A[i], end=" ")  
    print("")
  
if __name__ == "__main__":
  do_sort("4th_20221797_원영진/linkbench_short.trc")