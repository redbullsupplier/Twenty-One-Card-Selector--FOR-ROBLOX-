import tkinter as tk
from pathlib import Path

enemyCards = []
playerCards = []
root = tk.Tk()
root.title("Card Selecter")
root.resizable(False, False)
info_panel = tk.Text(root, width=40, height=20)
info_panel.grid(row=0, column=1,padx=50,pady=50)
enemyCard = tk.Label(root, text="", width=15, height=3, bg='red', relief='flat')
enemyCard.grid(row=0, column=0, padx=30,pady=30)
playerCard = tk.Label(root, text="", width=15, height=3, bg='blue', relief='flat')
playerCard.grid(row=0,column=2, padx=30,pady=10)

def enemy(string):
        if string not in enemyCards and string not in playerCards:
            info_panel.insert('end', "Opponent picked " + string + "\n")
            enemyCards.append(string)
            enemyCard.configure(text=str(enemyCards))
        else:
            info_panel.insert('end', string + " was already used. \n")
def player(string):
        if string not in playerCards and string not in enemyCards:
            info_panel.insert('end', "I picked " + string + "\n")
            playerCards.append(string)
            playerCard.configure(text=str(playerCards))
        else:
            info_panel.insert('end', string + " was already used. \n")

def resetAll():
     info_panel.delete(1.0, 'end')
     playerCard.configure(text='')
     enemyCard.configure(text='')
def resetPlayer():
     playerCard.configure(text='')
     playerCards.clear()
def resetEnemy():
     enemyCard.configure(text='')
     enemyCards.clear()
for i in range(1, 12):
    button = tk.Button(text=i, highlightbackground='red', command= lambda x=i: enemy(str(x))).grid(row=i, column=0, padx=10, pady=5)
    
for i in range(1, 12):
    button = tk.Button(text=i, highlightbackground='green', command= lambda x=i: player(str(x))).grid(row=i, column=2, padx=10, pady=5)
resetPlayer = tk.Button(root, text="Reset your cards?", command=resetPlayer).grid(row=3,column=1)
resetEnemy = tk.Button(root, text="Reset enemy?", command=resetEnemy).grid(row=4,column=1)
resetAll = tk.Button(root, text="Reset all?", command=resetAll).grid(row=5,column=1)

root.mainloop()
