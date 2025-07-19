from heapq import merge
import sys
from tkinter import CURRENT
from turtle import left, right

def mergeSort(nlst):
    print(nlst)
    if(len(nlst) > 1):
        mid = len(nlst) // 2
        lefthalf = nlst[:mid]
        righthalf = nlst[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0
        while(i < len(lefthalf) and j < len(righthalf)):
            if(lefthalf[i] < righthalf[j]):
                nlst[k] = lefthalf[i]
                i = i + 1
            else:
                nlst[k] = righthalf[j]
                j = j + 1
            k = k + 1
        while(i < len(lefthalf)):
            nlst[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while(j < len(righthalf)):
            nlst[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print(nlst)

def shellSort(alist):
    sublistcount = len(alist) // 2
    while(sublistcount > 0):
        for start in range(sublistcount):
            gap_InsertionSort(alist,start,sublistcount)
        print(sublistcount)
        sublistcount = sublistcount // 2

def gap_InsertionSort(nlist,start,gap):
    for i in range(start + gap, len(nlist), gap):
        current_value = nlist[i]
        position = i
        while(position >= gap and nlist[position-gap] > current_value):
            nlist[position] = nlist[position-gap]
            position = position - gap
        nlist[position] = current_value

def insertionSort(nlist):
    for index in range(1,len(nlist),1):
        currentvalue = nlist[index]
        position = index
        while(position > 0 and nlist[position-1] > currentvalue):
            nlist[position] = nlist[position - 1]
            position = position - 1
        nlist[position] = currentvalue

def selectionSort(nlist):
    for fillslot in range(len(nlist)-1,0,-1):
        maxpos = 0
        for location in range(1,fillslot+1,1):
            if(nlist[location] > nlist[maxpos]):
                maxpos = location
        tmp = nlist[fillslot]
        nlist[fillslot] = nlist[maxpos]
        nlist[maxpos] = tmp

def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if(nlist[i] > nlist[i+1]):
                tmp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = tmp


lst = [56,90,34,1,4,56,78,12,34,90,100]

selectionSort(lst)
for j in range(len(lst)):
    print(lst[j], end=' ')
bubbleSort(lst)
print()
for k in range(len(lst)):
    print(lst[k], end=' ')
insertionSort(lst)
print()
for i in range(len(lst)):
    print(lst[i], end=' ')
print()
shellSort(lst)
print(lst, end=' ')
print()
mergeSort(lst)
print(lst, end=' ')
print()


