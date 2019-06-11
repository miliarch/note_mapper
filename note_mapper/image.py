""" image - collection of classes and functions used in drawing component
parts of musical instruments on a canvas
"""
from PIL import Image, ImageDraw


class Canvas:
    """Canvas - collection of dimensions used for drawing"""
    image_box = (0, 0)

    def __init__(self, width, height):
        """Initialize Canvas. Available arguments:
            - width: canvas width in pixels
            - height: canvas height in pixels"""
        self.width = width
        self.height = height
        self.set_margins(0, 0, 0, 0)
        self.set_padding(0, 0, 0, 0)

    def pack_margins(self):
        """Update self.margins to match current padding* attributes"""
        self.margins = (
            self.margin_top,
            self.margin_right,
            self.margin_bottom,
            self.margin_left)

    def pack_padding(self):
        """Update self.padding to match current padding* attributes"""
        self.padding = (
            self.padding_top,
            self.padding_right,
            self.padding_bottom,
            self.padding_left)

    def set_margins(self, top, right, bottom, left):
        """Input tuple of pad spacing to update margin attributes"""
        self.margin_top = int(top)
        self.margin_right = int(right)
        self.margin_bottom = int(bottom)
        self.margin_left = int(left)
        self.pack_margins()
        self.update_image_box()

    def set_padding(self, top, right, bottom, left):
        """Input tuple of pad spacing to update padding attributes"""
        self.padding_top = int(top)
        self.padding_right = int(right)
        self.padding_bottom = int(bottom)
        self.padding_left = int(left)
        self.width_padded = self.width - (self.padding_left +
                                          self.padding_right)
        self.height_padded = self.height - (self.padding_top +
                                            self.padding_bottom)
        self.pack_padding()

    def update_image_box(self):
        """Update cartesian coordinates for use in Image.paste calls"""
        self.image_box = (
            self.margin_left,
            self.margin_top,
            self.width + self.margin_left,
            self.height + self.margin_top)

    def __repr__(self):
        return '{w}x{h}'.format(w=self.width, h=self.height)


class Fretboard(Canvas):
    """Object representation of a fretboard"""
    def __init__(self, guitar_neck, scale=1, ppi=72):
        """Initialize Neck object. Available arguments:
            - guitar_neck: guitar.Neck object used for output rendering
            - ppi: count of pixels per inch
            - string_note_sequence: tuple of open notes for each string
        """
        self.guitar_neck = guitar_neck
        self.scale = scale
        self.ppi = ppi
        self.gap_count = len(self.guitar_neck.strings) - 1

        # Init canvas
        self.width_px = int((guitar_neck.length * self.ppi) * self.scale)
        self.height_px = int((guitar_neck.nut_width * self.ppi) * self.scale)
        super(Fretboard, self).__init__(self.width_px, self.height_px)

        # Update image
        self.update_image()

    def draw_image(self):
        """Draw elements to the image"""
        draw = ImageDraw.Draw(self.image)

        # Draw strings
        for string in self.guitar_neck.strings:
            draw.rectangle(string.coords, fill='#000')

        # Draw nut
        nut_start_pos_x = self.padding_left
        nut_start_pos_y = self.padding_top
        nut_end_pos_x = nut_start_pos_x + (self.guitar_neck.strings[0].height * 3)
        nut_end_pos_y = self.height - nut_start_pos_y
        nut_coords = (
            nut_start_pos_x,
            nut_start_pos_y,
            nut_end_pos_x,
            nut_end_pos_y)
        draw.rectangle(nut_coords, fill='#000')

        # Draw end cap
        cap_start_pos_x = self.width - (self.padding_right +
                                        self.guitar_neck.strings[0].height)
        cap_start_pos_y = self.padding_top
        cap_end_pos_x = cap_start_pos_x + self.guitar_neck.strings[0].height
        cap_end_pos_y = self.height - cap_start_pos_y
        cap_coords = (
            cap_start_pos_x,
            cap_start_pos_y,
            cap_end_pos_x,
            cap_end_pos_y)
        draw.rectangle(cap_coords, fill='#000')

    def new_image(self):
        """Create a new blank self.image"""
        self.image = Image.new(
            'RGB',
            (self.width, self.height),
            '#FFF')

    def reduce_canvas_height(self, px):
        """Reduce self.height by px, then recalculate padding/margins"""
        self.height -= px
        self.set_padding(*self.padding)
        self.set_margins(*self.margins)

    def update_canvas_padding(self, top, right, bottom, left):
        """Update canvas padding and refresh image"""
        self.set_padding(top, right, bottom, left)
        self.update_image()

    def update_canvas_margins(self, top, right, bottom, left):
        """Update canvas margins and refresh image"""
        self.set_margins(top, right, bottom, left)
        self.update_image()

    def update_image(self):
        """Update dynamic values and redraw image"""
        self.update_string_heights()
        self.update_string_coords()
        self.new_image()
        self.draw_image()

    def update_string_coords(self):
        """Calculate and update self.guitar_neck.strings[*].coords for use in drawing"""
        start_pos_x = self.padding_left
        start_pos_y = self.padding_top
        for string in self.guitar_neck.strings:
            end_pos_x = self.width - self.padding_right
            end_pos_y = start_pos_y + string.height
            string.coords = (start_pos_x, start_pos_y, end_pos_x, end_pos_y)
            start_pos_y = start_pos_y + string.height + self.gap_height

    def update_string_heights(self, gap_bias=.90):
        """Calculate and update string and gap heights for use in drawing"""
        height_allowance = self.height_padded
        self.gap_height = int((height_allowance * gap_bias) / self.gap_count)
        height_allowance -= self.gap_height * self.gap_count
        for string in self.guitar_neck.strings:
            string.height = int(height_allowance / len(self.guitar_neck.strings))
        height_allowance -= self.guitar_neck.strings[0].height * len(self.guitar_neck.strings)
        if height_allowance != 0:
            # Adjust canvas to achieve perfect fit and restart at update_image
            self.reduce_canvas_height(height_allowance)
            self.update_image()
