import tkinter as tk

root = tk.Tk()

def send():

    send="You :" +e.get()
    text.insert(END,"\n"+send)
    if(e.get()=="hi"):
        text.insert(END,"\n"+"Bot : hello")


text =tk.Text(root,bg="light green",width=50)
text.grid(row=0,column=0,columnspan=2)
e=tk.Entry(root,width=50)
send=tk.Button(root,text="Send",bg="brown",width=15,command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("Chartbot")
tk.mainloop()