from tkinter import * 

import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe")

click = True
counter=0

def checker(buttons):
        global click
        global counter
        if buttons["text"] == " " and click == True:
                counter = counter + 1
                buttons["text"] = "X"
                click = False
            
        elif buttons["text"] == " " and click == False:
                counter = counter + 1
                buttons["text"] = "O"
                click = True
        if(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
          button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
          button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
          button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
          button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
          button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
          button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
          button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" ):
            
            tkinter.messagebox.showinfo("Winner X", "You have just won a game")
            exit()
                       
        elif(button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
            button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
            button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
            button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or
            button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
            button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
            button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
            button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" ):
             tkinter.messagebox.showinfo("Winner O", "You have just won a game")
             exit()
        if counter == 9:
                tkinter.messagebox.showinfo("DRAW!","It's a Draw!")
                exit()

FontStyle = ('Times 20 bold')

buttons=StringVar()

button1 = Button(tk,text=" ",font=FontStyle, height = 5, width =10, command=lambda:checker(button1))

button1.grid(row=1, column=0)

button2 = Button(tk,text=" ",font=FontStyle, height = 5, width =10, command=lambda:checker(button2))

button2.grid(row=1, column=1)

button3 = Button(tk,text=" ",font=FontStyle, height = 5, width =10, command=lambda:checker(button3))

button3.grid(row=1, column=2)

button4 = Button(tk,text=" ",font=FontStyle, height = 5, width =10, command=lambda:checker(button4))

button4.grid(row=2, column=0)

button5 = Button(tk,text=" ",font=FontStyle, height = 5, width =10, command=lambda:checker(button5))

button5.grid(row=2, column=1)

button6 = Button(tk,text=" ",font=FontStyle, height = 5, width =10, command=lambda:checker(button6))

button6.grid(row=2, column=2)

button7 = Button(tk,text=" ",font=FontStyle, height = 5, width =10, command=lambda:checker(button7))

button7.grid(row=3, column=0)

button8 = Button(tk,text=" ",font=FontStyle, height = 5, width =10, command=lambda:checker(button8))

button8.grid(row=3, column=1)

button9 = Button(tk,text=" ",font=FontStyle, height = 5, width =10, command=lambda:checker(button9))

button9.grid(row=3, column=2)

tk.mainloop()
