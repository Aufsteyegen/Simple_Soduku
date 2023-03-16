import tkinter as tk

class SudBlock:
    """
    Creates one 9x9 Sudoku block, with Tkinter 'Entry' objects
    as inputs. Each 'Entry' only accepts int numbers 1-9.
    """
    def __init__(self, start_row, start_column):
        """
        SudBlock constructor.

        Parameters:
            start_row : int : uppermost row of block
            start_column : int : leftmost column of block
        """
        self.start_row = start_row
        self.start_col = start_column
        self._entries = self.sort_entries()

    def new_block(self):
        """
        Creates a new 3x3 block with event listeners bound to
        each Tkinter 'Entry' instance.

        Parameters: nothing beyond self

        Returns: None
        """
        row_assign, col_assign = self.start_row, self.start_col
        for i in range(1, 10):
            txt_var = tk.StringVar()
            entry = tk.Entry(validate='key', bg="white", width=2, justify='center',
                             textvariable=txt_var, font=('Roboto', 40))
            entry['validatecommand'] = (entry.register(self.testVal), '%P', '%d', '%i')
            entry.bind("<d>", self.next_widget), entry.bind("<a>", self.next_widget),
            entry.bind("<s>", self.next_widget), entry.bind("<w>", self.next_widget),
            entry.bind("<Button-1>", self.next_widget)
            entry.message = (row_assign, col_assign)
            self._entries[(row_assign, col_assign)] = [entry.grid(row=row_assign, column=col_assign), entry]
            if i % 3 == 0 and row_assign == self.start_row + 2:
                break
            if i % 3 == 0:
                row_assign += 1
                col_assign = self.start_col
            else:
                col_assign += 1
        return None

    def sort_entries(self):
        """
        Create a dictionary to store data from SudBlock entries,
        with keys sorted by row.

        Each entry's coordinate is stored as a tuple key,
        mapping to a list of the entry item and its associated
        Tkinter 'Entry' object.

        Parameters: nothing

        Returns: dict[tuple, list[int, Entry()]
        """
        cur_row, cur_col = (1, 1)
        sorted_entries = {}
        while cur_row < 12 and cur_col < 12:
            if cur_col == 4 or cur_col == 8:
                cur_col += 1
                continue
            sorted_entries[(cur_row, cur_col)] = None
            if cur_col == 11:
                cur_row += 1
                cur_col = 1
            else:
                cur_col += 1
        return sorted_entries

    def next_widget(self, event):
        print(event.widget.message)
        print(self._entries)
        global cur_row
        global cur_col
        if isinstance(event.widget.message, tuple) and event.keysym == '??':
            cur_row = event.widget.message[0]
            cur_col = event.widget.message[1]
        elif event.keysym == 'd':
            if cur_col == 3 or cur_col == 7:
                cur_col += 2
            elif cur_col == 11:
                cur_col = 1
            else:
                cur_col += 1
        elif event.keysym == 'a':
            if cur_col == 5 or cur_col == 9:
                cur_col -= 2
            elif cur_col == 1:
                cur_col = 11
            else:
                cur_col -= 1
        elif event.keysym == 's':
            if cur_row == 3 or cur_row == 7:
                cur_row += 2
            elif cur_row == 11:
                cur_row = 1
            else:
                cur_row += 1
        elif event.keysym == 'w':
            if cur_row == 5 or cur_row == 9:
                cur_row -= 2
            elif cur_row == 1:
                cur_row = 11
            else:
                cur_row -= 1
        next_entry = self._entries[(cur_row, cur_col)][1]
        next_entry.focus_set()
        return 'break'

    def testVal(self, entry_val, action_type, idx):
        if idx != '0' or len(entry_val) > 1:
            return False
        if action_type == '1':
            if not entry_val.isdigit() or int(entry_val) == 0:
                return False
        return True
