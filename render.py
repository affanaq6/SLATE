import os
import subprocess
import tempfile

# Define the dictionary containing prompt keywords and corresponding Manim code examples
examples = {
    "square": """
from manim import *

class DrawSquare(Scene):
    def construct(self):
        # Create a square
        square = Square()
        # Set color and line width
        square.set_fill(BLUE, opacity=0.5)
        square.set_stroke(color=WHITE, width=4)

        # Show creation of the square
        self.play(Create(square))
        self.wait(1)
""",
    "circle": """
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
"""
}

def get_manim_code(prompt):
    # Search for matching prompt keywords in the examples
    for keyword, manim_code in examples.items():
        if keyword in prompt.lower():
            return manim_code
    return None

def render_video(manim_code):
    # Specify the output directory where the video will be rendered
    output_directory = "D:/slate/media/videos/"
    video_filename = "custom_video.mp4"  # Custom video filename

    # Create a temporary directory to execute Manim code
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a temporary Manim script file
        temp_manim_script = os.path.join(temp_dir, "temp_manim_script.py")
        with open(temp_manim_script, "w") as script_file:
            script_file.write(manim_code)

        # Execute Manim command to render the video
        subprocess.run(['manim', temp_manim_script, '-o', output_directory, '-n', video_filename])

def main():
    user_prompt = input("Enter your prompt:")

    # Get corresponding Manim code
    manim_code = get_manim_code(user_prompt)

    if manim_code:
        # Render the video
        render_video(manim_code)
        print("Video rendered successfully!")
    else:
        print("No matching Manim code found for the prompt.")

if __name__ == "__main__":
    main()
