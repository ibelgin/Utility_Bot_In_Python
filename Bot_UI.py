from tkinter import *
root = Tk()

def send():
    send="You :" +e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="hi"):
        txt.insert(END,"\n"+"Bot : hello")
        
txt =Text(root,bg="light green",width=50)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=50)
send=Button(root,text="Send",bg="brown",width=15,command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("Chartbot")
root.mainloop()
