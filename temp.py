
from manim import *

class CubeSphereRotation(ThreeDScene):
    def construct(self):
        # Create a cube and a sphere
        cube = Cube()
        sphere = Sphere()

        # Position the sphere to the right of the cube
        sphere.shift(RIGHT * 3)

        # Set initial colors
        cube.set_color(BLUE)
        sphere.set_color(RED)

        # Prepare the scene
        self.set_camera_orientation(phi=45 * DEGREES, theta=45 * DEGREES)
        self.add(cube, sphere)
        self.wait(1)

        # Animate rotation around the y-axis
        self.play(Rotate(cube, angle=PI/2, axis=UP), Rotate(sphere, angle=PI/2, axis=UP), run_time=2)
        self.wait(1)

        # Further rotation around the x-axis
        self.play(Rotate(cube, angle=PI/2, axis=RIGHT), Rotate(sphere, angle=PI/2, axis=RIGHT), run_time=2)
        self.wait(1)

