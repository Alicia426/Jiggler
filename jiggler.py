"""Alicia426's mouse jiggler script"""
#!/usr/bin/python3

import multiprocessing
from os import system as cmd
from time import sleep as slp
from random import randrange as rdr
from tkinter import Tk, Label, Button, TclError


class JigglerUI:
    """UI Class for jiggler"""
    def __init__(self, master):
        self.master = master
        master.title("Linux Mouse Jiggler")
        self.realistic_button = Button(
            master,
            text="Jiggle Mouse (Realistic)",
            bg='#ffea70',
            fg='#16243d',
            font=("Ubuntu", 18),
            width=22,
            relief="raised",
            command=self.start_jiggle)
        self.realistic_button.pack(padx=10, pady=5)

        self.jiggle_button = Button(
            master,
            text="Stop Jiggling",
            bg='#ffea70',
            fg='#16243d',
            font=("Ubuntu", 18),
            width=22, relief="raised",
            command=self.stop_jiggle)
        self.jiggle_button.pack(padx=10, pady=5)

    def move_relative(self, scr_x, scr_y):
        """Moves the mouse with xdotool"""
        cmd(f'xdotool mousemove_relative {scr_x} {scr_y}')

    def keep_alive(self):
        """Randomizes mouse movement"""
        while True:
            self.move_relative(rdr(8), rdr(8))
            slp(rdr(10, 30))

    def start_jiggle(self):
        """Starts jiggle as a process"""
        try:
            self.proc.terminate() # pylint: disable=access-member-before-definition
            self.jiggle.destroy() # pylint: disable=access-member-before-definition
        except AttributeError:
            pass
        finally:
            self.proc = multiprocessing.Process( # pylint: disable=attribute-defined-outside-init
                target=self.keep_alive, args=())

            self.proc.start()
            self.jiggle = Label(self.master,  text="Currently Jigglin'", # pylint: disable=attribute-defined-outside-init
                                bg='#fccf03', fg='#16243d', font=("Ubuntu", 20))
            self.jiggle.pack(padx=10, pady=5)

    def stop_jiggle(self):
        """Stops jiggle as a process"""
        try:
            self.proc.terminate()
            self.jiggle.destroy()
        except TclError:
            pass
        # print('Jiggling Stopped')


if __name__ == "__main__":
    root = Tk()
    root['background'] = '#fccf03'
    ui = JigglerUI(root)
    root.mainloop()
    ui.stop_jiggle()
