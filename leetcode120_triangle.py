# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 09:58:24 2018

@author: ljc
"""

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
#        index = 1
#        height = 1
        
        
        def get_min(triangle):
            min_sum = triangle[0][0]
#            index = 0
            if len(triangle) == 1:
                return min_sum
#            for i in range(1,len(triangle)):
#                if triangle[i][index]>triangle[i][index+1]:
#                    index = index
#                else:
#                    index = index + 1
#                min_sum = min_sum + min(triangle[i])
            new_tree_1 = gene_tree(triangle,1,0)
            new_tree_2 = gene_tree(triangle,1,1)
            res_1 =  min_sum + get_min(new_tree_1)
            res_2 = min_sum + get_min(new_tree_2)
            return min(res_1,res_2)
        
        
        
        def gene_tree(triangle,height,index):
            new_tree = []
            counter = 1
            for i in range(height,len(triangle)):
                new_tree.append(triangle[i][index:index + counter])
                counter += 1
            return new_tree
        return get_min(triangle)


a = Solution()
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
b = a.minimumTotal(triangle)
print(b)