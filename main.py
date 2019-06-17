from createFun import *
from IsSDFun import *
import wx
import random,math

createSD()   #创建数独矩阵 return matrix
print("完整矩阵")
print_grid(matrix)
#matrix1用于储存残缺矩阵,赋初值0;  matrix2用于作改变的中间矩阵
#matrix2和matrix1设置一样的初值，但是直接matrix2=matrix1，因为这样赋值是指针赋值，更改一个时另一个也变化
matrix1=[]
matrix2=[]
for i in range(9):
    matrix1.append([0] * 9)
    matrix2.append([0] * 9)
n=70    #设置显示个数
t=0
while t<n:
    i=random.randint(0,8)
    j=random.randint(0,8)
    if matrix1[i][j]==0:
        matrix1[i][j]=matrix[i][j] #从matrix中给matrix1对应位置赋值
        matrix2[i][j]=matrix[i][j]
        t+=1
print("残缺矩阵")
print_grid(matrix1)
#生成一个字典保存文本框对象，以（0到80）为键，81个文本框对象为值，
#用于残缺矩阵和窗口文本框之间传值
dic={}

class Frame1(wx.Frame):
    def __init__(self,superior):
        wx.Frame.__init__(self,parent=superior,title="数独",size=(800,600))
        panel=wx.Panel(self)
        
        for i in range(9):   #循环显示出matrix1,并给字典赋值
            for j in range(9):
                dic[i*9+j]=wx.TextCtrl(panel,value=str(matrix1[i][j]),pos=(55*j,55*i),size=(50,50),style=wx.TE_CENTER)
        #dic[0].SetValue("10")
        #print(dic[0].GetValue())
        #print(dic)
        self.btnCS=wx.Button(parent=panel,label=u"测  试",pos=(600,100),size=(100,30))
        self.btnCL=wx.Button(parent=panel,label=u"重  来",pos=(600,150),size=(100,30))
        self.TSText=wx.TextCtrl(parent=panel,pos=(550,250),size=(200,200))
        #按钮点击事件绑定函数
        self.Bind(wx.EVT_BUTTON,self.CS,self.btnCS)
        self.Bind(wx.EVT_BUTTON,self.CL,self.btnCL)
    def CS(self,event):
        for i in range(9):   #循环用把文本框的内容赋值给matrix2
            for j in range(9):
                matrix2[i][j]=eval(dic[i*9+j].GetValue())
        flag,ts=isSD(matrix2)
        self.TSText.SetValue(ts)
        
    def CL(self,event):
        for i in range(9):   #循环显示出matrix1，并给字典赋值
            for j in range(9):
                num=matrix1[i][j]
                dic[i*9+j].SetValue(str(num))
        

if __name__=="__main__":
    app=wx.App()
    frame=Frame1(None)
    frame.Show()
    app.MainLoop()
