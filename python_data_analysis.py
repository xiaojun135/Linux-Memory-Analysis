import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#from ctypes import *

#定义读取文件函数
def read_data(file_path):
    #columa_names所有列表的名称
    column_names = ['label',
     'cpu_minute_average_load_x_one','one_minute_data',
     'cpu_minute_average_load_x_five','five_minute_data',
     'cpu_minute_average_load_x_fifty', 'fifty_minute_data',
     'sysMemUse_x', 'sysMemUse_data',
     'sysMemFree_x', 'sysMemFree_data',
     'processMemUse_x', 'processMemUse_data',
     'processMemFree_x', 'processMemFree_data']
    data = pd.read_csv(file_path,header = None, names = column_names)

    return data

#画图线性图
def cpu_average_load_line_plot(x1,y1,x2,y2,x3,y3,figure_no):
    plt.figure(figure_no)
    plt.plot(x1,y1,color='red',alpha=1.00)
    plt.plot(x2,y2,color='blue',alpha=1.00)
    plt.plot(x3,y3,color='green',alpha=1.00)

  #  plt.xlabel('x values')
  #  plt.ylabel('y values')
    plt.xlabel('one_minute_data Red;five_minute_data Blue;fifty_minute_data Green')
    plt.ylabel('cpu_average_load values')

    plt.title('cpu_average_load_line_plot')

def Memery_sysMemUse_line_plot(x4,y4,figure_no):
    plt.figure(figure_no)
    plt.plot(x4,y4,color='green',alpha=1.00)

    plt.xlabel('sysMemUse_data Green')
    plt.ylabel('Memery values/Mb')

    plt.title('Memery_sysMemUse_line_plot')

def Memery_sysMemFree_line_plot(x5,y5,figure_no):
    plt.figure(figure_no)
    plt.plot(x5,y5,color='purple',alpha=1.00)

    plt.xlabel('sysMemFree_data Purple')
    plt.ylabel('Memery values/Mb')

    plt.title('Memery_sysMemFree_line_plot')

def Memery_processMemUse_line_plot(x6,y6,figure_no):
    plt.figure(figure_no)
    plt.plot(x6,y6,color='blue',alpha=1.00)

    plt.xlabel('processMemUse_data Blue')
    plt.ylabel('Memery values/Mb')

    plt.title('Memery_processMemUse_line_plot')

def Memery_processMemFree_line_plot(x7,y7,figure_no):
    plt.figure(figure_no)
    plt.plot(x7,y7,color='red',alpha=1.00)

    plt.xlabel('processMemFree_data Red')
    plt.ylabel('Memery values/Mb')

    plt.title('Memery_processMemFree_line_plot')

#调用函数读取数据
#dataset = read_data('data.txt')
dataset = read_data('sysCheckInfo.log')
figure_no=1
x1=dataset['cpu_minute_average_load_x_one']
y1=dataset['one_minute_data']
x2=dataset['cpu_minute_average_load_x_five']
y2=dataset['five_minute_data']
x3=dataset['cpu_minute_average_load_x_fifty']
y3=dataset['fifty_minute_data']

x4=dataset['sysMemUse_x']
y4=dataset['sysMemUse_data']
x5=dataset['sysMemFree_x']
y5=dataset['sysMemFree_data']
x6=dataset['processMemUse_x']
y6=dataset['processMemUse_data']
x7=dataset['processMemFree_x']
y7=dataset['processMemFree_data']

cpu_average_load_line_plot(x1,y1,x2,y2,x3,y3,figure_no)
figure_no+=1
Memery_sysMemUse_line_plot(x4,y4,figure_no)
figure_no+=1
Memery_sysMemFree_line_plot(x5,y5,figure_no)
figure_no+=1
Memery_processMemUse_line_plot(x6,y6,figure_no)
figure_no+=1
Memery_processMemFree_line_plot(x7,y7,figure_no)

plt.show()
