from builtins import range

import Main.ttmini

from Main import tk


class ttLarge:
    def __init__(self):
        self.winner = ""
        self.board = [[Main.ttmini() for j in range (3)] for i in range (3)]


tk.mainloop()