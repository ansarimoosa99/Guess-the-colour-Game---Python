# import the modules  
import tkinter 
import random 


# list of possible colour. 
colours = ['Red','Blue','Green','Pink','Black', 
           'Yellow','Orange','White','Purple','Brown'] 
score = 0
  
# the game time left, initially 30 seconds. 
timeleft = 30
  
# function that will start the game. 
def startGame(event): 
    
    if timeleft == 30: 
          
        # start the countdown timer. 
        countdown() 
          
    # run the function to 
    # choose the next colour. 
    nextColour() 
  
# Function to choose and 
# display the next colour. 
def nextColour(): 
  
    # use the globally declared 'score' 
    # and 'play' variables above. 
    global score 
    global timeleft 
  
    # if a game is currently in play 
    if timeleft > 0: 
  
        # make the text entry box active. 
        e.focus_set() 
  
        # if the colour typed is equal 
        # to the colour of the text 
        if e.get().lower() == colours[1].lower(): 
              
            score += 1
  
        # clear the text entry box. 
        e.delete(0, tkinter.END) 
          
        random.shuffle(colours) 
          
        # change the colour to type, by changing the 
        # text _and_ the colour to a random colour value 
        label.config(fg = str(colours[1]), text = str(colours[0])) 
          
        # update the score. 
        scoreLabel.config(text = "Score: " + str(score)) 
  
  
# Countdown timer function  
def countdown(): 
  
    global timeleft 
  
    # if a game is in play 
    if timeleft > 0: 
  
        # decrement the timer. 
        timeleft -= 1
          
        # update the time left label 
        timeLabel.config(text = "Time left: "
                               + str(timeleft)) 
                                 
        # run the function again after 1 second. 
        timeLabel.after(1000, countdown) 
  
  
    # Driver Code 
def start():     
    # create a GUI window 
    root = tkinter.Tk() 
      
    # set the title 
    root.title("COLORGAME") 
      
    # set the size 
    root.geometry("375x200") 
    global instructions
    # add an instructions label 
    instructions = tkinter.Label(root, text = "Type the colour"
                            "of the text, and not the text!", 
                                          font = ('Helvetica', 12)) 
    instructions.pack()  
    global scoreLabel
    # add a score label 
    scoreLabel = tkinter.Label(root, text = "Press enter to start", 
                                          font = ('Helvetica', 12)) 
    scoreLabel.pack() 
    
    global timeLabel
    # add a time left label 
    timeLabel = tkinter.Label(root, text = "Time left: " +
                  str(timeleft), font = ('Helvetica', 12)) 
                    
    timeLabel.pack() 
    global label  
    # add a label for displaying the colours 
    label = tkinter.Label(root, font = ('Helvetica', 60)) 
    label.pack() 
    global e  
    # add a text entry box for 
    # typing in colours 
    e = tkinter.Entry(root) 
      
    # run the 'startGame' function  
    # when the enter key is pressed 
    root.bind('<Return>', startGame) 
    e.pack() 
      
    # set focus on the entry box 
    e.focus_set() 
      
    # start the GUI 
    root.mainloop()


#lololol()
    
  
    
    
    
    
    
import tkinter as tk
from PIL import ImageTk, Image


root = tk.Tk()
root.title("GAME : Guess the colour !")
#c = tk.Canvas(root, width=100,height=100, bg="white")
root.geometry("600x600+40+20")

#def start():
#    print("STARTTTTTTTTT")
#    gamer()
#    global amount
#    root=tk.Tk()
#    root.geometry("400x120+40+20")
#    amount=tk.IntVar()
#    bid_amount=tk.Label(root,text="    Enter Bidding amount   :",textvariable=amount, font=(12))
#    bid_amount.grid(row=0,column=0,pady=10)
#    amount=tk.Entry(root)
#    amount.grid(row=0,column = 3)
#    
#    next=tk.Button(root,text="Next",font=("Helvetica",10))#,command=proj2jii.mainpage)
#    next.grid(row=2,column=2,pady=10)
#    root.destroy()
    
def howtoplay():
    top=tk.Tk()
    top.geometry("600x600+40+20")
    head=tk.Label(top,text="How to play !!",font=("Times new roman",20))
    head.grid(row=1,pady=20)
    rules="""   
    
                1.The name of a colour 
                  will be displayed
                
                
                2.You need to write the colour of the 
                  text and not the name of the colour being displayed.
    
    
                2.Complete the game in 30 seconds and your score will 
                be the number of correct answers you give.
                
                
                3.According to result either 
                  you lose or win the game!!
    """
    body=tk.Label(top,text=rules,font=("Arial",15))
    body.grid(row=3,pady=20)
    close=tk.Button(top,text="Close",height=2,width=30,font=("Helvetica",12),command=top.destroy)
    close.grid(row=6,column=0)



path="logo.jpg"
img=ImageTk.PhotoImage(Image.open(path))
l1=tk.Label(root,image=img)#="Guesss the colour !!", font=("Helvetica",40))
l1.grid(row=1,column=3, pady=30)

#l=tk.Label(root,text="7 UP & & DOWN", font=("Helvetica",20))
#l.grid(row=1,column=3, pady=30)
b1=tk.Button(root,text="Start" ,height=2,width=50,font=("Helvetica",12) , command= start )
b1.grid(row=3,column=3,  padx=80, pady=20) #,bg=Black,fg=White)
b2=tk.Button(root,text="How to play",height=2,width=50 ,font=("Helvetica",12), command=howtoplay)
b2.grid(row=5,column=3,  padx=3, pady=20)
b3=tk.Button(root,text="Quit",font=("Helvetica",12), command = root.destroy)
b3.grid(row=7 , column=3, padx=3, pady=20)
b3.config(height=2,width=50 )

root.mainloop()