import tkinter as tk
import tkinter.ttk as ttk
from sudblock import SudBlock
from play_logic import *


# main window
window = tk.Tk()
window.geometry("630x680")
window.title("Simple Sudoku")


#player data
wins = 0
plays = 0
fastest_win = 0

#widgets
stats = ttk.Label(text=f"Wins: {wins} | Plays: {plays} | Fastest Win: {fastest_win}",
                  font=('Roboto', 20))

stats.grid(row=0, column=3, rowspan=1, columnspan=8, pady=20, padx=20)

# cursor within Sudoku grid;
# persists across SudBlock instances
cur_row, cur_col = 0, 0

ttk.Frame(window, relief='flat').grid(row=1, column=0, rowspan=12, ipadx=10, ipady=30, sticky="nsw")
ttk.Frame(window, relief='flat').grid(row=1, column=12, rowspan=12, ipadx=10, ipady=30, sticky="nse")
ttk.Frame(window, relief='flat').grid(row=1, column=4, rowspan=12, ipadx=2, ipady=30, sticky="ns")
ttk.Frame(window, relief='flat').grid(row=1, column=8, rowspan=12, ipadx=2, ipady=30, sticky="ns")
ttk.Frame(window, relief='flat').grid(row=4, column=1, columnspan=12, ipady=2, sticky="ew")
ttk.Frame(window, relief='flat').grid(row=8, column=1, columnspan=12, ipady=2, sticky="ew")
ttk.Frame(window, relief='flat').grid(row=12, column=1, columnspan=12, ipady=2, sticky="ew")

def render_grid():
    row, col = 1, 1
    while row <= 9 and col <= 9:
        SudBlock(row, col).new_block()
        if col != 9:
            col += 4
        else:
            row += 4
            col = 1

render_grid()


# runs tkinter event loop
window.mainloop()
