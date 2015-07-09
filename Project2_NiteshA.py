import re
from tkinter import *

def proc(Z):
    nitesh=[]
    doc=open('icd10.txt','r',encoding='utf-8')
    regexp = re.compile(Z,re.IGNORECASE)
    count=-1
    String1="\nCode\tDescription\n"
    for li in doc:
        li=li.strip()
        if regexp.search(li):
            count+=1
            entry=li.split('\t')
            nitesh.append(entry)
            String1=String1+str(nitesh[count][0])+"\t"+str(nitesh[count][1]) + "\n"
            
    if count==-1:
        String1="Entry not found"
            
    doc.close()
    return String1

    
root2 = Tk()
Code=StringVar()
String2=StringVar()

def pet(event):
    String2.set(proc(Y.get()))

def reset():
    Code.set("")
    String2.set("")
        
label = Label(root2, text="Enter partial CODE or DESCRIPTION")
label.grid(row=0,column=0)
Y = Entry(root2,textvariable=Code)
Y.bind('<Return>', pet)
Y.grid(row=0,column=1)

K = Message(root2,textvariable=String2,width=5000)
K.grid(row=1,column=0)
reset_button = Button(root2, text="Reset", command=reset)
reset_button.grid(row=2,column=0)
quit_button = Button(root2, text="Close Window", command=root2.destroy)
quit_button.grid(row=2,column=1)
root2.mainloop()
    
 
  







    

