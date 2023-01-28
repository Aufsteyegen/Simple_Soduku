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
#stats = ttk.Label(text=f"Wins: {wins} | Plays: {plays} | Fastest Win: {fastest_win}",
#                  font=('Roboto', 20))

#stats.grid(row=0, column=0, sticky='ew')

def testVal(entry_val, action_type, idx):
    if idx != '0' or len(entry_val) > 1:
        return False
    if action_type == '1':
        if not entry_val.isdigit() or int(entry_val) == 0:
            return False
    return True


entries = {}
all_entries = []

def sort_entries():
    cur_row, cur_col = (1, 1)
    sorted_entries = {}
    while cur_row <= 9 and cur_col <= 9:
        sorted_entries[(cur_row, cur_col)] = None
        if cur_col == 10:
            cur_row += 1
            cur_col = 1
        else:
            cur_col += 1
    return sorted_entries

class SudBlock:
    def __init__(self, start_row, start_column):
        self.start_row = start_row
        self.start_col = start_column
        self.cur_row = start_row
        self.cur_col = start_column

    def next_widget(self, event):
        print(self.cur_row, self.cur_col)
        new_row, new_col = self.cur_row, self.cur_col
        if event.keysym == 'd':
            next_entry = entries[(new_row, new_col + 1)][1]
        elif event.keysym == 'a':
            next_entry = entries[(new_row, new_col - 1)][1]
        elif event.keysym == 's':
            next_entry = entries[(new_row + 1, new_col)][1]
        else:
            next_entry = entries[(new_row - 1, new_col)][1]
        next_entry.focus_set()

    def new_block(self):
        row_assign, col_assign = self.start_row, self.start_col
        for i in range(1, 10):
            txt_var = tk.StringVar()
            entry = tk.Entry(validate='key', bg="white", width=2, justify='center',
                             textvariable=txt_var, font=('Roboto', 40))
            entry['validatecommand'] = (entry.register(testVal), '%P', '%d', '%i')
            entry.bind("<d>", self.next_widget), entry.bind("<a>", self.next_widget),
            entry.bind("<s>", self.next_widget), entry.bind("<w>", self.next_widget)
            entries[(row_assign, col_assign)] = [entry.grid(row=row_assign, column=col_assign), entry]
            if i % 3 == 0 and row_assign == self.start_row + 2:
                break
            if i % 3 == 0:
                row_assign += 1
                col_assign = self.start_col
            else:
                col_assign += 1
            self.cur_row = row_assign
            self.cur_col = col_assign
        return None

ttk.Frame(window, relief='flat').grid(row=1, column=4, rowspan=10, ipadx=2, ipady=30, sticky="ns")
ttk.Frame(window, relief='flat').grid(row=1, column=8, rowspan=10, ipadx=2, ipady=30, sticky="ns")
SudBlock(1, 1).new_block()
SudBlock(1, 5).new_block()
SudBlock(1, 9).new_block()

print(entries)
# runs tkinter event loop
window.mainloop()
