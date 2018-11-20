# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 13:50:50 2018

@author: ljc
"""
def spiralOrder(matrix):
    if not matrix:
        return []
    A_keys = ['y','x','z','s'];
    A_bound = [len(matrix[0]),len(matrix),0,0]
    dictA = dict(zip(A_keys,A_bound))
    counter = 0
    key_counter = 0
    numb = len(matrix[0])*len(matrix)
    ans =''
    index_ans = []
    i = 0
    j = 0
    while counter<numb:
        if key_counter%4 == 0:
            while j<dictA[A_keys[key_counter%4]]:
                 ans += matrix[i][j]
                 index_ans.append([i,j])
                 j += 1
                 counter += 1
            key_counter += 1
            i +=1
            j = j-1
            dictA['y'] -= 1
        elif key_counter%4 == 1:
            while i<dictA[A_keys[key_counter%4]]:
                ans += matrix[i][j]
                index_ans.append([i,j])

                i += 1
                counter += 1
            key_counter += 1
            i -= 1
            j -= 1
            dictA['x'] -= 1

        elif key_counter%4 == 2:
            while j>=dictA[A_keys[key_counter%4]]:
                ans += matrix[i][j]
                index_ans.append([i,j])
                j -= 1
                counter += 1
            key_counter += 1
            j += 1
            i -= 1
            dictA['z'] += 1

        elif key_counter%4 == 3:
            while i>dictA[A_keys[key_counter%4]]:
                ans += matrix[i][j]
                index_ans.append([i,j])

                i -= 1
                counter += 1
            key_counter += 1
            i += 1
            j += 1
            dictA['s'] += 1 
    return ans,index_ans


def gene_new_board(matrix,index_m):
    i= index_m[0]
    j = index_m[1]
    if i!=0:
        if j==0:
            red = []
        else:
            red = matrix[i:,0:j]
        if j==matrix.shape[1]-1:
            blue =[]
            green =[]
        else:
            blue = matrix[0:i+1,j+1:]
            green = matrix[i:,j:]
    elif i==0:
        if j==0:
            red = []
        else:
            red = matrix[i+1:,0:j+1]
        if j==matrix.shape[1]-1:
            print('green')
            blue =[]
            green =[]
        else:
            blue = matrix[0:i+1,j+1:]
            green = matrix[i+1:,j:]
    red = list(red)
    blue = list(blue)
    green = list(green)
    red = rotate(rotate(rotate(red)))
    blue = rotate(blue)
    return red,blue,green
#    if not red:
#        red = []
#    elif len(red) ==1:
#        red = red
#    else:
#        red = rotate(rotate(rotate(red)))
#    if not red:
#        blue = []
#    elif len(blue)==1:
#        return blue
#    else:
#        blue = rotate(blue)
    red = rotate(rotate(rotate(red)))
    blue = rotate(blue)
    return red,blue,green
def rotate(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = map(list,zip(*matrix[::-1]))
        return matrix
    

def find_index_head(str_all,str_in,str_con):
#        str_in_len = len(str_in)
    first_ind = str_all.index(str_in[0])
    ans = []
    if type(first_ind)!=int or first_ind !=0:
        return ans
    else:
        i = first_ind
        while i < len(str_all):            
            while str_all[i] == str_in[0]:
                if len(str_in) == 1:
                    if i not in ans:
                        ans.append(i)
                    break
                str_in = str_in[1:]
                i += 1
            str_in = str_con
            i += 1
    return ans
        
def exist_head(board,word):
        matrix = np.array(board)
        matrix_t = matrix.T
        i = 0
        str_can_1 = []
        index_1 = []
        str_can_2 = []
        index_2 = []
        
        
        while i<=matrix.shape[0]:
            j=0
            while j<=matrix.shape[1]:
                if (i+1)*(j+1)>len(word):
#                    print(i,j)

                    [can_temp_1,can_index_1] = spiralOrder(list(matrix[0:i+1,0:j+1]))
                    [can_temp_2,can_index_2] = spiralOrder(list(matrix[0:i+1,0:j+1]))
                    print(i,j,matrix.shape,can_temp_1)

                    for iii in range(len(word)):
                        if word[:len(word)-iii] in can_temp_1:
                            index_need = find_index_head(can_temp_1,word[:len(word)-iii],word[:len(word)-iii])
                            
                            if iii == 0:
                                return True
                            else:
                                for m in index_need:
                                    index_m = can_index_1[m]
                                    print
                                    [new_board_1,new_board_2,new_board_3] = gene_new_board(matrix,index_m)
                                    return exist_head(new_board_1, word[len(word)-iii:])
                                    return exist_head(new_board_2, word[len(word)-iii:])
                                    return exist_head(new_board_3, word[len(word)-iii:])
                    for iii in range(len(word)):
                        if word[:len(word)-iii] in can_temp_2:
                            index_need = find_index_head(can_temp_1,word[:len(word)-iii],word[:len(word)-iii])
                            if iii == 0:
                                return True
                            else:
                                for m in index_need:
                                    index_m = can_index_1[m]
                                    [new_board_1,new_board_2,new_board_3] = gene_new_board(matrix,index_m)
                                    return exist_head(new_board_1, word[len(word)-iii:])
                                    return exist_head(new_board_2, word[len(word)-iii:])
                                    return exist_head(new_board_3, word[len(word)-iii:])
#                        
#str_can_1.append()
#                        str_can_2.append(spiralOrder(list(matrix_t[0:i,0:j])))
                    
                
                
                j+=1
            
            i+=1