from Modify_heap import *

def lfu_sim(cache_slots):
  data_dict = {}
  data_list = []
  cache_hit = 0
  tot_cnt = 0

  data_file = open("linkbench.trc")

  for line in data_file.readlines():
    lpn = line.split()[0]

    # Program het
    if len(data_dict) < cache_slots:
        if lpn in data_dict.keys():
            data_list[data_dict.get(lpn)][1] += 1
        else:
            data_dict[lpn] = len(data_dict)
            data_list.append([lpn, 1])
    else:
       if lpn in data_dict.keys():
          data_list[data_dict.get(lpn)][1] += 1
       else:          
          heapsort = Heap(data_list)
          heapsort.buildHeap()
          heapsort.delete
          del data_dict[lpn]
      
    

    print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", cache_hit / tot_cnt)

if __name__ == "__main__":
  for cache_slots in range(100, 1000, 100):
    lfu_sim(cache_slots)