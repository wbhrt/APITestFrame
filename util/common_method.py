#coding:utf-8
import json
from filecmp import cmp

def fun(list,num):
    #二分法
    list = sorted(list)
    low = 0
    right = len(list)
    while low < right:
        mid = int((low + right) / 2)
        if list[mid] > num:
            right = mid-1
        elif list[mid]  < num:
            low = mid+1
        return mid,list[mid]
def func(list):
    #冒泡排序
    n = len(list)
    for i in range(n):
        for j in range(n-1-i):
            if list[j] > list[j+1]:
                list[j],list[j+1]= list[j+1],list[j]
    return list
def is_contain(str1,str2):
    """
    判断一个字符串是否在另一个字符串中
    str1：查找的字符串
    str2:被查找的字符串
    :return:
    """
    flag = None
    # if isinstance(str1,'unicode'):
    #     str1 = str1.encode('unicode-escape').decode('string_escape')

    if str1 in str2:
        flag = True
    else:
        flag = False
    return flag

#判断2个字典是否相等
def is_equal_dic(dic_one,dic_two):
    if isinstance(dic_one,str):
        dic_one = json.loads(dic_one)
    if isinstance(dic_two, str):
        dic_two = json.loads(dic_two)
    cmp(dic_one,dic_two)

#快速排序
def min_location(list,low,high):
    i = low-1
    num = list[high]
    for j in range(low,high):
        if list[j]<=num:
            i = i+1
            list[i],list[j]= list[j],list[i]
    list[i+1],list[high] = list[high],list[i+1]
    return i+1

def fastsort(list,low,high):
    if low < high:
        pi = min_location(list,low,high)
        fastsort(list,low,pi-1)
        fastsort(list, pi+1, high)
 #快速排序
def quicsort(list):
    if len(list) <2:
        return list
    mid = list[len(list) // 2]
    low,high=[],[]
    list.remove(mid)
    for i in list:
        if i >=mid:
            high.append(i)
        else:
            low.append(i)
    return quicsort(low)+[mid]+quicsort(high)
#归并排序
def merge(left,right):
    arr = []
    i=j=0

    while i <len(left) and j <len(right):
        if left[i] <right[j]:
            arr.append(left[i])
            i +=1
        else:
            arr.append(right[j])
            j +=1
    if i == len(left):
        for n in right[j:]:
            arr.append(n)
    else:
        for m in left[i:]:
            arr.append(m)
    return arr
def mergesort(list):
    if len(list) <=1:
        return list
    mid = len(list)//2
    left = mergesort(list[:mid])
    right = mergesort(list[mid:])
    return merge(left,right)
if __name__ == '__main__':
    list = [1,2,7,8,9,4]
    print(mergesort(list))
    # fastsort(list,0,5)
    # for i in list:
    #     print(i)


