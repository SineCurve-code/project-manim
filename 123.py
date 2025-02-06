from manim import*
class video1(Scene):
def construct(self):
f=FunctionCraph(lambda x:x**2+x*3+1)
g=NumberPlane()
self.add(f,g)
