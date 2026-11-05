from matplotlib.sankey import UP

from manim import *


class Staff(VGroup):
    """A reusable five-line musical staff."""

    def __init__(
        self,
        width=8.0,
        line_spacing=0.3,
        color=WHITE,
        stroke_width=2,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.width = width
        self.line_spacing = line_spacing
        self.color = color

        # Five equally spaced horizontal lines, centred around y = 0.
        self.lines = VGroup()

        for i in range(5):
            y = (i - 2) * line_spacing

            line = Line(
                start=[-width / 2, y, 0],
                end=[width / 2, y, 0],
                color=color,
                stroke_width=stroke_width,
            )

            self.lines.add(line)

        self.add(self.lines)



class NoteGlyph(VGroup):
    def __init__(
        self,
        x=0,
        y=0,
        filled=True,
        stem=True,
        **kwargs
    ):
        super().__init__(**kwargs)

        # Draw the notehead
        head = Ellipse(
            width=0.24,
            height=0.16,
            color=WHITE,
            fill_color=WHITE,
            fill_opacity=1 if filled else 0,
            stroke_width=2,
        )

        head.rotate(-20 * DEGREES)
        self.add(head)

        # Add a stem
        if stem:
            stem_line = Line(
                [0.09, 0.02, 0],
                [0.09, 0.65, 0],
                stroke_width=2,
            )
            self.add(stem_line)

        # Position the entire note
        self.move_to([x, y, 0])
