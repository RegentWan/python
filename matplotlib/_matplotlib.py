# coding=utf-8
from matplotlib import pyplot as plt
from matplotlib import  font_manager

x=[x for x in range(1,12)]
y=[i**2 for i in x]
y2=[100/i for i in x]

# 中文字体
myfont=font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")

plt.figure(dpi=80,figsize=(10,8))
# plt.title("fig1.1")
plt.title("这是一个中文标题",fontproperties=myfont)
plt.xlabel('x')
xtick=["{}m".format(i) for i in x]
plt.xticks(x[::2],xtick[::2])
plt.xticks(rotation=45)
plt.ylabel('y')
plt.grid(alpha=0.5)

plt.plot(x,y,label='x^2的图像',color='r',linestyle='--',linewidth=5,alpha=0.6)
plt.plot(x,y2,label='100/x的图像')
plt.legend(prop=myfont,loc="upper center")
# plt.savefig("plt.jpg")
plt.show()