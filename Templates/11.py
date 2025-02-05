from manim import *

class BasicUsage(Scene):
    def construct(self):
        func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3
        k=Text("正弦曲线-SineCurve",font="Songti SC")
        self.add(StreamLines(func),k)