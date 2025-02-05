from manim import *

class functions(Scene):
    def construct(self):
      grid = NumberPlane()
      self.play(FadeIn(grid))
      grid.play(Write())
      self.wait(2)
      self.play(FadeOut(grid))
      self.wait()