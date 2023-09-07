import tkinter as tk
from tkinter import *

calculation=""
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"error")

def clear_field():
    global calculation
    calculation =""
    text_result.delete(1.0,"end")





















window=Tk()
window.geometry("500x500")
text_result=tk.Text(window,height=3,width=28,font=("Arial",24))
text_result.grid(columnspan=5)
button_1=tk.Button(window,text="1",command=lambda: add_to_calculation(1),width=5,font=("",15))
button_1.grid(row=1,column=0)
button_2=tk.Button(window,text="2",command=lambda: add_to_calculation(2),width=5,font=("",15))
button_2.grid(row=2,column=0)
button_3=tk.Button(window,text="3",command=lambda: add_to_calculation(3),width=5,font=("",15))
button_3.grid(row=3,column=0)
button_4=tk.Button(window,text="4",command=lambda: add_to_calculation(4),width=5,font=("",15))
button_4.grid(row=1,column=1)
button_5=tk.Button(window,text="5",command=lambda: add_to_calculation(5),width=5,font=("ameen",15))
button_5.grid(row=2,column=1)
button_6=tk.Button(window,text="6",command=lambda: add_to_calculation(6),width=5,font=("ameen",15))
button_6.grid(row=3,column=1)
button_7=tk.Button(window,text="7",command=lambda: add_to_calculation(7),width=5,font=("ameen",15))
button_7.grid(row=1,column=2)
button_8=tk.Button(window,text="8",command=lambda: add_to_calculation(8),width=5,font=("ameen",15))
button_8.grid(row=2,column=2)
button_9=tk.Button(window,text="9",command=lambda: add_to_calculation(9),width=5,font=("ameen",15))
button_9.grid(row=3,column=2)
button_10=tk.Button(window,text="0",command=lambda: add_to_calculation(0),width=5,font=("ameen",15))
button_10.grid(row=4,column=2)
button_11=tk.Button(window,text="+",command=lambda: add_to_calculation("+"),width=5,font=("ameen",15))
button_11.grid(row=1,column=4)
button_12=tk.Button(window,text="-",command=lambda: add_to_calculation("-"),width=5,font=("ameen",15))
button_12.grid(row=2,column=4)
button_13=tk.Button(window,text="*",command=lambda: add_to_calculation("*"),width=5,font=("ameen",15))
button_13.grid(row=3,column=4)
button_14=tk.Button(window,text="/", command=lambda: add_to_calculation("/"),width=5,font=("ameen",15))
button_14.grid(row=4,column=4)
button_15=tk.Button(window,text="=", command=  evaluate_calculation,width=5,font=("ameen",15))
button_15.grid(row=4,column=1)
button_16=tk.Button(window,text=".", command=lambda: add_to_calculation("."),width=5,font=("ameen",15))
button_16.grid(row=4,column=0)
button_17=tk.Button(window,text="c", command= clear_field,width=6,font=("ameen",15))
button_17.grid(row=5,column=0)
button_18=tk.Button(window,text="(",command=lambda: add_to_calculation("("),width=6,font=("ameen",15))
button_18.grid(row=5,column=1)
button_18=tk.Button(window,text=")",command=lambda: add_to_calculation(")"),width=6,font=("ameen",15))
button_18.grid(row=5,column=2)









window.mainloop()
