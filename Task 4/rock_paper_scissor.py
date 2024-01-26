from tkinter import *
from PIL import Image, ImageTk
from random import randint

#main window
root = Tk()
root.title("Rock Paper Scissor Game")
root.configure(background="black")

# Resize the image using resize() method
resize_image1 = Image.open("rock_user.png").resize((200,200))
resize_image2 = Image.open("paper_user.png").resize((200,200))
resize_image3 = Image.open("scissor_user.png").resize((200,200))
resize_image4 = Image.open("rock_computer.png").resize((200,200))
resize_image5 = Image.open("paper_computer.png").resize((200,200))
resize_image6 = Image.open("scissor_computer.png").resize((200,200))

#pictures
rock_user = ImageTk.PhotoImage(resize_image1)
paper_user = ImageTk.PhotoImage(resize_image2)
scissor_user = ImageTk.PhotoImage(resize_image3)
rock_computer = ImageTk.PhotoImage(resize_image4)
paper_computer = ImageTk.PhotoImage(resize_image5)
scissor_computer = ImageTk.PhotoImage(resize_image6)


#insert image
user_label = Label(root, image = paper_user,bg="black")
computer_label = Label(root, image = paper_computer,bg="black")
computer_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#scores
playerScore = Label(root,text=0,font=100,bg="black", fg="white")
computerScore = Label(root,text=0,font=100,bg="black", fg="white")
computerScore.grid(row=1,column=1)
playerScore.grid(row=1,column=3)

#indicators
user_indicator = Label(root,font=50,text="USER",bg="black",fg="white").grid(row=0,column=3)
computer_indicator = Label(root,font=50,text="COMPUTER",bg="black",fg="white").grid(row=0,column=1)

# result feedback messages
msg = Label(root,font=50,bg="black",fg="white")
msg.grid(row=5,column=2)

#update message
def updateMessage(x):
    msg['text'] = x

#update user score
def updateUserScore():
    score = int(playerScore['text'])
    score += 1
    playerScore["text"] = str(score)

#update computer score
def updateCompScore():
    score = int(computerScore['text'])
    score += 1
    computerScore["text"] = str(score)

#check winner
def checkWinner(player,computer):
    if player==computer:
        updateMessage("It's a Tie")

    elif player=="rock":
        if computer == "paper":
            updateMessage("You Loose")
            updateCompScore()
        elif computer=="scissor":
            updateMessage("You Won")
            updateUserScore()
    
    elif player=="paper":
        if computer == "scissor":
            updateMessage("You Loose")
            updateCompScore()
        elif computer=="rock":
            updateMessage("You Won")
            updateUserScore()

    elif player=="scissor":
        if computer == "rock":
            updateMessage("You Loose")
            updateCompScore()
        elif computer=="paper":
            updateMessage("You Won")
            updateUserScore()

    else:
        pass
    

# update choices
choices = ["rock","paper","scissor"]
def updateChoice(x):

#for computer
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        computer_label.configure(image=rock_computer)
    elif compChoice == "paper":
        computer_label.configure(image=paper_computer)
    elif compChoice == "scissor":
        computer_label.configure(image=scissor_computer)

#for user
    if x=="rock":
        user_label.configure(image=rock_user)
    elif x=="paper":
        user_label.configure(image=paper_user)
    elif x=="scissor":
        user_label.configure(image=scissor_user)

    checkWinner(x,compChoice)

#buttons
rock = Button(root, width=20, height=2, text="ROCK", bg="#0000ff",fg="white",command= lambda:updateChoice("rock")).grid(row=2,column=1)
paper = Button(root, width=20, height=2, text="PAPER", bg="#ff0000",fg="white",command= lambda:updateChoice("paper")).grid(row=2,column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#ff0066",fg="white",command= lambda:updateChoice("scissor")).grid(row=2,column=3)

root.mainloop()
