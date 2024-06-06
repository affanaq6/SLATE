import os
import subprocess
import difflib

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
    # Write Manim code to a temporary file
    with open('temp_manim_code.py', 'w') as file:
        file.write(manim_code)

    # Execute Manim command to render the video
    subprocess.run(['manim', 'temp_manim_code.py'])

    # Remove temporary file
    os.remove('temp_manim_code.py')

def main():
    while True:
        # Prompt user for input
        user_prompt = input("Enter your prompt: ")

        # Get corresponding Manim code
        manim_code = get_manim_code(user_prompt)

        if manim_code:
            print("Manim Code:", manim_code)

            # Render the video
            render_video(manim_code)
        else:
            print("No matching Manim code found for the prompt.")

        # Ask user if they want to continue
        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
