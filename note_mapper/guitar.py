from PIL import Image, ImageDraw
from .image import Canvas


class Note:
    """Object representing a musical note"""
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class String:
    """Object representing a guitar string"""
    note_names = (
        'A', 'A#/B♭', 'B', 'C',
        'C#/D♭', 'D', 'D#/E♭', 'E',
        'F', 'F#/G♭', 'G', 'G#/A♭')
    height = None
    coords = None

    def __init__(self, name, note_count):
        """Initialize String object. Available arguments:
            - name: name of string
            - note_count: count of notes to track on string
        """
        self.name = name
        self.note_count = note_count
        self.build_string_notes()

    def build_string_notes(self):
        """Build note sequence tuple for string"""
        open_note = self.name
        string_notes = [Note(open_note)]
        current_note_idx = list(self.note_names).index(open_note)
        for i in range(self.note_count):
            next_note_idx = self.get_next_note_idx(current_note_idx)
            string_notes.append(Note(self.note_names[next_note_idx]))
            current_note_idx = next_note_idx

        self.notes = tuple(string_notes)

    def get_next_note_idx(self, note_idx):
        """Get index of next note in note sequence"""
        return note_idx + 1 if len(self.note_names) > note_idx + 1 else 0

    def __repr__(self):
        """Return text map of notes"""
        return ', '.join(map(str, self.notes))


class Neck:
    """Object representing the neck of a guitar"""
    string_names = ('E', 'B', 'G', 'D', 'A', 'E')

    def __init__(self, **kwargs):
        """Initialize Neck object. Available arguments:
            - length: length of neck (inches)
            - nut_width: width of neck at nut (inches)
            - fret_count: count of frets on neck
            - scale: overall scale of components
            - ppi: count of pixels per inch
        """
        # Assign kwargs and set defaults
        self.length = kwargs['length'] if 'length' in kwargs else 25.5
        self.nut_width = kwargs['nut_width'] if 'nut_width' in kwargs else 1.89
        self.fret_count = kwargs['fret_count'] if 'fret_count' in kwargs else 21
        self.scale = kwargs['scale'] if 'scale' in kwargs else 1
        self.ppi = kwargs['ppi'] if 'ppi' in kwargs else 75
        self.strings = [String(name, self.fret_count) for name in self.string_names]
        self.gap_count = len(self.strings) - 1

        # Init canvas
        width_px = int((self.length * self.ppi) * self.scale)
        height_px = int((self.nut_width * self.ppi) * self.scale)
        self.canvas = Canvas(width_px, height_px)

        # Update image
        self.update_image()

    def draw_image(self):
        """Draw elements to the image"""
        draw = ImageDraw.Draw(self.image)

        # Draw strings
        for string in self.strings:
            draw.rectangle(string.coords, fill='#000')

        # Draw nut
        nut_start_pos_x = self.canvas.padding_left
        nut_start_pos_y = self.canvas.padding_top
        nut_end_pos_x = nut_start_pos_x + (self.strings[0].height * 3)
        nut_end_pos_y = self.canvas.height - nut_start_pos_y
        nut_coords = (
            nut_start_pos_x,
            nut_start_pos_y,
            nut_end_pos_x,
            nut_end_pos_y)
        draw.rectangle(nut_coords, fill='#000')

        # Draw end cap
        cap_start_pos_x = self.canvas.width - (self.canvas.padding_right +
                                               self.strings[0].height)
        cap_start_pos_y = self.canvas.padding_top
        cap_end_pos_x = cap_start_pos_x + self.strings[0].height
        cap_end_pos_y = self.canvas.height - cap_start_pos_y
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
            (self.canvas.width, self.canvas.height),
            '#FFF')

    def reduce_canvas_height(self, px):
        """Reduce self.canvas.height by px, then recalculate padding/margins"""
        self.canvas.height -= px
        self.canvas.set_padding(*self.canvas.padding)
        self.canvas.set_margins(*self.canvas.margins)

    def update_canvas_padding(self, top, right, bottom, left):
        """Update canvas padding and refresh image"""
        self.canvas.set_padding(top, right, bottom, left)
        self.update_image()

    def update_canvas_margins(self, top, right, bottom, left):
        """Update canvas margins and refresh image"""
        self.canvas.set_margins(top, right, bottom, left)
        self.update_image()

    def update_image(self):
        """Update dynamic values and redraw image"""
        self.update_string_heights()
        self.update_string_coords()
        self.new_image()
        self.draw_image()

    def update_string_coords(self):
        """Calculate and update self.strings[*].coords for use in drawing"""
        start_pos_x = self.canvas.padding_left
        start_pos_y = self.canvas.padding_top
        for string in self.strings:
            end_pos_x = self.canvas.width - self.canvas.padding_right
            end_pos_y = start_pos_y + string.height
            string.coords = (start_pos_x, start_pos_y, end_pos_x, end_pos_y)
            start_pos_y = start_pos_y + string.height + self.gap_height

    def update_string_heights(self, gap_bias=.90):
        """Calculate and update string and gap heights for use in drawing"""
        height_allowance = self.canvas.height_padded
        self.gap_height = int((height_allowance * gap_bias) / self.gap_count)
        height_allowance -= self.gap_height * self.gap_count
        for string in self.strings:
            string.height = int(height_allowance / len(self.strings))
        height_allowance -= self.strings[0].height * len(self.strings)
        if height_allowance != 0:
            # Adjust canvas to achieve perfect fit and restart at update_image
            self.reduce_canvas_height(height_allowance)
            self.update_image()

    def __repr__(self):
        """Return text map of strings:notes"""
        return '\n'.join(map(str, self.strings))
