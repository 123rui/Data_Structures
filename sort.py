"""
排序算法  python
杨锐  2018-4-18
起泡排序    O(n2)
选择排序    O(n2)
归并排序    O(nlogn)
快速排序    O(nlogn)
堆排序      O(nlogn)
"""

###冒泡排序
def bubblingSort(lis):
    bubblingSort_Heaper(lis,0,len(lis)-1)

def bubblingSort_Heaper(lis,start,end):
    """
    冒泡排序-从小到大（加入序列后段排序好后下次无需比较的优化）
    :param lis: list 待排序列表
    :param start: 排序开始索引
    :param end: 排序结束索引
    :return: None
    """
    stern = end  #stern指向待排序部分尾部，其后已排序完成
    label = stern  #标记每次冒泡过程最后一次交换，作为下一次冒泡的stern
    while start < stern:
        current = start  #每轮冒泡初始化current和label
        label = current
        while current < stern:
            if lis[current+1] < lis[current]:
                lis[current+1],lis[current] = lis[current],lis[current+1]
                label = current
            current += 1
        stern = label


###选择排序
def selectionSort(lis):
    selectionSort_Heaper(lis,0,len(lis)-1)

def selectionSort_Heaper(lis,start,end):
    """
    选择排序，针对列表结构做交换不做删除插入。需要调用求最函数
    :param lis: 待排序列表
    :param start: 排序开始索引
    :param end: 排序结束索引
    :return: None
    """
    stern = end
    while start < stern:
        max_1 = selectionMax(lis,start,stern)
        lis[max_1],lis[stern] = lis[stern],lis[max_1]
        stern -= 1

def selectionMax(lis,start,end):
    """
    顺序遍历寻找列表中最大元素
    :param lis: 待排序列表
    :param start: 排序开始索引
    :param stern: 排序结束索引
    :return: 最大大元素索引
    """
    maxValue = lis[start]   #初始化最大值与索引
    maxIndex = start
    while start <  end:
        start += 1
        if maxValue <= lis[start]:
            maxValue = lis[start]
            maxIndex = start
    return maxIndex


###归并排序
def mergeSort(lis):
    mergeSort_Heaper(lis,0,len(lis)-1)

def mergeSort_Heaper(lis,start,end):
    """
    并归排序
    :param lis:  待排序列表
    :param start:   列表开始
    :param end: 列表结束
    :return: None
    """
    if end-start<=0:    #支持输入长度为0和1的list
        return
    if end-start<=2 :
        if list_1[start+1]>list_1[end]:     #保证传入都为有序序列
            list_1[start+1],list_1[end] = list_1[end],list_1[start+1]
        merge(list_1,start,start,end)
    mid = (start+end)//2
    mergeSort_Heaper(list_1,start,mid)
    mergeSort_Heaper(list_1,mid+1,end)
    merge(lis,start,mid,end)


def merge(lis,start,mid,end):
    """
    二路归并，list中顺序的两个部分[start:mid+1],[mid+1:end+1]合并为一个顺序list
    :param lis: 待排序列表
    :param start: 列表开始
    :param mid: 列表中间
    :param end: 列表结尾
    :return: None
    """
    listA = lis[start:mid+1]  #开辟一个缓存区存放[start:mid+1]部分数据
    lengthA = len(listA)
    pointerA = 0  #指向listA排到节点
    pointerB = mid + 1  #指向lis[mid+1:end+1]区域已排到节点
    #start指向归并到的节点
    while pointerA < lengthA and pointerB <= end :  #重复至某一个区域放完
        if listA[pointerA] <= lis[pointerB] :  #等号保证重复元素在右边的一直在右边
            lis[start] = listA[pointerA]
            start += 1
            pointerA += 1
        else:
            lis[start] = lis[pointerB]
            start += 1
            pointerB += 1
    #A区域先放完已排序完成，若B区域先放完还需将A区域后续部分搬至原列表后部
    if pointerB == end + 1:
        lis[start:end+1] = listA[pointerA:lengthA]

###快速排序
def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)

def quick_sort_helper(a_list, first, last):
    """
    快速排序
    :param a_list: 待排序列表
    :param first: 排序开始索引
    :param last: 排序结束索引
    :return: None
    """
    if first < last:
        split_point = partition(a_list, first, last)  #列表变为有序的三部分，[first:split_point]小于[split_point],
                                                      #[split_point+1:last+1]大于[split_point],
        quick_sort_helper(a_list, first, split_point - 1)
        quick_sort_helper(a_list, split_point + 1, last)

def partition(a_list, first, last):
    pivot_value = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp
    temp = a_list[first]
    a_list[first] = a_list[right_mark]
    a_list[right_mark] = temp
    return right_mark

###堆排序
import heapq

def heapdSort(lis):
    """
    堆排序  ***注意该函数返回的是排序后列表，原list将会变空
    :param lis: list 待排序列表
    :return: list 排序完成列表
    """
    heapq.heapify(lis)  #建堆
    return [heapq.heappop(lis) for i in range(len(lis))]

if __name__ == '__main__':
    #冒泡排序
    list_1 = [442,2,5465,7634,23,6,7,78,3,31,4,5,2,3,3]
    bubblingSort(list_1)
    print("冒泡排序测试：",list_1)

    #选择排序
    list_1 = [442, 2, 5465, 7634, 23, 6, 7, 78, 3, 31, 4, 5, 2, 3, 3]
    selectionSort(list_1)
    print("选择排序测试：",list_1)

    #二路归并
    list_1 = [2,3,3,4,10,29,1,1,5,8,13,21]
    merge(list_1,0,5,11)
    print("二路归并测试：",list_1)

    #并归排序
    list_1 = [442, 2, 5465, 7634, 23, 6, 7, 78, 3, 31, 4, 5, 2, 3, 3]
    mergeSort(list_1)
    print("并归排序测试：",list_1)

    #快速排序
    list_1 = [442, 2, 5465, 7634, 23, 6, 7, 78, 3, 31, 4, 5, 2, 3, 3]
    quick_sort(list_1)
    print("快速排序测试：",list_1)

    #堆排序
    list_1 = [442, 2, 5465, 7634, 23, 6, 7, 78, 3, 31, 4, 5, 2, 3, 3]
    list_1 = heapdSort(list_1)
    print("堆排序测试：",list_1)