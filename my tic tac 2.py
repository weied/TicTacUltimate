import numpy
import tkinter.messagebox
from tkinter import *

tk = Tk()
tk.title("Tic Tac Toe")

bclick = True

def ttt(buttons):
     global bclick
     if buttons["text"] == " " and bclick == True:
          buttons["text"] = "X"
          bclick = False
     if buttons["text"] == " " and bclick == False:
          buttons["text"] = "O"
          bclick = True

     if(button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X'or
          button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X'or
          button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X'or
          button1['text'] == 'X'  and button5['text'] == 'X' and button9['text'] == 'X'or
          button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'or
          button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X'or
          button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X'or
          button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X'or
          button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
          tkinter.messagebox.showinfo("Player O",'Winner is O !!!!')
          sys.exit()
          
     if(button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O'or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O'or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O'or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O'or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O'or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
          tkinter.messagebox.showinfo("Player O",'Winner is O !!!!')
          sys.exit()



          
     
     
