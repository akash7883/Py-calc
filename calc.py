from Tkinter import *
root=Tk()
root.title("My Calci") # Giving Title of the project
#creating a operation box
en=Entry(root,borderwidth=1)
en.grid(row=0,column=0,padx=2,pady=2,columnspan=3)
# creating a quit button
#button_quit=Button(root,text="EXIT",command=root.quit)
#button_quit.grid(row=1,column=0,ipadx=10,ipady=2)
# defination a func
def solve(num):
    current=en.get()
    en.delete(0,END)
    en.insert(0,str(current)+str(num))
# func for cleaning
def clear():    
     en.delete(0,END)  
# fun to add
def add():
    global f_num
    f_num=en.get()
    global math
    math="Addition"
    en.delete(0,END)
# func to calculate
def calc():   
    second_num=en.get()
    en.delete(0,END)
    if math=="Addition":
        en.insert(0,int(f_num)+int(second_num))  
    if math=="subtraction":
        en.insert(0,int(f_num)-int(second_num)) 
    if math=="Multiplication":
        en.insert(0,int(f_num)*int(second_num)) 
    if math=="division":
        en.insert(0,int(f_num)/int(second_num)) 
    if math=="Squareroot":
        en.insert(0,int(second_num)**0.5) 
    if math=="Cuberoot":
        en.insert(0,int(second_num)**(1./3))    
# fun to sub
def sub():
    f_num=en.get()
    global f_num
    global math
    math="subtraction"
    en.delete(0,END)
# fun to sub    
def div():
    f_num=en.get()
    global f_num
    global math
    math="division"
    en.delete(0,END)
 # fun to sub   
def mult():
    f_num=en.get()
    global f_num
    global math
    math="Multiplication"
    en.delete(0,END)
# fun to sub    
def sqt():
    global math
    math="Squareroot"
    en.delete(0,END)
 # fun to sub   
def cut():
    global math
    math="Cuberoot"
    en.delete(0,END) 
#creating buttons 
button1=Button(root,text="1",command= lambda: solve(1))
button2=Button(root,text="2",command=lambda: solve(2))
button3=Button(root,text="3",comman=lambda: solve(3))
button4=Button(root,text="4",command=lambda: solve(4))
button5=Button(root,text="5",command=lambda:solve(5))
button5=Button(root,text="5",command=lambda: solve(5))
button6=Button(root,text="6",command=lambda: solve(6))
button7=Button(root,text="7",command=lambda: solve(7))
button8=Button(root,text="8",command=lambda: solve(8))
button9=Button(root,text="9",command=lambda: solve(9))
button0=Button(root,text="0",command=lambda: solve(0))
button_calc=Button(root,text="Calculate",command=calc)
button_mul=Button(root,text="*",command=mult)
button_add=Button(root,text="+",command=add)
button_div=Button(root,text="/",command=div)
button_sub=Button(root,text="-",command=sub)
button_sq=Button(root,text="sqrt",command=sqt)
button_cu=Button(root,text="curt",command=cut)
button_clear=Button(root,text="Clear",command=clear)
# packing all buttons
button_clear.grid(row=7,column=2,ipadx=10,ipady=2)
button_calc.grid(row=7,column=1,padx=2,ipady=2)
button0.grid(row=7,column=0,ipadx=20,ipady=2)
button1.grid(row=6,column=0,ipadx=20,ipady=2)
button2.grid(row=6,column=1,ipadx=20,ipady=2)
button3.grid(row=6,column=2,ipadx=20,ipady=2)
button4.grid(row=5,column=0,ipadx=20,ipady=2)
button5.grid(row=5,column=1,ipadx=20,ipady=2)
button6.grid(row=5,column=2,ipadx=20,ipady=2)
button7.grid(row=4,column=0,ipadx=20,ipady=2)
button8.grid(row=4,column=1,ipadx=20,ipady=2)
button9.grid(row=4,column=2,ipadx=20,ipady=2) 
button_add.grid(row=3,column=0,ipadx=19,ipady=2)
button_sub.grid(row=3,column=1,ipadx=21,ipady=2)
button_mul.grid(row=3,column=2,ipadx=20,ipady=2)
button_div.grid(row=2,column=0,ipadx=20,ipady=2)
button_sq.grid(row=2,column=1,ipadx=14,ipady=2)
button_cu.grid(row=2,column=2,ipadx=12,ipady=2)
# looping the window
root.mainloop()