from manim import *

class SineWave3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()  # Create a three dimensional coordinate axis system. 

        sineWave = ParametricFunction(lambda u : np.array([
            u,np.sin(u),0]),t_range=[0,TAU],color=BLUE).fade()  # Creates function to represent sine wave

        grid = NumberPlane(x_radius =10, z_radius=5).fade(opacity=.5) # creates the grid plane

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.play(Create(axes), Create(grid))  # Creates axes and grid simultaneously
        self.wait(.69)                                   

        self.play(ShowCreation(sineWave)) # Shows Sine wave animation
        self.wait()