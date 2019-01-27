#import numpy
import os
import tkinter.messagebox
from tkinter import *

tk = Tk()
tk.title("Tic Tac Toe")

bclick = True

winmat= [[None,None,None],[None,None,None],[None,None,None]]

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def ttt(buttons):
     global bclick
     print(winmat)
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
          winmat[0][0] = "X"
          
     if(button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O'or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O'or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O'or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O'or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O'or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
          winmat[0][0] = "O"


     if(button10['text'] == 'X' and button11['text'] == 'X' and button12['text'] == 'X'or
          button13['text'] == 'X' and button14['text'] == 'X' and button15['text'] == 'X'or
          button16['text'] == 'X' and button17['text'] == 'X' and button18['text'] == 'X'or
          button10['text'] == 'X'  and button14['text'] == 'X' and button18['text'] == 'X'or
          button12['text'] == 'X' and button14['text'] == 'X' and button16['text'] == 'X'or
          button12['text'] == 'X' and button15['text'] == 'X' and button18['text'] == 'X'or
          button10['text'] == 'X' and button13['text'] == 'X' and button16['text'] == 'X'or
          button11['text'] == 'X' and button14['text'] == 'X' and button17['text'] == 'X'or
          button16['text'] == 'X' and button15['text'] == 'X' and button18['text'] == 'X'):
          winmat[0][1] = "X"

          
     if(button10['text'] == 'O' and button11['text'] == 'O' and button12['text'] == 'O'or
          button13['text'] == 'O' and button14['text'] == 'O' and button15['text'] == 'O'or
          button16['text'] == 'O' and button17['text'] == 'O' and button18['text'] == 'O'or
          button10['text'] == 'O' and button14['text'] == 'O' and button18['text'] == 'O'or
          button12['text'] == 'O' and button14['text'] == 'O' and button16['text'] == 'O'or
          button10['text'] == 'O' and button11['text'] == 'O' and button12['text'] == 'O'or
          button10['text'] == 'O' and button13['text'] == 'O' and button16['text'] == 'O'or
          button11['text'] == 'O' and button14['text'] == 'O' and button17['text'] == 'O'or
          button16['text'] == 'O' and button15['text'] == 'O' and button18['text'] == 'O'):
          winmat[0][1] = "O"


     if(button19['text'] == 'X' and button20['text'] == 'X' and button21['text'] == 'X'or
          button22['text'] == 'X' and button23['text'] == 'X' and button24['text'] == 'X'or
          button25['text'] == 'X' and button26['text'] == 'X' and button27['text'] == 'X'or
          button19['text'] == 'X'  and button23['text'] == 'X' and button27['text'] == 'X'or
          button21['text'] == 'X' and button23['text'] == 'X' and button25['text'] == 'X'or
          button19['text'] == 'X' and button20['text'] == 'X' and button21['text'] == 'X'or
          button19['text'] == 'X' and button22['text'] == 'X' and button25['text'] == 'X'or
          button20['text'] == 'X' and button23['text'] == 'X' and button26['text'] == 'X'or
          button25['text'] == 'X' and button24['text'] == 'X' and button27['text'] == 'X'):
          winmat[0][2] = "X"

          
     if(button19['text'] == 'O' and button20['text'] == 'O' and button21['text'] == 'O'or
          button22['text'] == 'O' and button23['text'] == 'O' and button24['text'] == 'O'or
          button25['text'] == 'O' and button26['text'] == 'O' and button27['text'] == 'O'or
          button19['text'] == 'O' and button23['text'] == 'O' and button27['text'] == 'O'or
          button21['text'] == 'O' and button23['text'] == 'O' and button25['text'] == 'O'or
          button19['text'] == 'O' and button20['text'] == 'O' and button21['text'] == 'O'or
          button19['text'] == 'O' and button22['text'] == 'O' and button25['text'] == 'O'or
          button20['text'] == 'O' and button23['text'] == 'O' and button26['text'] == 'O'or
          button25['text'] == 'O' and button24['text'] == 'O' and button27['text'] == 'O'):
          winmat[0][2] = "O"

               
     if(button28['text'] == 'X' and button29['text'] == 'X' and button30['text'] == 'X'or
          button31['text'] == 'X' and button32['text'] == 'X' and button33['text'] == 'X'or
          button34['text'] == 'X' and button35['text'] == 'X' and button36['text'] == 'X'or
          button28['text'] == 'X'  and button32['text'] == 'X' and button36['text'] == 'X'or
          button30['text'] == 'X' and button32['text'] == 'X' and button34['text'] == 'X'or
          button28['text'] == 'X' and button29['text'] == 'X' and button30['text'] == 'X'or
          button28['text'] == 'X' and button31['text'] == 'X' and button34['text'] == 'X'or
          button29['text'] == 'X' and button32['text'] == 'X' and button35['text'] == 'X'or
          button34['text'] == 'X' and button33['text'] == 'X' and button36['text'] == 'X'):
          winmat[1][0] = "X"
          
     if(button28['text'] == 'O' and button29['text'] == 'O' and button30['text'] == 'O'or
          button31['text'] == 'O' and button32['text'] == 'O' and button33['text'] == 'O'or
          button34['text'] == 'O' and button35['text'] == 'O' and button36['text'] == 'O'or
          button28['text'] == 'O' and button32['text'] == 'O' and button36['text'] == 'O'or
          button30['text'] == 'O' and button32['text'] == 'O' and button34['text'] == 'O'or
          button28['text'] == 'O' and button29['text'] == 'O' and button30['text'] == 'O'or
          button28['text'] == 'O' and button31['text'] == 'O' and button34['text'] == 'O'or
          button29['text'] == 'O' and button32['text'] == 'O' and button35['text'] == 'O'or
          button34['text'] == 'O' and button33['text'] == 'O' and button36['text'] == 'O'):
          winmat[1][0] = "O"


     if(button55['text'] == 'X' and button56['text'] == 'X' and button57['text'] == 'X'or
          button58['text'] == 'X' and button59['text'] == 'X' and button60['text'] == 'X'or
          button61['text'] == 'X' and button62['text'] == 'X' and button63['text'] == 'X'or
          button55['text'] == 'X'  and button59['text'] == 'X' and button63['text'] == 'X'or
          button57['text'] == 'X' and button59['text'] == 'X' and button61['text'] == 'X'or
          button55['text'] == 'X' and button56['text'] == 'X' and button57['text'] == 'X'or
          button55['text'] == 'X' and button58['text'] == 'X' and button61['text'] == 'X'or
          button56['text'] == 'X' and button59['text'] == 'X' and button62['text'] == 'X'or
          button61['text'] == 'X' and button60['text'] == 'X' and button63['text'] == 'X'):
          winmat[2][0] = "X"

          
     if(button55['text'] == 'O' and button56['text'] == 'O' and button57['text'] == 'O'or
          button58['text'] == 'O' and button59['text'] == 'O' and button60['text'] == 'O'or
          button61['text'] == 'O' and button62['text'] == 'O' and button63['text'] == 'O'or
          button55['text'] == 'O' and button59['text'] == 'O' and button63['text'] == 'O'or
          button57['text'] == 'O' and button59['text'] == 'O' and button61['text'] == 'O'or
          button55['text'] == 'O' and button56['text'] == 'O' and button57['text'] == 'O'or
          button55['text'] == 'O' and button58['text'] == 'O' and button61['text'] == 'O'or
          button56['text'] == 'O' and button59['text'] == 'O' and button62['text'] == 'O'or
          button61['text'] == 'O' and button60['text'] == 'O' and button63['text'] == 'O'):
          winmat[2][0] = "O"


     if(button37['text'] == 'X' and button38['text'] == 'X' and button39['text'] == 'X'or
          button40['text'] == 'X' and button41['text'] == 'X' and button42['text'] == 'X'or
          button43['text'] == 'X' and button44['text'] == 'X' and button45['text'] == 'X'or
          button37['text'] == 'X'  and button41['text'] == 'X' and button45['text'] == 'X'or
          button39['text'] == 'X' and button41['text'] == 'X' and button43['text'] == 'X'or
          button39['text'] == 'X' and button42['text'] == 'X' and button45['text'] == 'X'or
          button37['text'] == 'X' and button40['text'] == 'X' and button43['text'] == 'X'or
          button38['text'] == 'X' and button41['text'] == 'X' and button44['text'] == 'X'or
          button43['text'] == 'X' and button42['text'] == 'X' and button45['text'] == 'X'):
          winmat[1][1] = "X"

          
     if(button37['text'] == 'O' and button38['text'] == 'O' and button39['text'] == 'O'or
          button40['text'] == 'O' and button41['text'] == 'O' and button42['text'] == 'O'or
          button43['text'] == 'O' and button44['text'] == 'O' and button45['text'] == 'O'or
          button37['text'] == 'O' and button41['text'] == 'O' and button45['text'] == 'O'or
          button39['text'] == 'O' and button41['text'] == 'O' and button43['text'] == 'O'or
          button37['text'] == 'O' and button38['text'] == 'O' and button39['text'] == 'O'or
          button37['text'] == 'O' and button40['text'] == 'O' and button43['text'] == 'O'or
          button38['text'] == 'O' and button41['text'] == 'O' and button44['text'] == 'O'or
          button43['text'] == 'O' and button42['text'] == 'O' and button45['text'] == 'O'):
          winmat[1][1] = "O"


     if(button64['text'] == 'X' and button65['text'] == 'X' and button66['text'] == 'X'or
          button67['text'] == 'X' and button68['text'] == 'X' and button69['text'] == 'X'or
          button70['text'] == 'X' and button71['text'] == 'X' and button72['text'] == 'X'or
          button64['text'] == 'X'  and button68['text'] == 'X' and button72['text'] == 'X'or
          button66['text'] == 'X' and button68['text'] == 'X' and button70['text'] == 'X'or
          button66['text'] == 'X' and button69['text'] == 'X' and button72['text'] == 'X'or
          button64['text'] == 'X' and button67['text'] == 'X' and button70['text'] == 'X'or
          button65['text'] == 'X' and button68['text'] == 'X' and button71['text'] == 'X'or
          button70['text'] == 'X' and button69['text'] == 'X' and button72['text'] == 'X'):
          winmat[2][1] = "X"

          
     if(button64['text'] == 'O' and button65['text'] == 'O' and button66['text'] == 'O'or
          button67['text'] == 'O' and button68['text'] == 'O' and button69['text'] == 'O'or
          button70['text'] == 'O' and button71['text'] == 'O' and button72['text'] == 'O'or
          button64['text'] == 'O' and button68['text'] == 'O' and button72['text'] == 'O'or
          button66['text'] == 'O' and button68['text'] == 'O' and button70['text'] == 'O'or
          button64['text'] == 'O' and button65['text'] == 'O' and button66['text'] == 'O'or
          button64['text'] == 'O' and button67['text'] == 'O' and button70['text'] == 'O'or
          button65['text'] == 'O' and button68['text'] == 'O' and button71['text'] == 'O'or
          button70['text'] == 'O' and button69['text'] == 'O' and button72['text'] == 'O'):
          winmat[2][1] = "O"


     if(button46['text'] == 'X' and button47['text'] == 'X' and button48['text'] == 'X'or
          button49['text'] == 'X' and button50['text'] == 'X' and button51['text'] == 'X'or
          button52['text'] == 'X' and button53['text'] == 'X' and button54['text'] == 'X'or
          button46['text'] == 'X'  and button50['text'] == 'X' and button54['text'] == 'X'or
          button48['text'] == 'X' and button50['text'] == 'X' and button52['text'] == 'X'or
          button46['text'] == 'X' and button47['text'] == 'X' and button48['text'] == 'X'or
          button46['text'] == 'X' and button49['text'] == 'X' and button52['text'] == 'X'or
          button47['text'] == 'X' and button50['text'] == 'X' and button53['text'] == 'X'or
          button52['text'] == 'X' and button51['text'] == 'X' and button54['text'] == 'X'):
          winmat[1][2] = "X"

          
     if(button46['text'] == 'O' and button47['text'] == 'O' and button48['text'] == 'O'or
          button49['text'] == 'O' and button50['text'] == 'O' and button51['text'] == 'O'or
          button52['text'] == 'O' and button53['text'] == 'O' and button54['text'] == 'O'or
          button46['text'] == 'O' and button50['text'] == 'O' and button54['text'] == 'O'or
          button48['text'] == 'O' and button50['text'] == 'O' and button52['text'] == 'O'or
          button46['text'] == 'O' and button47['text'] == 'O' and button48['text'] == 'O'or
          button46['text'] == 'O' and button49['text'] == 'O' and button52['text'] == 'O'or
          button47['text'] == 'O' and button50['text'] == 'O' and button53['text'] == 'O'or
          button52['text'] == 'O' and button51['text'] == 'O' and button54['text'] == 'O'):
          winmat[1][2] = "O"


     if(button73['text'] == 'X' and button74['text'] == 'X' and button75['text'] == 'X'or
          button76['text'] == 'X' and button77['text'] == 'X' and button78['text'] == 'X'or
          button79['text'] == 'X' and button80['text'] == 'X' and button81['text'] == 'X'or
          button73['text'] == 'X'  and button77['text'] == 'X' and button81['text'] == 'X'or
          button75['text'] == 'X' and button77['text'] == 'X' and button79['text'] == 'X'or
          button73['text'] == 'X' and button74['text'] == 'X' and button75['text'] == 'X'or
          button73['text'] == 'X' and button76['text'] == 'X' and button79['text'] == 'X'or
          button74['text'] == 'X' and button77['text'] == 'X' and button80['text'] == 'X'or
          button79['text'] == 'X' and button78['text'] == 'X' and button81['text'] == 'X'):
          winmat[2][2] = "X"

          
     if(button73['text'] == 'O' and button74['text'] == 'O' and button75['text'] == 'O'or
          button76['text'] == 'O' and button77['text'] == 'O' and button78['text'] == 'O'or
          button79['text'] == 'O' and button80['text'] == 'O' and button81['text'] == 'O'or
          button73['text'] == 'O' and button77['text'] == 'O' and button81['text'] == 'O'or
          button75['text'] == 'O' and button77['text'] == 'O' and button79['text'] == 'O'or
          button73['text'] == 'O' and button74['text'] == 'O' and button75['text'] == 'O'or
          button73['text'] == 'O' and button76['text'] == 'O' and button79['text'] == 'O'or
          button74['text'] == 'O' and button77['text'] == 'O' and button80['text'] == 'O'or
          button79['text'] == 'O' and button78['text'] == 'O' and button81['text'] == 'O'):
          winmat[2][2] = "O"

     if (winmat[0][0] == "O" == winmat[0][1] == winmat[0][2] or
          winmat[1][0] == "O" == winmat[1][1] == winmat[1][2] or
          winmat[2][0] == "O" == winmat[2][1] == winmat[2][2] or
          winmat[0][0] == "O" == winmat[1][0] == winmat[2][0] or
          winmat[0][1] == "O" == winmat[1][1] == winmat[2][1] or
          winmat[0][2] == "O" == winmat[1][2] == winmat[2][2] or
         winmat[0][0] == "O" == winmat[1][1] == winmat[2][2] or
         winmat[0][2] == "O" == winmat[1][1] == winmat [2][0]) :
          if tkinter.messagebox.askyesno("Player O has won!",'Restart?') == True:
               restart_program()
          else:
               sys.exit()
               
     if (winmat[0][0] == "X" == winmat[0][1] == winmat[0][2] or
          winmat[1][0] == "X" == winmat[1][1] == winmat[1][2] or
          winmat[2][0] == "X" == winmat[2][1] == winmat[2][2] or
          winmat[0][0] == "X" == winmat[1][0] == winmat[2][0] or
          winmat[0][1] == "X" == winmat[1][1] == winmat[2][1] or
          winmat[0][2] == "X" == winmat[1][2] == winmat[2][2] or
         winmat[0][0] == "X" == winmat[1][1] == winmat[2][2] or
         winmat[0][2] == "X" == winmat [1][1] == winmat [2][0]) :
          
          if tkinter.messagebox.askyesno("Player X has won!",'Restart?') == True:
               restart_program()
          else:
               sys.exit()

button1 = Button(tk,text=" ",font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button1))
button1.grid(row=1,column=0,sticky = S+N+E+W)

