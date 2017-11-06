#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Student:
   '学生资料'
   empCount = 1
 
   def __init__(self, name, number,classnumber,gender):
      self.name = name
      self.studentnumber = number
      self.gender = gender
      Student.empCount += 1
      
   def speakFrencg(self):
     print self.name,"can speak French!!!"
 
   def canWriting(self):
      print self.name,"can Wirting!!!"

   def canBadminton(self):
      print self.name,"can Badminton!!!"
