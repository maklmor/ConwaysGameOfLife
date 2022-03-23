from typing import List


class Conway:
  def __init__(self, state):
    self.state = state


  def get_state(self) -> List[List[int]]:
    state = self.state
    self.change_state()
    return state


  def change_state(self) -> None:
    self.state = self.next_gen(self.state)


  def next_gen(self, cells):
      next_state = []
      for y in range(len(cells)):
          next_row = []
          for x in range(len(cells[y])):
              # determine the next state of this cell
              neighbours = self.survey_peers(cells, x, y)
              if neighbours > 3 or neighbours < 2:
                  state = 0
              elif neighbours == 3:
                  state = 1
              else:
                  # preserve previous state
                  state = cells[y][x]

              next_row.append(state)
          next_state.append(next_row)
      return next_state


  def survey_peers(self, arr: list, x: int, y: int) -> int:
      """returns the number of live neighbouring cells"""
      count = 0
      # pre-made template to survey all possible neighbours
      neighbours = ((y-1, x-1), (y-1, x), (y-1, x+1), # upper row
                    (y, x-1),             (y, x+1),   # adjacent cells
                    (y+1, x-1), (y+1, x), (y+1, x+1)) # cells below

      # loops through all neighbouring cells and checks those that are inside our NxM plane
      for r, c in neighbours:
          if r >= 0 and r < len(arr) and c >= 0 and c < len(arr[0]):
              count += arr[r][c]
      return count