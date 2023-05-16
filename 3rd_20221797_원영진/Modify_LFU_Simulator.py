from Modify_heap import *

def lfu_sim(cache_slots):
  data_list = []
  data_dict = {}
  cache_heap = MinHeap()
  cache_hit = 0
  tot_cnt = 0

  data_file = open("3rd_20221797_원영진/linkbench.trc")

  for line in data_file.readlines():
    lpn = line.split()[0]
    data_list.append(lpn)

  for i in range(0, len(data_list)):
    tot_cnt += 1
    data = data_list[i]

    if cache_heap.size() < cache_slots:
      if data in data_dict.keys():
        data_dict[data] += 1
        cache_hit += 1
        cache_heap.UpdateHeap(data)
      else:
        data_dict[data] = 1
        cache_heap.Insert([data, 1])

    else:
      if data in data_dict.keys():
        if cache_heap.CacheIn(data) == True:
          data_dict[data] += 1
          cache_hit += 1
          cache_heap.UpdateHeap(data)
        else:
          data_dict[data] += 1
          cache_heap.UpdateMin([data, data_dict[data]])
      else:
        data_dict[data] = 1
        cache_heap.UpdateMin([data, 1])

  print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", cache_hit / tot_cnt)

if __name__ == "__main__":
  for cache_slots in range(100, 1000, 100):
    lfu_sim(cache_slots)