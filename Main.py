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
        for i in range (0,3):
            for j in range (0,3):
                self.mBoard[i][j] = Button(tk, text=" ", font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,command=lambda: ttt(self.mBoard[i][j]))
                self.mBoard[i][j].grid(row=i, column=j, sticky=S + N + E + W)

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

    def isTaken(self,xPos,yPos):
        return self.mBoard[xPos][yPos]["text"] != ""

    def click(self,player,xPos,yPos):
        global bclick
        if ~(ttmini.isTaken(xPos,yPos)):
            if player:
                self.mBoard[xPos][yPos]["text"]= "X"
            else:
                self.mBoard[xPos][yPos]["text"] = "O"
            bclick = ~bclick
#
# def ttt(buttons):
#     global bclick
#     if buttons["text"] == " " and bclick == True:
#         buttons["text"] = "X"
#         bclick = False
#     if buttons["text"] == " " and bclick == False:
#         buttons["text"] = "O"
#         bclick = True
#
#     if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
#             button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
#             button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
#             button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
#             button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
#             button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
#             button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
#             button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
#             button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
#         tkinter.messagebox.showinfo("Player X", 'Winner is X !!!!')
#         sys.exit()
#
#     if (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
#             button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
#             button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
#             button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
#             button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
#             button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
#             button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
#             button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
#             button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
#         tkinter.messagebox.showinfo("Player O", 'Winner is O !!!!')
#         sys.exit()
#
#
buttons = StringVar()
#
# button1 = Button(tk, text=" ", font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
#                  command=lambda: ttt(button1))
# button1.grid(row=1, column=0, sticky=S + N + E + W)
#
# button2 = Button(tk, text=' ', font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
#                  command=lambda: ttt(button2))
# button2.grid(row=1, column=1, sticky=S + N + E + W)
#
# button3 = Button(tk, text=' ', font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
#                  command=lambda: ttt(button3))
# button3.grid(row=1, column=2, sticky=S + N + E + W)
#
# button4 = Button(tk, text=' ', font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
#                  command=lambda: ttt(button4))
# button4.grid(row=2, column=0, sticky=S + N + E + W)
#
# button5 = Button(tk, text=' ', font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
#                  command=lambda: ttt(button5))
# button5.grid(row=2, column=1, sticky=S + N + E + W)
#
# button6 = Button(tk, text=' ', font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
#                  command=lambda: ttt(button6))
# button6.grid(row=2, column=2, sticky=S + N + E + W)
#
# button7 = Button(tk, text=' ', font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
#                  command=lambda: ttt(button7))
# button7.grid(row=3, column=0, sticky=S + N + E + W)
#
# button8 = Button(tk, text=' ', font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
#                  command=lambda: ttt(button8))
# button8.grid(row=3, column=1, sticky=S + N + E + W)
#
# button9 = Button(tk, text=' ', font=('Times 20 bold'), bg='gray', fg='white', height=4, width=8,
#                  command=lambda: ttt(button9))
# button9.grid(row=3, column=2, sticky=S + N + E + W)

tk.mainloop()