button2 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button2))
button2.grid(row=1,column=1,sticky = S+N+E+W)

button3 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button3))
button3.grid(row=1,column=2,sticky = S+N+E+W)

button4 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button4))
button4.grid(row=2,column=0,sticky = S+N+E+W)

button5 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button5))
button5.grid(row=2,column=1,sticky = S+N+E+W)

button6 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button6))
button6.grid(row=2,column=2,sticky = S+N+E+W)

button7 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button7))
button7.grid(row=3,column=0,sticky = S+N+E+W)

button8 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button8))
button8.grid(row=3,column=1,sticky = S+N+E+W)

button9 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button9))
button9.grid(row=3,column=2,sticky = S+N+E+W)

button10 = Button(tk,text=" ",font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button10))
button10.grid(row=1,column=3,sticky = S+N+E+W)

button11 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button11))
button11.grid(row=1,column=4,sticky = S+N+E+W)

button12 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button12))
button12.grid(row=1,column=5,sticky = S+N+E+W)

button13 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button13))
button13.grid(row=2,column=3,sticky = S+N+E+W)

button14 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button14))
button14.grid(row=2,column=4,sticky = S+N+E+W)

button15 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button15))
button15.grid(row=2,column=5,sticky = S+N+E+W)

button16 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button16))
button16.grid(row=3,column=3,sticky = S+N+E+W)

