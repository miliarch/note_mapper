#!/usr/bin/env python3
import common
from note_mapper.guitar import Neck

TESTS = []

# standard 6 string tuning sequence
STD_6 = ('E', 'B', 'G', 'D', 'A', 'E')
STD_6_ANS_SHARP = 'E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D\nB, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A\nG, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F\nD, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C\nA, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G\nE, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D'
STD_6_ANS_FLAT = 'E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D\nB, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A\nG, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F\nD, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C\nA, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G\nE, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D'
TESTS.append({'test': STD_6, 'answer_sharp': STD_6_ANS_SHARP, 'answer_flat': STD_6_ANS_FLAT})

# drop d 6 string tuning sequence
DROP_D_6 = ('E', 'B', 'G', 'D', 'A', 'D')
DROP_D_6_ANS_SHARP = 'E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D\nB, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A\nG, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F\nD, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C\nA, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G\nD, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C'
DROP_D_6_ANS_FLAT = 'E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D\nB, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A\nG, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F\nD, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C\nA, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G\nD, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C'
TESTS.append({'test': DROP_D_6, 'answer_sharp': DROP_D_6_ANS_SHARP, 'answer_flat': DROP_D_6_ANS_FLAT})

# drop g 6 string tuning sequence
DROP_G_6 = ('A♯', 'F', 'C♯', 'G♯', 'D♯', 'G♯')
DROP_G_ANS_SHARP = 'A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯\nF, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯\nC♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B\nG♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯\nD♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯\nG♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯'
DROP_D_6_ANS_FLAT = 'B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭\nF, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭\nD♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B\nA♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭\nE♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭\nA♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭'
TESTS.append({'test': DROP_G_6, 'answer_sharp': DROP_G_ANS_SHARP, 'answer_flat': DROP_D_6_ANS_FLAT})

# 6 string lowered D tuning sequence
LOW_D_6 = ('D', 'A', 'F', 'C', 'G', 'D')
LOW_D_6_ANS_SHARP = 'D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C\nA, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G\nF, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯\nC, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯\nG, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F\nD, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C'
LOW_D_6_ANS_FLAT = 'D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C\nA, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G\nF, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭\nC, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭\nG, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F\nD, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C'
TESTS.append({'test': LOW_D_6, 'answer_sharp': LOW_D_6_ANS_SHARP, 'answer_flat': LOW_D_6_ANS_FLAT})

# 12 string standard tuning sequence
STD_12 = ('E', 'E', 'B', 'B', 'G', 'G', 'D', 'D', 'A', 'A', 'D', 'D')
STD_12_ANS_SHARP = 'E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D\nE, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D\nB, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A\nB, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A\nG, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F\nG, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F\nD, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C\nD, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C\nA, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G\nA, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G\nD, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C\nD, D♯, E, F, F♯, G, G♯, A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯, A, A♯, B, C'
STD_12_ANS_FLAT = 'E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D\nE, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D\nB, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A\nB, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A\nG, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F\nG, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F\nD, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C\nD, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C\nA, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G\nA, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G\nD, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C\nD, E♭, E, F, G♭, G, A♭, A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭, A, B♭, B, C'
TESTS.append({'test': STD_12, 'answer_sharp': STD_12_ANS_SHARP, 'answer_flat': STD_12_ANS_FLAT})


def main():
    for t in TESTS:
        test_input = t['test']
        answer_sharp = t['answer_sharp']
        answer_flat = t['answer_flat']
        guitar_neck = Neck(fret_count=22, string_note_sequence=test_input)
        string_notes_sharp = []
        string_notes_flat = []
        for string in guitar_neck.strings:
            sharps = ', '.join(map(str, string.get_fret_notes(sharps=True)))
            flats = ', '.join(map(str, string.get_fret_notes(sharps=False)))
            string_notes_sharp.append(sharps)
            string_notes_flat.append(flats)
        string_note_map_sharp = '\n'.join(map(str, string_notes_sharp))
        string_note_map_flat = '\n'.join(map(str, string_notes_flat))
        sharps_pass = True if string_note_map_sharp == answer_sharp else False
        flats_pass = True if string_note_map_flat == answer_flat else False
        output_str = 'Input: {}\n'.format(test_input)
        output_str += 'Sharps Pass: {}\n'.format(sharps_pass)
        output_str += 'Sharp Notes:\n{}\n\n'.format(string_note_map_sharp)
        if not sharps_pass:
            output_str += 'Expected Sharp Notes:\n{}\n\n'.format(answer_sharp)
        output_str += 'Flats Pass: {}\n'.format(flats_pass)
        output_str += 'Flat Notes:\n{}\n\n'.format(string_note_map_flat)
        if not flats_pass:
            output_str += 'Expected Flat Notes:\n{}\n\n'.format(answer_flat)
        print(output_str)


if __name__ == '__main__':
    main()
