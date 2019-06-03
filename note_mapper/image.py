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
