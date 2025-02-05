from manim import *
class MovingFrameBox(Scene):
    def construct(self):
        text1=MathTex(r"\zeta(s)=\sum_{n=1}^{\infty }\frac{1}{n^s}")
        text2=Text("我思故我在 \\ --笛卡尔",font="Songti TC")
        self.play(Write(text1),run_time=1)
        self.wait(1)
        self.play(ReplacementTransform(text1,text2),run_time=1)
        self.wait(1)
        self.play(FadeOut(text2))
        self.wait(1)