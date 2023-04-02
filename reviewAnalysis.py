import pandas as pd
from circularDoublyLinkedList import *
from circularDoublyLinkedListFilter import *

def show_review_
  
def load_data(dataset: CircularDoublyLinkedList):
  with open('amazon_reviews_us_PC_v1_00.tsv/amazon_reviews_us_PC_v1_00.tsv', 'r') as file:
    s = 1
    end = 10
    for line in file:
      fileds = line.split('\t')
      print(fileds)
      s += 1
      if s >= end:
        break

def get_data(dataset: CircularDoublyLinkedList):
  filtered = dataset.filter(CircularDoublyLinkedListFilter())

a = CircularDoublyLinkedListFilter()
a.load_data()

# ['marketplace',
# 'customer_id',
# 'review_id',
# 'product_id',
# 'product_parent',
# 'product_title',
# 'product_category',
# 'star_rating',
# 'helpful_votes',
# 'total_votes',
# 'vine',
# 'verified_purchase',
# 'review_headline',
# 'review_body',
# 'review_date\n']