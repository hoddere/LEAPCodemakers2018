#File: QuizItUpPrototype.py
#Author: Emily Hodder
#Date Created: May 15, 2018
#Date Edited: July 22, 2018

from tkinter import *
#from tkinter import ttk

class QuizFrame():

    def __init__(self,master):
        #Configure the main frame
        self.mainframe=Frame(master,bg="black")
        self.mainframe.grid(column=0,row=0,columnspan=10,rowspan=10,sticky=W+E+N+S)

        self.mainPage(master)

    def mainPage(self,master):
        #Create heading label
        header=Label(self.mainframe,text="CodeMakers++ Quiz It Up!",font=("Verdana",25,"bold italic"),fg="red",bg="black",anchor=CENTER)
        header.grid(row=0, columnspan = 10)

        #Create name entry field with label
        self.nameLabel=Label(self.mainframe,text="Enter your name:",font=("Verdana",15),fg="white",bg="black")
        self.nameLabel.grid(row = 1, columnspan = 10)
        self.nameBox=Entry(self.mainframe,validate='all',validatecommand=(master.register(self.validateNameField),'%P'),bg="black",fg="white")
        self.nameBox.grid(row = 2, rowspan=2, columnspan = 10)

        #Create start game button
        self.startButton=Button(self.mainframe,text="Start Game",state=DISABLED,command=lambda:self.startGame(master),bg="black",fg="white")
        self.startButton.grid(row = 4, rowspan = 2, columnspan = 10)

    def validateNameField(self,N): #Checks if the name entry box contains input and enables/disables the start button 
        if self.nameBox.get() != '':
            self.startButton.config(state=NORMAL)
        else:
            self.startButton.config(state=DISABLED)
            
        return True

    def startGame(self,master):
        #Get player name
        self.playerName=self.nameBox.get()
        
        #Delete main page widgets 
        self.nameLabel.grid_forget()
        self.nameBox.grid_forget()
        self.startButton.grid_forget()
        self.question(master,0)
  
def main():
    master=Tk()


    QuizFrame(master)

    master.title("CodeMakers++ Quiz It Up!")
    master.mainloop()

if __name__=='__main__':
    main()

    
