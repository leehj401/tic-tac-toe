from tkinter import *
import tkinter.messagebox

def winning() :      
      x = 0           
      #row checking      
      while x<=6 :            
            if list[x]["text"] == list[x+1]["text"] == list[x+2]["text"] != "     ":
                  End(1)            
            x = x + 3
      x = 0
      #col checking      
      while x<=2 :            
            if list[x]["text"] == list[x+3]["text"] == list[x+6]["text"] != "     " :                  
                  End(1)            
            x = x + 1
      #dia checking      
      if list[0]["text"] == list[4]["text"] == list[8]["text"] != "     " :
            End(1)                  
      if list[2]["text"] == list[4]["text"] == list[6]["text"] != "     " :
            End(1)      
            
def End(win) :      
      global player      
      if win == 1:            
            if player == "X" :                  
                  player = "O"            
            else :                 
                  player = "X"
            tkinter.messagebox.showinfo("Game Over","Winner is " + player)
            quit()      
      if win == 2:            
            tkinter.messagebox.showinfo("Game Over", " TIE")            
            quit()
def checked(i) :      
      global player      
      button = list[i]            
      if button["text"] != "     " :            
            return      
      button["text"] = player       
      button["bg"] = "yellow"
      if player == "X" :            
            player = "O"            
            button["bg"] = "yellow"      
      else :            
            player = "X"            
            button["bg"] = "lightgreen"                  
      winning()
      
window = Tk()player = "X"list= []
for i in range(9) :      
      b = Button(window, text="     ", command=lambda k=i: checked(k))      
      b.grid(row=i//3, column=i%3)      list.append(b)

window.mainloop()
