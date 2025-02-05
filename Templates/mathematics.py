from manim import *

class mathematics(Scene):
    def construct(self):
        text = Text("我思故我在")
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))
        
