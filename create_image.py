#!/usr/bin/env python3
from PIL import Image, ImageDraw
from note_mapper.guitar import Neck
from note_mapper.image import Canvas, Fretboard


def main():
    # Define guitar neck and initialize attributes
    string_note_sequence = ('E', 'B', 'G', 'D', 'A', 'D')
    guitar_neck = Neck(
        length=15,
        nut_width=2,
        fret_count=11,
        string_note_sequence=string_note_sequence)

    # Initialize fretboard for visual rendering
    fretboard = Fretboard(guitar_neck, scale=1)
    fretboard.update_canvas_padding(20, 20, 20, 20)
    fretboard.update_canvas_margins(20, 20, 20, 20)

    # Define parent canvas attributes
    canvas_width = fretboard.width
    canvas_width += fretboard.margin_left + fretboard.margin_right
    canvas = Canvas(canvas_width, 1024)

    # Create parent image
    image = Image.new('RGB', (canvas.width, canvas.height), '#FFF')

    # Paste fretboard image within parent image
    image.paste(fretboard.image, box=fretboard.image_box)

    # Display final image
    image.show()


if __name__ == '__main__':
    main()