button17 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button17))
button17.grid(row=3,column=4,sticky = S+N+E+W)

button18 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button18))
button18.grid(row=3,column=5,sticky = S+N+E+W)

button19 = Button(tk,text=" ",font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button19))
button19.grid(row=1,column=6,sticky = S+N+E+W)

button20 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button20))
button20.grid(row=1,column=7,sticky = S+N+E+W)

button21 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button21))
button21.grid(row=1,column=8,sticky = S+N+E+W)

button22 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button22))
button22.grid(row=2,column=6,sticky = S+N+E+W)

button23 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button23))
button23.grid(row=2,column=7,sticky = S+N+E+W)

button24 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button24))
button24.grid(row=2,column=8,sticky = S+N+E+W)

button25 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button25))
button25.grid(row=3,column=6,sticky = S+N+E+W)

button26 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button26))
button26.grid(row=3,column=7,sticky = S+N+E+W)

button27 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button27))
button27.grid(row=3,column=8,sticky = S+N+E+W)

button28 = Button(tk,text=" ",font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button28))
button28.grid(row=4,column=0,sticky = S+N+E+W)

button29 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button29))
button29.grid(row=4,column=1,sticky = S+N+E+W)

button30 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button30))
button30.grid(row=4,column=2,sticky = S+N+E+W)

