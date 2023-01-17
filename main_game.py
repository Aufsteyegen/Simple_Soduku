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
                  font=('Roboto', 20))

# stats.pack(pady=20)

def testVal(entry_val, action_type, idx):
    if idx != '0':
        return False
    if action_type == '1':
        if not entry_val.isdigit() or int(entry_val) == 0:
            return False
    return True

class SudBlock:
    def __init__(self, start_row, start_column):
        self.start_row = start_row
        self.start_column = start_column

    def next_widget(self, event):
        if event.keysym == 'd':
            event.widget.tk_focusNext().focus()
        elif event.keysym == 'a':
            event.widget.tk_focusPrev().focus()
        elif event.keysym == 's':
            event.widget.tk_focusNext().tk_focusNext().tk_focusNext().focus()
        else:
            event.widget.tk_focusPrev().tk_focusPrev().tk_focusPrev().focus()

    def new_block(self):
        entries = {}
        cur_row, cur_column = self.start_row, self.start_column
        for i in range(1, 10):
            txt_var = tk.StringVar()
            entry = tk.Entry(validate='key', bg="white", width=2, justify='center',
                             textvariable=txt_var, font=('Roboto', 40))
            entry['validatecommand'] = (entry.register(testVal), '%P', '%d', '%i')
            entry.bind("<d>", self.next_widget), entry.bind("<a>", self.next_widget)
            entry.bind("<s>", self.next_widget), entry.bind("<w>", self.next_widget)
            entries[(cur_row, cur_column)] = entry.grid(row=cur_row, column=cur_column)
            if i % 3 == 0:
                cur_row += 1
                cur_column = self.start_column
            else:
                cur_column += 1
        return entries

SudBlock(1, 1).new_block(), SudBlock(1, 4).new_block()
SudBlock(1, 7).new_block(), SudBlock(4, 1).new_block()
SudBlock(4, 4).new_block(), SudBlock(4, 7).new_block()
SudBlock(7, 1).new_block(), SudBlock(7, 4).new_block()
SudBlock(7, 7).new_block()




#adds widgets to window


#events







# runs tkinter event loop
window.mainloop()

