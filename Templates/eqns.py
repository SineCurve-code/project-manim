from manim import *
class Functions(ThreeDScene) :
    def construct(self):
        n = NumberPlane()
        axes = ThreeDAxes()
        p= Surface(lambda u,v:
                   np.array(
                    [np.cos(2*u)*np.sin(3*v),
                     np.sin(3*u)*np.cos(2*v),
                     np.cos(4*u)]),
                     v_range=[0,PI],u_range=[-PI, PI],
                     checkerboard_colors=[BLUE_C,BLUE_D])
        axes.add_coordinates()
        s=Surface(lambda u, v:
                   np.array(
                    [1.5 * np.cos(u) * np.cos(v),
                     1.5 * np.cos(u) * np.sin(v),
                     1.5 * np.sin(u)]),
                     v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
                     checkerboard_colors=[RED_D, RED_E], 
                     resolution=(15, 32))
        self.set_camera_orientation(phi=70*DEGREES,theta=30*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.7)
        self.play(Create(n),Create(axes)) 
        self.play(Write(s))
        self.wait()
        self.play(Unwrite(s))
        self.wait(0.5)
        self.play(Write(p))
        self.wait()
        