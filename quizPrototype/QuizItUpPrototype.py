#File: QuizItUpPrototype.py
#Author: Emily Hodder
#Date Created: May 15, 2018
#Date Edited: May 15, 2018

from tkinter import *
from winsound import *
from tkinter import ttk

def play():
    PlaySound('funky.wav', SND_ALIAS | SND_ASYNC)

class QuizFrame():
    questions = (("Which year was McMaster University founded?","1857","1867","1877", "1887"),("Under which faculty is computer science at McMaster?", "Science", "Engineering", "Computing", "Mathematics"), ("Which program did Emily start in at McMaster?", "Physics", "Health Sciences", "Humanities", "Shrekology"))
    answers = ("1887", "Engineering", "Physics")

    score = 1

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
        
    def question(self,master,num):
        self.questionLabel = Label (self.mainframe, text = self.questions[num][0], font = ("Veranda", 15), fg="white", bg = "black")
        self.questionLabel.grid(row = 1, columnspan = 10)

        self.answerA = Button (self.mainframe, text=self.questions[num][1], command=lambda:self.checkAnswer(master,num,1), bg="black",fg="white")
        self.answerB = Button (self.mainframe, text=self.questions[num][2], command=lambda:self.checkAnswer(master,num,2), bg="black",fg="white")
        self.answerC = Button (self.mainframe, text=self.questions[num][3], command=lambda:self.checkAnswer(master,num,3), bg="black",fg="white")
        self.answerD = Button (self.mainframe, text=self.questions[num][4], command=lambda:self.checkAnswer(master,num,4), bg="black",fg="white")

        self.answerA.grid(row = 2, columnspan = 2, column = 2)
        self.answerB.grid(row = 2, columnspan = 2, column = 4)
        self.answerC.grid(row = 3, columnspan = 2, column = 2)
        self.answerD.grid(row = 3, columnspan = 2, column = 4)

        #Create score label
        self.level = Label (self.mainframe, text = "Round " + str(self.score), font = ("Veranda", 15), fg = "white", bg = "black")
        self.level.grid(row = 4, column = 0)
        
    def shrek(self, master):
        logo = PhotoImage (file = 'shrek.gif')
        self.dance = Label (image = logo)
        self.dance.grid(row = 0, columnspan = 10)
        
    def checkAnswer(self, master, num, responseNum):
        print(self.answers[0])
        self.questionLabel.grid_forget()
        self.answerA.grid_forget()
        self.answerB.grid_forget()
        self.answerC.grid_forget()
        self.answerD.grid_forget()

        if self.questions[num][responseNum] == "Shrekology":
            self.shrek(master)
        else:
            
            if self.questions[num][responseNum] == self.answers[num]:
                try:
                    self.score += 1
                    self.level.grid_forget()
                    self.question(master, num+1)
                except:
                    self.winningScreen(master)
            else:
                self.gameOver(master)

    def gameOver(self,master):
        self.lostLabel=Label(self.mainframe,text="Sorry, " + self.playerName + ", you lost. You made it to round " + str(self.score) + ".\n Would you like to play again?",font=("Verdana",15),fg="white",bg="black")
        self.lostLabel.grid(row = 4,columnspan = 10)
        self.replayButton=Button(self.mainframe,text="Play Again",state=NORMAL,command=lambda:self.clearGameOver(master),bg="black",fg="white")
        self.replayButton.grid(row = 5,columnspan = 10)
        self.level.grid_forget()
        self.score = 0

    def clearGameOver(self,master):
        self.lostLabel.grid_forget()
        self.replayButton.grid_forget()
        self.mainPage(master)

    def clearWinningScreen(self,master):
        self.winLabel.grid_forget()
        self.replayButton.grid_forget()
        self.mainPage(master)

    def winningScreen(self,master):
        self.winLabel=Label(self.mainframe,text="Congratulations, " + self.playerName + ", you beat all " + str(self.score) + " levels and won the game! :) \n Would you like to play again?",font=("Verdana",15),fg="white",bg="black")
        self.winLabel.grid(row = 3, columnspan = 10)
        self.replayButton=Button(self.mainframe,text="Play Again",state=NORMAL,command=lambda:self.clearWinningScreen(master),bg="black",fg="white")
        self.replayButton.grid(row = 4,columnspan = 10)
        self.level.grid_forget()
        self.score = 0
    
def main():
    master=Tk()


    QuizFrame(master)

    master.title("CodeMakers++ Quiz It Up!")
    master.mainloop()

if __name__=='__main__':
    main()

    
