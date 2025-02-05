from manim import *

class ShowGraph(Scene): 
    def construct(self): 
        print("dot = Dot()")
        dot = Dot()
        self.wait(2)

        print("dot.to_edge(UL)")
        dot.to_edge(UL)
        self.play(FadeIn(dot))
        self.wait(2)

        print("text = TextMobject(\"text\")")
        text = Text,  Mobject("text")
        self.wait(2)

        print("text.to_corner(UP)")
        text.to_corner(UP)
        self.play(Write(text))
        self.wait(2)
        Scene=0 
        Dot=1
        UL=2
        