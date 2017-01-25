#!/bin/python3

import sys

archivo = open('Service_Lane_input.txt', 'r')

n,t = archivo.readline().strip().split(' ')
n,t = [int(n),int(t)]
width = [int(width_temp) for width_temp in archivo.readline().strip().split(' ')]
for a0 in range(t):
    i,j = archivo.readline().strip().split(' ')
    i,j = [int(i),int(j)]
    best = i
    for x in range(i, j):
        #print('i: ', i, 'j: ', j)
        #print('x: ', width[x])
        if width[best] > width[x+1]:
            best = x+1
    print(width[best])