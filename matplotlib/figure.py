# coding=utf-8

'''
Author:Regent Wan
Email:wanrunjun@gmail.com
微信公众号：学术创客
Github:https://github.com/RegentWan

Date:2019/8/29 11:19
Desc:
'''

import matplotlib.pyplot as plt

x=[i for i in range(10)]
y=[j**2 for j in x]

# 折线图
# plt.plot(x,y)

# 散点图
# plt.scatter(x,y)

# 纵向条形图
''''''
x=[i for i in range(1,6)]
label=["G{}".format(i) for i in x]
width=0.2
men_x=[i-width for i in x]
women_x=x
other_x=[i+width for i in x]
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
other_means=[23, 22, 44, 40, 35]

plt.bar(men_x,men_means,width=width,label="men")
plt.bar(women_x,women_means,width=width,label="women")
plt.bar(other_x,other_means,width=width,label="other")
plt.xticks(x,label)
plt.legend()


# 横向条形图
'''
height=0.2
x=[i for i in range(3)]
year=[i for i in range(2017,2020)]
print(year)
beijing=[57768,59868,59906]
shanghai=[50017,49446,50420]
guangzhou=[22205,22188,22055]

plt.barh([i-height for i in x],beijing,height=height,label="beijing")
plt.barh(x,shanghai,height=height,label="shanghai")
plt.barh([i+height for i in x],guangzhou,height=height,label="guangzhou")
plt.yticks(range(len(year)),year)
plt.legend()
plt.grid(alpha=0.5)
'''

# 直方图
'''
time=[131,98,125,131,124,139,131,117,128,108,135,138,131,102,107,114,119,128,121,142,127,130,124,101,116,117,110,128,128,115,99,136,126,134,95,138,117,111,78,132,124,113,150,110,117,86,95,144,105,126,130,126,130,126,116,123,106,112,138,123,86,101,99,136,123,117,119,105,137,123,128,125,104,109,134,125,127,105,120,107,129,116,108,132,103,136,118,102,120,114,105,115,132,145,119,121,112,139,125,138,109,132,134,156,106,117,127,144,139,139,119,140,83,110,102,123,107,143,115,136,118,139,123,112,118,125,109,119,133,112,114,122,109,106,123,116,131,127,115,118,112,135,115,146,137,116,103,144,83,123,111,110,111,100,154,136,100,118,119,133,134,106,129,126,110,111,109,141,120,117,106,149,122,122,110,118,127,121,114,125,126,114,140,103,130,141,117,106,114,121,114,133,137,92,121,112,146,97,137,105,98,117,112,81,97,139,113,134,106,144,110,137,137,111,104,117,100,111,101,110,105,129,137,112,120,113,133,112,83,94,146,133,101,131,116,111,84,137,115,122,106,144,109,123,116,111,111,133,150]
binWidth=3
binNum=int((max(time)-min(time))/binWidth)
plt.hist(time,binNum)
plt.xticks((range(min(time),max(time)+binWidth))[::binWidth],rotation=30)
plt.grid(linestyle="-.",alpha=0.5)
'''

# 饼图
'''
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
'''

# 子图
'''
data=[57768,59868,59906]
plt.subplot(1,2,1)
plt.plot(range(len(data)),data)

plt.subplot(1,2,2)
plt.bar(range(len(data)),data)
'''

plt.show()