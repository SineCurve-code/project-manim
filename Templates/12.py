from manim import*
class M(Scene):
    def construct(self):
        v= lambda pos:(pos[0])
        r=MathTex(r"\zeta (s)=\sum_{n=0}^{\infty}\frac{1} {n^s}").scale(2.5)
        self.add(r)