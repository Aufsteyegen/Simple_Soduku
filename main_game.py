import tkinter as tk
import tkinter.ttk as ttk
from play_logic import *


# main window
window = tk.Tk()
window.geometry("630x630")
window.title("Simple Sudoku")

#player data
wins = 0
plays = 0
fastest_win = 0

#widgets
stats = ttk.Label(text=f"Wins: {wins} | Plays: {plays} | Fastest Win: {fastest_win}",
                  font=('Arial', 20))

# stats.pack(pady=20)


def validate_entry(entry):
    var = entry.get()
    print(var + '1')

def doSomething(event):
    print(event.char)



class SudBlock:
    def __init__(self, start_row, start_column):
        self.start_row = start_row
        self.start_column = start_column

    def new_block(self):
        entries = {}
        cur_row, cur_column = self.start_row, self.start_column
        for i in range(1, 10):
            txt_var = tk.StringVar()
            entry = tk.Entry(validatecommand=validate_entry(txt_var), validate='key', bg="white", width=2,
                             justify='center', textvariable=txt_var, font=('Arial', 40))
            entry.bind("<Key>", doSomething)
            entries[(cur_row, cur_column)] = entry.grid(row=cur_row, column=cur_column)
            if i % 3 == 0:
                cur_row += 1
                cur_column = self.start_column
            else:
                cur_column += 1
        return entries

SudBlock(1, 1).new_block()




#adds widgets to window


#events







# runs tkinter event loop
window.mainloop()

