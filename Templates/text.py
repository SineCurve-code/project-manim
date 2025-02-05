from manim import *
class TransformExample(Scene):
    def construct(self):
        A = Text("Text-A").scale(3)
        B = Text("Text-B").scale(3)
        C = Text("C-Text").scale(3)

        self.add(A)
        self.wait()
        self.play(Transform(A, B))
        self.wait()
        self.play(Transform(A, C)) # notice here
        self.wait()