button31 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button31))
button31.grid(row=5,column=0,sticky = S+N+E+W)

button32 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button32))
button32.grid(row=5,column=1,sticky = S+N+E+W)

button33 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button33))
button33.grid(row=5,column=2,sticky = S+N+E+W)

button34 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button34))
button34.grid(row=6,column=0,sticky = S+N+E+W)

button35 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button35))
button35.grid(row=6,column=1,sticky = S+N+E+W)

button36 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button36))
button36.grid(row=6,column=2,sticky = S+N+E+W)

button55 = Button(tk,text=" ",font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button55))
button55.grid(row=7,column=0,sticky = S+N+E+W)

button56 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button56))
button56.grid(row=7,column=1,sticky = S+N+E+W)

button57 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button57))
button57.grid(row=7,column=2,sticky = S+N+E+W)

button58 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button58))
button58.grid(row=8,column=0,sticky = S+N+E+W)

button59 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button59))
button59.grid(row=8,column=1,sticky = S+N+E+W)

button60 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button60))
button60.grid(row=8,column=2,sticky = S+N+E+W)

button61 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button61))
button61.grid(row=9,column=0,sticky = S+N+E+W)

button62 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button62))
button62.grid(row=9,column=1,sticky = S+N+E+W)

button63 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button63))
button63.grid(row=9,column=2,sticky = S+N+E+W)

