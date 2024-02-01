#!/usr/bin/python3
 
from tkinter import * 
from tkinter import filedialog
from RT_data_import_and_pre_process import *


def browsefunc1(): 
    browsebutton1.configure(background='green')
    browsebutton2.configure(background='gray')
    browsebutton3.configure(background='gray')
    browsebutton4.configure(background='white')
    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    listb1.grid(row=0, column=0)
    listb2.grid_forget()
    listb3.grid_forget()
    


    

def browsefunc2(): 
    browsebutton1.configure(background='gray')
    browsebutton2.configure(background='green')
    browsebutton3.configure(background='gray')
    browsebutton4.configure(background='white')
    button1.grid_forget()
    button2.grid_forget()
    button3.grid_forget()
    listb1.grid_forget()
    listb2.grid(row=0, column=0)
    listb3.grid(row=0, column=1)


def browsefunc3(): 
    browsebutton1.configure(background='gray')
    browsebutton2.configure(background='gray')
    browsebutton3.configure(background='green')
    browsebutton4.configure(background='white')

def browsefunc4(): 
    #filename = filedialog.askopenfilename() 
    #MyText3.set(filename)
    browsebutton1.configure(background='gray')
    browsebutton2.configure(background='gray')
    browsebutton3.configure(background='gray')
    browsebutton4.configure(background='green')

def operation1():
    #address1 = MyText1.get()
    #address2 = MyText2.get()
    #address3 = MyText3.get()
    #fetch_data_from_excel(address1)

    filename = filedialog.askopenfilename() 
    MyText3.set(filename)





if __name__ == '__main__':
    root = Tk()

    MyText1= StringVar() 
    MyText2= StringVar() 
    MyText3= StringVar()
    
    ####
    frame1 = Frame(root)
    frame2 = Frame(root)
    frame3 = Frame(root)
    frame4 = Frame(root)
    frame5 = Frame(root)
    frame6 = Frame(root)
    ####


    ####

    root.title("RtSha")
    root.geometry('680x510')
    
    #lb = Label(frame1,text='tRSharing',\
    #        bg='#003399',\
    #        fg='black',\
    #        width=60,\
    #        height=1,\
    #        justify='left')
    #lb.pack()
    #####frame 2 3 4 5##############################################################################

    
    browsebutton1 = Button(frame1, text="RT libirary", command=browsefunc1,height = 2,width = 30,background='gray') 
    browsebutton1.pack(side = TOP) 
    
    browsebutton2 = Button(frame1, text="RT prediction", command=browsefunc2,height = 2,width = 30,background='gray') 
    browsebutton2.pack(side = TOP) 

    browsebutton3 = Button(frame1, text="ARI prediction", command=browsefunc3,height = 2,width = 30,background='gray') 
    browsebutton3.pack(side = TOP) 


    filelistEntry = Entry(frame5,textvariable = MyText1,width=30)
    filelistEntry.pack(side=TOP) 
    browsebutton4 = Button(frame5, text="search compound", command=browsefunc4,height = 1,width = 30,background='white') 
    browsebutton4.pack(side = TOP) 

    listb1  = Listbox(frame2,height = 25,width = 62) 
    listb1.grid(row=0, column=0)
    
    listb2  = Listbox(frame6,height = 25,width = 31) 

    listb3  = Listbox(frame6,height = 25,width = 31) 

    lb = Label(frame3,text='status',
            bg='#003399',
            fg='black',
            width=30,
            height=1)
    lb.pack()

    #listb  = Listbox(frame3,height = 20,width = 20) 
    #listb.pack()

    #filelistEntry = Entry(frame2,textvariable = MyText1,width=60)
    #filelistEntry.pack() 
    
    
    

    button1 = Button(frame4, text="upload",bg='#b5b5b5',width=20,command = operation1)#### command=
    button1.grid(row=0, column=0)
    button2 = Button(frame4, text="download example",bg='#b5b5b5',width=20,command = operation1)#### command=
    button2.grid(row=0, column=1)
    button3 = Button(frame4, text="download",bg='#b5b5b5',width=20,command = operation1)#### command=
    button3.grid(row=0, column=2) 

    #####frame 6 7 8 9##############################################################################
    
    #frame1.pack(padx=5,pady=5)
    frame1.grid(row=0, column=0, padx=1, pady=1, sticky='w')
    frame2.grid(row=0, column=1, padx=1, pady=1, sticky='w',rowspan=10)
    frame3.grid(row=13, column=0, padx=1, pady=1, sticky='w')
    frame4.grid(row=13, column=1, padx=1, pady=1, sticky='w')
    frame5.grid(row=5, column=0, padx=1, pady=1, sticky='w')
    frame6.grid(row=0, column=1, padx=1, pady=1, sticky='w',rowspan=10)
    root.mainloop()



