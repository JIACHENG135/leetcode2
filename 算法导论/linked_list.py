# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 21:11:53 2018

@author: ljc
"""

class Node(object):
    def __init__(self,data,pnext=None):
        self._next = pnext
        self.data = data
    def __repr__(self):
        return str(self.data)
class linked_list(object):
    def __init__(self):
        self.head=None
        self.length = 0
    def __str__(self):
        str_init = ''
        if not self.isEmpty():
            node = self.head
            while node._next:
                str_init += str(node.data)
                str_init += '-->'
                node = node._next
        str_init += str(node.data)
        return str_init
    def isEmpty(self):
        return self.length ==0
    def append(self,dataOrnode):
        item = None
        if isinstance(dataOrnode,Node):
            item = dataOrnode
        else:
            item = Node(dataOrnode)
            
        if not self.head:
            self.head = item
            self.length+=1
        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = item
            self.length +=1 
            
    def insert(self,dataOrnode,index):
        if self.isEmpty():
            print('Linked list is already empty now initialize')
            self.__init__()
        if index>self.length or index<0:
            print('index error')
        else:
            item = None
            if isinstance(dataOrnode,Node):
                item = dataOrnode
            else:
                item = Node(dataOrnode)
            if index == 0:
                head = self.head
                item._next = head
                self.head = item
                self.length += 1

            else:
                counter = index-1
                node = self.head
                self.length += 1
                
                while counter>0:
                    node = node._next
                    counter -=1
                node_next = node._next
                item._next = node_next
                node._next = item
    def delete(self,index):
        if self.isEmpty():
            print('Linked list is empty')
        elif index == 0:
            node = self.head._next
            self.head = node
        elif index>=self.length or index<0:
            print('index too big or small')
        else:
            node = self.head
            while index-1>0:
                node = node._next
                index -= 1
            node_next = node._next
            node._next = node_next._next
            
        
        
            
            
if __name__ == '__main__':
    first_list = linked_list()
#    first_list.insert(20,0)
    first_list.append(60)
    first_list.append(80)
    first_list.insert(70,first_list.length)
    print(first_list)
    print(first_list.length)
    first_list.delete(3)
    
    print(first_list)
    a = first_list.head
#    print(first_list,first_list.head.data)
    
    
            
                
                
            
            
            
            
            
            