from tkinter import *
from tkinter import font
import random



class Calculator(Tk):
    def __init__(self,name):
        super().__init__()   #create Tk object
        self.title(name)
        self.geometry("500x498")
        self.addButtons()

    def generaterandomcolors(self):
        COLORS = [
                  'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
                  'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
                  'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
                  'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
                  'indian red', 'saddle brown', 'sandy brown',
                  'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
                  'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
                  'pale violet red', 'maroon', 'medium violet red', 'violet red',
                  'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
                  'thistle', 'snow2', 'snow3',
                  'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
                  'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
                  'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
                  'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
                  'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
                  'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
                  'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
                  'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
                  'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
                  'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
                  'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2']
        color=random.choices(COLORS,k=15)

        return color






    def addButtons(self):
        pdx="50"
        pdy="30"


        color=self.generaterandomcolors()
        print(color)
        myfont=font.Font(family="Arial Black",size=10,weight="bold")
        user_inp=Text(self,width=50,height=3,borderwidth=5,font=myfont)
        user_inp.grid(row=0,column=0,columnspan=4)

        def Button_clicked(num):
            global sign
            if num != "=":
                user_inp.insert(END,num)
            wholenum=user_inp.get("1.0",END).strip()
            if num == "*" or num=="+" or num=="/" or num=="-":
                sign = str(num)
                print(sign)
            if str(num) == "=":
                Calculation(wholenum)

        def findastr(searchstr,value): #bruteforce search algorithm
            i = 0
            j = 0
            while i <= len(searchstr) - len(value):
                while j < len(value):
                    if searchstr[i + j] == value[j]:
                        j = j + 1
                    else:
                        j = 0
                        break

                if j == len(value):
                    return i
                    break
                else:
                    i = i + 1
        def Calculation(wholenum):
            index = findastr(wholenum, sign)
            myfirstnum = wholenum[:index]
            mysecondnum = wholenum[index + 1:]
            x1 = "".join(myfirstnum)
            x2 = "".join(mysecondnum)
            if sign == "+":
                user_inp.delete("1.0", END)
                result = int(x1) + int(x2)
                user_inp.insert(END, result)
            elif sign == "*":
                user_inp.delete("1.0", END)
                result = int(x1) * int(x2)
                user_inp.insert(END, result)
            elif sign=="/":
                user_inp.delete(1.0,END)
                result = int(x1) / int(x2)
                user_inp.insert(END, result)
            else:
                user_inp.delete(1.0, END)
                result = int(x1) - int(x2)
                user_inp.insert(END, result)








































        #create buttons

        button0=Button(self,text="0",padx=pdx,pady=pdy,bg=color[0],command=lambda:Button_clicked(button0.cget("text")))
        button0.grid(row=1, column=0)
        button1=Button(self,text="1",padx=pdx,pady=pdy,bg=color[1],command=lambda:Button_clicked(button1.cget("text")))
        button1.grid(row=1,column=1)
        button2=Button(self,text="2",padx=pdx,pady=pdy,bg=color[2],command=lambda:Button_clicked(button2.cget("text")))
        button2.grid(row=1,column=2)
        button3=Button(self,text="3",padx=pdx,pady=pdy,bg=color[3],command=lambda:Button_clicked(button3.cget("text")))
        button3.grid(row=1,column=3)
        button4=Button(self,text="4",padx=pdx,pady=pdy,bg=color[4],command=lambda:Button_clicked(button4.cget("text")))
        button4.grid(row=2,column=0)
        button5=Button(self,text="5",padx=pdx,pady=pdy,bg=color[5],command=lambda:Button_clicked(button5.cget("text")))
        button5.grid(row=2,column=1)
        button6=Button(self,text="6",padx=pdx,pady=pdy,bg=color[6],command=lambda:Button_clicked(button6.cget("text")))
        button6.grid(row=2,column=2)
        button7=Button(self,text="7",padx=pdx,pady=pdy,bg=color[7],command=lambda:Button_clicked(button7.cget("text")))
        button7.grid(row=2,column=3)
        button8=Button(self,text="8",padx=pdx,pady=pdy,bg=color[8],command=lambda:Button_clicked(button8.cget("text")))
        button8.grid(row=3,column=0)
        button9=Button(self,text="9",padx=pdx,pady=pdy,bg=color[9],command=lambda:Button_clicked(button9.cget("text")))
        button9.grid(row=3,column=1)
        buttonplus=Button(self,text="+",padx=pdx,pady=pdy,bg=color[10],command=lambda:Button_clicked(buttonplus.cget("text")))
        buttonplus.grid(row=4,column=0)
        buttonminus=Button(self,text="-",padx=pdx,pady=pdy,bg=color[11],command=lambda:Button_clicked(buttonminus.cget("text")))
        buttonminus.grid(row=4,column=1)
        buttondiv=Button(self,text="/",padx=pdx,pady=pdy,bg=color[12]).grid(row=4,column=2)
        buttonmulti=Button(self,text="*",padx=pdx,pady=pdy,bg=color[13],command=lambda:Button_clicked(buttonmulti.cget("text")))
        buttonmulti.grid(row=4,column=3)
        buttonequa=Button(self,text="=",padx="110",pady=pdy,relief='solid',bg=color[14],command=lambda:Button_clicked(buttonequa.cget("text")))
        buttonequa.grid(row=5,column=0,columnspan=2)












calcul=Calculator("calculator")
calcul.mainloop()

