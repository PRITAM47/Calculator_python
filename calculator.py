from tkinter import *


def btnClick(numbers):
    global operator
    operator=operator+ str(numbers)
    text_input.set(operator)
    
def btnClearDisplay():
    global operator
    operator=""
    text_input.set("")

def btnEqualsInput():
    global operator
    sumup= str(eval(operator))
    text_input.set(sumup)
    operator=""


root = Tk()
root.title("calculator")
operator=""
text_input= StringVar()

txtDisplay= Entry(root,font=("arial",20,'bold'), textvariable=text_input, bd=30,
                  insertwidth=4,bg="powder blue", justify='right').grid(columnspan=4)

btn7=Button(root,padx=16,pady=16,bd=8, fg="black",font=("arial",20,'bold'),
            bg="powder blue",text="7",command=lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(root,padx=16,pady=16,bd=8, fg="black",font=("arial",20,'bold'),
            bg="powder blue",text="8",command=lambda:btnClick(8)).grid(row=1,column=1)
btn9=Button(root,padx=16,pady=16,bd=8, fg="black",font=("arial",20,'bold'),
            bg="powder blue",text="9",command=lambda:btnClick(9)).grid(row=1,column=2)
Addition=Button(root,padx=16,pady=16,bd=8, fg="black",font=("arial",20,'bold'),
            bg="powder blue",text="+",command=lambda:btnClick("+")).grid(row=1,column=3)
#=======================================================================
btn4=Button(root,padx=16,pady=16,bd=8, fg="black",font=("arial",20,'bold'),
            bg="powder blue",text="4",command=lambda:btnClick(4)).grid(row=2,column=0)
btn5=Button(root,padx=16,pady=16,bd=8, fg="black",font=("arial",20,'bold'),
            bg="powder blue",text="5",command=lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(root,padx=16,pady=16,bd=8, fg="black",font=("arial",20,'bold'),
            bg="powder blue",text="6",command=lambda:btnClick(6)).grid(row=2,column=2)
Subtraction=Button(root,padx=16,pady=16,bd=8, fg="black",font=("arial",20,'bold'),
            bg="powder blue",text="-",command=lambda:btnClick("-")).grid(row=2,column=3)

#==========================================================================
btn1=Button(root,padx=16,pady=16,bd=8, fg="black",font=("arial",20,'bold'),
            bg="powder blue",text="1",command=lambda:btnClick(1)).grid(row=3,column=0)
btn2=Button(root,padx=16,pady=16,bd=8, fg="black",font=("arial",20,'bold'),
            bg="powder blue",text="2",command=lambda:btnClick(2)).grid(row=3,column=1)
btn3=Button(root,padx=16,pady=16,bd=8, fg="black",font=("arial",20,'bold'),
            bg="powder blue",text="3",command=lambda:btnClick(3)).grid(row=3,column=2)
Multiply=Button(root,padx=16,pady=16,bd=8, fg="black",font=("arial",20,'bold'),
            bg="powder blue",text="*",command=lambda:btnClick("*")).grid(row=3,column=3)
#==========================================================================
btn0=Button(root,padx=16,pady=16,bd=8, fg="black",font=("arial",20,'bold'),
            bg="powder blue",text="0",command=lambda:btnClick(0)).grid(row=4,column=0)
btnClear=Button(root,padx=16,pady=16,bd=8, fg="black",font=("arial",20,'bold'),
            bg="powder blue",text="C",command=btnClearDisplay).grid(row=4,column=1)
btnEquals=Button(root,padx=16,pady=16,bd=8, fg="black",font=("arial",20,'bold'),
            bg="powder blue",text="=",command=btnEqualsInput).grid(row=4,column=2)
Division=Button(root,padx=16,pady=16,bd=8, fg="black",font=("arial",20,'bold'),
            bg="powder blue",text="/",command=lambda:btnClick("/")).grid(row=4,column=3)



root.mainloop()
