from manim import *
class 圆(Scene) :
    def construct(self):
        c=Circle(radius=2,color=BLUE)
        d=Dot()
        t=MathTex("P").next_to(d,DR)
        line=Line([2,0,0],[-2,0,0],color=GREEN)
        line2=Line([2*0.866025,1,0],[-2*0.7071,-2*0.7071,0],color=GREEN)
        line3=Line([2*0.98901,-2*0.1478,0],[2*0.84245,2*0.53877,0],color=GREEN)
        self.play(Write(c)) #显现一个圆
        self.play(Write(d)) #标注圆心
        self.wait()
        self.play(Write(t),run_time=0.5)
        self.wait()
        self.play(Write(line))#l1
        self.wait()
        self.play(ReplacementTransform(line,line2))
        self.wait()
        self.play(ReplacementTransform(line2,line3))
        self.wait()
        self.play(Uncreate(line3))
        self.wait()
        