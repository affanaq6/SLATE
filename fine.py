from manim import *

class DrawCircle(Scene):
    def construct(self):
        # Create a circle
        circle = Circle()
        # Set color and line width
        circle.set_fill(PINK, opacity=0.5)
        circle.set_stroke(color=WHITE, width=4)

        # Show creation of the circle
        self.play(Create(circle))
        self.wait(1)
