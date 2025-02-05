from __future__ import annotations
from manim import*

class Video1(Scene):
    def construct(self):
        s1=Text(" 2023年全国高中数学联赛福建省预赛 \\第一题", color=YELLOW).to_edge(UP)
        line = Line(LEFT*7, RIGHT*7, color=WHITE).next_to(s1, DOWN, buff=0.3)
       
        self.play(Write(s1,line))
        self.wait()
        self.play(Write(s2),run_time=2.5)
        
        

