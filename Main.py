from builtins import range

import tkinter.messagebox
from tkinter import *

tk = Tk()
tk.title("Tic Tac Toe")

bclick = True

class ttmini:
    def __init__(self):
        self.winner = ""
        self.mBoard = [[None,None,None],[None,None,None],[None,None,None]]
        for i in range (1):
            for j in range (1):
                self.mBoard[i][j] = Button(tk, text="", font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,command=lambda: ttmini.ttt(self,self.mBoard[i][j]))
                self.mBoard[i][j].grid(row=i+1, column=j, sticky=S + N + E + W)

    def getWinner(self):
        return self.winner

    def checkWinCond(self):
        for i in range (0,3):
            if ((self.mBoard[i][0]["text"] == "X" and self.mBoard[i][1]["text"] == "X" and self.mBoard[i][2]["text"] == "X") or
                    (self.mBoard[0][i]["text"] == "X" and self.mBoard[1][i]["text"] == "X" and self.mBoard[2][i]["text"] == "X")):
                self.winner = "X"
            if ((self.mBoard[i][0]["text"] == "O" and self.mBoard[i][1]["text"] == "O" and self.mBoard[i][2]["text"] == "O") or
                    (self.mBoard[0][i]["text"] == "O" and self.mBoard[1][i]["text"] == "O" and self.mBoard[2][i]["text"] == "O")):
                self.winner = "O"

        if ((self.mBoard[0][0]["text"] == self.mBoard[1][1]["text"] == self.mBoard[2][2]["text"]) or
                (self.mBoard[0][2]["text"] == self.mBoard[1][1]["text"] == self.mBoard[2][0]["text"])) :
            if self.mBoard[1][1]["text"] != "":
                self.winner = self.mBoard[1][1]
        return self.winner

    def ttt(ttmini,buttons):
        global bclick
        if buttons["text"] == "" and bclick == True:
            buttons["text"] = "X"
            print(ttmini.mBoard[1][0]["text"])
            bclick = False
        if buttons["text"] == "" and bclick == False:
            buttons["text"] = "O"
            bclick = True

        hasWon = ttmini.checkWinCond()
        if hasWon == "X":
            tkinter.messagebox.showinfo("Player X", 'Winner is X !!!!')
            sys.exit()
        if hasWon == "O":
            tkinter.messagebox.showinfo("Player O", 'Winner is O !!!!')
            sys.exit()

buttons = StringVar()
ttmini()

tk.mainloop()
