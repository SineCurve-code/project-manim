from manim import *
class 漫士沉思录(Scene):
    def construct(self):
        m=Text("M","athematic","S")
        m[0].set_color(BLUE)
        m[2].set_color(MAROON_A)
        ms= Text("漫士沉思录",font="Songti SC",color=YELLOW).scale(1.5)
        self.play(Write(m),run_time=1)
        self.wait(0.5)
        self.play(m[0].animate.shift(RIGHT * 3+UP*2),
            m[2].animate.shift(LEFT * 3+UP*1.8),FadeOut(m[1]),DrawBorderThenFill(ms))
        self.wait()
