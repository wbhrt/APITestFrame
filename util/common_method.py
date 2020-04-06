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
if __name__ == '__main__':
    list = [1,2,7,8,9,4]
    num = func(list)
    print(num)

