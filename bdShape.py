from multiprocessing.connection import wait
from sqlite3 import Row
import tkinter as t
from tkinter import *
from turtle import bgcolor

from matplotlib.pyplot import grid, text
tk = t.Tk()
tk.title('Body  Shape  Calculator')

def calculate():
    
    #If (bust - hips) ≤ 1" AND (hips - bust) < 3.6" AND (bust - waist) ≥ 9" OR (hips - waist) ≥ 10"
    if (((bust - hip) <= 1) & ((hip - bust) < 3.6 )& ((bust - waist) >= 9) or ((hip -waist) >= 10)):
        Label (tk,text = "Your body shape is Hourglass shape.",bg="green",fg = "black").grid(row =4,cloumn =1)
    #If (hips - bust) ≥ 3.6" AND (hips - bust) < 10" AND (hips - waist) ≥ 9" AND (high hip/waist) < 1.193
    try:
        (((hip - bust)>= 3.6) & ((hip - bust)< 10) & ((hip - waist)>= 9) & ((hip/waist)<1.193))
        Label(tk,text="Your bodyshape is Bottom Hourglass shape.",bg="green",fg="red").grid(row=4,column=1)
    except ZeroDivisionError:
        print("Zero Division Error is occured.")
    #Top hourglass shape
    if(((bust - hip) > 1) & ((bust - hip) < 10) & ((bust - waist) >= 9)):
        Label(tk, text= "Your body shape is Top Hourglass shape.",bg= "green",fg="red").grid(row=4,column=1)
    #Spoon shape
    # if (((hip-bust)>2)& ((hip - waist)>= 7 & ((hip /waist)>= 1.193)):
    #     Label( tk,text="Your body shape is Spoon shape.",bg = "green",fg = "red").grid(row=1,column=3)
    # Triangle shape
    
    if(((hip - bust)>= 3.6)& ((hip-waist)<9)):
        Label(tk,text = "Your body shape is Triangle shape.",bg ="green",fg = "red").grid(row=4,column=1)
    # Inverted Triangle shape
    if (((bust-hip)>= 3.6)&((bust-waist)<9)):
        Label (tk,text = "Your body shape is Inverted Triangle shape.",bg = "green",fg = "red").grid(row =4,column = 1)
    # Ractangle shape
    elif(((hip - bust )<3.6) & ((bust - hip)<3.6) & ((bust-waist)<9) &((hip-waist)<10)):
        Label(tk,text="Your body shape is Ractangle shape.",bg="green",fg="red").grid(row=4,column =1)
    else :
        Label(tk, text = " Sorry. You gave invalid input .Try again...!",fg = 'red').grid(row=4,col=1)

Label(tk , text = 'Enter Your Bust Size ').grid(row=1)
Label(tk,text='Enter Your Hip Size ').grid(row=2)
Label(tk,text='Enter Your waist Size ').grid(row=3)

busty = t.Entry(tk)
busty.grid(row = 1,column=1)


hippy = t.Entry(tk)
hippy.grid(row = 2,column=1)


waisty = t.Entry(tk)
waisty.grid(row = 3,column=1)

bust = int(busty.get())
hip = int(hippy.get())
waist = int (waisty.get())

Button(tk, text = "Calculate", bg = 'green',command=calculate).grid(row =1 , column= 2)
Button(tk,text = "quit",bg = 'red',command= tk.destroy).grid(row = 2, column= 2)


tk.mainloop()
