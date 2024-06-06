from manim import *

class BarChartExample(Scene):
    def construct(self):
        # Data for the bar chart
        data = [2, 5, 3, 6]  # Sample data values
        categories = ["A", "B", "C", "D"]  # Categories for the data

        # Create a bar chart
        bar_chart = BarChart(
            values=data,
            bar_names=categories,
            bar_colors=[BLUE, YELLOW, GREEN, RED],
            y_range=[0, 10, 1],  # Setting the range for the y-axis
            y_length=6,  # The vertical length of the bars
            x_length=6,  # The horizontal spacing of the bars
        )

        # Title for the bar chart
        title = Title("Bar Chart Example")

        # Animate the creation of the bar chart
        self.play(
            Write(title),
            Create(bar_chart),
            run_time=4
        )
        self.wait(2)

