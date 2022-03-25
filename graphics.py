from conway import Conway
from tkinter import Canvas, Tk
from config import SCALE, FRAME_LENGTH, STARTING_STATE


class Animator:
    """Dummy class in order to preserve independence of Conway class from graphics"""

    def __init__(self, root, data_source):
        self.root = root  # root window
        self.data_source = data_source  # data_source should be a Object that implements get_state() method
        self.paused = False

    def change_paused_state(self, event) -> None:
        self.paused = False if self.paused else True
        self.draw()

    def draw(self):
        if not self.paused:
            state = self.data_source.get_state()
            for y in range(len(state)):
                for x in range(len(state[y])):
                    color = "black" if state[y][x] else "white"
                    canvas.create_rectangle(
                        x * SCALE,
                        y * SCALE,
                        (x + 1) * SCALE,
                        (y + 1) * SCALE,
                        fill=color,
                    )
            self.root.after(FRAME_LENGTH, self.draw)


if __name__ == "__main__":
    root = Tk()
    canvas = Canvas(root, height=500, width=500)
    canvas.pack()

    # Main animation loop
    conway = Conway(STARTING_STATE)
    animator = Animator(root, conway)
    animator.draw()

    root.bind("<space>", animator.change_paused_state)
    root.mainloop()
