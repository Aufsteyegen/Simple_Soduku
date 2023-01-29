import tkinter as tk
import tkinter.ttk as ttk
from sudblock import SudBlock
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

# cursor within Sudoku grid;
# persists across SudBlock instances
cur_row, cur_col = 0, 0

ttk.Frame(window, relief='flat').grid(row=1, column=4, rowspan=10, ipadx=2, ipady=30, sticky="ns")
ttk.Frame(window, relief='flat').grid(row=1, column=8, rowspan=10, ipadx=2, ipady=30, sticky="ns")
SudBlock(1, 1).new_block()
SudBlock(1, 5).new_block()
SudBlock(1, 9).new_block()

# runs tkinter event loop
window.mainloop()
