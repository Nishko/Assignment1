# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:54:49 2019

@author: Rowan
"""
import string
import re
def same(item, target):
    return sum(c == t for c, t in zip(item,target))
#return len([c for (c, t) in zip(item, target) if c == t])


def build(pattern, words, seen, list):
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in list]

#function determines if a users input is valid if it is not valid
#function prints "Invalid Input"
def invalid_input(word):
    for c in word:
        if c.isdigit():
            print("Invalid Input")
            return True
    if has_punctuation(word):
        print("Invalid Input")
        return True
    if len(word) <= 1:
        print("Invalid Input")
        return True
    return False
    
def find(word, words, seen, target, path):
  list = []
  for i in range(len(word)):
    list += build(word[:i] + "." + word[i + 1:], words, seen, list)
  if len(list) == 0:
    return False
  list = sorted([(same(w, target), w) for w in list])
  for (match, item) in list:
    if match >= len(target) - 1:
      if match == len(target) - 1:
        path.append(item)
      return True
    seen[item] = True
  for (match, item) in list:
    path.append(item)
    if find(item, words, seen, target, path):
      return True
    path.pop()

#function determines if the user input has punctuation in it
def has_punctuation(s):
    for c in s:
        for p in string.punctuation:
            if p == c:
                return True
    return False
                
        

#user will enter a directory name
fname = input("Enter dictionary name: ")
#set lines to an empty list
lines = []
#open the file so that the program can access it
with open(fname) as file: 
    lines = file.readlines()
while True:
  start = input("Enter start word:")
#call to function defined at the start
  if invalid_input(start):
     break
  words = []
  for line in lines:
    word = line.rstrip()
    if len(word) == len(start):
      words.append(word)
  target = input("Enter target word:")
#call to function defined at the start
  if invalid_input(target):
      break
  break

count = 0
path = [start]
seen = {start : True}
if find(start, words, seen, target, path):
  path.append(target)
  print(len(path) - 1, path)
else:
  print("No path found")

