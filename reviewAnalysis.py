import pandas as pd
from circularDoublyLinkedList import *
from circularDoublyLinkedListFilter import *
  
def load_data(dataset: CircularDoublyLinkedList):
  i = 0
  with open('amazon_reviews_us_PC_v1_00.tsv/amazon_reviews_us_PC_v1_00.tsv', 'r') as file:
    for line in file:
      fileds = line.split('\t')
      if i != 0:
        dataset.append(i, fileds[7])
      i += 1
      if i == 11001:
        break

def get_data(dataset: CircularDoublyLinkedList, value):
  filtered = dataset.filter(dataset, value)
  print(filtered)
  
if __name__ == '__main__':
  dataset = CircularDoublyLinkedList()
  load_data(dataset)
  get_filter_list = get_data(dataset, '1')
