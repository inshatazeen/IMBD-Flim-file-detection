# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 23:46:01 2021

@author: User
"""

class SentimentLexicon():
  
  def __init__(self,d,file1,file2):
    self.d = d
    self.file1 = file1
    self.file2 = file2
  
  def reader(self,file1,file2):
    negative = (self.file1).readlines()
    positive = (self.file2).readlines()


    for i in negative[31:]:
      if i in (self.d):
        self.d[i]-=1
      else:
        self.d[i] = -1
    
    for i in positive[30:]:
      if i in (self.d):
        self.d[i]+=1
      else:
        self.d[i] = 1
    
    return self.d

class Classifier():
  
  def __init__(self,D,string):
    self.D = D
    self.string = string
  
  def classify(self,string):
    score = 0
    
    for i in string:
      if i == '.':
        string2 = string.replace(".",'') 
      elif i == ',':
        string2 = string.replace(",",'')
      elif i == '!':
        string2 = string.replace("!",'')
    
    string_split = string2.split()
    
    L = list(self.D.keys())
    J = []
    plist = []
    nlist = []
    score = 0

    for i in L:
      J.append(i.strip())
    
    for i in J[4782:]:
      plist.append(i)
    for i in J[:4782]:
      nlist.append(i)

    for i in string_split:
      if i in plist:
        score = score + 1

    for i in string_split:
      if i in nlist:
        score = score - 1
      if i == 'not':
        count = 1
        break
      
    new_dict = {}
    new_dict['text'] = string
    new_dict['sentiment'] = 0
    if score < 0:
      new_dict['sentiment'] = -1
    elif score > 0:
      new_dict['sentiment'] = 1
    elif score == 0:
      new_dict['sentiment'] = 0
    
    return new_dict

F1 = open("negative-words.txt")
F2 = open("positive-words.txt")
diction = {}

s = SentimentLexicon(diction,F1,F2)
Read = s.reader(F1,F2)

cl = Classifier(Read,"I love Python.")
q = cl.classify("I love Python.")
print(q)