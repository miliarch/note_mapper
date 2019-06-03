#!/usr/bin/env python3
from PIL import Image, ImageDraw
from note_mapper.guitar import Neck
from note_mapper.image import Canvas

def main():
    # Define guitar attributes and create objects
    guitar_neck = Neck(width=12, nut_width=4, fret_count=12, scale=.75)
    guitar_neck.update_canvas_padding(20, 20, 20, 20)
    guitar_neck.update_canvas_margins(20, 20, 20, 20)

    # Define image attributes
    canvas_width = guitar_neck.canvas.width
    canvas_width += guitar_neck.canvas.margin_left
    canvas_width += guitar_neck.canvas.margin_right
    canvas = Canvas(canvas_width, 1024)
    
    image = Image.new('RGB', (canvas.width, canvas.height), '#FFF')
    image.paste(guitar_neck.image, box=guitar_neck.canvas.image_box)
    image.show()

if __name__ == '__main__':
    main()