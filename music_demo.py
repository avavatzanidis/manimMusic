from manim import *
from music_data import MusicalNote
from music_objects import NoteGlyph


class MusicalStaff(Scene):
    def construct(self):
        # Create a five-line staff
        staff = VGroup()

        for i in range(5):
            y = i * 0.3

            staff.add(
                Line(
                    LEFT * 4 + UP * y,
                    RIGHT * 4 + UP * y,
                )
            )

        # Create several reusable note objects
        notes = VGroup(
            NoteGlyph(x=-2, y=0.0),
            NoteGlyph(x=-1, y=0.15),
            NoteGlyph(x=0, y=0.3),
            NoteGlyph(x=1, y=0.45),
            NoteGlyph(x=2, y=0.6),
        )

        # Animate the staff, then the notes
        self.play(Create(staff))
        self.play(
            LaggedStart(
                *[FadeIn(note) for note in notes],
                lag_ratio=0.2,
            )
        )

        self.wait(2)


        # Part 2: Create a MusicalNote object and print its details
        note = MusicalNote(
            pitch="C4",
            start_beat=0,
            duration=1,
        )

        print(note)

        # The visual representation is a separate object.
        glyph = NoteGlyph(x=0, y=0)

        self.play(FadeIn(glyph))
        self.wait()