from abc import ABC, abstractmethod


class Comparable():

    __num_compares = 0 
        
    @abstractmethod     
    def compare(object):
        Comparable.__num_compares += 1
    
    @classmethod
    def get_num_compares(cls):
        return Comparable.__num_compares
    
    @classmethod
    def clear_compares(cls):
        Comparable.__num_compares = 0
