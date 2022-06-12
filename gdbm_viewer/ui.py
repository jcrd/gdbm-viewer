from tkinter import *


class UI(Tk):
    def __init__(self):
        super().__init__()

        self.title("gdbm-viewer")
        self.state = []

    def new_entry(self):
        return Entry(self, disabledforeground="black", disabledbackground="white")

    def set(self, d):
        self.clear()
        i = 0

        for p in sorted(d.items(), key=lambda p: p[0]):
            state = (self.new_entry(), self.new_entry())
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
