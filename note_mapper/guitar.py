""" guitar - collection of classes and functions used to represent and
reconfigure component parts of a guitar
"""
from copy import deepcopy


class Note:
    """Object representing a musical note"""
    notes_all = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    notes_sharp = ('A', 'C', 'D', 'F', 'G')
    notes_flat = ('B', 'D', 'E', 'G', 'A')

    def __init__(self, name, sharp=False, flat=False):
        if len(name) > 1:
            # Convert note as it includes notation
            converted_note = self.convert_thick_note(name)
            self.name = converted_note[0]
            self.sharp = converted_note[1]
            self.flat = converted_note[2]
        else:
            # Initialize as normal
            self.name = name
            self.sharp = sharp
            self.flat = flat

    def _get_next_note_down(self):
        """Return next note name down the sequence"""
        note_idx = self.notes_all.index(self.name)
        try:
            next_note_idx = note_idx - 1
            next_note = self.notes_all[next_note_idx]
        except IndexError:
            next_note_idx = -1
            next_note = self.notes_all[next_note_idx]
        return next_note

    def _get_next_note_up(self):
        """Return next note name up the sequence"""
        note_idx = self.notes_all.index(self.name)
        try:
            next_note_idx = note_idx + 1
            next_note = self.notes_all[next_note_idx]
        except IndexError:
            next_note_idx = 0
            next_note = self.notes_all[next_note_idx]
        return next_note

    def convert_thick_note(self, note):
        """Check input note str for length. If > 1, assume note name includes
        notation at index 1 (♯/♭), verify, and return tuple of
        (note str, sharp bool, flat bool)
        """
        sharp = False
        flat = False
        if len(note) > 1:
            if note[1] == '♯':
                sharp = True
            elif note[1] == '♭':
                flat = True
            note = note[0]

        return (note, sharp, flat)

    def convert_to_flat(self):
        """Convert note to flat"""
        if not self.sharp and not self.flat and self.name in self.notes_flat:
            # Convert unmodified note to flat if it can be
            self.sharp = False
            self.flat = True
        elif self.sharp:
            # Convert sharp to flat (next flat note up + attributes to ♭)
            self.name = self._get_next_note_up()
            self.sharp = False
            self.flat = True

    def convert_to_sharp(self):
        """Convert note to sharp"""
        if not self.flat and not self.sharp and self.name in self.notes_sharp:
            # Convert unmodified note to sharp if it can be
            self.sharp = True
            self.flat = False
        elif self.flat:
            # Convert flat to sharp (next note down + attributes to ♯)
            self.name = self._get_next_note_down()
            self.sharp = True
            self.flat = False

    def decrement(self):
        """Decrement note to next note down the scale"""
        next_note = self._get_next_note_down()
        flat_valid = True if self.name in self.notes_flat else False
        sharp_valid = True if next_note in self.notes_sharp else False
        if not self.sharp and not self.flat:
            if flat_valid:
                self.flat = True
            elif sharp_valid:
                self.name = next_note
                self.flat = False
                self.sharp = True
            else:
                self.name = next_note
        elif self.flat and sharp_valid:
            self.name = next_note
            self.flat = False
            self.sharp = True
        elif self.flat:
            self.name = next_note
            self.flat = False
        elif self.sharp:
            self.sharp = False

    def increment(self):
        """Increment note to next note up the scale"""
        next_note = self._get_next_note_up()
        sharp_valid = True if self.name in self.notes_sharp else False
        flat_valid = True if next_note in self.notes_flat else False
        if not self.sharp and not self.flat:
            if sharp_valid:
                self.sharp = True
            elif flat_valid:
                self.name = next_note
                self.sharp = False
                self.flat = True
            else:
                self.name = next_note
        elif self.sharp and flat_valid:
            self.name = next_note
            self.sharp = False
            self.flat = True
        elif self.sharp:
            self.name = next_note
            self.sharp = False
        elif self.flat:
            self.flat = False

    def __repr__(self):
        if self.sharp:
            return '{n}{s}'.format(n=self.name, s='♯')
        elif self.flat:
            return '{n}{s}'.format(n=self.name, s='♭')
        else:
            return '{}'.format(self.name)


class Fret:
    """Object representing a fret on a guitar neck"""
    def __init__(self, string_name, position, notes):
        """Initialize Fret object. Attributes:
            - position: fret position on the neck/fretboard
            - note: primary note played on fret (standard or sharp)
            - enharmonic: boolean tracking whether fret note represents multiple notes depending on context
            - enharmonic_note: alternate representation of fret note (flat)
        """
        self.string_name = string_name
        self.position = position
        self.note = notes[0]
        self.enharmonic = True if len(notes) > 1 else False
        self.enharmonic_note = notes[-1] if self.enharmonic else self.note

    def get_note_str(self, sharp=True):
        """Return string representation of note present in fret"""
        if sharp:
            return '{}'.format(self.note)
        else:
            return '{}'.format(self.enharmonic_note)

    def __repr__(self):
        return self.get_note_str()


class String:
    """Object representing a guitar string"""
    height = None
    coords = None

    def __init__(self, name, fret_count):
        """Initialize String object. Attributes:
            - name: name of string (synonymous with open note)
            - fret_count: count of frets to sequence on string
            - frets: list of Fret objects present on string
        """
        self.name = name
        self.fret_count = fret_count
        self.frets = self._generate_frets()

    def _generate_frets(self):
        """Generate and return list of Fret objects, starting at string
        note (self.name), ending after self.fret_count frets
        """
        # Pack first fret
        frets = []
        open_note = Note(self.name)
        next_note = deepcopy(open_note)
        next_note.increment()
        fret_notes = self._pack_fret_note_list(open_note, next_note)
        frets.append(Fret(self.name, 0, fret_notes))

        # Pack remaining frets
        for i in range(self.fret_count):
            current_note = deepcopy(fret_notes[-1])
            current_note.increment()
            next_note = deepcopy(current_note)
            next_note.increment()
            fret_notes = self._pack_fret_note_list(current_note, next_note)
            frets.append(Fret(self.name, i + 1, fret_notes))

        return frets

    def _pack_fret_note_list(self, current_note, next_note):
        if current_note.sharp and next_note.flat:
            return [current_note, next_note]
        else:
            return [current_note]

    def get_fret_notes(self, sharp=True):
        fret_notes = []
        for fret in self.frets:
            if sharp:
                fret_notes.append(fret.get_note_str(sharp=True))
            else:
                fret_notes.append(fret.get_note_str(sharp=False))
        return fret_notes

    def __repr__(self):
        """Return text map of notes"""
        return ', '.join(map(str, self.get_fret_notes(sharps=True)))


class Neck:
    """Object representing the neck of a guitar"""
    def __init__(self, length=25.25, nut_width=1.89, fret_count=21,
                 string_note_sequence=('E', 'B', 'G', 'D', 'A', 'E')):
        """Initialize Neck object. Attributes:
            - length: length of neck (inches)
            - nut_width: width of neck at nut (inches)
            - fret_count: count of frets on neck
            - string_note_sequence: tuple of open notes on each string (high to low)
            - strings: list of String objects
        """
        self.length = length
        self.nut_width = nut_width
        self.fret_count = fret_count
        self.string_note_sequence = string_note_sequence
        self.strings = []
        for note_name in self.string_note_sequence:
            self.strings.append(String(note_name, self.fret_count))

    def __repr__(self):
        """Return text map of strings:notes"""
        return '\n'.join(map(str, self.strings))