button37 = Button(tk,text=" ",font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button37))
button37.grid(row=4,column=3,sticky = S+N+E+W)

button38 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button38))
button38.grid(row=4,column=4,sticky = S+N+E+W)

button39 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button39))
button39.grid(row=4,column=5,sticky = S+N+E+W)

button40 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button40))
button40.grid(row=5,column=3,sticky = S+N+E+W)

button41 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button41))
button41.grid(row=5,column=4,sticky = S+N+E+W)

button42 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button42))
button42.grid(row=5,column=5,sticky = S+N+E+W)

button43 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button43))
button43.grid(row=6,column=3,sticky = S+N+E+W)

button44 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button44))
button44.grid(row=6,column=4,sticky = S+N+E+W)

button45 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button45))
button45.grid(row=6,column=5,sticky = S+N+E+W)

button64 = Button(tk,text=" ",font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button64))
button64.grid(row=7,column=3,sticky = S+N+E+W)

button65 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button65))
button65.grid(row=7,column=4,sticky = S+N+E+W)

button66 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button66))
button66.grid(row=7,column=5,sticky = S+N+E+W)

button67 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button67))
button67.grid(row=8,column=3,sticky = S+N+E+W)

button68 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button68))
button68.grid(row=8,column=4,sticky = S+N+E+W)

