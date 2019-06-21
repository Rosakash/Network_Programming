from tkinter import *
from tkinter import scrolledtext
import tkinter as tk
import socket
import requests
from threading import Thread
import sys
import getopt
from time import sleep

class request_performer():
    def __init__( self):
        self.root=Tk()
        self.root.title("Resource Finder -created by Akash Roshan")
        self.root.geometry("500x500+0+0")
        self.root.resizable(0,0)
        
        #=========================== TOP HEADING ==========================#
        self.tops = Frame(self.root,width=800,height=20,bg="green",relief=SUNKEN)
        self.tops.pack(side=TOP)
        
        self.l1=Label(self.tops,font=('arial',40,'bold'),text="Resource Finder")
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
        
        
        self.f6 = Frame(self.root,width=800,height=50,bg="green",relief=SUNKEN)
        self.f6.pack(side=TOP)
        
        scrolW  = 50; scrolH = 20
        self.scr = scrolledtext.ScrolledText(self.f6, width=scrolW, height=scrolH, wrap=WORD)
        self.scr.grid(column=0, row=3, sticky='WE', columnspan=3)
    def create_thread(self):
        runt = Thread(target=self.run)
        runt.start()
    def run(self):
        x=0
        f=open('file.txt', mode='r')
        #print(len('file.txt'))
        #line= iter(f)
        #word=next(line)
        while x <= len('file.txt'):
            for line in f:
                word=line
                
                url =("http://www."+self.e1.get()+".com/")
            
                self.word = word
                self.urly = (url+self.word)
                self.url = self.urly
                print(self.url)
                self.scr.insert(INSERT,self.url)
                sleep(1)
            try:
                r = requests.get(self.url)
                print (self.url + " - " + str(r.status_code))
                self.scr.insert(INSERT,self.url + " - " + str(r.status_code))
                sleep(1)
                x = x+1
                #if x <= len('file.txt'):
                 #   self.run()
            except Exception:
                    print ("Can not connect.")
                    self.scr.insert(INSERT,"Can not connect.")
            

r = request_performer()
r.root.mainloop()
