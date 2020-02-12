# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 17:49:05 2020

@author: Rajiv
"""

class Repeater2:
    def __init__(self, value):
        self.value = value
    
    def __iter__(self):
        return RepeaterIterator(self)
    



class Repeater:
    def __init__(self, value):
        self.value = value
        
    def __iter__(self):
        return RepeaterIterator(self)
    
class RepeaterIterator:
    def __init__(self, source):
        self.source = source
        
    def __next__(self):
        return self.source.value
    
repeater = Repeater2("hello")
for item in repeater:
    print(item)