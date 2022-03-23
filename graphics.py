from conway import Conway
from tkinter import Canvas, Tk

SCALE = 100
FRAME_LENGTH = 400 # in ms
starting_state = [
  [1,0,1,0,1],
  [0,1,0,1,0],
  [1,0,1,0,1],
  [0,1,0,1,0],
  [1,0,1,0,1]
  ]

class Animator:
  """Dummy class in order to preserve independence of Conway class from graphics"""
  def __init__(self, root, data_source):
      self.root = root # root window
      self.data_source = data_source # data_source should be a Object that implements get_state() method

  def draw(self):
    state = self.data_source.get_state()
    for y in range(len(state)):
      for x in range(len(state[y])):
        color = "black" if state[y][x] else "white"
        canvas.create_rectangle(x * SCALE, y * SCALE, (x+1) * SCALE, (y+1) * SCALE, fill=color)
    self.root.after(FRAME_LENGTH, self.draw)


if __name__=="__main__":
  root = Tk()
  canvas = Canvas(root, height=500, width=500)
  canvas.pack()

  # Main animation loop
  conway = Conway(starting_state)
  animator = Animator(root, conway)
  root.after(FRAME_LENGTH, animator.draw)

  root.mainloop()