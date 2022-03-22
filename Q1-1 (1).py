# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 19:03:25 2021

@author: User
"""

import csv

class Film:
    def __init__(self,title,year,runtime):
      self.title = title
      self.year = year
      self.runtime = runtime

    def getTitle(self):
      return self.title


    def getYear(self):
        return self.year
    
    def getRuntime(self):
        return self.runtime

class Films:
    def __init__(self,read_file,new_list):
      self.read_file = read_file
      self.new_list = new_list
    
    def readFile(self):
      for i in self.read_file:
        print(i)

    def createFilmsList(self):
      for i in self.read_file:
        self.new_list.append([i[1],i[2],i[4]])

    def getFilmsList(self):
      return self.new_list

F = open("imdb_top_1000.csv")
Read = csv.reader(F)
top = []
top = next(Read)
lis =[]


f_obj = Films(Read,lis)

J = f_obj.createFilmsList()

K = f_obj.getFilmsList()

print("FILMS RELEASED AFTER 2019:")
for i in K:
  if i[1]>'2019':
    print(i[0], "was released in", i[1], "and has a runtime of", i[2])

print("\n")
print("FILMS HAVING RUNTIME LESS THAN 70 MINUTES:")
for i in K:
  if i[2]>'321 min' and i[2]<'70 min':
    print(i[0], "was released in", i[1], "and has a runtime of", i[2])



F.close()