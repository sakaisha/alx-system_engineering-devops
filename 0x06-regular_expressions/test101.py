#!/usr/bin/python3
import re

def check_regex_match(pattern):
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dic = {'i0': 0, 'i1': 0, 'i2': 0, 'i3': 0}
    y = 0
    temp_lis = ['A', 'A', 'A', 'A']
    cpy_lis = []
    row = []
    while 1:
        temp_lis[0] = string[dic['i0']]
        temp_lis[1] = string[dic['i1']]
        temp_lis[2] = string[dic['i2']]
        temp_lis[3] = string[dic['i3']]
        temp_str = "".join(temp_lis)
        if re.fullmatch(pattern, temp_str):
            cpy_lis = [el for el in temp_lis]
            row += [cpy_lis]
        if dic['i0'] == 25 and dic['i1'] == 25 and dic['i2'] == 25 and dic['i3'] == 25:
            break
        elif dic['i0'] == 25 and dic['i1'] == 25 and dic['i2'] == 25:
            dic['i3'] += 1
            dic['i0'] = 0
            dic['i1'] = 0
            dic['i2'] = 0
        elif dic['i0'] == 25 and dic['i1'] == 25:
            dic['i2'] += 1
            dic['i1'] = 0
            dic['i0'] = 0
        elif dic['i0'] == 25:
            dic['i1'] += 1
            dic['i0'] = 0
        else:
            dic['i0'] += 1
        y += 1
    return(row)

def check_regex_match_ver_col(pat_lis, matrix):
    y = 0
    temp_lis = ['A', 'A', 'A', 'A']
    cpy_lis = []
    row = []
    i = 0
    while i < 4:
        temp_lis[0] = matrix[0][i]
        temp_lis[1] = matrix[1][i]
        temp_lis[2] = matrix[2][i]
        temp_lis[3] = matrix[3][i]
        temp_str = "".join(temp_lis)
        pat_check = pat_lis[i]
        if re.fullmatch(pat_check, temp_str) == None:
            return False
        i += 1
    return True

def combination_maker(pat_lis, matrix_3D):
    j0 = 0
    j1 = 0
    j2 = 0
    j3 = 0
    l0 = len(matrix_3D[0])
    l1 = len(matrix_3D[1])
    l2 = len(matrix_3D[2])
    l3 = len(matrix_3D[3])
    y = 0
    while 1:
        temp_2D_mat = []
        temp_2D_mat += [matrix_3D[0][j0]]
        temp_2D_mat += [matrix_3D[1][j1]]
        temp_2D_mat += [matrix_3D[2][j2]]
        temp_2D_mat += [matrix_3D[3][j3]]
        if check_regex_match_ver_col(pat_lis, temp_2D_mat) == True:
            print(temp_2D_mat)
            break
        if j0 == l0 - 1 and j1 == l1 - 1 and j2 == l2 - 1 and j3 == l3 - 1:
            break
        elif j0 == l0 - 1 and j1 == l1 - 1 and j2 == l2 - 1:
            j3 += 1
            j0 = 0
            j1 = 0
            j2 = 0
        elif j0 == l0 - 1 and j1 == l1 - 1:
            j2 += 1
            j0 = 0
            j1 = 0
        elif j0 == l0 - 1:
            j1 += 1
            j0 = 0
        else:
            j0 += 1
        # y += 1

patR1 = "R+D"
patR2 = "[^WORK]*ING?"
patR3 = ".*[IN].*"
patR4 = "C{0}N[NECT]*"
# patC1 = "RAIN"
# patC2 = "RIAC"
# patC3 = "RNAC"
# patC4 = "DGAC"
patC1 = ".(LN|K|D)*"
patC2 = "([MBERS]*)\1"
patC3 = "(ENG|INE|E|R)"
patC4 = "[LINKED]*IN"

matrix = []
matrix += [check_regex_match(patR1)]
matrix += [check_regex_match(patR2)]
matrix += [check_regex_match(patR3)]
matrix += [check_regex_match(patR4)]

pat_lis = [patC1, patC2, patC3, patC4]
combination_maker(pat_lis, matrix)
