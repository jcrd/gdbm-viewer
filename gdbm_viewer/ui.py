import math
from tkinter import *


class UI(Tk):
    @staticmethod
    def new_entry(root):
        return Entry(root, disabledforeground="black", disabledbackground="white")

    @staticmethod
    def new_state(root):
        return (UI.new_entry(root), UI.new_entry(root))

    def __init__(self, max_lines):
        super().__init__()

        self.title("gdbm-viewer")

        self.max_lines = max_lines
        self.frames = []
        self.state = []

    def set(self, d):
        self.clear()

        for i in range(math.ceil(len(d) / self.max_lines)):
            f = Frame(self)
            f.grid(row=0, column=i, sticky="n")
            self.frames.append(f)

        i = 0
        f = 0

        for p in sorted(d.items(), key=lambda p: p[0]):
            if i % self.max_lines == 0:
                i = 0
                frame = self.frames[f]
                f += 1

            state = UI.new_state(frame)

            for j in range(2):
                state[j].insert(END, str(p[j]))
                state[j].config(state=DISABLED)
                state[j].grid(row=i, column=j)

            self.state.append(state)

            i += 1

    def clear(self):
        for p in self.state:
            for j in range(2):
                p[j].config(state=NORMAL)
                p[j].delete(0, END)

        self.state = []
