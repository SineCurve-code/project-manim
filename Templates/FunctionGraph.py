from manim import *

class PlotParametricFunction(Scene):
    def construct(self):
        self.camera
        func = ParametricFunction(lambda t:(np.sin(2*t),np.sin(3*t),0),t_range=[0,TAU], )
        z=NumberPlane()
        self.play(Write(z))
        self.play(self.camera.move_to(func))
        self.play(Write(func),run_time=4)
        