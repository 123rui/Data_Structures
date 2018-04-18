"""
有序列表去重  python
杨锐  2018-4-17
根据顺序表与链表两种结构的差异使用不同的方式
"""

def uniquify(lis):
    return uniquify_heaper(lis,0,len(lis)-1)

def uniquify_heaper(lis,start,end):
    """
    有序列表去重(使用修改数据而不是删除数据)
    :param lis: 待去重有序列表
    :param start: 去重初始索引
    :param end: 去重结束索引
    :return: 去重后列表(从start开始)
    """
    current = start
    j = start + 1
    while j <= end:
        if lis[current] == lis[j]:
            pass
        else:
            current += 1
            lis[current] = lis[j]
        j += 1
    return lis[start,current+1]