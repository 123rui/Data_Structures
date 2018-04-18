"""
搜索算法  python
杨锐  2018-4-17
无序列表    顺序查找    O(n)
有序列表    二分查找    O(logn)
有序列表    插值查找    波动较大，最坏情况为O(n)
散列        Hash查找   O(1)    对于python直接构建dict即可
"""


def sequential_search(lis,key):
    """
    顺序查找
    :param lis: list 待查找列表
    :param key: value  待查找值
    :return: i 最左端key值对应索引，若无返回None
    """
    length = len(lis)
    for i in range(length):
        if lis[i] == key:
            return i
    return None


def binSearch(lis,key):
    return binSearch_heaper(lis,key,0,len(lis))

def binSearch_heaper(lis,key,start,sentry):
    """
    二分查找
    :param lis: list  待查找有序列表
    :param key: value   待查找值
    :param start: 列表中开始查找的索引
    :param sentry: 列表中结束查找的索引的后一位
    :return: 列表中小于等于key中最靠右的元素的索引
    注意：该函数并非返回key的索引，如需查找是否存在某元素需在函数外再比较
    """
    while start < sentry:
        middle = ( start + sentry )//2  #除2取整
        if key < lis[middle]:
            sentry = middle
        else:
            start = middle + 1
    return start-1



def Interpolation_Search(list_1,obj):
    return Interpolation_Search_Heaper(list_1,obj,0,len(list_1)-1)

def Interpolation_Search_Heaper(list_1,obj,start,end):
    """
    插值查找(假设均匀随机分布)
    :param list_1: list 待查找列表
    :param obj: value  待查找值
    :param start: 查找开始索引
    :param end: 查找结束索引
    :return: 列表中小于等于key中最靠右的元素的索引
    注意：该函数并非返回key的索引，如需查找是否存在某元素需在函数外再比较
    """
    mid = int(start + (end-start)*(obj-list_1[start])/(list_1[end]-list_1[start]))
    if mid >= end:     #防止默认条件不成立
        return end
    if mid < start:
        return -1
    while mid>=start:
        if obj<list_1[mid]:
            end = mid - 1
        else :
            start = mid +1
        if start<end:
            mid = int(start + (end-start)*(obj-list_1[start])/(list_1[end]-list_1[start]))
        elif start == end :
            if obj<list_1[start]:
                return start-1
            else :
                return start
        else:
            return start-1
    return start-1
