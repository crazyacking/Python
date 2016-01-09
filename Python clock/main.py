#encoding:utf8
from sys import platform
from os import system
from time import sleep,localtime

assert isinstance(pi,object )
from math import sin,cos,pi

clsCmd={'win32':'cls','linux2':'clear','linux':'clear'}[platform] #不同平台下的控制台清屏命令
infill=" "*2 # 背景填充字符
width=39 #点阵宽度(这里将创建一个39x39的点阵)
O=int((width-1)/2) #圆心
r=width/2.0-1 # 半径
drad=pi/180 #1°=pi/180 rad@

while True:
    matrix=[[infill for col in range(width)] for row in range(width)]
    now=localtime()
    h_d=now.tm_hour*30 # 时针与12点钟方向的夹角
    m_d=now.tm_min*6 # 分针与...
    s_d=now.tm_sec*6 # 秒针与...
    # 创建表盘:
    for deg in range(360):
        row=int(cos(deg*drad)*r+O)
        col=int(sin(deg*drad)*r+O)
        matrix[row][col]=str((deg+14)//30).zfill(2)
    # 创建时针:
    for Hr in range(int(r-7)):
        row=int(cos((h_d+m_d/12)*drad)*Hr+O)
        col=int(sin((h_d+m_d/12)*drad)*Hr+O)
        matrix[row][col]=str(now.tm_hour).zfill(2)
    # 创建分针:
    for Mr in range(int(r-5)):
        row=int(cos((m_d+s_d/60)*drad)*Mr+O)
        col=int(sin((m_d+s_d/60)*drad)*Mr+O)
        matrix[row][col]=str(now.tm_min).zfill(2)
    # 创建秒针:
    for Sr in range(int(r-1)):
        row=int(cos(s_d*drad)*Sr+O)
        col=int(sin(s_d*drad)*Sr+O)
        matrix[row][col]=str(now.tm_sec).zfill(2)
    # 点缀表盘中心:
    matrix[O][O]="{}"

    # 最后清屏输出:
    system(clsCmd)
    print('\n'.join(''.join(row) for row in reversed(matrix)))
    sleep(1)

