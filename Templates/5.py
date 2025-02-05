from manim import *

class VectorScene(Scene):
    def construct(self):
        # Define the mathematical expression using LaTeX syntax
        expression = Tex(
            "\\frac{d}{dt}\\left[ \\begin{array}{c} x \\\\ y \\end{array} \\right]="
            "f\\left( x,y \\right),"
            "\\\\"
            "\\left[ \\begin{array}{c} x \\\\ y \\end{array} \\right]="
            "\\left[ \\begin{array}{c} x_{0} \\\\ 0 \\end{array} \\right],"
            "\\\\"
            "t=0 \\ldots 5"
        )
        
        # Play the animation to write the expression on the screen
        self.play(Write(expression))
        
        # Wait for a moment to let the viewer see the expression
        self.wait()
        
        # Play the animation to fade out the expression
        self.play(FadeOut(expression))