button69 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button69))
button69.grid(row=8,column=5,sticky = S+N+E+W)

button70 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button70))
button70.grid(row=9,column=3,sticky = S+N+E+W)

button71 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button71))
button71.grid(row=9,column=4,sticky = S+N+E+W)

button72 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button72))
button72.grid(row=9,column=5,sticky = S+N+E+W)



button46 = Button(tk,text=" ",font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button46))
button46.grid(row=4,column=6,sticky = S+N+E+W)

button47 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button47))
button47.grid(row=4,column=7,sticky = S+N+E+W)

button48 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button48))
button48.grid(row=4,column=8,sticky = S+N+E+W)

button49 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button49))
button49.grid(row=5,column=6,sticky = S+N+E+W)

button50 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button50))
button50.grid(row=5,column=7,sticky = S+N+E+W)

button51 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button51))
button51.grid(row=5,column=8,sticky = S+N+E+W)

button52 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button52))
button52.grid(row=6,column=6,sticky = S+N+E+W)

button53 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button53))
button53.grid(row=6,column=7,sticky = S+N+E+W)

button54 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button54))
button54.grid(row=6,column=8,sticky = S+N+E+W)

button73 = Button(tk,text=" ",font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button73))
button73.grid(row=7,column=6,sticky = S+N+E+W)

button74 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button74))
button74.grid(row=7,column=7,sticky = S+N+E+W)

button75 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button75))
button75.grid(row=7,column=8,sticky = S+N+E+W)

button76 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button76))
button76.grid(row=8,column=6,sticky = S+N+E+W)

button77 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button77))
button77.grid(row=8,column=7,sticky = S+N+E+W)

button78 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button78))
button78.grid(row=8,column=8,sticky = S+N+E+W)

button79 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button79))
button79.grid(row=9,column=6,sticky = S+N+E+W)

button80 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button80))
button80.grid(row=9,column=7,sticky = S+N+E+W)

button81 = Button(tk,text=' ',font=('Times 20 bold'),bg='gray',fg='white',height=2,width=4,command=lambda:ttt(button81))
button81.grid(row=9,column=8,sticky = S+N+E+W)


tk.mainloop()
