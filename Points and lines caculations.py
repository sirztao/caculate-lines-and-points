# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 17:27:28 2018

@author: tao
"""
"""
已知两点，求过两点直线的方程。已知第三点，求第三点到直线的距离，过第三点与此点的垂线、平行线方程。以及垂足
已知两点为(x1，y1),(x2，y2)第三点为(x0,y0)
输出以上所有结果
k为斜率
"""
import csv
import math
fo=open('C:\work\直线距离垂足问题.txt','w')
varys=[]
i=0
#数据格式要求，前四个数据为确定直线的数据，最后两个数据为直线外一点
with open('C:\work\data\pdata2.txt','r',encoding='utf-8') as foo:
    datas=csv.reader(foo,dialect="excel-tab")
    for data in datas:
        for da in data:
            varys.append(float(da))
            i+=1
x1=varys[0]
y1=varys[1]
x2=varys[2]
y2=varys[3]
x0=varys[4]
y0=varys[5]
if abs(y2-y1)<=1E-5:
    A=0
    B=1
    C=-y1
    k=0
    if -y1>=0:    
        fo.write('直线方程为:\n y'+'+'+str(-y1)+'=0\n')
    else:
        fo.write('直线方程为: \ny'+'-'+str(y1)+'=0\n')
elif abs(x2-x1)<=1E-5:
    A=1
    B=0
    C=-x1
    if -x1<=0:       
        fo.write('直线方程为: \nx'+'-'+str(x1)+'=0\n')
    else:
        fo.write('直线方程为: \nx'+'+'+str(-x1)+'=0\n')
else:
    k=(y2-y1)/(x2-x1)
    A=-k
    B=1
    C=-y1+k*x1
    print('直线方程为:'+str(A)+'x'+'+'+str(B)+'y'+str(C)+'=0')
    fo.write('直线方程为:\n'+str(A)+'x'+'+'+str(B)+'y'+'+'+str(C)+'=0\n')
#定点到此直线的距离
d=abs(A*x0+B*y0+C)/math.sqrt(A*A+B*B)
print('此点到直线的距离为',d)
#垂线方程
if k==0:
   A0=1
   B0=0
   C0=-x0
else:
    A0=1/k
    B0=1
    C0=-y0-x0/k
print('垂线方程为：\n',str(A0)+'x+'+str(B0)+'y+'+str(C0)+'=0\n')
fo.write('垂线方程为：\n'+str(A0)+'x+'+str(B0)+'y+'+str(C0)+'=0\n')
#平行线
fo.write('平行线方程为:\n'+str(A)+'x'+'+'+str(B)+'y'+'+'+str(k*x0-y0)+'=0\n')
#求垂足
x3=(B*B*x0-A*B*y0-A*C)/(A*A+B*B)
y3=(-A*B*x0+A*A*y0-B*C)/(A*A+B*B)
print('垂足坐标为:\n（',x3,',',y3,')')
fo.write('此点到直线的距离为：\n'+str(d)+'\n')
fo.write('垂足坐标为:\n（'+str(x3)+','+str(y3)+')\n')
#求到左端点距离，x2和y2都要改为x1和y1
s1=math.sqrt(math.pow((x3-x2),2)+math.pow((y3-y2),2))
print(s1)
fo.write('左端点到垂足的距离为：\n'+str(s1)+'\n')
fo.close()
