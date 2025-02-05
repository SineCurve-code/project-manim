from manim import *

class ScaleVectorFieldFunction(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[-2]) * RIGHT + np.cos(pos[1]) * UP
        fc= lambda pos: np.sin(pos[1]* LEFT + np.cos(pos[1] ) *DOWN)
        vector_field = ArrowVectorField(func,color=GREEN)
        vct2=ArrowVectorField(fc,color=BLUE)
        self.add(vector_field)
        func = VectorField.scale_func(func, 0.5)
        self.play(vector_field.animate.become(ArrowVectorField(func)))
        self.play(vector_field.animate.become(ArrowVectorField(fc)))
        self.wait()