from manim import *
class Try(Scene):
    def construct(self):
      c = Circle(fill_opacity=1)
      s = Square(color=YELLOW,fill_opacity=1)
      self.play(FadeIn(c))
      self.wait()
      self.play(ReplacementTransform(c,s),run_time=2)
      self.wait()
      self.play(FadeOut(s))
      self.wait()