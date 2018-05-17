#File: QuizItUpPrototype.py
#Author: Emily Hodder
#Date Created: May 15, 2018
#Date Edited: May 15, 2018

from tkinter import *
from tkinter import ttk


class QuizFrame():
    questions = (("What celebrity does Jack identify with?","Beyonce","Brittany Spears","Kanye West", "Chris Evans"),("What is Emily's favourite animal?", "Elephants", "Dolphins", "Dogs", "Cats"))
    answers = ("Beyonce", "Dogs")
    def __init__(self,master):
        #Configure the main frame
        self.mainframe=Frame(master,bg="black")
        self.mainframe.grid(column=0,row=0,columnspan=500,rowspan=500,sticky=W+E+N+S)

        self.mainPage(master)

    def mainPage(self,master):
        #Create heading label
        header=Label(self.mainframe,text="CodeMakers++ Quiz It Up!",font=("Verdana",25,"bold italic"),fg="red",bg="black",anchor=CENTER)
        header.grid(row=1,rowspan = 2)

        #Create name entry field with label
        self.nameLabel=Label(self.mainframe,text="Enter your name:",font=("Verdana",15),fg="white",bg="black")
        self.nameLabel.grid(rowspan=1,columnspan=6)
        self.nameBox=Entry(self.mainframe,validate='all',validatecommand=(master.register(self.validateNameField),'%P'),bg="black",fg="white")
        self.nameBox.grid(rowspan = 1, columnspan=6)

        #Create start game button
        self.startButton=Button(self.mainframe,text="Start Game",state=DISABLED,command=lambda:self.startGame(master),bg="black",fg="white")
        self.startButton.grid(rowspan=1, columnspan=6)

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
        
    def question(self,master,num):
        self.questionLabel = Label (self.mainframe, text = self.questions[num][0], font = ("Veranda", 15), fg="white", bg = "black")
        self.questionLabel.grid(rowspan=1,columnspan=20)

        self.answerA = Button (self.mainframe, text=self.questions[num][1], command=lambda:self.checkAnswer(master,num,1), bg="black",fg="white")
        self.answerB = Button (self.mainframe, text=self.questions[num][2], command=lambda:self.checkAnswer(master,num,2), bg="black",fg="white")
        self.answerC = Button (self.mainframe, text=self.questions[num][3], command=lambda:self.checkAnswer(master,num,3), bg="black",fg="white")
        self.answerD = Button (self.mainframe, text=self.questions[num][4], command=lambda:self.checkAnswer(master,num,4), bg="black",fg="white")

        self.answerA.grid(row = 20, column = 10)
        self.answerB.grid(row = 20, column = 20)
        self.answerC.grid(row = 30, column = 10)
        self.answerD.grid(row = 30, column = 20)

    def checkAnswer(self, master, num, responseNum):
        print(self.answers[0])
        self.questionLabel.grid_forget()
        self.answerA.grid_forget()
        self.answerB.grid_forget()
        self.answerC.grid_forget()
        self.answerD.grid_forget()
            
        if self.questions[num][responseNum] == self.answers[num]:
            try:
                self.question(master, num+1)
            except:
                self.winningScreen(master)
        else:
            self.gameOver(master)

    def gameOver(self,master):
        self.lostLabel=Label(self.mainframe,text="Sorry, " + self.playerName + ", you got a question wrong :( \n Would you like to play again?",font=("Verdana",15),fg="white",bg="black")
        self.lostLabel.grid(rowspan=1,columnspan=20)
        self.replayButton=Button(self.mainframe,text="Play Again",state=NORMAL,command=lambda:self.clearGameOver(master),bg="black",fg="white")
        self.replayButton.grid(rowspan=1,columnspan=6)

    def clearGameOver(self,master):
        self.lostLabel.grid_forget()
        self.replayButton.grid_forget()
        self.mainPage(master)

    def clearWinningLabel(self,master):
        self.winLabel.grid_forget()
        self.replayButton.grid_forget()
        self.mainPage(master)

    def winningScreen(self,master):
        self.winLabel=Label(self.mainframe,text="Congratulations, " + self.playerName + ", you beat the game! :) \n Would you like to play again?",font=("Verdana",15),fg="white",bg="black")
        self.winLabel.grid(rowspan=1,columnspan=20)
        self.replayButton=Button(self.mainframe,text="Play Again",state=NORMAL,command=lambda:self.clearWinningScreen(master),bg="black",fg="white")
        self.replayButton.grid(rowspan=1,columnspan=6)
    
def main():
    master=Tk()


    QuizFrame(master)

    master.title("CodeMakers++ Quiz It Up!")
    master.mainloop()

if __name__=='__main__':
    main()

    
