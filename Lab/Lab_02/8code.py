# 人工智能引论作业：宽度优先搜索探索九宫格走法
# 在最后一层的最后一个节点，达到了目标状态
# python==3.7.3
# matplotlib==3.1.0
# numpy==1.16.4

import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy as dp
# 用于matplotlib正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']

# 矩阵标签的像素大小。
lableSize = 8

# 获取0的位置，即空的位置


def getZeroPosition(twoArray):
    for i in range(len(twoArray)):
        for k in range(len(twoArray[i])):
            if twoArray[i][k] == 0:
                return i, k

# 进行0（空位置）与其他位置的交换：操作符/算子定义


def zeroUp(myArray):
    zero_x, zero_y = getZeroPosition(myArray)
    t = myArray[zero_x-1][zero_y]
    myArray[zero_x-1][zero_y] = 0
    myArray[zero_x][zero_y] = t


def zeroDown(myArray):
    zero_x, zero_y = getZeroPosition(myArray)
    # print(zero_x,zero_y)
    t = myArray[zero_x+1][zero_y]
    myArray[zero_x+1][zero_y] = 0
    myArray[zero_x][zero_y] = t


def zeroRight(myArray):
    zero_x, zero_y = getZeroPosition(myArray)
    t = myArray[zero_x][zero_y+1]
    myArray[zero_x][zero_y+1] = 0
    myArray[zero_x][zero_y] = t


def zeroLeft(myArray):
    zero_x, zero_y = getZeroPosition(myArray)
    t = myArray[zero_x][zero_y-1]
    myArray[zero_x][zero_y-1] = 0
    myArray[zero_x][zero_y] = t


# 初始状态
beginData = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
# 目标状态
endData = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

# 矩阵建立坐标系：坐标原点在矩阵的左上角，以纵向为x轴，横向为y轴。
# 节点层次
level = 1
# open表
lineList = [(beginData, level)]
# closed表
reList = []
# 主循环：open表不空
while lineList != []:
    # 避免同层次矩阵重复
    if lineList[0] in reList:
        del lineList[0]
        continue
    else:
        # 获得当前节点信息
        thisArray = lineList[:][0][0]
        level = lineList[0][1]
        zero_x, zero_y = getZeroPosition(thisArray)
        # 进行4项可能移动，将新节点加入open表尾部
        if zero_x != 2:
            timely = dp(thisArray)
            zeroDown(timely)
            lineList.append((timely, level+1))

        if zero_x != 0:
            timely = dp(thisArray)
            zeroUp(timely)
            lineList.append((timely, level+1))
        if zero_y != 2:
            timely = dp(thisArray)
            zeroRight(timely)
            lineList.append((timely, level+1))
            # reList.append((thisArray,level+1))
        if zero_y != 0:
            timely = dp(thisArray)
            zeroLeft(timely)
            lineList.append((timely, level+1))
            # reList.append((thisArray,level+1))
        # 加入closed表
        reList.append(lineList[0])
        # 目标状态判定
        if lineList[0][0] == endData:
            break
        # print(lineList)
        # 删除当前节点
        del lineList[0]
# 两个函数用于得到合适的在图上显示的x坐标


def getXList(array):
    oldLevel = 1
    times = 0
    xList = []
    for i in range(len(array)):
        nowLevel = array[i][1]
        if nowLevel == oldLevel:
            times += 1
        else:
            xList.append(times)
            times = 1
            oldLevel = nowLevel
    xList.append(times)
    return xList


def getXEList(array):
    xEList = []
    for i in array:
        for k in range(i):
            xEList.append(20/(i+1)*(k+1))
    return xEList


plt.xlim(xmax=22, xmin=0)
plt.ylim(ymax=7, ymin=0)
plt.xlabel('同层次节点个数 ')
plt.ylabel('层次')
t = getXList(reList)
# x,y存储节点位置，lable存储字符串化矩阵
x = getXEList(t)
y = []
lable = []
for i in reList:
    y.append(7-i[1])
    strArray = str(i[0])
    lable.append(strArray[0:11]+'\n'+strArray[11:22]+'\n'+strArray[22:])
    # lable.append("[1,3]")
# 绘制节点
plt.scatter(x, y, s=3)
# 为节点添加标签
for i in range(len(x)):
    plt.annotate(lable[i], xy=(x[i], y[i]), size=lableSize)
plt.show()
